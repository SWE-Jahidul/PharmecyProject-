from django.contrib import admin
from .models import Category, Medicine, Generic, Mtypes

# Register your models here.
admin.site.register(Medicine)
admin.site.register(Category)
admin.site.register(Generic)
admin.site.register(Mtypes)