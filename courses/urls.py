
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index),
    path('<kurs_adi>',views.details),
    path('category/<int:category_id>',views.getCoursesByCategoryId),
    path('category/<str:category_name>',views.getCoursesByCategoryName,name='courses_by_category'),
    
]