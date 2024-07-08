from django.shortcuts import render
from . import forms

# Create your views here.


def home(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = forms.ContactForm()
    return render(request, "home.html", {"form": form})
