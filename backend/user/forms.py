from allauth.account.forms import SignupForm
from .models import CustomUser
from django import forms


class RegistrationForm(SignupForm):
    print("this is custom")
    phone = forms.CharField(required=True, max_length=20)

    class Meta:
        model = CustomUser
        fields = ("email", 'phone', "password1", "password2")


    def save(self, request):
        user = super(RegistrationForm, self).save(request)
        user.save()

        return user