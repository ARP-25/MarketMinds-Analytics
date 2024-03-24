# MarketMinds Analytics
![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711241305/amiresponsive_b86ttt.png) 


## Introduction
Our platform is a Django-based solution for managing and selling subscription plans in the trading sector. It features a custom admin panel that allows site administrators to control subscription plans thoroughly, with complete CRUD (Create, Read, Update, Delete) capabilities. Integrated with Stripe API, the platform ensures secure payment processing and maintains database integrity through Stripe webhooks for all subscription-related operations.

Additionally, the platform includes 'Trade Insights,' a content delivery system that allows for the direct provision of trading resources and information to subscribers, bypassing the need for external media platforms. Administrators have full control over this content, ensuring timely and relevant updates.

A key component is the 'Platform Metrics' section in the admin panel, providing administrators with essential financial data and metrics about the site and its subscriptions. This helps in making informed decisions about the site's operation and growth.

Overall, the platform offers a comprehensive toolset for subscription management and content delivery in the trading domain, emphasizing security, reliability, and ease of administration.
[Click here to view the Live Project](https://marketminds-analytics-31d309061593.herokuapp.com/)


## Table of contents
- [Features](#Features)
- [User Stories (US)](#User-Stories-(US))
- [Technical Details and Design](#Design)
- [Technologies Used](#Technologies-Used)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Business Plan](#Business-Plan)
- [SEO](#Search-Engine-Optimization)
- [Credits](#Credits)


## Features

### Existing Features

-   **F 1.0 - Landing Page**
    -   **F 1.1** - Navigation Bar (present on all pages)
    -   **F 1.2** - Hero Image with Hero Text 
    -   **F 1.3** - Services Information with Credentials 
    -   **F 1.4** - Stay in Touch section with Social Links and Mailchimp   Newsletter Form
    -   **F 1.5** - Footer (present on all pages)

-   **F 2.0 - Get Started Page** 
    -   **F 2.1** - Special Offers section
    -   **F 2.2** - Subscription Plan section

-   **F 3.0 - Trade Insight Page**
    -   **F 3.1** - TradingView Ticker Tape (present on all Trade Insight pages)
    -   **F 3.2** - TradingView Global Markets (present on all Trade Insight pages)
    -   **F 3.3** - TradingView News (present on all Trade Insight pages)
    -   **F 3.5** - Subscription Showcase (present aon all Trade Insight pages)
    -   **F 3.6** - Trade Insight Mainstage
    -   **F 3.7** - Trade Insight Secondstage

-   **F 4.0 - Tade Insight Detail Page**
    -   **F 4.1** - Insight Full Content/Restricted Content

-   **F 5.0 - Admin Access Subscription Plan Page**
    -   **F 5.1** - Subscription Plan CRUD

-   **F 6.0 - Admin Access Trade Insight Page**
    -   **F 6.1** - Trade Insight CRUD

-   **F 7.0 - Admin Access Financial Metrics Page**
    -   **F 6.1** - Financial Metrics Data Charts Diagrams

-   **F 8.0 - User Profile Information Page**
    -   **F 8.1** - User Profile Information CRUD
    -   **F 8.2** - User Profile Active Subscription Terminal











## User Experience (UX)

### User stories

- **__US01 - Visitor:__**
    - As a visitor, I want to see a clear and engaging landing page that highlights the benefits of subscribing to MarketMinds Analytics.
    - As a visitor, I want to easily navigate through the site to learn more about available subscription plans for crypto, forex, and stocks.

- **__US02 - Registered User:__**
    - As a registered user, I want to have my own profile where I can view and manage my active subscriptions.
    - As a registered user, I want the ability to edit my profile information, including personal details and subscription preferences.

- **__US03 - Subscriber:__**
    - As a subscriber, I want to receive regular market insights, trade recommendations, and updates based on my chosen subscription plan.
    - As a subscriber, I want the option to unsubscribe or switch to a different subscription plan at any time.

- **__US04 - Superuser (Site Owner):__**
    - As a superuser, I want to access a custom admin panel to add, edit, or delete subscription plans.
    - As a superuser, I want to view analytics and user statistics to understand the popularity of different subscription plans.

- **__US05 - Admin Access User:__**
    - As an admin access user, I want to log in and access a dedicated admin page outside the Django admin to manage the platform.
    - As an admin access user, I want the ability to perform administrative tasks such as managing users, reviewing analytics, and handling support requests.

- **__US06 - Potential Subscriber:__**
    - As a potential subscriber, I want to easily find information about the benefits of each subscription plan before making a decision.
    - As a potential subscriber, I want a straightforward and secure subscription process with clear pricing information.

- **__US07 - User Interested in Updates:__**
    - As a user interested in updates, I want the option to subscribe to newsletters or notifications to receive the latest market trends and special offers.






## Design
-   ### Styling
    -  For Styling the Bootstrap 4.6.2 library was imported. Additionaly you will find some custom CSS in the project level static folder, app level static folder and occasionally inline styling to fit in some custom needs.

-   ### Colour Scheme
    -  The color Scheme is adjusted to mainly provide good contrast and readability but still offers an appealing design and fit the theme of Trading.
    -  As "theme-color" I chose #00b4d8 which is a modern and eye catching blue. I used this also to design the MarketMinds Analytics Logo, coloring buttons and various other element's.
    -  For background's and menu element's I decided to utilizie a color panel consisting of #0d1b2a, #1b263b, #415a77 and , #1b4965. These color in conjunction provide good contrast and complement each other.
    -  For seperation lines I chose a signaling color #FCA311.
    -  Font Color is adjusted through the game to give good contrast to specific background-color.
        -   Color Palette
        ![ColorPalette](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705672444/color_palette_xct6l3.png)

-   ### Typography
    -   Google Fonts was utilized to import fonts into styles.css. Lato was chosen for the majority of the content due to its excellent readability. Rubik Mono One was selected for specific titles and various elements to make them stand out and distinguish them from the rest of the content.

-   ### Wireframes
    ![Landing](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705686222/figma_landing_page_i1xthl.png)
    ![GetStarted](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705686221/figma_get_started_page_g0vzcs.png)
    ![Bag](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705686222/figma_bag_yo98nu.png)
    ![Checkout](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705686223/figma_checkout_awiwky.png)
    ![Profile](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705686223/figma_profile_ri58zv.png)
    ![Admin](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705686222/figma_admin_access_zhgpsp.png)

### Database Models

#### ActiveSubscription

| Field                | Type                  | Description                                   |
|----------------------|-----------------------|-----------------------------------------------|
| user                 | ForeignKey(User)      | User associated with the active subscription. |
| subscription_plan    | ForeignKey(SubscriptionPlan) | Subscription plan associated with the subscription.|
| start_date           | DateTimeField         | Date and time when the subscription started.  |
| end_date             | DateTimeField         | Date and time when the subscription ends.     |
| status               | CharField             | Status of the subscription (e.g., Active, Expired).|
| payment_status       | CharField             | Payment status of the subscription.           |
| created_at           | DateTimeField         | Date and time of creation.                    |
| purchase_number      | CharField             | Unique purchase number (UUID) associated with the subscription.|

##### Methods:

- `is_expired`: Check if the subscription has expired.
- `refresh_subscription`: Refresh the subscription by extending the end date by 30 days.

##### Internal Methods:

- `_generate_purchase_number`: Generate a unique purchase number using UUID.

##### `__str__` Method:

- Returns a string representation of the active subscription, showing the subscription plan title and start date.

---

#### SubscriptionPlan

Model representing a subscription plan.

| Field       | Type              | Description                                           |
|-------------|-------------------|-------------------------------------------------------|
| title       | CharField         | Title of the subscription plan.                        |
| image       | ImageField        | Image uploaded for the subscription plan.              |
| description | TextField         | Description of the subscription plan.                 |
| price       | DecimalField      | Price of the subscription plan.                        |
| details     | TextField         | Additional details about the subscription plan.        |
| sku         | CharField         | Stock keeping unit (optional) associated with the plan.|

##### `__str__` Method:

- Returns a string representation of the subscription plan, showing its title.

---

#### UserProfile

Model representing user profile information.

| Field             | Type              | Description                                            |
|-------------------|-------------------|--------------------------------------------------------|
| user              | OneToOneField(User)| One-to-One relationship with the User model.           |
| bio               | TextField         | Text field for user's bio or description.              |
| birth_date        | DateField         | Date field for user's birth date.                       |
| full_name         | CharField         | Char field for user's full name.                        |
| email             | EmailField        | Email field for user's email address.                   |
| phone_number      | CharField         | Char field for user's phone number.                     |
| country           | CharField         | Char field for user's country.                          |
| postcode          | CharField         | Char field for user's postal code.                      |
| town_or_city      | CharField         | Char field for user's town or city.                     |
| street_address1   | CharField         | Char field for user's street address (line 1).          |
| street_address2   | CharField         | Char field for user's street address (line 2).          |
| county            | CharField         | Char field for user's county.                           |

##### Methods:

- `get_active_subscriptions`: Returns active subscriptions for the user.

##### Signal Receiver:

- `create_or_update_user_profile`: Creates or updates a user profile upon User creation or update.



## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Django Template Language](https://docs.djangoproject.com/en/4.2/ref/templates/language/)
-   [Markdown](https://de.wikipedia.org/wiki/Markdown)


### Frameworks, Libraries & Programs Used

- [Gitpod:](https://gitpod.io) Used as the IDE for code development, offering compatibility with GitHub and useful IDE extensions.

- [GitHub:](https://github.com/) Repository for the project's code, facilitating version control and collaboration.

- [Heroku:](https://heroku.com) Platform used for deploying the project to make it accessible online.

- [Django:](https://docs.djangoproject.com/en/5.0/) Main framework for rapid development and pragmatic design in Python.

- [django-allauth:](https://github.com/pennersr/django-allauth) Manages everything from registration to account management.

- [django-crispy-forms:](https://github.com/django-crispy-forms/django-crispy-forms) Enhances Django forms with Bootstrap for easy customization.

- [django-summernote:](https://github.com/summernote/django-summernote) Provides simple WYSIWYG editing in Django for content creation.

- [gunicorn:](https://docs.gunicorn.org/en/stable/) Handles Python WSGI HTTP Server and deployment for Django.

- [Pillow:](https://pillow.readthedocs.io/en/stable/) Image processing library for handling image files in Django applications.

- [python-dotenv:](https://github.com/theskumar/python-dotenv) Reads key-value pairs from a .env file, setting them as environment variables.

- [s3transfer:](https://pypi.org/project/s3transfer/) Python library for transferring files to/from Amazon S3, used in conjunction with boto3.

- [stripe:](https://stripe.com/docs) Payment processing library for secure credit card payments on checkout.

- [aws-s3-bucket:](https://docs.aws.amazon.com/s3/) Storage connected with Django application to store and serve media and static files to Heroku.

- [boto3:](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) AWS SDK for Python, interacts with AWS services, used for managing static and media files on Amazon S3.

- [oauthlib:](https://github.com/oauthlib/oauthlib) Handles OAuth request-signing logic.

- [asgiref:](https://pypi.org/project/asgiref/) Handles asynchronous request handling in Django.

- [dj-database-url:](https://pypi.org/project/dj-database-url/) Utilized for database URLs in Django settings.

- [dj3-cloudinary-storage:](https://pypi.org/project/dj3-cloudinary-storage/) Custom storage backend for Django using Cloudinary.

- [psycopg2:](https://pypi.org/project/psycopg2/) Enables Python code to execute PostgreSQL commands.

- [cloudinary:](https://cloudinary.com) Database used in the deployed version of the project.

- [Bootstrap:](https://getbootstrap.com) CSS framework used for styling the project.

- [ILoveImg:](https://www.iloveimg.com) Used for resizing images and editing photos for the website.

- [Figma:](https://www.figma.com/) Utilized for creating wireframes during the design process.

- [Canva:](https://www.canva.com) Used for designing a logo.

- [Google Fonts:](https://fonts.google.com/) Imported fonts for use in the project.

- [Font Awesome:](https://fontawesome.com/) Added icons for aesthetic and UX purposes.



## Testing

### Validating Code
#### HTML & CSS
W3C Markup Validator (https://validator.w3.org/)      
W3C CSS Validator (https://jigsaw.w3.org/css-validator/)

- While these validators effectively assess standard HTML and CSS, they encountered issues comprehending Django's templating language, resulting in reported errors. However, it's important to note that the standard HTML and custom CSS passed validation without errors when processed through these validators.

#### JavaScript
JSHint (https://jshint.com/)

- JavaScript was only sporadically used in this Project but its still worth to note that it gets error free validated by JSHint

#### Python
Pylint (https://pylint.pycqa.org/en/latest/)
Black (https://black.readthedocs.io/en/stable/)

- I integrated Pylint into my project to ensure adherence to the PEP 8 standard. 
- I used Black for autocode formatting to strictly align with PEP 8 guidelines, ensuring consistent and readable code.

The 'Too few public methods' warnings in various classes suggests the potential need for additional methods. However, considering the current functionality of the Classes and Form, its purpose is adequately fulfilled with the existing structure. No further methods are required to enhance their functionality or readability, hence, the warnings can be disregarded.


### Performance

Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website. 

- **Landing**
![Landing](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705704749/lighthouse_testing_landing_pvojuv.png)
- **Get Started**
![Get Started](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705704749/lighthouse_testing_get_started_n64oof.png)
- **Profile**
![Profile](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705704749/lighthouse_testing_profile_zr1mcs.png)
- **Admin**
![Admin](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705704748/lighthouse_testing_admin_s4ra9i.png)

### Test Cases and Results
#### Manual Testing
##### Allauth Login and Registration

| Test Case                    | Expected Outcome                                                  | Test Passed |
|------------------------------|-------------------------------------------------------------------|--------------|
| Register with valid details  | Confirmation email sent, user redirected to the site as logged in | ✔️     |
| Register with existing email | Form not submitting                                                 | ✔️     |
| Register with invalid data   | Form not submitting                                                | ✔️     |
| Login with correct details   | Redirects user to authenticated area/dashboard                   | ✔️     |
| Login with incorrect password| Error message indicates invalid login credentials                 | ✔️     |


##### Profile Functionality

| Test Case                     | Expected Outcome                                                  | Test Passed |
|-------------------------------|-------------------------------------------------------------------|--------------|
| View Profile                  | Displays user profile information and active subscriptions.        | ✔️     |
| Edit Profile                  | Allows the user to update profile information successfully.         | ✔️     |
| Cancel Active Subscription    | Successfully cancels an active subscription.                        | ✔️     |
| Attempt to Edit with Invalid Data | Displays validation errors and does not save changes.           | ✔️     |

##### Bag View
| Test Case                  | Expected Outcome                                                    | Test Passed |
|----------------------------|---------------------------------------------------------------------|--------------|
| Access Bag Page            | Successfully loads the bag page with saved subscription plans.       | ✔️     |
| Deleting Bag items                  | Bag items gets successfully deleted  | ✔️     |


##### Add to Bag Functionality
| Test Case                  | Expected Outcome                                                                 | Test Passed |
|----------------------------|----------------------------------------------------------------------------------|--------------|
| Add Plan to Bag            | Adds a subscription plan to the bag and redirects to 'get_started'.               | ✔️     |
| Plan Already in Bag        | When attempting to add a plan already in the bag, displays an appropriate message.| ✔️     |

##### Get Started View
| Test Case                | Expected Outcome                                                       | Test Passed |
|--------------------------|------------------------------------------------------------------------|--------------|
| Access GetStarted Page   | Successfully loads the page displaying subscription plans.              | ✔️     |
| Pagination               | Displays subscription plans paginated, with 6 plans per page.           | ✔️     |
| Plans Ordered            | Plans are displayed in ascending order based on their IDs.              | ✔️     |

##### Admin Access View
| Test Case          | Expected Outcome                                   | Test Passed |
|--------------------|----------------------------------------------------|--------------|
| Access Admin Panel | Successfully loads the admin panel page.           | ✔️     |
| Sort Plans         | Clicking on the sort button sorts the plans.       | ✔️     |
| Delete Plan        | Clicking on delete removes the selected plan.      | ✔️     |

##### Admin Access Add Functionality
| Test Case          | Expected Outcome                                       | Test Passed |
|--------------------|--------------------------------------------------------|--------------|
| Add New Plan       | Successfully adds a new plan through the form.         | ✔️     |
| Invalid Form Data  | Form does not submit.                                  | ✔️     |
| Redirect           | After adding, user is redirected to admin access page. | ✔️     |

##### Admin Access Delete Functionality
| Test Case             | Expected Outcome                                    | Test Passed |
|-----------------------|-----------------------------------------------------|--------------|
| Delete Existing Plan  | Successfully deletes an existing plan by its ID.    | ✔️     |
| Redirect              | After deletion, user is redirected to admin access. | ✔️     |

##### Admin Access Edit Functionality
| Test Case          | Expected Outcome                                       | Test Passed |
|--------------------|--------------------------------------------------------|--------------|
| Edit Plan           | Successfully edits an existing plan through the form.  | ✔️     |
| Invalid Form Data  | Form does not submit                                  | ✔️     |
| Redirect           | After editing, user is redirected to admin access.     | ✔️     |

##### Checkout View
| Test Case                          | Expected Outcome                                                              | Test Passed |
|------------------------------------|-------------------------------------------------------------------------------|--------------|
| Access Checkout Page               | Successfully loads the checkout page.                                         | ✔️     |
| Already subscribed                | Disable checkout function and notify user that he has already subscribed.              | ✔️     |
| Remove Item from checkout                 | Successfully remove a item from the bag via the checkout page if notified.              | ✔️     |
| User Authenticated                 | Checks if the user is authenticated to proceed with the checkout.              | ✔️     |
| Process Subscription Payment       | Completes the subscription payment for selected plans.                         | ✔️     |
| Subscription Creation              | Successfully creates a subscription after payment.                              | ✔️     |
| Save User Profile                  | Checks if user profile information is saved if 'save-info' checkbox is selected.| ✔️     |
| Bag Items Removed                  | Ensures bag items are removed from the session after checkout.                  | ✔️     |
| Stripe Integration                 | Verifies that the Stripe integration works properly.                            | ✔️     |
| Stripe webhook handler          | Handles creating entry in database for Active Subscription after payment intent succeeded if form submission/checkout view fails to do so.           | ✔️     |


### Browser Compatibility

- Testing has been carried out on the following browsers :
    - Chrome Version 119.0.6045.200 (Official Build) (64-bit)
    - Firefox Version 120.0.1 (64-Bit)
    - Safari on iPhone (iOS-Version 17.1 (c))


## Deployment


### Deployment to Heroku:

1. **Create a new Database at ElephantSQL:**
   - Set up a new database on ElephantSQL, an external PostgreSQL database service.

2. **Create a new Heroku App:**
   - Set up a new Heroku app for deploying the project.

3. **Save Database URL as Config Var in Heroku:**
   - Obtain the database URL from ElephantSQL and save it as a config variable in Heroku (e.g., `DATABASE_URL`).

4. **Install Required Packages:**
   - Install `dj_database_url` and `psycopg2` using the command `pip3 install dj_database_url==0.5.0 psycopg2`, which are necessary to connect to an external database.
   - Save the installed packages using `pip3 freeze > requirements.txt`.

5. **Update Django Settings:**
   - Import `dj_database_url` in the project settings.
   - Modify the `DATABASES` setting to dynamically choose the appropriate database based on the environment:
     ```python
     if 'DATABASE_URL' in os.environ:
         DATABASES = {
             'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
         }
     else:
         DATABASES = {
             'default': {
                 'ENGINE': 'django.db.backends.sqlite3',
                 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
             }
         }
     ```

6. **Database Migrations and Superuser:**
   - Run `python3 manage.py showmigrations` to ensure all migrations are listed.
   - Apply migrations with `python3 manage.py migrate`.
   - If applicable, load fixture data using `python3 manage.py loaddata "fixtures"`.
   - Create a superuser with `python3 manage.py createsuperuser`.

7. **Configure Procfile for Gunicorn:**
   - Install Gunicorn with `pip3 install gunicorn` and save the package in `requirements.txt`.
   - Create a `Procfile` with the command `web: gunicorn marketminds_analytics.wsgi`.

8. **Heroku Deployment:**
   - Log in to Heroku with `heroku login`.
   - Temporarily disable static file collection with `heroku config:set DISABLE_COLLECTSTATIC=1 --app marketminds-analytics`.
   - Add Heroku as a remote branch with `git remote add heroku marketminds-analytics`.
   - Deploy the project to Heroku using `git push heroku master`.

9. **Configure Allowed Hosts:**
   - After deployment, access the Heroku app URL from the error message.
   - Add the Heroku app URL to the `ALLOWED_HOSTS` setting in Django.

10. **Final Deployment:**
    - Push the changes to GitHub.
    - Deploy again on Heroku, ensuring the `ALLOWED_HOSTS` change is included.

11. **Automatic GitHub Deployment in Heroku:**
    - Set up automatic deployment from GitHub in the Heroku dashboard for practical and convenient deployments.

12. **Handling Static Files:**
    - Later define environment variables for AWS serving the static and media files after CSV file in AWS for the s3bucket is created.


### Database Setup: 
#### Steps to Create and Configure S3 Bucket for Django Project on Heroku:
1. **Create an S3 Bucket:**
   - Log in to the [AWS Management Console](https://aws.amazon.com/).
   - Navigate to the S3 service.
   - Click on "Create bucket."
   - Choose a unique name for your bucket and select the region.

2. **Configure Bucket Permissions:**
   - In the bucket properties, go to the "Permissions" tab.
   - Edit the bucket policy to allow public access. Replace `"BucketName"` with your actual bucket name.
     ```json
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Effect": "Allow",
                 "Principal": "*",
                 "Action": "s3:GetObject",
                 "Resource": "arn:aws:s3:::BucketName/*"
             }
         ]
     }
     ```

3. **Create IAM User and Group:**
   - Navigate to the IAM (Identity and Access Management) service.
   - Create a new group (e.g., `S3-Group`) and attach the `AmazonS3FullAccess` policy to it.
   - Create a new user (e.g., `S3-User`) and add them to the group.

4. **Generate AWS Access Keys:**
   - Generate AWS access keys for the `S3-User`.
   - Save the access key and secret key securely.

5. **Download Access Keys CSV:**
   - Create a CSV file containing the access key and secret key.
   - Download the CSV file for future reference.

6. **Configure Django Settings:**
   - Install the required packages:
     ```
     pip install boto3 django-storages
     ```

7. **Update Django Settings:**
   - Add the following configurations to your Django settings:
     ```python
     AWS_ACCESS_KEY_ID = 'YourAccessKey'
     AWS_SECRET_ACCESS_KEY = 'YourSecretKey'
     AWS_STORAGE_BUCKET_NAME = 'YourBucketName'
     AWS_S3_REGION_NAME = 'YourRegion'
     AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
     AWS_DEFAULT_ACL = 'public-read'
     ```

8. **Use `django-storages` for Static and Media Files:**
   - Update your `STATICFILES_STORAGE` and `DEFAULT_FILE_STORAGE` settings in Django settings:
     ```python
     STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
     ```

9. **Update AWS CORS Configuration (Optional but Recommended):**
   - Add CORS rules to your S3 bucket to allow requests from your Heroku app.
   - Edit the bucket CORS configuration:
     ```xml
     <CORSConfiguration>
         <CORSRule>
             <AllowedOrigin>https://your-heroku-app.herokuapp.com</AllowedOrigin>
             <AllowedMethod>GET</AllowedMethod>
             <MaxAgeSeconds>3000</MaxAgeSeconds>
             <AllowedHeader>Authorization</AllowedHeader>
         </CORSRule>
     </CORSConfiguration>
     ```

10. **Update `ALLOWED_HOSTS` in Django Settings:**
   - Add your Heroku app URL to the `ALLOWED_HOSTS` setting:
     ```python
     ALLOWED_HOSTS = ['your-heroku-app.herokuapp.com']
     ```

11. **Deploy Changes:**
   - Deploy your Django project to Heroku with the updated settings.

12. **Test the Deployment:**
   - AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY need to be set in Heroku Config Vars.
   - Visit your Heroku app and ensure static and media files are being served from the S3 bucket.



### How to clone the repository

- Go to the https://arp-25.github.io/tradeconnect/ repository on GitHub.
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there.
- Open a GitBash terminal and navigate to the directory where you want to locate the clone.
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process.


## Business Plan 
-   **__1 - Executive Summary__**
    - **Overview:**
      - Subscription-based market analysis for forex, crypto, and stock markets.
    - **Mission:**
      - Providing Subscribers with in depth market analysis which enables subscriber to trade profitable. 

-   **__2 - Business Description__**
    - **Services:**
        - Market Analysis and outlooks which contain potential buying and selling zones.
    - **Target Audience:**
      - Traders and Investors.

-   **__3 - Subscription Plans__**
    - **Plan Structure:**
      - Every Plan consists of its basic buy and selling , market outlooks and some dynmaic content depening on market conditions.
    - **Pricing:**
      - Targeting below 100$/month for each package.

-   **__4 - Marketing and Sales__**
    - **Marketing Strategy:**
      - Digital marketing, social media, and partnerships.
    - **Sales Channels:**
      - Website.
    - **Customer Acquisition:**
      - Count in costs for customer acquisition.

-   **__5 - Operational Plan__**
    - **Technology:**
      - The subscriber will receive an email containing written analyses accompanied by pictures and/or videos. In the later stages of MarketMinds Analytics webpage development, a database for market analyses and a user interface (UI) for accessing them will be implemented.

    - **Team:**
      - Market Analyst's and Software Developer's.

-   **__6 - Metrics for Success__**
    - **Key Performance Indicators (KPIs) for measuring success:**
      - Number of subscribers, retention rate, revenue growth.


## SEO Optimization Implementation in Project:

### On-Page SEO Strategies:
1. **Keyword Placement:**
   - Utilized semantic HTML elements (h1, h2, strong, em, nav, header, a, etc.) for strategic keyword placement.

2. **rel="noopener" for Social Anchor Tags:**
   - Applied `rel="noopener"` to social anchor tags to indicate to search engines not to assess them for ranking, as they do not contribute significant information about the page.

3. **Alt Attribute for Images:**
   - Included relevant keywords in the `alt` attribute of images for better search engine understanding.

4. **Filename Descriptions for Images:**
   - Ensured descriptive filenames for images to enhance search engine optimization.

5. **Head Section Optimization:**
   - Placed the most important keywords, meta description, and meta keywords in the head section of HTML files.

### Off-Page SEO Strategies:
1. **Sitemap.xml:**
   - Generated and implemented an XML sitemap (sitemap.xml) in the root directory to provide search engines with a structured understanding of the website's URLs.

2. **Robots.txt:**
   - Improved SEO ranking by configuring the `robots.txt` file with directives like:
     ```txt
        User-agent: *
        Disallow: /login/
        Disallow: /register/
        Disallow: /admin/
        Sitemap: https://marketminds-analytics-31d309061593.herokuapp.com/sitemap.xml
     ```

## Credits 


### Code

Examples and instructions for basic html and CSS code:

- https://developer.mozilla.org
- https://www.w3schools.com
- https://learn.codeinstitute.net/

Additional searching for problemfixes:

- https://stackoverflow.com
- https://www.youtube.com/?gl=DE&hl=de

### Media 
- All images are bought and licensed from https://stock.adobe.com/.
- All icons were taken from [Font Awesome](https://fontawesome.com/).
- All fonts used were imported from [Google Fonts](https://fonts.google.com/).


### Shoutout

Special thanks to my Mentor Oluwafemi Medale for helping me out whenever I have a question.



## Update 24.03.2024

### New Features

- New Design for Landing Page
- Content Delivery System "Trade Insights"
- New Design Profile Info Page and New Functionalities
- New Design Admin Access Page and New Functionalities
