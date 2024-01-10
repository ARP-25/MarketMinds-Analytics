# TradeConnect - Tradeboard <br>
![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701634734/amiresponsive_1_a8dglf.png) 
## Description
TradeConnect  An interactive Django-powered platform designed for traders. Share your trade strategies, engage in insightful discussions, and refine your approach with user ratings and comments. Join us, elevate your trading game, and connect with fellow traders on this vibrant platform crafted for growth and success.

[Click here to view the Live Project](https://tradeconnect-d0f5a2fe7023.herokuapp.com/)

## Table of contents

- [User Experience (UX)](#User-Experience-(UX))
- [Features](#Features)
- [Design](#Design)
- [Technologies Used](#Technologies-Used)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Credits](#Credits)


## User Experience (UX)

### User stories

- US01 Register/Login to the App

- US02 Create a Trade Post

- US03 Edit a Trade Post

- US04 Search for Trade Post and get a sorted view

- US05 Delete a Trade Post

- US06 Rate a Trade Post

- US07 Inspect detailed Trade Post

- US08 Comment a Trade Post

- US09 Contact Site Owner

## Features

### Existing Features

-  F01 NavBar 
    -   NavBar with Label(redirects to Main Page) and three elements: Home(redirects to Main Page), Login(redirects to Login Page) and Register(redirects to Register Page)
        -   Helps users easily navigate and access various parts of the site
    ![Header](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690782/01_nav_bar_sho6uh.png)  

-  F02 Sign Up Page
    -   Sign Up
    ![SignUp](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690782/02_sign_up_b1lt0o.png) 

-  F03 Login Page
    -   Login
    ![Login](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690782/03_login_nq4vqk.png) 

-  F04 Post Trade Button
    -   Is shifted to Login Button when user is not logged in yet and redirects to Login Page
    -   If logged in redirects to Create Post Page
    ![Post a Trade Button](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690781/04_post_trade_button_dze2tl.png) 

-  F05 Sort Selection Button
    -   By clicking user is able to sort existing Trade Post's
    ![Sort Selection Button](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690781/05_sort_selection_button_s6obo6.png) 

-  F06 Trade Post List
    -   Released Trade Post's are found here
    ![Trade Post List](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690780/06_trade_post_list_ra0wf0.png)

-  F07 Pagination Controls
    -   Enhance user experience by simplifying navigation through a vast amount of content. Instead of presenting a long list or a substantial amount of data on one page
    ![Pagination Controls](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690781/07_pagination_controls_sdiedk.png) 

-  F08 Delete and Edit Button
    -   This feature is available for logged in user's and on their own Trade Post's
    -   Delete: Deletes Trade Post
    -   Edit: Redirects to Edit Trade Post Page
    ![Delete and Edit Button](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690781/08_delete_edit_hpuvjy.png)

-  F09 Edit Trade Post Page
    -   User is able to take changes on his Trade Post
    ![Edit Trade Post Page](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690779/09_edit_page_smyzlp.png)

-  F10 Detailed Trade Post Page
    -   By clicking on a Trade Post inside the Trade Post List(F06) user gets redirected to Detailed Trade Post Page
    -   Here the user gets a detailed view of the Trade Post, the ability to rate a Trade Post or simply leave a comment
    ![Edit Trade Post Page](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690781/10_detailed_trade_post_page_gcomt8.png)
    -   Commenting
    ![Comments](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690780/10_detailed_trade_post_page_comments_ca64fz.png)
    -   Rating
    ![Rating](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690780/10_detailed_trade_post_page_rating_hjzfxa.png)

-  F11 Message Form
    -   Site visitors are able to contact the site owner without having to create an account
    ![Edit Trade Post Page](https://res-console.cloudinary.com/dbui0ebjv/thumbnails/v1/image/upload/v1701690780/MTFfbWVzc2FnZV9mb3JtX213aDdjYw==/preview)

### Table of Features and User Stories combined

In this table you can see that every User Story is covered by an implemented Feature.

|     | US 1     | US 2     | US 3     | US 4     | US 5     | US 6     | US 7     | US 8     |  US 9    | 
|-----|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| F 1 |     x    |          |          |          |          |          |          |          |          |
| F 2 |     x    |          |          |          |          |          |          |          |          |
| F 3 |     x    |          |          |          |          |          |          |          |          |
| F 4 |     x    |    x     |          |          |          |          |          |          |          |
| F 5 |     x    |          |          |   x      |          |          |          |          |          |
| F 6 |          |          |          |   x      |          |          |          |          |          |
| F 7 |          |          |          |   x      |  x       |          |          |          |          |
| F 8 |          |          |          |          |  x       |          |          |          |          |
| F 9 |          |          |   x      |          |          |          |          |          |          |
| F10 |          |          |          |          |          |   x      |  x       |      x   |          |
| F11 |          |          |          |          |          |   x      |  x       |      x   |    x     |

### Features which could be implemented in the future

- Ranking System that displays the users with the highest Average Rating on his Trade Post's
- Trading Journal. Should be preferably its own App but in the same Project


## Design
-   ### Styling
    -  For Styling the Bootstrap 5.2.3 library was imported. Additionaly you will find some custom CSS at the top of the style.css file to fit in some custom needs.

-   ### Colour Scheme
    -  The color Scheme is adjusted to mainly provide good contrast and readability but still offers an appealing design and fit the theme of Trading.
    -  The specific areas have the background-color: 
        -   Royal Blue(#4169E1): This color signifies trust, professionalism, and reliability. In the financial and trading sector,         establishing trust is crucial. Royal blue exudes a sense of security, stability, and confidence, which are vital for financial platforms. Black Grey: 
        -   Dark Grey(#333333): Black and shades of grey are often used in conjunction with blue to create a sense of sophistication, seriousness, and elegance. These colors are associated with formality and can convey a professional, sleek appearance.
    -  Font Color is adjusted through the game to give good contrast to specific background-color.

-   ### Typography
    -   Google Fonts was used to import font into styles.css. Montserrat was chosen because it's known for elegance and readability, it's a great choice for conveying a professional tone.

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