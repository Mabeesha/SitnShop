from .models import Customer, Shop
from django import forms
from django.db import transaction
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ['ShopOwner', 'ShopName', 'Address', 'NumOfAds', 'ProfilePic', 'Advertisement']



class CustomerSignUp(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user