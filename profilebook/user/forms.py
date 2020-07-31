from django import forms
from django.contrib.auth import get_user_model
# class UserTableDetail(forms.ModelForm):
#     class Meta:
#         model =get_user_model()
#         fields =['username','first_name','last_name','email']


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from  django.urls import reverse

class UserTableDetail(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))


USER =get_user_model()
class SignupForm(forms.Form):
    username=forms.CharField(max_length=150)
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=150)
    email=forms.EmailField()
    password = forms.CharField(max_length=128,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=128,widget=forms.PasswordInput)

    def clean_username(self):
        if USER.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('UserName Taken')
        return self.cleaned_data['username']

    def clean_email(self):
        if USER.objects.filter(username=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Email Already Taken')
        return self.cleaned_data['email']

    def clean(self):
        password=self.cleaned_data['password']
        confirm_password=self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Password Do Not Match")