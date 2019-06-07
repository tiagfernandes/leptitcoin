from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('nouveau', views.annonce_new, name="annonce_new"),
    path('modification/<int:id>', views.annonce_update, name="annonce_update"),
    path('<int:id>', views.annonce_read, name="annonce_read"),
    path('suppression/<int:id>', views.annonce_remove, name="annonce_remove"),
    path('contact/<int:id>', views.annonce_contact, name="annonce_contact"),
]
