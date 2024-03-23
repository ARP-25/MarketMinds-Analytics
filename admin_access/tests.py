from datetime import date
import datetime
from unittest.mock import MagicMock, patch
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.storage.fallback import FallbackStorage
from django.core.files.base import ContentFile
from django.contrib.messages import get_messages
from subscription.models import SubscriptionPlan
from trade_insights.models import Insight
from checkout.models import ActiveSubscription
from profiles.models import UserProfile
from trade_insights.models import Insight
from platform_metrics.models import FinancialMetrics
from admin_access.forms import InsightForm
from .views import is_superuser
from .views import remove_plan_from_bag
from django.core.files.uploadedfile import SimpleUploadedFile
from decimal import Decimal


from io import BytesIO
from PIL import Image

# Helper Functions
def create_test_image():
    file = BytesIO()
    image = Image.new('RGB', (100, 100))
    image.save(file, 'jpeg')
    file.name = 'test.jpg'
    file.seek(0)
    return ContentFile(file.getvalue(), name='test.jpg')

def create_active_subscription(self):
    # Erstellen eines Benutzers und eines Abonnementplans (oder Verwendung existierender Objekte)
    user = User.objects.create(username='testuser', password='password', email='testuser@example.com')
    subscription_plan = SubscriptionPlan.objects.create(title='Test Plan', description='Test Description', price=10)

    # Erstellen der ActiveSubscription
    active_subscription = ActiveSubscription.objects.create(
        user=user,
        subscription_plan=subscription_plan,
        stripe_subscription_id="stripe_test_id",
        start_date=timezone.now(),
        current_period_end=timezone.now() + datetime.timedelta(days=30),
        status='active',
        billing_amount=Decimal('10.00'),
        monthly_cost=Decimal('10.00')
    )
    return active_subscription
class MockStripeResponse:
    def __init__(self, id):
        self.id = id


