from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from item.models import Item,Category
from django.urls import reverse


# Create your views here.


from .forms import SignupForm





def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, "core/index.html",{
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login"))
    else:
        form = SignupForm()
    return render(request, "core/signup.html", {
        "form": form
          })