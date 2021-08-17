from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404

from .filters import OrderFilter
from .forms import ItemForm
from .models import Item


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.success(request, ("Пользователь не найден"))
            return redirect("login")
    else:
        return render(request, "autentication/login.html", {})


def home(request):
    if request.user.is_authenticated:
        item_ = Item.objects.all()
        item_filter = OrderFilter(request.GET, request=request, queryset=item_)

        return render(request, "home.html", {"filter": item_filter})
    else:
        return redirect("login")


def item_edit(request, item_id):
    item = get_object_or_404(Item, trace_id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    user = request.user
    if form.is_valid():
        form.save()
        print(form.save())
        print(user)
        f = open("demo.txt", "a")
        f.write("Пользователь: " + str(user) + " Id записи: " + str(form.save()) + "\n")
        f.close()
        return redirect("home")

    edit = True

    return render(
        request,
        "new.html",
        {"form": form, "edit": edit, "item_id": item_id, "item": item},
    )
