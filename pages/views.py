from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

data ={
    "programlama":"programlama kategorisine ait kurslar","web-gelistirme":"web gelistirme kategorisine ait kurslar","mobil":"mobil gelistirme kategorisine ait kurslar"
}
def index(request):
    courses = [
        {'name': 'Python Programlama', 'instructor': 'Ahmet Yılmaz', 'price': 250},
        {'name': 'Web Geliştirme', 'instructor': 'Mehmet Çelik', 'price': 200},
        {'name': 'Makine Öğrenmesi', 'instructor': 'Ayşe Demir', 'price': 300},
    ]
    context = {'courses': courses}
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')