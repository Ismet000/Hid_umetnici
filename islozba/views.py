from django.shortcuts import render

# Create your views here.
from .models import *
from .forms import ExhibitionForm


def index(request):
    all_exhibitions = Exhibition.objects.all()

    # context = {
    #     'exh': all_exhibitions
    # }

    return render(request, 'index.html', {'all_exh': all_exhibitions})


def exhibitions(request):
    exh = Exhibition.objects.filter(location='Skopje').all()

    # form = ExhibitionForm()

    if request.method == "POST":
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExhibitionForm()

    return render(request, "exhibitions.html", {"form": form, 'exh': exh})


