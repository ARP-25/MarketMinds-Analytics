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
- [Features x User Stories](Features-x-User-Stories)
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
    -   **F 1.5** - Interactive Footer (present on all pages)
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296233/navbar_hero_kphpmk.png) 
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296238/services_credentials_yw5pl9.png) 
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296238/socials_newsletter_x3tbsm.png) 
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296231/footer_wew99n.png) 


-   **F 2.0 - Get Started Page** 
    -   **F 2.1** - Special Offers section
    -   **F 2.2** - Subscription Plan section
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296674/get_started_1_fduhwh.png) 
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296671/get_started_2_zq4icp.png)  


-   **F 3.0 - Trade Insight Page**
    -   **F 3.1** - TradingView Ticker Tape (present on all Trade Insight pages)
    -   **F 3.2** - TradingView Global Markets (present on all Trade Insight pages)
    -   **F 3.3** - TradingView News (present on all Trade Insight pages)
    -   **F 3.5** - Subscription Showcase (present aon all Trade Insight pages)
    -   **F 3.6** - Trade Insight Mainstage
    -   **F 3.7** - Trade Insight Secondstage
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296242/trade_insight_page_1_qmgn5w.png)  
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296243/trade_insight_page_2_gproap.png)  
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296244/trade_insight_page_3_zvprnt.png)  


-   **F 4.0 - Tade Insight Detail Page**
    -   **F 4.1** - Insight Full Content/Restricted Content
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296239/trade_insight_detail_page_1_yjsm5a.png)  
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296241/trade_insight_detail_page_2_pwqufr.png)  


-   **F 5.0 - Admin Access Subscription Plan Page**
    -   **F 5.1** - Subscription Plan CRUD
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296230/aa_splan_xsecnb.png)  


-   **F 6.0 - Admin Access Trade Insight Page**
    -   **F 6.1** - Trade Insight CRUD
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296229/aa_insight_kfp2vl.png)  


-   **F 7.0 - Admin Access Financial Metrics Page**
    -   **F 6.1** - Financial Metrics Data Charts Diagrams
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296229/aa_metrics_vic3vk.png)  


-   **F 8.0 - User Profile Information Page**
    -   **F 8.1** - User Profile Information CRUD
    -   **F 8.2** - User Profile Active Subscription Terminal
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296234/profile_info_1_cyv1os.png)  
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296236/profile_info_3_orjbjo.png)  
    ![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296236/profile_info_2_iir0v7.png)  





## User Stories (US)

### 1. Newsletter Subscription
- **As a** website visitor,  
  **I want to** subscribe to a newsletter,  
  **So that** I can stay informed about the latest news, updates, and offers from the platform.

### 2. Social Media Engagement
- **As a** user,  
  **I want to** easily find and follow the platform’s social media profiles from the website,  
  **So I can** engage with their content and stay connected with their community.

### 3. Checkout Confirmation Email
- **As a** customer,  
  **After** completing a purchase,  
  **I want to** receive a confirmation email,  
  **So that** I can have detailed information and a record of my transaction.

### 4. Admin CRUD Functionality for Subscription Plans
- **As an** admin,  
  **I need** full Create, Read, Update, and Delete (CRUD) capabilities for managing subscription plans,  
  **So that** I can effectively maintain and tailor the subscription options to meet customer demands and business needs.

### 5. Admin CRUD Functionality for Trade Insights
- **As an** admin,  
  **I require** the ability to create, view, modify, and remove trade insights,  
  **So that** I can ensure the content is current, relevant, and valuable for my subscribers.

### 6. Accessing Subscription Services
- **As a** subscriber,  
  **I want to** have a dedicated platform or medium through which I can access and utilize the services provided by my subscription,  
  **Ensuring that** I receive the full value of the content and features available to me.

### 7. Exploring Services and Company Information
- **As a** website visitor,  
  **I want to** learn more about the services and the company,  
  **So that** I can better understand what is being offered and who is providing these services.

### 8. Admin Access to Platform Metrics
- **As an** admin,  
  **I want to** have an overview of the platform metrics, particularly financial metrics,  
  **So that** I can understand the performance of the platform in terms of active subscriptions and revenue.


