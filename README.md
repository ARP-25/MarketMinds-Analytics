# TradeConnect - Tradeboard <br>
![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705585263/amiresponsive_marketminds_kbhhrn.png) 


## Description
MarketMinds Analytics is a powerful Django web application tailored for traders and investors seeking expert market analysis in the fields of crypto, forex, and stocks. Users can seamlessly purchase subscriptions to gain valuable insights into financial markets and enhance their trading strategies.
Users have the flexibility to choose from a variety of subscription plans tailored for crypto, forex, and stocks.
Plans offer in-depth market analysis, trade insights, and strategies to empower traders for success.
The web app is equipped with custom admin access page, providing superusers the ability to manage the platform with an intuitive interface.
Superusers can effortlessly add, edit, and delete subscription plans, ensuring dynamic and responsive adjustments to market demands.
[Click here to view the Live Project](https://marketminds-analytics-31d309061593.herokuapp.com/)


## Business Plan 
-   __**Executive Summary**__
   - **Overview:**
      - Subscription-based market analysis for forex, crypto, and stock markets.
   - **Mission:**
      - Providing Subscribers with in depth market analysis which enables subscriber to trade profitable. 

### 2. Business Description
   - **Services:**
      - Market Analysis and outlooks which contain potential buying and selling zones.
   - **Target Audience:**
      - Traders and Investors.

### 3. Subscription Plans
   - **Plan Structure:**
      - Every Plan consists of its basic buy and selling , market outlooks and some dynmaic content depening on market conditions.
   - **Pricing:**
      - Targeting below 100$/month for each package.

### 5. Marketing and Sales
   - **Marketing Strategy:**
      - Digital marketing, social media, and partnerships.
   - **Sales Channels:**
      - Website.
   - **Customer Acquisition:**
      - Count in costs for customer acquisition.

### 6. Operational Plan
   - **Technology:**
      - The subscriber will receive an email containing written analyses accompanied by pictures and/or videos. In the later stages of MarketMinds Analytics webpage development, a database for market analyses and a user interface (UI) for accessing them will be implemented.

   - **Team:**
      - Market Analyst's and Software Developer's.

### 7. Metrics for Success
   - **Key Performance Indicators (KPIs) for measuring success:**
      - Number of subscribers, retention rate, revenue growth.



## Table of contents
- [User Experience (UX)](#User-Experience-(UX))
- [Features](#Features)
- [Business Plan](#Business-Plan)
- [Design](#Design)
- [Technologies Used](#Technologies-Used)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Credits](#Credits)


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

## Features

### Existing Features

-   **__F01 - Navigation Bar__**
    -   Logo(redirects to the Main Page) 
    -   Home(redirects to the Main Page)
    -   Trade Insights(redirects to the Trade Insights Page which is still under construction)
    -   Get Started(redirects to the Get Started Page)
    -   Profile Icon(opens dropdown menu on click with varying content depending if user is authenticated or superuser(admin) is authenticated)
    -   Bag Icon(redirects to the shipping bag)
    -   Collapses down to a hamburger menu on smaller screen sizes
        - Navigation Bar
            ![NavBar](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705594298/F01_navbar_plrw0x.png)

        - Not Authenticated Profile Menu  
            ![NotAuthenticated](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705594936/F01_navbar_profile_menu_hfeje3.png)

        - Authenticated as User
            ![UserAuthenticated](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705594935/F01_navbar_profile_menu_authenticated_jswrmd.png)

        - Authenticated as Admin
            ![SuperuserAuthenticated](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705594937/F01_navbar_profile_menu_superuser_bvoy1g.png)

        - Hamburger clicked
            ![HamburgerClicked](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705594297/F01_navbar_hamburger_xkmeld.png)

-   **__F02 - Authentication__**
    -   Django-Allauth was used for semseless and secure authentication processes.
    -   The Django-Allauth templates were modfied to match the style of the rest of the project
        -   Sign In
        ![SignIn](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705596331/F02_authentication_login_1_1_yzedsw.png) 
        -   Sign Up
        ![SignUp](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705596330/F02_authentication_register_1_xe8c2u.png)

-   **__F03 - Langing Image with Short-Description and Get-Started-Button__**
    -   Dynamic welcome section
    -   Presenting brief overview of what to expect
    -   Get-Started-Button enables visitors to instantly to have quick access to the Get Started Page
        -   Landing
        ![LandingSection](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705597448/F03_landing_section_lb0beg.png)

-   **__F04 - Services and Credentials__**
    -   Information about what services can be expected 
    -   Credentials and Track-Record
        - Services
        ![Services](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705598378/F04_services_yiyyyn.png)
        - Credentials and Track-Record
        ![CredTrack](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705598376/F04_credentials_emihyu.png)

-   **__F05 - Stay in Touch__**
    -   Social links (Facebook Business Page)
    -   Newsletter Subscription Form (Mailchimp)
        - Stay in Touch
        ![StayInTouch](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705598377/F05_socials_newsletter_vwb4xd.png)

-   **__F06 - Profile Info__**
    -   Profile Info
    -   Profile Edit Function
    -   Active Subscription Info 
    -   Cancel Active Subscription Function
        -   Profile Info
        ![Profile Info](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705600046/F06_profile_info_pv4met.png)
        -   Profile Edit
        ![ProfileEdit](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705663756/F06_profile_edit_mp3915.png)
        -   Cancel Subscription Popup
        ![CancelPopup](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705663878/F06_profile_unsubscribe_wdq7lb.png)

-   **__F07 - Admin Access__**
    -   Admin Access View (only as superuser accessible)
    -   Access to all Subscription Plan's in Database
    -   Option to add new, edit oder delete Subscription Plan's
    -   Option to select which Subscription Plan's get featured on "Get Started Site" __(functionality currently under construction)__
    -   Option to sort the Subscription Plan's by various criterias __(functionality currently under construction)__
        -   Admin Access Part 1   
        ![AdminAccess](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705664181/F07_admin_access_1_fetua7.png)
        -   Admin Access Part 2
        ![AdminAccess](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705664204/F07_admin_access_2_qzrcpb.png)
        -  Admin Access Add Subscription Plan 
        ![AdminAccessAdd](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705664937/F07_admin_access_add_e9ly2s.png)
        -  Admin Access Edit Subscription Plan
        ![AdminAccessEdit](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705664937/F07_admin_access_edit_lmgypl.png)
        -  Admin Access Delete Subscription Plan
        ![AdminAccessDelete](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705664937/F07_admin_access_delete_kf2byo.png)

-   **__F08 - Get Started__**
    -   Get Started View
    -   Site Visitor can choose from a selection of Subscription Plan's and put them into their shopping bag
    -   Special Offers Section which presents special offers to customers __(functionality to make this section dynamic and editable in the frontend by navigating to Admin Access Page is under construction)__
    -   Subscription Plan Section which presents featured Subscription Plan's
        -   Get Started
        ![GetStarted](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705665180/F08_get_started_khvnqg.png)

-   **__F09 - Shopping Bag__**
    -   Customer can review his Shopping Bag, delete items from it, return to Get Started Page or proceed with Checkout
        -   Shopping Bag View
        ![ShoppingBag](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705667239/F09_shopping_bag_yulg7c.png)
-   **__F10 - Checkout__**
    -  Customer sees a miniature view of his shopping bag items __(if user has already subscribed the user gets notified, the Subscription Plan gets marked in a signaling color and secure checkout form gets disabled)__
    -  Checkout Form __(Stripe Secure CreditCard Payment)__
        -   Checkout View not authenticated
        ![CheckoutAuth](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705668950/F10_checkout_not_authenticated_avyu2f.png)
        -   Checkout View authenticated
        ![CheckoutNotAuth](https://res.cloudinary.com/dbui0ebjv/image/upload/v1705667783/F10_checkout_fvgtko.png)
         

### Table of Features and User Stories combined

In this table you can see that every User Story is covered by an implemented Feature.

| Feature         | US01 - Visitor | US02 - Registered User | US03 - Subscriber | US04 - Superuser (Site Owner) | US05 - Admin Access User | US06 - Potential Subscriber | US07 - User Interested in Updates |
| --------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **F01 Navigation Bar** | ✔️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **F02 Authentication** | ❌ | ✔️ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **F03 Landing Image** | ✔️ | ❌ | ❌ | ❌ | ❌ | ✔️ | ❌ |
| **F04 Services and Credentials** | ✔️ | ❌ | ❌ | ❌ | ❌ | ✔️ | ❌ |
| **F05 Stay in Touch** | ✔️ | ❌ | ❌ | ❌ | ❌ | ❌ | ✔️ |
| **F06 Profile Info** | ❌ | ✔️ | ✔️ | ❌ | ❌ | ❌ | ❌ |
| **F07 Admin Access** | ❌ | ❌ | ❌ | ✔️ | ✔️ | ❌ | ❌ |
| **F08 Get Started** | ❌ | ❌ | ❌ | ❌ | ❌ | ✔️ | ❌ |
| **F09 Shopping Bag** | ❌ | ❌ | ❌ | ❌ | ❌ | ✔️ | ❌ |
| **F10 Checkout** | ❌ | ❌ | ❌ | ❌ | ❌ | ✔️ | ❌ |


### Features which are currently under construction
-   Sort functionaliy in Admin Acces
-   Feature functionality in Admin Access
-   Special Offers Disclaimer on Get Started Page dynamic and editable by Admin in Admin Access

### Features which could be implemented in the future
-   More Social Pages (Instagram , X, YouTube etc.)
-   Switching from monthly to yearly payment by preference



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
    -   Google Fonts was used to import font into styles.css. Lato was chosen for most of the content because of it's great readability and Rubik Mono One was chosen for some of the titles and various elements I wanted to point out and seperate from the rest of the content.

-   ### Wireframes

    ![WireFrames TradeConnect - TradeBoard](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701699587/tradeconnect_figma_n8cjwk.png)

### Database Models

## TradePost

| Field         | Type              | Description                                   |
|---------------|-------------------|-----------------------------------------------|
| title         | CharField         | The title of the trade post.                  |
| slug          | SlugField         | URL-friendly version of the title.            |
| author        | ForeignKey(User)  | Author of the trade post (linked to User).    |
| description   | TextField         | Description of the trade post.                |
| trade_image   | CloudinaryField   | Image associated with the trade post.          |
| created_at    | DateTimeField     | Date and time of creation.                    |
| updated_at    | DateTimeField     | Date and time of the last update.             |
| status        | IntegerField      | Status of the trade post (Draft or Published).|

### Methods:

- `average_rating`: Calculate the average rating based on ratings associated with the trade post.

---

## Rating

| Field    | Type                  | Description                               |
|----------|-----------------------|-------------------------------------------|
| post     | ForeignKey(TradePost) | Trade post associated with the rating.     |
| user     | ForeignKey(User)      | User who rated the trade post.            |
| rating   | IntegerField          | Rating value given to the trade post.     |

---

## Comment

| Field        | Type                  | Description                                      |
|--------------|-----------------------|--------------------------------------------------|
| tradepost    | ForeignKey(TradePost) | Trade post associated with the comment.            |
| name         | CharField             | Name of the commenter.                            |
| email        | EmailField            | Email of the commenter.                           |
| body         | TextField             | Content of the comment.                           |
| created_at   | DateTimeField         | Date and time of creation.                        |
| approved     | BooleanField          | Approval status of the comment (default is True). |

---

## ContactMessage

| Field          | Type       | Description                               |
|----------------|------------|-------------------------------------------|
| name           | CharField  | Name of the sender.                        |
| email          | EmailField | Email of the sender.                       |
| phone_number   | CharField  | Phone number of the sender.                |
| body_message   | TextField  | Content of the message.                    |

---

### Signals:

- `create_slug`: Pre-save signal to generate a slug for a TradePost instance based on its title.


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Django Template Language](https://docs.djangoproject.com/en/4.2/ref/templates/language/)
-   [Markdown](https://de.wikipedia.org/wiki/Markdown)


### Frameworks, Libraries & Programs Used

-   [Gitpod:](https://gitpod.io) was used as IDE to create the code. It provides good compatibility with github and offers useful IDE extensions.
-   [GitHub:](https://github.com/) is used as the respository for the projects code after being pushed from Git.
-   [Heroku:](https://heroku.com) was used to deploy the Project.
-   [Django:](https://pypi.org/project/asgiref/)  was used as main Framework for rapid development and pragmatic design.
-   [django-allauth:](https://github.com/pennersr/django-allauth) was used for handling everything from registration to account management.
-   [django-crispy-forms:](https://github.com/django-crispy-forms/django-crispy-forms) was used with Django to easily build, customize, and manage forms using Bootstrap.
-   [django-summernote:](https://github.com/summernote/django-summernote) was used for simple WYSIWYG editing in Django.
-   [gunicorn:](https://pypi.org/project/asgiref/) was used in Django for handling Python WSGI HTTP Server and deployment.
-   [oauthlib:](https://github.com/oauthlib/oauthlib) was used for OAuth request-signing logic.
-   [asgiref:](https://pypi.org/project/asgiref/) was used in Django for handling asynchronous request handling.
-   [dj-database-url:](https://pypi.org/project/dj-database-url/) was utilized for database URLs in settings.
-   [dj3-cloudinary-storage:](https://pypi.org/project/dj3-cloudinary-storage/) was used for custom storage backend for Django using Cloudinary.
-   [psycopg2:](https://pypi.org/project/psycopg2/) was used to enable python code to execute PostgreSQL commands.
-   [cloudinary:](https://cloudinary.com) was used as database thorughout the project.
-   [Bootstrap:](https://getbootstrap.com) was used for styling.
-   [ILoveImg:](https://www.iloveimg.com) was used for resizing images and editing photos for the website.
-   [Figma:](https://www.figma.com/) was used to create the wireframes during the design process.
-   [Google Fonts:](https://fonts.google.com/) was used to import fonts.
-   [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.


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

![Lighthouse Testing](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701694712/lighthouse_testing_1_jdfasw.png)




### Test Cases and Results

#### Automated Testing
[Heres the Link to the Test Class in my Repo.](https://github.com/ARP-25/TradeConnect/blob/main/tradeboard/test.py)
For this iteration of the App I chose to leave out docstring's for the testcases etc. because the test declarations are very short, descriptive and pregnant. I felt commenting them out largely is massively reducing their readability. However, for future iterations the test's will have to get expanded and I plan to define multiple test files to modulate them and providing docstrings for more complex test's.

Automated Testing completes with zero errors:
![Automated Testing Results](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701696911/automated_testing_results_ta4xew.png)

#### Manual Testing
##### Allauth Login and Registration

| Test Case                    | Expected Outcome                                                  | Test Passed |
|------------------------------|-------------------------------------------------------------------|--------------|
| Register with valid details  | Confirmation email sent, user redirected to the site as logged in | &#10004;     |
| Register with existing email | Form not submitting                                                 | &#10004;     |
| Register with invalid data   | Form not submitting                                                | &#10004;     |
| Login with correct details   | Redirects user to authenticated area/dashboard                   | &#10004;     |
| Login with incorrect password| Error message indicates invalid login credentials                 | &#10004;     |
| Login with non-existing email| Error message prompts user to register or indicates invalid email | &#10004;     |

##### Profile Functionality

| Test Case                     | Expected Outcome                                                  | Test Passed |
|-------------------------------|-------------------------------------------------------------------|--------------|
| View Profile                  | Displays user profile information and active subscriptions.        | &#10004;     |
| Edit Profile                  | Allows the user to update profile information successfully.         | &#10004;     |
| Cancel Active Subscription    | Successfully cancels an active subscription.                        | &#10004;     |
| Attempt to Cancel Non-existing Subscription | Redirects to the profile without any action.          | &#10004;     |
| Attempt to Edit with Invalid Data | Displays validation errors and does not save changes.           | &#10004;     |

##### Bag View
| Test Case                  | Expected Outcome                                                    | Test Passed |
|----------------------------|---------------------------------------------------------------------|--------------|
| Access Bag Page            | Successfully loads the bag page with saved subscription plans.       | &#10004;     |
| Empty Bag                  | If bag is empty, displays a message indicating no items in the bag.  | &#10004;     |
| Non-Existent Plan          | Attempts to access a non-existent subscription plan in the bag.     | &#10004;     |

##### Add to Bag Functionality
| Test Case                  | Expected Outcome                                                                 | Test Passed |
|----------------------------|----------------------------------------------------------------------------------|--------------|
| Add Plan to Bag            | Adds a subscription plan to the bag and redirects to 'get_started'.               | &#10004;     |
| Plan Already in Bag        | When attempting to add a plan already in the bag, displays an appropriate message.| &#10004;     |

##### Get Started View
| Test Case                | Expected Outcome                                                       | Test Passed |
|--------------------------|------------------------------------------------------------------------|--------------|
| Access GetStarted Page   | Successfully loads the page displaying subscription plans.              | &#10004;     |
| Pagination               | Displays subscription plans paginated, with 6 plans per page.           | &#10004;     |
| Plans Ordered            | Plans are displayed in ascending order based on their IDs.              | &#10004;     |

##### Admin Access View
| Test Case          | Expected Outcome                                   | Test Passed |
|--------------------|----------------------------------------------------|--------------|
| Access Admin Panel | Successfully loads the admin panel page.           | &#10004;     |
| Sort Plans         | Clicking on the sort button sorts the plans.       | &#10004;     |
| Delete Plan        | Clicking on delete removes the selected plan.      | &#10004;     |

##### Admin Access Add Functionality
| Test Case          | Expected Outcome                                       | Test Passed |
|--------------------|--------------------------------------------------------|--------------|
| Add New Plan       | Successfully adds a new plan through the form.         | &#10004;     |
| Invalid Form Data  | Form does not submit.                                  | &#10004;     |
| Redirect           | After adding, user is redirected to admin access page. | &#10004;     |

##### Admin Access Delete Functionality
| Test Case             | Expected Outcome                                    | Test Passed |
|-----------------------|-----------------------------------------------------|--------------|
| Delete Existing Plan  | Successfully deletes an existing plan by its ID.    | &#10004;     |
| Redirect              | After deletion, user is redirected to admin access. | &#10004;     |

##### Admin Access Edit Functionality
| Test Case          | Expected Outcome                                       | Test Passed |
|--------------------|--------------------------------------------------------|--------------|
| Edit Plan           | Successfully edits an existing plan through the form.  | &#10004;     |
| Invalid Form Data  | Form does not submit                                  | &#10004;     |
| Redirect           | After editing, user is redirected to admin access.     | &#10004;     |

##### Checkout View
| Test Case                          | Expected Outcome                                                              | Test Passed |
|------------------------------------|-------------------------------------------------------------------------------|--------------|
| Access Checkout Page               | Successfully loads the checkout page.                                         | &#10004;     |
| No Items in Bag                    | Displays an error message if the bag is empty.                                 | &#10004;     |
| User Authenticated                 | Checks if the user is authenticated to proceed with the checkout.              | &#10004;     |
| Process Subscription Payment       | Completes the subscription payment for selected plans.                         | &#10004;     |
| Subscription Creation              | Successfully creates a subscription after payment.                              | &#10004;     |
| Save User Profile                  | Checks if user profile information is saved if 'save-info' checkbox is selected.| &#10004;     |
| Bag Items Removed                  | Ensures bag items are removed from the session after checkout.                  | &#10004;     |
| Stripe Integration                 | Verifies that the Stripe integration works properly.                            | &#10004;     |
| Stripe Public Key Missing          | Displays a warning if the Stripe public key is missing.                         | &#10004;     |


### Browser Compatibility

- Testing has been carried out on the following browsers :
    - Chrome Version 119.0.6045.200 (Official Build) (64-bit)
    - Firefox Version 120.0.1 (64-Bit)
    - Safari on iPhone (iOS-Version 17.1 (c))


## Deployment

### How this site was deployed

- Installing Django and Required Libraries:

    - Install Django 3.2 and Gunicorn.
    - Install supporting libraries like dj_database_url, psycopg2, dj3-cloudinary-storage, and others using pip.[Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used)
    - Create a requirements.txt file to track all installed packages.
    - Creating Django Project and App:
    - Create a Django project using django-admin startproject PROJ_NAME .
    - Add a new app within the project using python3 manage.py startapp APP_NAME.
    - Update INSTALLED_APPS in settings.py.
    
- Database Setup:

    - Create a database on Cloudinary.
    - Create a new Heroku app and configure its environment variables, adding the DATABASE_URL.
    - Environment and Settings Configuration:
    - Create an env.py file to set environment variables locally.
    - Update settings.py to reference these environment variables for sensitive information like SECRET_KEY and DATABASE_URL.
    - Storing Static and Media Files on Cloudinary:
    - Retrieve the Cloudinary URL/API environment variable.
    - Add the Cloudinary URL to environment variables locally and on Heroku.
    - Configure settings.py to use Cloudinary for storing static and media files.

- Heroku Deployment Setup:

    - Create necessary directories (media, static, templates) and a Procfile.
    - Configure the Procfile to instruct Heroku to run the Django project using Gunicorn.
    - Add, commit, and push the changes to your GitHub repository.
    - Deploy the content through Heroku's deploy section in the Dashboard.(https://dashboard.heroku.com/apps/"name-of-app"/deploy/github)

  The live link can be found here - [Tradeconnect](https://tradeconnect-d0f5a2fe7023.herokuapp.com/) 

### How to clone the repository

- Go to the https://arp-25.github.io/tradeconnect/ repository on GitHub.
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there.
- Open a GitBash terminal and navigate to the directory where you want to locate the clone.
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process.

## Credits 

### Content 

All the Trade Post data is either fictional or out of my own database.
For styling I tried to imply as much bootstrap as possible, since it was heavily taught in the buildup learning content to pp4.
There was some css integrated for button styling from (https://getcssscan.com/css-buttons-examples).
I also used (https://startbootstrap.com/) and selected a theme as boilerplate to start from.

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