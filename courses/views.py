from datetime import date,datetime
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Course,Category
from django.core.paginator import Paginator



def index(request):
    # list comprhensions
    kurslar=Course.objects.filter(isActive=1)
    kategoriler=Category.objects.all()
    
    # for kurs in db["courses"]:
    #     if kurs["isActive"]==True:
    #         kurslar.append(kurs)
    return render(request,'courses/index.html',{'categories':kategoriler,                    'courses':kurslar})


def details(request,slug):
    try:
        course=Course.objects.get(slug=slug)
    except:
        raise Http404
    
    context={
        'course':course
    }
    return render(request,'courses/details.html',context)

def getCoursesByCategory(request,slug):
    kurslar=Course.objects.filter(categories__slug=slug,isActive=True).order_by("date")
    kategoriler=Category.objects.all()
    
    paginator = Paginator(kurslar,3)
    page=request.GET.get('page',1)
    page_obj=paginator.get_page(page)
    
    print(paginator.count)
    print(paginator.num_pages)
    
    return render(request,'courses/index.html',{
        'categories':kategoriler,
        'page_obj':page_obj,
        'seciliKategori':slug
    })



