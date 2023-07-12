from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms import widgets
from django.contrib import messages
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].widget=widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget=widgets.PasswordInput(attrs={"class":"form-control"})
        
    def clean_username(self):
        username=self.cleaned_data.get("username")
        
        if username=="admin":
            messages.add_message(self.request,messages.SUCCESS,"hoş geldin admin")
            
        return username
    
class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ("first_name","last_name","username","email",)
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["first_name"].widget=widgets.TextInput(attrs={"class":"form-control"})
        self.fields["last_name"].widget=widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password1"].widget=widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget=widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["username"].widget=widgets.TextInput(attrs={"class":"form-control"})
        self.fields["email"].widget=widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["email"].required=True
    
  
        
    def clean_email(self):
        email=self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exists():
            self.add_error("email","Mail already exists in the database.")
        
        return email
        
            