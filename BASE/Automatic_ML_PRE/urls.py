from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('preprocessing/', views.preprocessing_form_view, name='preprocessing_form'),
    path('get_columns/', views.get_columns, name='get_columns'),

]