## Features x User Stories
| Feature ID | Feature Description                                  | User Story 1 | User Story 2 | User Story 3 | User Story 4 | User Story 5 | User Story 6 | User Story 7 | User Story 8 |
|------------|------------------------------------------------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| F 1.1      | Navigation Bar (present on all pages)                |              | ✔            |              |              |              |              |              |              |
| F 1.2      | Hero Image with Hero Text                            |              |              |              |              |              |              | ✔            |              |
| F 1.3      | Services Information with Credentials                |              |              |              |              |              |              | ✔            |              |
| F 1.4      | Stay in Touch section with Social Links and Mailchimp| ✔            | ✔            | ✔            |              |              |              | ✔            |              |
| F 1.5      | Interactive Footer (present on all pages)            |              |              |              |              |              |              | ✔            |              |
| F 2.1      | Special Offers section                               |              |              |              |              |              |              |         ✔     |              |
| F 2.2      | Subscription Plan section                            |              |              |              | ✔            |              | ✔            |              |              |
| F 3.1-3.7  | Various Trade Insight Features                       |              |              |              |              | ✔            | ✔            |              |              |
| F 4.1      | Insight Full Content/Restricted Content              |              |              |              |              | ✔            | ✔            |              |              |
| F 5.1      | Subscription Plan CRUD                               |              |              |              | ✔            |              |              |              |              |
| F 6.1      | Trade Insight CRUD                                   |              |              |              |              | ✔            |              |              |              |
| F 7.1      | Financial Metrics Data Charts Diagrams               |              |              |              |              |              |              |              | ✔            |
| F 8.1-8.2  | User Profile Information and Subscription Terminal   |              |              | ✔            |              |              | ✔            |              |              |

Legend:
✔ - This feature supports the corresponding user story.



## Technical Details and Design
### ERD-Diagram
![titelimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296246/ERD_MMA_uncut_kyd9qi.png)

### Database Models
#### UserProfile
| Field Name          | Data Type          | Description                    |
|---------------------|--------------------|--------------------------------|
| user                | OneToOneField      | Link to the Django User model  |
| email               | EmailField         | Email address of the user      |
| stripe_customer_id  | CharField          | Stripe Customer ID             |

#### ActiveSubscription
| Field Name            | Data Type      | Description                                |
|-----------------------|----------------|--------------------------------------------|
| user                  | ForeignKey     | Link to the User model                     |
| subscription_plan     | ForeignKey     | Link to the SubscriptionPlan model         |
| stripe_subscription_id| CharField      | Stripe Subscription ID                     |
| start_date            | DateTimeField  | Subscription start date                    |
| current_period_end    | DateTimeField  | End of the current subscription period     |
| renewal_date          | DateTimeField  | Date of the next renewal                   |
| canceled_at           | DateTimeField  | Date when the subscription was canceled    |
| status                | CharField      | Subscription status                        |
| created_at            | DateTimeField  | Creation date of the subscription record   |
| billing_amount        | DecimalField   | Total amount billed                        |
| monthly_cost          | DecimalField   | Monthly cost of the subscription           |

#### SubscriptionPlan
| Field Name       | Data Type      | Description                                 |
|------------------|----------------|---------------------------------------------|
| title            | CharField      | Title of the subscription plan              |
| image            | ImageField     | Image representing the plan                 |
| description      | TextField      | Description of the plan                     |
| price            | DecimalField   | Price of the plan                           |
| details          | TextField      | Additional details about the plan           |
| created_at       | DateTimeField  | Creation date of the plan                   |
| staged           | BooleanField   | Indicates if the plan is staged             |
| stripe_price_id  | CharField      | Stripe price ID                             |

#### Insight Model
| Field Name        | Data Type      | Description                             |
|-------------------|----------------|-----------------------------------------|
| title             | CharField      | Title of the insight                    |
| slug              | SlugField      | SEO-friendly URL slug                   |
| release_date      | DateField      | Release date of the insight             |
| content           | TextField      | Main content of the insight             |
| category          | ForeignKey     | Linked subscription plan                |
| short_description | TextField      | Brief summary of the insight            |
| author            | ForeignKey     | Author of the insight                   |
| cover_image       | ImageField     | Optional cover image                    |
| stage             | CharField      | Categorization of the insight           |
| display           | CharField      | Display type (e.g., Text, Image)        |


