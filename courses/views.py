from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

data ={
    "programlama":"programlama kategorisine ait kurlsar",
    "web-gelistirme":"web-gelistirme kategorisine ait kurlsar",
    "mobil":"mobil kategorisine ait kurlsar",
}

def kurslar(request):
    return HttpResponse('kurs listesi')

def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} detay sayfası')

def getCoursesByCategoryName(request,category_name):
    try:
        category_text= data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")

def getCoursesByCategoryId(request,category_id):
    try:
        category_list =list(data.keys())
        category_name = category_list[category_id-1]
        redirect_url=reverse('courses_by_category',args=[category_name])
        return redirect(redirect_url)
    except:
        return HttpResponseNotFound("Geçerli kurs indeksi giriniz.")
        

