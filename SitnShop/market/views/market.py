
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from ..models import Shop, Customer

from el_pagination.decorators import page_template
from el_pagination.views import AjaxListView


# new function 1
def LoginINAs(request):
    if request.method == "GET":

        template_name = "market/logInAs.html"
        context = {}

        return render(request, template_name, context)

def Profile(request):
    user = request.user
    c = Shop.objects.filter(user=user)
    if user.is_anonymous or len(c) == 0:
        print("hey you are not you")
        return redirect("/home/")

    else:

        ad_list = [["1","a"],  ["2", "b"], ["3", "c"]]
        template_name = "market/profile_index.html"
        pk = str(c[0].pk)
        context = {"user" : user, "ad_list": ad_list, "pk": pk}
        return render(request, template_name, context)


def public_profile(request, pk):

    u = Shop.objects.filter(pk = pk)


    if len(u) == 0:
        return redirect("/home/")

    else:
        c = u[0]
        ad_list = [["1","a"],  ["2", "b"], ["3", "c"]]
        template_name = "market/profile_public.html"
        pk = str(c.pk)
        context = {"user" : c, "ad_list": ad_list, "pk": pk}
        return render(request, template_name, context)



def LogOUT(request):
    user = request.user
    if user is not None:
        logout(request)
    return redirect("/home/login/")