#### Financial Metrics
| Field Name             | Data Type     | Description                              |
|------------------------|---------------|------------------------------------------|
| period                 | DateField     | Date for the financial metrics            |
| monthly_revenue        | DecimalField  | Total revenue for the month              |
| renewed_subscriptions  | IntegerField  | Number of renewed subscriptions          |
| new_subscriptions      | IntegerField  | Number of new subscriptions              |
| canceled_subscriptions | IntegerField  | Number of canceled subscriptions         |


#### Relationships
- `UserProfile` has a one-to-one relationship with `User`.
- `ActiveSubscription` has foreign key relationships with `User` and `SubscriptionPlan`.
- `Insight` is linked to `SubscriptionPlan` (category) and `UserProfile` (author).
- `SubscriptionPlan` is related to `ActiveSubscription` and `Insight`.
- `FinancialMetrics` does not have direct relationships with other models.



### Django Signals

Django signals are used in the application to automatically update the `FinancialMetrics` model in response to changes in the `ActiveSubscription` model. This ensures the financial data remains accurate and up-to-date.

#### Signal: `post_save` on `ActiveSubscription`

- **Purpose**: To update financial metrics upon subscription changes (creation, renewal, cancellation).
- **Method**: `update_metrics_on_subscription_update`.
- **Trigger**: After saving an instance of `ActiveSubscription`.
- **Functionality**:
  - Increments the count of new, renewed, or canceled subscriptions.
  - Adjusts the monthly revenue in `FinancialMetrics` model.
- **Notes**:
  - Automatically invoked post-save of an `ActiveSubscription`.
  - Determines the current period and updates or creates `FinancialMetrics` accordingly.

### Stripe Webhooks
Stripe webhooks synchronize the application's database with Stripe's subscription data. They react to specific events from Stripe, updating `ActiveSubscription` and `SubscriptionPlan` models.

#### Webhook Endpoint
- **Function**: `stripe_webhook`.
- **Responsibility**: To process and respond to Stripe events.
- **Implementation**: Verifies events' authenticity and dispatches them to respective handlers.

#### Event Handling
- **Subscription Events**: Managed by updating the `ActiveSubscription` instances.
- **Price Events**: Modify `SubscriptionPlan` instances to reflect changes in Stripe's pricing.

#### Integration with Models

- `ActiveSubscription`: Updated by subscription-related webhooks to mirror Stripe's data.
- `SubscriptionPlan`: Modified via price-related webhooks, representing current subscription plans.

#### Summary

The use of Django signals and Stripe webhooks ensures real-time data integrity and synchronization between this Django application and Stripe's subscription services. This system is key to maintaining accurate subscription statuses and financial metrics.


### Design
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



## Validating
### W3C Markup Validator ([W3C Validator](https://validator.w3.org/))

#### Pages Validated and Error-Free:
- Landing Page
- Get Started
- Bag
- Checkout
- Checkout Success
- Profile Info (with specific note)
- Edit Profile
- Admin Access Subscription
- Admin Access Subscription Add
- Admin Access Subscription Edit
- Admin Access Insight (with specific note)
- Admin Access Insight Add (with specific note)
- Admin Access Insight Edit (with specific note)
- Admin Access Financial Metrics

#### Pages with Notable Validation Results:

##### Trade Insight and Trade Insight Detail View:
- **Error Noted**: _Expected space, tab, newline, or slash in script content but found {...}_
- **Explanation**: The error is related to embedding JSON in script tags for the TradingView widget. This practice is standard for many external widgets. It's considered safe to ignore due to its widespread use, lack of impact on functionality, and SEO neutrality.

##### Profile Info:
- **Error Noted**: _Bad value for attribute action on element form: Must be non-empty._
- **Explanation**: The action attribute of the form is dynamically filled using JavaScript, making this validation error negligible as the functionality is ensured through the script that dynamically creates the required action attribute.

##### Admin Access Subscription:
- **Error Noted**: _Bad value for attribute action on element form: Must be non-empty._
- **Explanation**: Similar to Profile Info, the form's action attribute is dynamically assigned via a script, ensuring proper functionality despite the validation error.

