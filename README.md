# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

> Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

---

> [Deployed Web](https://ferryhusnil-pbp-assignment.herokuapp.com/katalog/)

---

## 1. Bagan

<br>

![Bagan](https://github.com/ferryhusnil/pbp-assignment/blob/main/assets/images/bagan.png)

> Referensi: https://python.plainenglish.io/the-mvt-design-pattern-of-django-8fd47c61f582 > <br>

> Django merupakan framework yang menggunakan arsitektur Model-View-Template (MVT) yang terdiri dari 3 komponen utama yaitu model (mengatur data dari database), view (menerima HTTP request dan mengirim HTTP response), template (front-end website). Untuk mendapatkan web page sesuai request dari client yang diinginkan, dalam framework Django yang memiliki arsitektur MVT adalah sebagai berikut. Pertama, client melakukan HTTP request berdasarkan route/endpoint yang diberikan dan route ini akan ditangkap oleh `urls.py`. Setelah itu, request akan diteruskan menuju `views.py` sesuai route yang bersesuaian. Dalam `views.py`, akan dilakukan pengambilan data dari database (jika diperlukan) dari `models.py`. Setelah dilakukan pengembalian data dan proses pengolahan data selesai, data-data tersebut akan diteruskan sebagai parameter web page yang ada dalam `templates/katalog.html` dan akan dikembalikan kepada client sebagai HTTP response.

<br>

## 2. Virtual Environment

> Virtual environment berfungsi untuk memisahkan dependency untuk berbagai project yang ada. Sehingga, hal ini dapat menghilangkan kemungkinan bug-bug atau konflik yang tidak diinginkan apabila projek dijalankan dalam device yang berbeda dikarenakan perbedaan versi dependency yang ada dalam setiap environment device tersebut. Membuat aplikasi tanpa menggunakan virtual environment bisa-bisa saja, tetapi sangat disarankan penggunaan virtual environment untuk menghindari potensi bug dan konflik yang mungkin terjadi apabila dijalankan di device yang berbeda-beda.

<br>

## 3. Implementasi

> Membuat virtual environment dengan menggunakan `python -m venv env`. Kemudian, jalankan virtual environment dengan command `env\Scripts\activate.bat` untuk versi windows dan `source env/bin/activate` untuk versi linux atau mac. Setelah itu, install semua dependencies yang ada dalam `requirements.txt` dengan command `pip install -r requirements.txt`.

> Membuat setting awal model katalog terlebih dahulu yang ada dalam file `models.py`.

```python
from django.db import models


class CatalogItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField()
    item_stock = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    item_url = models.URLField()
```

> Setelah itu, buat migration dengan command `python manage.py makemigrations` dan terapkan migration tersebut untuk membuat database awal di `sqlite` sesuai setting database dari projek tersebut dengan command `python manage.py migrate`. Pada tahap ini, masih diperlukan pengisian data-data menuju database karena database tersebut masih kosong masih belum memiliki data sama sekali, isi database tersebut dengan data-data yang ada pada file yang berformat json pada `fixtures/initial_catalog_data.json` dengan menggunakan command `python manage.py loaddata initial_catalog_data.json`.

> Menambahkan route baru untuk HTTP request pada file `urls.py`.

```python
# TODO: Implement Routings Here
from django.urls import path
from katalog.views import show_katalog

app_name = "wishlist"

urlpatterns = [
    path("", show_katalog, name="show_katalog"),
]
```

> Dan tambahkan juga route baru pada file `urls.py` yang ada pada folder `project_django` yaitu `katalog/`.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("example_app.urls")),
    path("katalog/", include("katalog.urls")),
]
```

> Setelah itu buat fungsi `show_katalog` yang ada pada file `views.py` untuk mengatur bagaimana HTTP request tersebut diteruskan.

```python
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
```

> Pada file tersebut, akan diambil data-data yang ada dalam database menggunakan variabel `CatalogItem.objects.all()` yang datanya akan diteruskan sebagai parameter yang ada dalam web html yang ada pada file `templates/katalog.html`.

```
  {% for item in data_catalog_item %}
  <tr>
    <td>{{item.item_name}}</td>
    <td>{{item.item_price}}</td>
    <td>{{item.item_stock}}</td>
    <td>{{item.rating}}</td>
    <td>{{item.description}}</td>
    <td><a href={{item.item_url}}>{{item.item_url}}</a></td>
  </tr>
  {% endfor %}
```

> Tambahkan unit test pada `tests.py` untuk menguji ketiga endpoint apakah mengembalikan respon `HTTP 200 OK`.

```python
from django.test import TestCase

# Create your tests here.
class MyWatchlistTests(TestCase):
    def test_html_endpoint(self):
        resp = self.client.get("/mywatchlist/html/")
        self.assertEqual(resp.status_code, 200)

    def test_xml_endpoint(self):
        resp = self.client.get("/mywatchlist/xml/")
        print(resp)
        self.assertEqual(resp.status_code, 200)

    def test_json_endpoint(self):
        resp = self.client.get("/mywatchlist/json/")
        self.assertEqual(resp.status_code, 200)
