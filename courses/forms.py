from courses.models import Course
from django import forms 
from django.forms import SelectMultiple, TextInput,Textarea

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(label="Kurs Başlığı",required=True,error_messages={"required":"Kurs başlığı girmelisiniz."},widget=forms.TextInput(attrs={"class":"form-control"}))
#     description=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug=forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     #edit

class CourseCreateForm(forms.ModelForm):
    """A form for creating a new course."""
    class Meta:
        model=Course
        fields=('title','description','imageUrl','slug')
        labels={
            "title":"Kurs Başlığı",
            "description":"Açıklama"
        }
        widgets={
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "imageUrl":TextInput(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"})
        }
        error_messages={
            "title":{
                "required":"kurs başlığı girmelisiniz.",
                "max_kength":"maksimum 50 karakter girmelisiniz."
            },
            "description":{
                "required":"kurs açıklaması gereklidir."
            }
        }
        
class CourseEditForm(forms.ModelForm):
    """A form for creating a new course."""
    class Meta:
        model=Course
        fields=('title','description','imageUrl','slug',"categories","isActive")
        labels={
            "title":"Kurs Başlığı",
            "description":"Açıklama"
        }
        widgets={
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "imageUrl":TextInput(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"}),
            "categories":SelectMultiple(attrs={"class":"form-control"})
        }
        error_messages={
            "title":{
                "required":"kurs başlığı girmelisiniz.",
                "max_kength":"maksimum 50 karakter girmelisiniz."
            },
            "description":{
                "required":"kurs açıklaması gereklidir."
            }
        }