##### Admin Access Insight View:
- **Error Noted**: _Bad value for attribute action on element form: Must be non-empty._
- **Explanation**: As with other forms, the action attribute is dynamically set through JavaScript, rendering the validation error as non-critical.

##### Admin Access Insight Add and Edit View:
- **Error Noted**: Errors reported by Summernote.
- **Explanation**: These errors are common with complex web editors like Summernote and do not impact the functionality or user experience. The editor operates as intended within the application; hence, these errors can be safely overlooked.



### W3C CSS Validator (https://jigsaw.w3.org/css-validator/)
#### Files Validated and Error-Free:
- MarketMinds-Analytics\static\css\base.css
### JSHint JS Validator (https://jshint.com/)
#### Files Validated and Error-Free:
- MarketMinds-Analytics\static\js\base.js
- MarketMinds-Analytics\checkout\static\checkout\js\active_subscription_handler.js
- MarketMinds-Analytics\checkout\static\checkout\js\stripe_elements.js
- MarketMinds-Analytics\profiles\static\profiles\js\profiles.js


### Performance

Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website. 

- **Landing**
![Landing](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711305570/lighthouse_landing_e0zr4p.png)
- **Get Started**
![Get Started](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711305556/lighthouse_get_started_nh54tb.png)
- **Profile**
![Profile](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711305558/lighthouse_profile_qvu5l1.png)
- **Admin Subscription Plan**
![Admin](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711305557/lighthouse_admin_splan_jcdpoa.png)
- **Admin Trade Insight**
![Admin](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711305557/lighthouse_admin_insight_ony7kr.png)
- **Admin Financial Metrics**
![Admin](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711305557/lighthouse_admin_metrics_jkimaw.png)
- **Trade Insight**
![Admin](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711306692/lighthouse_trade_insight_hj9lkw.png)

#### Explanation low Best Practices and Performance on Trade Insight
While the integration of TradingView widgets as seen in some of the screenshots has slightly lowered the best practice score in our Lighthouse report, this is a trade-off I consider acceptable for the value they provide. These widgets are widely recognized for their reliability and are essential for presenting live financial data and insights directly on the platform.

The lower score primarily pertains to performance optimization standards and not to security or operational functionality. The modern browsers' approach to handling third-party widgets through partitioned cookie access and specific referrer policies is a standard privacy measure, indicating no compromise in the widgets' safety.

I’ve chosen to prioritize the significant functional benefits these widgets offer for an enhanced user experience, despite the minor impact on certain performance metrics. This ensures that users have access to critical financial information and insights without navigating away from the platform.

An important aspect of our platform's functionality involves dynamically handling images, which are uploaded through model field URLs and displayed across various sections of the application. In the Lighthouse performance analysis, it was observed that some images appear too large for their containers. This issue arises because the application utilizes these images in different contexts where their sizes are optimally suited.


# Testing
## Automated Testing and Data Model Validation
In my application, ensuring data integrity and seamless integration with Stripe's API is paramount. Given the complexity and importance of accurate data representation, particularly regarding subscriptions and active subscriptions, thorough testing has been conducted. This section details my approach to validating my data models and their interactions with Stripe's API.

### Test Suite Description
#### ActiveSubscription and SubscriptionPlan Testing
Tests for `ActiveSubscription` and `SubscriptionPlan` models are central to ensuring that my database remains in sync with Stripe's API. The CRUD operations for these models are mirrored in Stripe to guarantee consistency and security.

- **ActiveSubscription Creation and Updates**: Tests simulate the creation and modification of active subscriptions, reflecting these changes both in my database and on Stripe's platform.
- **SubscriptionPlan Modifications**: Tests cover creating, updating, and deleting subscription plans, checking for accurate reflection in the database and Stripe's records.

#### FinancialMetrics Testing
`FinancialMetrics` model testing ensures the proper tracking and updating of financial data related to subscriptions. These tests are crucial for providing an accurate financial overview of the platform's performance.

- **Automated Update of Financial Metrics**: When a subscription is created, renewed, or canceled, my tests verify the automatic adjustment of relevant financial metrics, such as revenue, new subscriptions, and canceled subscriptions.

