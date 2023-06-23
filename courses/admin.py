from django.contrib import admin
from .models import Course,Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug")
    list_display_links=("title","slug",)
    prepopulated_fields={"slug": ("title",),}
    list_filter=("isActive",)
    list_editable=("isActive",)
    search_fields=("title","description")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug")
    prepopulated_fields={"slug": ("name",),}
