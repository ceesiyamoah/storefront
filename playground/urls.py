from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = 'Store Front Admin'
admin.site.index_title = 'Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.say_hello)
]
