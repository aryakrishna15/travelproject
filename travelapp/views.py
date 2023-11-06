from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Places
from .form import PlaceForm


def index(request):
    places = Places.objects.all()

    content = {
        'place_list': places
    }
    return render(request, 'index.html', content)


def detail(request, places_id):
    places = Places.objects.get(id=places_id)
    return render(request, "detail.html", {'places': places})


def add(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        img = request.FILES['img']
        places = Places(name=name, desc=desc, img=img)
        places.save()
    return render(request, 'add.html')


def update(request, id):
    places = Places.objects.get(id=id)
    form = PlaceForm(request.POST or None, request.FILES, instance=places)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'places': places})


def delete(request, id):
    if request.method == 'POST':
        places = Places.objects.get(id=id)
        places.delete()
        return redirect('/')
    return render(request, 'delete.html')
