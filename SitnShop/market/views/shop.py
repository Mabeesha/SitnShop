from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from ..forms import ShopSignUpForm, ShopLogInForm
from ..models import Shop, Advertisement

from ..forms import UserForm, AdvertisementForm
import datetime

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

class IndexView(generic.ListView):
    template_name = 'market/home.html'
    context_object_name = 'adds'
    def get_queryset(self):
        return Advertisement.objects.all()

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
                adds = Advertisement.objects.filter(shop=shop)
                return render(request, 'market/shop_profile_editable.html', {'shop': shop, 'adds': adds})
            else:
                return render(request, 'market/shop_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'market/shop_login.html', {'error_message': 'Invalid login'})
    print("hey not a post")
    return render(request, 'market/shop_login.html')


def checkFileType(file_type):
    if file_type not in IMAGE_FILE_TYPES:
        return False
    return True


def signupShop(request):
    form = ShopSignUpForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # print(username + " " + password + " " + user.username)

        if user is not None and form.is_valid() and Shop.objects.filter(user=user).exists() is False:
            if user.is_active:
                login(request, user)
                user.is_shop = True
                shop = form.save(commit=False)
                shop.user = request.user
                user.save()
                user.profile.is_shop = True
                user.save()
                # shop.Advertisement = request.FILES['Advertisement']
                shop.ProfilePic = request.FILES['ProfilePic']
                correct_type = True
                # correct_type = checkFileType(shop.Advertisement.url.split('.')[-1]) and correct_type
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




def edit_shop(request):
    return redirect('market:homepage')


def create_addvertisement(request):

    form = AdvertisementForm(request.POST or None, request.FILES or None)
    # shop = get_object_or_404(Shop, pk=shop_id)
    shop = Shop.objects.get(user=request.user)
    if form.is_valid():
        advertisement = form.save(commit=False)
        advertisement.shop = shop
        advertisement.Advertisement_data = request.FILES['Advertisement_data']
        correct_type = True
        correct_type = checkFileType(advertisement.Advertisement_data.url.split('.')[-1]) and correct_type
        if correct_type is False:
            context = {
                'advertisement': advertisement,
                'form': form,
                'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            return render(request, 'market/create_advertisement.html', context)
        advertisement.save()
        redirect('market:homepage')
        # return render(request, 'market:homepage', {'shop': album})
    context = {
        "form": form,
    }
    return render(request, 'market/create_advertisement.html', context)

#
# def delete_advertisement(request):
#     advertisement = Album.objects.get(pk=album_id)
#     album.delete()
#     albums = Album.objects.filter(user=request.user)
#     return render(request, 'music/index.html', {'albums': albums})