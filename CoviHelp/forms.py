from django import forms

## login forms
class UserSignIn(forms.Form):
    email = forms.CharField(label='Email', max_length=20)
    password = forms.CharField(label='Password', max_length=20)

class OxygenUser(UserSignIn):
    pass

class PharmaUser(UserSignIn):
    pass

class HospitalUser(UserSignIn):
    pass


## registration forms
class User(forms.Form):
    company = forms.CharField(label='Company Name', max_length=100)
    name = forms.CharField(label='Contact Person Name', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
