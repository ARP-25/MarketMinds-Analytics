from datetime import date
import datetime
from unittest.mock import MagicMock, patch
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from subscription.models import SubscriptionPlan
from trade_insights.models import Insight
from checkout.models import ActiveSubscription
from profiles.models import UserProfile
from .views import is_superuser
from django.core.files.uploadedfile import SimpleUploadedFile
from decimal import Decimal


from io import BytesIO
from PIL import Image


def create_test_image():
    file = BytesIO()
    image = Image.new('RGB', (100, 100))
    image.save(file, 'jpeg')
    file.name = 'test.jpg'
    file.seek(0)
    return file


class MockStripeResponse:
    def __init__(self, id):
        self.id = id


class AdminAccessTests(TestCase):

    def setUp(self):
        # Set up users without creating UserProfiles manually
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@test.com', password='adminpass')
        self.user = User.objects.create_user(
            username='user', email='user@test.com', password='userpass')

        # Create a mock image file and assign it as an instance attribute
        self.mock_image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

        # Create and assign the SubscriptionPlan object using the mock image
        self.subscription_plan = SubscriptionPlan.objects.create(
            title='Basic Plan', description='A basic plan', price=10, image=self.mock_image)

        # Create an Insight object using the created SubscriptionPlan and mock image
        Insight.objects.create(
            title='Test Insight', 
            content='Some insightful content', 
            release_date=date.today(), 
            category=self.subscription_plan, 
            cover_image=self.mock_image
        )

        # Create a mock Stripe subscription ID
        self.mock_stripe_subscription_id = 'sub_test'
        # Create an ActiveSubscription instance
        self.active_subscription = ActiveSubscription.objects.create(
            user=self.user,
            subscription_plan=self.subscription_plan,
            stripe_subscription_id=self.mock_stripe_subscription_id,
            start_date=timezone.now(), 
            current_period_end=timezone.now() + datetime.timedelta(days=30),
            status='active',
            billing_amount=Decimal('10.00'),
            monthly_cost=Decimal('10.00')
        )


    def test_is_superuser(self):
        # Test the is_superuser function
        self.assertTrue(is_superuser(self.admin_user))
        self.assertFalse(is_superuser(self.user))

    def test_AdminAccessSubscription_get(self):
        # Test the GET request for AdminAccessSubscription
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('AdminAccessSubscription'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Basic Plan')


    @patch('stripe.Price.create')
    @patch('stripe.Product.create')
    def test_admin_access_subscription_add_post(self, mock_product_create, mock_price_create):
        mock_product_create.return_value = MockStripeResponse('prod_test')
        mock_price_create.return_value = MockStripeResponse('price_test')

        # Ensure user is logged in as admin
        self.client.login(username='admin', password='adminpass')

        # Prepare valid form data
        form_data = {
            'title': 'Test Plan',
            'description': 'Description for Test Plan',
            'price': 10,
            'details': 'Additional details about the plan',
            'image': create_test_image()  
        }

        response = self.client.post(reverse('admin_access_subscription_add'), form_data)

        if response.status_code == 302:
            print("Redirected to:", response.url)
        elif hasattr(response, 'context'):
            print(response.context.get('form').errors)
        else:
            print("No context available in response")

        self.assertEqual(response.status_code, 302)

        # Verify that the SubscriptionPlan was created
        self.assertTrue(SubscriptionPlan.objects.filter(title='Test Plan').exists())



    @patch('stripe.Price.create')
    @patch('stripe.Product.create')
    def test_admin_access_subscription_edit_post(self, mock_product_create, mock_price_create):
        self.client.login(username='admin', password='adminpass')

        # Set up the return values for the mocked methods
        mock_product = MagicMock(id='prod_test123')
        mock_price = MagicMock(id='price_test123')
        mock_product_create.return_value = mock_product
        mock_price_create.return_value = mock_price
        
        original_price = self.subscription_plan.price
        original_id = self.subscription_plan.id

        # Test case 1: Price unchanged
        form_data_unchanged = {
            'title': 'Basic Plan',
            'description': 'A basic plan - updated description',
            'price': 10,
            'details': 'Updated details',
            'image': create_test_image(),
        }
        response = self.client.post(reverse('admin_access_subscription_edit', args=[self.subscription_plan.id]), form_data_unchanged)
        if response.status_code != 302:
            print("Form Errors:", response.context['form'].errors)
        self.assertEqual(response.status_code, 302)
        self.subscription_plan.refresh_from_db()
        self.assertEqual(self.subscription_plan.description, 'A basic plan - updated description')
        mock_price_create.assert_not_called()

        # Test case 2: Price changed with active subscriptions
        new_price = 20
        form_data_changed = {
            'title': 'Basic Plan - New Price',
            'description': 'A basic plan with new price',
            'price': new_price,
            'details': 'Updated details with new price',
            'image': create_test_image(),
        }
        response = self.client.post(reverse('admin_access_subscription_edit', args=[self.subscription_plan.id]), form_data_changed)
        if response.status_code != 302:
            print("Form Errors:", response.context['form'].errors)
        new_plan = SubscriptionPlan.objects.latest('id')
        self.assertNotEqual(new_plan.id, original_id)
        self.assertEqual(new_plan.price, Decimal(new_price))
        mock_price_create.assert_called_once()






    def test_admin_access_insight_add_post(self):
        self.client.login(username='admin', password='adminpass')
        form_data = {
            'title': 'New Insight',
            'content': 'Insight Content',
            'release_date': date.today(),
            'category': self.subscription_plan.id, 
            'short_description': 'Short description',
            'author': self.admin_user.id,  # Assuming author is required
            'stage': 'MS',  # Assuming stage is required
            'display': 'TXT',  # Assuming display is required
            'cover_image': create_test_image(),  
            'details': 'Some details', 
        }
        response = self.client.post(reverse('admin_access_insight_add'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Insight.objects.filter(title='New Insight').exists())

