Users
================

Files
---------------------------------
### admin [(admin.py)](admin.py)

Defines a custom user admin model *CustomUserAdmin*.

### forms [(forms.py)](forms.py)

Defines custom user creation and change forms.

### managers [(managers.py)](managers.py)

Defines a custom user manager with methods for creating users and superusers.

### models [(models.py)](models.py)

Defines a custom user model *CustomUser*, consisting of the following fields:

* user_id
* email
* is_staff
* is_active
* date_joined

Also assigns *CustomUserManager* to *CustomUser*.

### urls [(urls.py)](urls.py)

Connects the urls *login/* and *sign-up/* to their corresponding views located within *views.py*.

### views [(views.py)](views.py)

Defines login and sign-up views, both of which handle *POST* requests made to either *login/* or *sign-up/*, respectively.

Folders
---------------------------------
### locale/es/LC_MESSAGES [(locale/es/LC_MESSAGES)](locale/es/LC_MESSAGES)

Locale data, specifically Spanish translations.

### tests [(tests)](tests)

Contains unit tests for the *Django* users app.

Navigation
---------------------------------
### Previous Folder

<--- backend [(backend)](../../)
