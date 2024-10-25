# django-news-paper

In this project we will build a news paper app, that will include `custom user model` and the ability to *view*, *update* and *delete* each article, according to `roles and permissions`.\
**This is for learning purposes for me at first place then anyone who can find this useful**
**this project was made by following the book `Django for Beginners` by `WILLIAM S. VINCENT`**
where you can but his book from [this link](https://djangoforbeginners.com/).

As we did in the previous project : [Django Blog app](https://github.com/) we will devide our work here into chapter where in each chapter i will share with you the things i learned in it.

# CHAPTER ONE : `CUSTOM USER MODEL`:
in this chapter we will handle creating a custom user model for our application.
Starting with : 
### 1. Creating the project and mini-app for users :
so first thing first is that we create a new repository for our project then we create a new app in it :
```powershell
# we will start by going to a desired repository for our project
cd ./django-news-paper
django-admin startproject newspaper_project
python manage.py startapp users
```

**!!! DO NOT MAKE MIGRATIONS IN THE APP**\
because if we use the command 
```powershell
python manage.py makemigrations
python manage.py migrate
```
this will create default django.auth model for our users in this project. which is **not what we want**

Once we created our app we need to include it in the settings of the django project 
```python
# in the file : newspaper_project/settings.py

INSTALLED_APPS = [
    # other apps
    'users.apps.UsersConfig', # our new app
]
```

### 2. Creating our model :
Now everything is set up, we can create the new user model in the repository `/users/models.py`
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)    
```
in this class we are using `AbstractUser` that will get us the default attributes of the user model provided by Django, and then what will do is adding a new attribute to it, as in this case the **age**.

**But** our app is still using the default user model, **So how do we change that?**

Well, all we have to do is update our `settings.py` file, all we need to do is add this one line :

```python
# in the file : newspaper_project/settings.py

AUTH_USER_MODEL = 'users.CustomUserModel'
```

### 3. Including the new model in the Admin page :
Now, what we will do is give the ability to the admin to manage our new model, for that the first thing we need to do is make the migrations :
```powershell
python manage.py makemigrations users
python manage.py migrate users

# Something i would like to mention here is the the word users that i added in the last of the command
# It is a better application for django developers to specify which app they want to make the migrations for it, maybe it doesn't matter in small projects, but once the porject is big this could save a lot of time
```

Now that our model is set in the database, we need to create its needs, which are : `creation form` and `changing form`. For that we will create a new file `forms.py` in the users mini-app.

```python
# in file : users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUserModel
        fields = ('username', 'email' ,'age',)
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'email' ,'age',)
```
---
after that the migrations are effected, we will update our `admin.py` file, so he has access to creating and changing :
```python
# in file : users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel

class CustomAdminModel(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel
    list_display = ['username', 'email' ,'age', 'is_staff', 'is_superuser']
    
admin.site.register(CustomUserModel, CustomAdminModel)
```

now we can view our users in the admin menu, but we will need to use the new forms in our templates, so like in the previous project, we will have to create a templtaes folder and then put the `login.html` and `signup.html` files in the `templates/registration` folder.

### 4. Creating the Views/URLs/templates :

Let's create the folders and files, required for the templates to work properly:
```powershell
mkdir templates
mkdir templates/registration

touch templates/registration/login.html
touch templates/registration/signup.html
```

and now all we need to do is to import the forms that we have in the templates : 
```html
<!-- in the file : templates/registration/signup.html -->

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
</form>
```
this is for the sign up part

---
```html
<!-- in the file : templates/registration/login.html -->

<h2>Log In</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Log In</button>
</form>
```

and like this all we are left to do is to import the views, and accord the urls to them.

---
1. **Creating the URLs**
for the urls we will need 2 only, we start by importing the apps URLs in the project `urls.py` file :

```python
# in the file : newspaper_project/urls.py

from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), # this will be the responsible for the Login
    path('accounts/', include('users.urls')) # this will be responsible for the signup
]
    # if you can remember that the login view is already imported as 'login' BUT the signup view must be created manually 
```

Now for the `urls.py` of our mini-app :
```python
# in the file : users/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
```

once our URLs are set, they will need the views to import it from it.\
**in this case its only the signup view that we will need**

---
2. **Creating the Views**

all we will need in this part is the signup view, so let's create it :
```python
# in the file : users/views.py

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class  = CustomUserCreationForm
    template_name ='registration/signup.html'
    success_url = reverse_lazy('home')
```

lets break this code : 
- **CustomUserCreationForm**: this is the form that we set up previously, will be used here for the signup process.
- **reverse_lazy**: give us the possibility to redirect after that the request is answered.
- **CreateView**: this is the a predifined class that will give us the opportunity to create our own view, with the form that we like.

Now all we need to do is is to launch our server and navigate to the signup page, to create an account!

*(Dont forget to create a home page, or import the one i used, its so basic that i wont be talking about it now.)*