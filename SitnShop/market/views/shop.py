from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from ..forms import ShopForm
from ..models import Shop

from ..forms import UserForm
import datetime

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

class IndexView(generic.ListView):
    template_name = 'market/home.html'
    context_object_name = 'shops'
    def get_queryset(self):
        return Shop.objects.all()

class DetailView(generic.DetailView):
    model = Shop
    template_name = 'market/profile_public.html'

def loginShop(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None and Shop.objects.filter(user=user).exists() is True:
            if user.is_active:
                login(request, user)
                shop = Shop.objects.get(user=request.user)
                print(shop.ShopName)
                return render(request, 'market/edit_shop_profile.html', {'shop': shop})
            else:
                return render(request, 'market/login_page.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'market/login_page.html', {'error_message': 'Invalid login'})
    print("hey not a post")
    return render(request, 'market/login_page.html')


def checkFileType(file_type):
    if file_type not in IMAGE_FILE_TYPES:
        return False
    return True

def signupShop(request):
    form = ShopForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # print(username + " " + password + " " + user.username)

        if user is not None and form.is_valid() and Shop.objects.filter(user=user).exists() is False:
            if user.is_active:
                login(request, user)
                shop = form.save(commit=False)
                shop.user = request.user
                shop.Advertisement = request.FILES['Advertisement']
                shop.ProfilePic = request.FILES['ProfilePic']
                correct_type = True
                correct_type = checkFileType(shop.Advertisement.url.split('.')[-1]) and correct_type
                correct_type = checkFileType(shop.ProfilePic.url.split('.')[-1]) and correct_type

                if correct_type is False:
                    context = {
                        'shop': shop,
                        'form': form,
                        'error_message': 'Image file must be PNG, JPG, or JPEG',
                    }

                    return render(request, 'market/shop_signup.html', context)

                shop.timestamp = datetime.datetime.now()
                # shop = Shop.objects.get(user=request.user)
                shop.save()
                return render(request, 'market/edit_shop_profile.html', {'shop': shop})
            else:
                return render(request, 'market/shop_signup.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'market/shop_signup.html', {"form": form, 'error_message': 'Invalid login'})
    return render(request, 'market/shop_signup.html', {"form": form})










