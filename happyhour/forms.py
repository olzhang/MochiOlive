from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def clean_password2(self):
	    password1 = self.cleaned_data.get('password1')
	    password2 = self.cleaned_data.get('password2')

	    if not password2:
	        raise forms.ValidationError("You must confirm your password")
	    if password1 != password2:
	        raise forms.ValidationError("Your passwords do not match")
	    return password2

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.username = self.cleaned_data["username"]
		user.email = self.cleaned_data["email"]
		self.clean_password2()

		if commit:
			user.save()

		return user
