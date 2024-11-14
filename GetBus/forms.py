from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        #fields="__all__"    # fields all to get all variable
        model = User
        #to set spacific field enter that variable
        fields = ["username", "first_name", "last_name", "email"]