#### Admin Access Testing

Tests under the `AdminAccessTests` class focus on the admin functionalities for managing subscription plans and trade insights.

- **CRUD Operations on Subscription Plans and Insights**: These tests ensure that admins can effectively manage subscription plans and insights, with all changes reflected correctly in the database and, where applicable, in Stripe's API.
- **Sorting and Filtering Functionality**: Tests validate the sorting and filtering functionalities for insights, ensuring a seamless admin experience.

### Test Implementation

Our test suite employs Django's `TestCase` framework, utilizing mock objects and patches to simulate Stripe's responses. This allows us to test my application's behavior in a controlled environment, mimicking real-world scenarios without actual API calls.

- **MockStripeResponse**: Used to mock Stripe's response objects.
- **Helper Functions**: Functions like `create_test_image()` and `create_active_subscription()` set up necessary test data.

### Importance of Testing

Given the critical nature of subscription-based services, the tests are designed to eliminate any discrepancies between my database and Stripe's API. Ensuring data accuracy and integrity is not just a matter of functionality but also of maintaining user trust and financial accuracy.

- **Maintaining Data Consistency**: Tests validate that all changes in subscription status or plan details are accurately mirrored between my database and Stripe.
- **Error Handling**: Tests ensure robust error handling and data validation, reducing the risk of data corruption or inconsistency.
- **Security and Reliability**: By thoroughly testing my integration with Stripe, we ensure the security and reliability of my payment and subscription systems.

#### Results
![ErrorFree](https://res.cloudinary.com/dbui0ebjv/image/upload/v1711296245/unit_tests_mma_qqukcm.png)

### Conclusion
Extensive testing practices were a cornerstone of my commitment to reliability and accuracy. They are critical in maintaining the high standards of my platform's subscription management and financial tracking functionalities.

## Manual Testing
### Allauth Login and Registration

| Test Case                    | Expected Outcome                                                  | Test Passed |
|------------------------------|-------------------------------------------------------------------|--------------|
| Register with valid details  | Confirmation email sent, user redirected to the site as logged in | ✔️     |
| Register with existing email | Form not submitting                                                 | ✔️     |
| Register with invalid data   | Form not submitting                                                | ✔️     |
| Login with correct details   | Redirects user to authenticated area/dashboard                   | ✔️     |
| Login with incorrect password| Error message indicates invalid login credentials                 | ✔️     |


### Profile Functionality

### Bag View
| Test Case                  | Expected Outcome                                                    | Test Passed |
|----------------------------|---------------------------------------------------------------------|--------------|
| Access Bag Page            | Successfully loads the bag page with saved subscription plans.       | ✔️     |
| Deleting Bag items                  | Bag items gets successfully deleted  | ✔️     |

### Add to Bag Functionality
| Test Case                  | Expected Outcome                                                                 | Test Passed |
|----------------------------|----------------------------------------------------------------------------------|--------------|
| Add Plan to Bag            | Adds a subscription plan to the bag and redirects to 'get_started'.               | ✔️     |
| Plan Already in Bag        | When attempting to add a plan already in the bag, displays an appropriate message.| ✔️     |

### Get Started View
| Test Case                | Expected Outcome                                                       | Test Passed |
|--------------------------|------------------------------------------------------------------------|--------------|
| Access GetStarted Page   | Successfully loads the page displaying subscription plans.              | ✔️     |
| Pagination               | Displays subscription plans paginated, with 6 plans per page.           | ✔️     |
| Plans Ordered            | Plans are displayed in ascending order based on their IDs.              | ✔️     |

### Admin Access View
| Test Case          | Expected Outcome                                   | Test Passed |
|--------------------|----------------------------------------------------|--------------|
| Access Admin Panel | Successfully loads the admin panel page.           | ✔️     |
| Sort Plans         | Clicking on the sort button sorts the plans.       | ✔️     |
| Delete Plan        | Clicking on delete removes the selected plan.      | ✔️     |

### Checkout View
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
- All icons were taken from [Font Awesome](https://fontawesome.com/).
- All fonts used were imported from [Google Fonts](https://fonts.google.com/).


### Shoutout

Special thanks to my Mentor Oluwafemi Medale for helping me out whenever I have a question.

