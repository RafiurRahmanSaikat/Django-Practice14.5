from django import forms
import datetime
from django.forms.widgets import NumberInput

BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
FAVORITE_COLORS_CHOICES = [
    ("blue", "Blue"),
    ("green", "Green"),
    ("black", "Black"),
]


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(
        label="Please enter your email address",
    )
    roll_number = forms.IntegerField(help_text="Enter 6 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput())
    agree = forms.BooleanField()
    date = forms.DateField(initial=datetime.date.today)
    # comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    birth_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )
    value = forms.DecimalField()
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