class AdminAccessTests(TestCase):
    # Helper Functions
    def create_test_image():
        file = BytesIO()
        image = Image.new('RGB', (100, 100))
        image.save(file, 'jpeg')
        file.name = 'test.jpg'
        file.seek(0)
        return ContentFile(file.getvalue(), name='test.jpg')

    def create_active_subscription(self):
        # Erstellen eines Benutzers und eines Abonnementplans (oder Verwendung existierender Objekte)
        user = User.objects.create(username='testuser', password='password', email='testuser@example.com')
        subscription_plan = SubscriptionPlan.objects.create(title='Test Plan', description='Test Description', price=10)

        # Erstellen der ActiveSubscription
        active_subscription = ActiveSubscription.objects.create(
            user=user,
            subscription_plan=subscription_plan,
            stripe_subscription_id="stripe_test_id",
            start_date=timezone.now(),
            current_period_end=timezone.now() + datetime.timedelta(days=30),
            status='active',
            billing_amount=Decimal('10.00'),
            monthly_cost=Decimal('10.00')
        )
        return active_subscription

    def setUp(self):
        # Set up users without creating UserProfiles manually
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@test.com', password='adminpass')
        self.user = User.objects.create_user(
            username='user', email='user@test.com', password='userpass')

        self.factory = RequestFactory()

        # Create an image using create_test_image function
        test_image = create_test_image()

        # Create and assign the SubscriptionPlan object using the mock image
        self.subscription_plan = SubscriptionPlan.objects.create(
            title='Basic Plan', description='A basic plan', price=10, image=test_image)

        # Create insights with different release dates and categories
        Insight.objects.create(
            title='Insight 1',
            content='Content for Insight 1',
            release_date=date(2024, 3, 21),  # Older date
            category=self.subscription_plan,
            cover_image=create_test_image(),
            stage='MS'
        )
        Insight.objects.create(
            title='Insight 2',
            content='Content for Insight 2',
            release_date=date(2024, 3, 23),  # Newer date
            category=self.subscription_plan,
            cover_image=create_test_image(),
            stage='SS'
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

    def test_remove_plan_from_bag(self):
        # Create a request and attach a session and messages
        request = self.factory.get('/fake-url')
        middleware = SessionMiddleware(lambda _: _)
        middleware.process_request(request)
        request.session.save()
        setattr(request, 'session', request.session)
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        # Add a subscription plan to the session
        request.session['bag_items'] = ['1', '2', '3']  # Example subscription IDs

        # Call the remove_plan_from_bag view
        remove_plan_from_bag(request, '2')  # Remove subscription with ID '2'

        # Test if the plan was removed correctly
        self.assertNotIn('2', request.session['bag_items'])
        self.assertIn('1', request.session['bag_items'])
        self.assertIn('3', request.session['bag_items'])

    # Testfälle für die Subscription-Verwaltung
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

        initial_plan_count = SubscriptionPlan.objects.count()
        original_id = self.subscription_plan.id

        # Test case 1: Price unchanged
        # Expectation: SubscriptionPlan should be updated in the database, but no new Stripe Price should be created
        form_data_unchanged = {
            'title': 'Basic Plan',
            'description': 'A basic plan - updated description',
            'price': self.subscription_plan.price,  # Keeping the price unchanged
            'details': 'Updated details',
            'image': create_test_image(),
        }
        response = self.client.post(reverse('admin_access_subscription_edit', args=[self.subscription_plan.id]), form_data_unchanged)
        self.assertEqual(response.status_code, 302)
        self.subscription_plan.refresh_from_db()
        self.assertEqual(self.subscription_plan.description, 'A basic plan - updated description')
        mock_price_create.assert_not_called()

        # Test case 2: Price changed without active subscriptions
        # Expectation: The existing SubscriptionPlan should be updated, no new SubscriptionPlan created
        new_price = 20
        form_data_changed = {
            'title': 'Basic Plan - New Price',
            'description': 'A basic plan with new price',
            'price': new_price,
            'details': 'Updated details with new price',
            'image': create_test_image(),
        }

        # Deactivate or remove all active subscriptions for the test plan
        ActiveSubscription.objects.filter(subscription_plan=self.subscription_plan).delete()

        response = self.client.post(reverse('admin_access_subscription_edit', args=[self.subscription_plan.id]), form_data_changed)
        self.assertEqual(response.status_code, 302)
        self.subscription_plan.refresh_from_db()

        # Check if the SubscriptionPlan has been updated with new details
        self.assertEqual(self.subscription_plan.price, Decimal(new_price))
        self.assertEqual(self.subscription_plan.title, 'Basic Plan - New Price')
        self.assertEqual(self.subscription_plan.description, 'A basic plan with new price')
        # Am Ende des Testfalls
        self.assertEqual(SubscriptionPlan.objects.count(), initial_plan_count)


        # Verify that a new plan was not created
        self.assertEqual(SubscriptionPlan.objects.count(), initial_plan_count)  # assuming initial_plan_count is defined
        mock_price_create.assert_called_once()  # assuming Stripe Price should still be created

    @patch('stripe.Plan.delete')
    def test_admin_access_subscription_delete(self, mock_stripe_plan_delete):
        mock_stripe_plan_delete.return_value = MagicMock()

        # Test case 1: Deleting a plan with active subscriptions
        self.create_active_subscription()  # Create an active subscription using the helper function
        response = self.client.post(reverse('admin_access_subscription_delete', args=[self.subscription_plan.id]))
        self.assertEqual(response.status_code, 302)
        self.subscription_plan.refresh_from_db()
        self.assertFalse(self.subscription_plan.staged)  # Plan should be marked as invisible
        self.assertTrue(SubscriptionPlan.objects.filter(id=self.subscription_plan.id).exists())  # Plan should still exist in DB
        mock_stripe_plan_delete.assert_not_called()  # Stripe API should not be called

        # Test case 2: Deleting a plan without active subscriptions
        ActiveSubscription.objects.filter(subscription_plan=self.subscription_plan).delete()
        response = self.client.post(reverse('admin_access_subscription_delete', args=[self.subscription_plan.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(SubscriptionPlan.objects.filter(id=self.subscription_plan.id).exists())  


    # Testfälle für die Insight-Verwaltung
    def test_admin_access_insight_sort_most_recent(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('AdminAccessInsight') + '?sort=most_recent')
        self.assertEqual(response.status_code, 200)
        insights = response.context['trade_insights']
        self.assertTrue(insights.ordered)  # Check if queryset is ordered
        self.assertGreaterEqual(insights[0].release_date, insights[1].release_date)  # Newest first

    def test_admin_access_insight_sort_oldest(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('AdminAccessInsight') + '?sort=oldest')
        self.assertEqual(response.status_code, 200)
        insights = response.context['trade_insights']
        self.assertTrue(insights.ordered)
        self.assertLessEqual(insights[0].release_date, insights[1].release_date)  # Oldest first

    def test_admin_access_insight_sort_a_z(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('AdminAccessInsight') + '?sort=a_z')
        self.assertEqual(response.status_code, 200)
        insights = response.context['trade_insights']
        self.assertTrue(all(insights[i].title <= insights[i + 1].title for i in range(len(insights) - 1)))

    def test_admin_access_insight_sort_z_a(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('AdminAccessInsight') + '?sort=z_a')
        self.assertEqual(response.status_code, 200)
        insights = response.context['trade_insights']
        self.assertTrue(all(insights[i].title >= insights[i + 1].title for i in range(len(insights) - 1)))

    def test_admin_access_insight_filter_crypto(self):
        # Create insights with 'Crypto' category if not already done in setUp
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('AdminAccessInsight') + '?sort=crypto')
        self.assertEqual(response.status_code, 200)
        insights = response.context['trade_insights']
        self.assertTrue(all(insight.category.title == 'Crypto' for insight in insights))

    def test_admin_access_insight_filter_forex(self):
        # Create insights with 'Forex' category if not already done in setUp
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('AdminAccessInsight') + '?sort=forex')
        self.assertEqual(response.status_code, 200)
        insights = response.context['trade_insights']
        self.assertTrue(all(insight.category.title == 'Forex' for insight in insights))

    def test_admin_access_insight_filter_stocks(self):
        # Create insights with 'Stocks' category if not already done in setUp
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('AdminAccessInsight') + '?sort=stocks')
        self.assertEqual(response.status_code, 200)
        insights = response.context['trade_insights']
        self.assertTrue(all(insight.category.title == 'Stocks' for insight in insights))

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

    def test_access_edit_page(self):
        self.client.login(username='admin', password='adminpass')
        self.insight = Insight.objects.create(
            title='Insight for Edit',
            content='Test Content',
            release_date=date.today(),
            category=self.subscription_plan,
            cover_image=None,
            stage='MS'
        )
        self.edit_url = reverse('admin_access_insight_edit', args=[self.insight.id])
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], InsightForm)

    def test_edit_insight_with_valid_data(self):
        self.client.login(username='admin', password='adminpass')
        user_profile, created = UserProfile.objects.get_or_create(user=self.admin_user)

        # Create a test insight
        insight = Insight.objects.create(
            title='Original Title',
            content='Original Content',
            release_date=date.today(),
            category=self.subscription_plan,
            cover_image=None,  
            short_description='Original Short Description',
            author=user_profile,  
            stage=Insight.MAINSTAGE,
            display=Insight.TEXT
        )
        edit_url = reverse('admin_access_insight_edit', args=[insight.id])

        # Updated data for the insight
        updated_data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
            'release_date': insight.release_date,
            'category': insight.category.id,
            'short_description': 'Updated Short Description',
            'author': user_profile.id ,  
            'stage': Insight.SECOND_STAGE,
            'display': Insight.IMAGE
        }

        # Create a form instance with the updated data
        form = InsightForm(updated_data, instance=insight)
        
        # Check if the form is valid and print errors
        if not form.is_valid():
            print("Form errors:", form.errors.as_data())

        # Make the POST request using the form
        response = self.client.post(edit_url, updated_data)

        # Assertions
        self.assertEqual(response.status_code, 302)  
        insight.refresh_from_db()
        self.assertEqual(insight.title, 'Updated Title')
        self.assertEqual(insight.content, 'Updated Content')
        self.assertEqual(insight.stage, 'SS')

    def test_admin_access_insight_delete(self):
        # Login as admin
        self.client.login(username='admin', password='adminpass')

        # Create a test insight
        insight = Insight.objects.create(
            title='Test Insight',
            content='Test Content',
            release_date=date.today(),
            category=self.subscription_plan,
            stage=Insight.MAINSTAGE,
            display=Insight.TEXT
        )

        # Get the count of insights before deletion
        insights_count_before = Insight.objects.count()

        # URL for deleting the insight
        delete_url = reverse('admin_access_insight_delete', args=[insight.id])

        # Make POST request to delete view
        response = self.client.post(delete_url)

        # Check if the insight count decreased
        insights_count_after = Insight.objects.count()
        self.assertEqual(insights_count_before - 1, insights_count_after)

        # Check for success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Trade Insight has been deleted successfully.')

        # Check for redirection
        self.assertRedirects(response, reverse('AdminAccessInsight'))

        # Check that the insight no longer exists
        with self.assertRaises(Insight.DoesNotExist):
            Insight.objects.get(pk=insight.id)


class AdminAccessMetricTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create instances of FinancialMetrics for testing
        FinancialMetrics.objects.create(
            period=date(2021, 1, 1),
            monthly_revenue=10000.00,
            renewed_subscriptions=150,
            new_subscriptions=50,
            canceled_subscriptions=20
        )
        FinancialMetrics.objects.create(
            period=date(2021, 2, 1),
            monthly_revenue=12000.00,
            renewed_subscriptions=180,
            new_subscriptions=70,
            canceled_subscriptions=30
        )

    def setUp(self):
        # Create a superuser and login for testing
        self.admin_user = User.objects.create_superuser(
            username='admin', 
            email='admin@example.com', 
            password='adminpass'
        )
        self.client.login(username='admin', password='adminpass')

    def test_metrics_list_view(self):
        # Test the default behavior of the view (without sorting)
        response = self.client.get(reverse('AdminAccessMetric'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_access/admin_access_metric.html')
        self.assertEqual(len(response.context['trade_insights']), FinancialMetrics.objects.count())

