from django.test import TestCase
from django.urls import reverse

from market.forms import *

class UserFormTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(username="sitnshop", email="sitnshop@gmail.com", password="sit123")

class User_Form_Test(TestCase):
    def test_UserForm_valid(self):
        form = UserForm(data={'username':"sitnshop",'email':"sitnshop@gmail.com",'password':"sit123"})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = UserForm(data={'username':"",'email':"sitns",'password':"s23"})
        self.assertFalse(form.is_valid())

    def test_ShopLogInForm_valid(self):
        form = ShopLogInForm(data={'username':"sitnshop",'password':"sit123"})
        self.assertTrue(form.is_valid())

    def test_ShopLogInForm_invalid(self):
        form = UserForm(data={'username':"",'password':"s23"})
        self.assertFalse(form.is_valid())

class CreateAdvertisementFormTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = Advertisement.objects.create(Advertisement_text="adtext", Advertisement_data="adtext data")

class CreateAdvertisementForm_Test(TestCase):
    def test_CreateAdvertisementForm_valid(self):
        form = CreateAdvertisementForm(data={'Advertisement_text':"adtext", 'Advertisement_data':"adtext data"})
        self.assertFalse(form.is_valid()) #ad data should be an image therefore, this should result in a form invalid

class CreateQuickAdvertisementFormTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = QuickAdd.objects.create(QuickAdd_text="quickadtext", QuickAdd_data="quick adtext data")

class CreateQuickAdvertisementForm_Test(TestCase):
    def test_CreateQuickAdvertisementForm_valid(self):
        form = CreateQuickAdvertisementForm(data={'QuickAdd_text':"quickadtext", 'QuickAdd_data':"quick adtext data"})
        self.assertFalse(form.is_valid())        

class UpdatekAdvertisementFormTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = Advertisement.objects.create(Advertisement_text="adtext")

class UpdateAdvertisementForm_Test(TestCase):
    def test_UpdateAdvertisementForm_valid(self):
        form = UpdateAdvertisementForm(data={'Advertisement_text':"adtext"})
        self.assertTrue(form.is_valid())

    def test_UpdateAdvertisementForm_invalid(self):
        form = UpdateAdvertisementForm(data={'Advertisement_text':""})
        self.assertFalse(form.is_valid())

class CustomerSignUp(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(username="customer", email="customer@gmail.com", password="custom123")

class CustomerSignUp_Test(TestCase):
    def test_CustomerSignUp_valid(self):
        form = UserForm(data={'username':"customer",'email':"customer@gmail.com",'password':"custom123"})
        self.assertTrue(form.is_valid())

    def test_CustomerSignUp_invalid(self):
        form = UserForm(data={'username':"",'email':"sitns",'password':"s23"})
        self.assertFalse(form.is_valid())

























    