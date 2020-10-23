from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput, TimeInput
from users.models import Profile
from .models import Job

USER_ROLES = [
    ('field_engineer', 'Field Engineer'),
    ('manager', 'Manager')
]


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email


class ProfileUpdateForm(forms.ModelForm):
    full_name = forms.CharField(max_length=200)
    passport_no = forms.CharField(max_length=200)
    contact_no = forms.CharField(max_length=200)
    state = forms.CharField(max_length=200)
    country = forms.CharField(max_length=200)
    role = forms.ChoiceField(choices=USER_ROLES)

    class Meta:
        model = Profile
        fields = ['full_name', 'passport_no',
                  'contact_no', 'state', 'country', 'role']


class JobAddForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput)
    status = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    SVR_ID = forms.CharField(max_length=200)
    LCON_name = forms.CharField(max_length=200)
    LCON_contact_no = forms.CharField(max_length=200)

    class Meta:
        model = Job
        fields = ['date', 'time', 'status', 'location',
                  'description', 'SVR_ID', 'LCON_name', 'LCON_contact_no']
