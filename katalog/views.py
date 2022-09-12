from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        "data_catalog_item": data_catalog_item,
        "name": "Mohammad Ferry Husnil Arif",
        "student_id": "2106709112",
    }
    return render(request, "katalog.html", context)
