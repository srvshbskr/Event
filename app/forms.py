
from django.forms import ModelForm , TextInput,EmailInput,PasswordInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username','email','password1','password2']
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'formfield','placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class':'formfield','placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'class':'formfield','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'formfield','placeholder':' Confirm password'})
        
    username= TextInput(attrs={'class':'formfield'})
    email= EmailInput(attrs={'class':'formfield'})
    password1= PasswordInput(attrs={'class':'formfield'})
    password2= PasswordInput(attrs={'class':'formfield'})

class Loginform(AuthenticationForm):
    class Meta:
        model = User
        fields = [ 'username','password']
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'formfield','placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'class':'formfield','placeholder':'Password'})
    