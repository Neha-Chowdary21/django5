from django import forms
from django.contrib.auth.models import User
from django.core.checks import messages
from django.core.exceptions import ValidationError
from datetime import date

from django.shortcuts import redirect, render


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    date_of_birth = forms.DateField(
        label="Date of Birth",
        widget=forms.SelectDateWidget(years=range(1950, 2010))
    )

    phone_number = forms.CharField(
        max_length=10,
        label="Phone Number",
    )

    otp = forms.CharField(
        max_length=6,
        label="OTP (One-Time Password)",
        help_text="Enter the 6-digit OTP sent to your phone number."
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'date_of_birth', 'phone_number', 'otp']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("The passwords do not match.")
        return cleaned_data


    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

        if age < 18:
            raise ValidationError("You must be at least 18 years old to register.")

        return date_of_birth

    from django.core.exceptions import ValidationError

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        try:
            # Attempt to convert the phone number to an integer
            phone_number_int = int(phone_number)
        except ValueError:
            # If conversion fails, raise a ValidationError with a popup-friendly message
            raise ValidationError("Please enter a valid phone number.")

        # Check if the phone number is within the desired range
        if not (6000000000 <= phone_number_int <= 9999999999):
            raise ValidationError("Phone number must be between 6,000,000,000 and 9,999,999,999")

        return phone_number


class ChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']