```

> Setelah itu tes aplikasi dengan menggunakan command `python manage.py test` untuk menguji apakah tes berhasil.

> Deploy menggunakan platform Heroku. Login ke Heroku lalu copy `API-KEY` yang ada pada profile Heroku. Lalu buat aplikasi baru tempat untuk push django project. Setelah itu, pergi ke settings yang ada di repository github. Kemudian menuju ke `Settings -> Secrets -> Actions` dan tambahkan dua variabel `repository secret` beserta value nya yaitu.

```
HEROKU_API_KEY: <VALUE_API_KEY_ANDA>
HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU_ANDA>
```

> Setelah workflow dijalankan, maka website sudah sukses terdeploy.

# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

> Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

---

## Live Web

> [HTML page](https://ferryhusnil-pbp-assignment.herokuapp.com/mywatchlist/html)

> [XML page](https://ferryhusnil-pbp-assignment.herokuapp.com/mywatchlist/xml)

> [JSON page](https://ferryhusnil-pbp-assignment.herokuapp.com/mywatchlist/json)

---

## Perbedaan antara HTML, XML, dan JSON!

> XML (Extensible Markup Language) adalah sebuah markup languange yang digunakan untuk menyimpan dan mentransfer data. XML dapat membuat suatu markup elemen dan membuat custom markup language. Selanjutnya, JSON (JavaScript Object Notation) adalah file format yang menggunakan human-readable text untuk menyimpan dan mentransmisi objek data yang mengandung attrivute-value pairs dan arrays. Sementara itu, HTML (Hyper Text Markup Language) adalah sebuah markup language yang digunakan untuk menstruktur suatu web page beserta kontennya. Berbeda dengan XML dan JSON, HTML tidak dapat digunakan untuk pertukaran data antar aplikasi.

<br>

## Pentingnya data delivery dalam pengimplementasian sebuah platform

> Software aplikasi pada umumnya terdiri dari dua bagian besar yaitu backend (database dan logic app) dan frontend (bagian yang terlihat user). Data delivery sangatlah diperlukan karena pada umumnya pada bagian frontend tidak terdapat penyimpanan data sama sekali. Semua data yang berkaitan dengan platform semuanya tersimpan dalam database. Oleh karena itu, agar-agar data-data tersebut dapat ditampilkan pada halaman user maka diperlukan suatu data delivery pada platform

<br>

## Implementasi

> Membuat virtual environment dengan menggunakan `python -m venv env`. Kemudian, jalankan virtual environment dengan command `env\Scripts\activate.bat` untuk versi windows dan `source env/bin/activate` untuk versi linux atau mac. Setelah itu, install semua dependencies yang ada dalam `requirements.txt` dengan command `pip install -r requirements.txt`.

> Buat aplikasi baru yaitu `mywatchlist` dengan menggunakan command `python manage.py startapp mywatchlist`

> Membuat setting awal model mywatchlist terlebih dahulu yang ada dalam file `models.py`.

```python
from django.db import models

class MyWatchList(models.Model):

    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    release_date = models.DateField()
    watched = models.BooleanField(default=False)
    review = models.TextField()
```

> Setelah itu, buat migration dengan command `python manage.py makemigrations` dan terapkan migration tersebut untuk membuat database awal di `sqlite` sesuai setting database dari projek tersebut dengan command `python manage.py migrate`. Pada tahap ini, masih diperlukan pengisian data-data menuju database karena database tersebut masih kosong masih belum memiliki data sama sekali, isi database tersebut dengan data-data yang ada pada file yang berformat json pada `fixtures/initial_mywatchlist_data.json` dengan menggunakan command `python manage.py loaddata initial_mywatchlist_data.json`.

> Menambahkan route baru untuk HTTP, XML, JSON pada file `urls.py`.

```python
# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_html, show_xml, show_json

app_name = "mywatchlist"

urlpatterns = [
    path("html", show_html, name="show_html"),
    path("xml", show_xml, name = "show_xml"),
    path("json", show_json, name="show_json"),
]

```

> Dan tambahkan juga route baru pada file `urls.py` yang ada pada folder `project_django` yaitu `mywatchlist/`.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("example_app.urls")),
    path("katalog/", include("katalog.urls")),
    path("mywatchlist/", include("mywatchlist.urls")),
]
```

> Setelah itu buat fungsi `show_html`, `show_xml`, dan `show_json` yang ada pada file `views.py` untuk mengatur bagaimana HTTP request dan data delivery XML dan JSON tersebut dilakukan.

```python
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_html(request):
    data_mywatchlist_item = MyWatchList.objects.all()
    context = {
        "data_mywatchlist_item": data_mywatchlist_item,
        "name": "Mohammad Ferry Husnil Arif",
        "student_id": "2106709112",
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
```

> Untuk membuat tampilan HTML, akan diambil data-data yang ada dalam database menggunakan variabel `MyWatchList.objects.all()` yang datanya akan diteruskan sebagai parameter yang ada dalam web html yang terletak pada file `templates/mywatchlist.html`.

```
    {% for item in data_mywatchlist_item %}
    <tr>
      <td>{{item.title}}</td>
      <td>{{item.rating}}</td>
      <td>{{item.release_date}}</td>
      <td>{{item.watched}}</td>
      <td>{{item.review}}</td>
    </tr>
    {% endfor %}
```

> Deploy menggunakan platform Heroku. Login ke Heroku lalu copy `API-KEY` yang ada pada profile Heroku. Lalu buat aplikasi baru tempat untuk push django project. Setelah itu, pergi ke settings yang ada di repository github. Kemudian menuju ke `Settings -> Secrets -> Actions` dan tambahkan dua variabel `repository secret` beserta value nya yaitu.

```
HEROKU_API_KEY: <VALUE_API_KEY_ANDA>
HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU_ANDA>
```

> Setelah workflow dijalankan, maka website sudah sukses terdeploy.

## Screenshot Postman

> - HTML

![HTML](https://github.com/ferryhusnil/pbp-assignment/blob/main/assets/images/html.png)

> - XML

![XML](https://github.com/ferryhusnil/pbp-assignment/blob/main/assets/images/xml.png)

> - JSON

![JSON](https://github.com/ferryhusnil/pbp-assignment/blob/main/assets/images/json.png)