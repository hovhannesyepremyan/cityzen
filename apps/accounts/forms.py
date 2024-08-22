from django import forms
from django.contrib.auth import get_user_model, password_validation

from core.models import District
from .models import User


class BaseSignupForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        user = get_user_model().objects.filter(email__iexact=email).first()
        if user:
            raise forms.ValidationError('There is a user with this email!')

        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        self.instance.email = self.cleaned_data.get('email')
        password_validation.validate_password(password, self.instance)

        return password


class SignupForm(BaseSignupForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    age = forms.IntegerField(required=False)
    district = forms.ModelChoiceField(queryset=District.objects.all(), required=True)
    bio = forms.CharField(required=False)
    volunteer = forms.BooleanField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'age', 'district', 'bio', 'volunteer', 'avatar')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(),
    )
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    def clean(self):
        cleaned_data = super().clean()
        error_messages = {
            'invalid_credentials': 'Invalid login credentials!',
        }

        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:

            user = get_user_model().objects.filter(email__iexact=email).first()

            if not user or not user.check_password(password):
                raise forms.ValidationError(error_messages['invalid_credentials'])

            if not user.is_active:
                raise forms.ValidationError(error_messages['inactive'])

            return user, cleaned_data.get('remember_me')

        return None, None
