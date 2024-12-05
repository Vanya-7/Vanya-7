from django.contrib import admin
from django.urls import path
from women.views import index, categories, main

urlpatterns = [
    path('admin/', admin.site.urls),
    path("women/", index),
    path("cat/", categories),
    path("", main),

]
