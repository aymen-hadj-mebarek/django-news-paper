from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel

#* this will specify the forms that we will use for our application, 
# we specified the adding form, the updating form, and the model that we will be using
class CustomAdminModel(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel
    #! to include the attributes that will be shown in the menu of users in the admin page, we can specify them in the list
    list_display = ['username', 'email' ,'age', 'is_staff', 'is_superuser']
    

#? This will make us able to create new admings and users in the correct way (form) from the admin page
admin.site.register(CustomUserModel, CustomAdminModel)