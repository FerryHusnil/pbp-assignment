from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_html(request):
    data_mywatchlist_item = MyWatchList.objects.all()
    watched_count = len(MyWatchList.objects.filter(watched=True))
    not_watched_count = len(MyWatchList.objects.filter(watched=False))
    if watched_count >= not_watched_count:
        msg = "Selamat, kamu sudah banyak menonton!"
    else:
        msg = "Wah, kamu masih sedikit menonton!"
    context = {
        "data_mywatchlist_item": data_mywatchlist_item,
        "name": "Mohammad Ferry Husnil Arif",
        "student_id": "2106709112",
        "msg": msg,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_mywatchlist_item = MyWatchList.objects.all()
    data = serializers.serialize("xml", data_mywatchlist_item)
    return HttpResponse(data, content_type="text/xml")

def show_json(request):
    data_mywatchlist_item = MyWatchList.objects.all()
    data = serializers.serialize("json", data_mywatchlist_item)
    return HttpResponse(data, content_type="application/json")