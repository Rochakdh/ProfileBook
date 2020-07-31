from  django import forms
from . models import Blog
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title','images','content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))