from string import ascii_letters
import random

from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET

import requests

from app.forms import URLForm
from app.models import Shortener, Url

# Create your views here.


@require_GET
def home(request, short=""):
    if short != "":
        url_short = Shortener.objects.filter(short_form=short)[0]
        if url_short:
            url_long = url_short.url.long_form
            return redirect(url_long)
    return redirect("/shortener")


@require_GET
def index(request):

    form = URLForm(data=request.GET or None)
    short_url = ""

    if form.is_valid():
        long_url = form.cleaned_data["long_form"]
        response = requests.get(long_url)
        rand_letters = ""
        if response.ok:
            while True:
                rand_letters = "".join(random.choices(ascii_letters, k=8))
                s = Shortener.objects.filter(short_form=rand_letters)
                if s.count() == 0:
                    break

            short_url = "http://localhost:8000/" + rand_letters
            long_url = form.save()
            short = Shortener(url=long_url, short_form=rand_letters, is_active=True)
            short.save()

        else:
            short_url = response.reason

    return render(
        template_name="index.html",
        request=request,
        context={"url_form": form, "short_url": short_url},
    )
