from django.shortcuts import render
from .models import Url
import uuid
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.


def index(request):
    return render(request, 'shortener/index.html')


def create(request):
    if request.method == "POST":
        link = request.POST.get("link")
        if len(link) >= 1:
            uuid1 = str(uuid.uuid4())[:5]
            link1 = Url(link=link, uuid=uuid1)
            link1.save()
            return render(request, 'shortener/index.html', context={"link": link1.uuid})


def redirect_go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
