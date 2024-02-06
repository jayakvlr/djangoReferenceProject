from django.urls import path
from . import views
#views.index is a refrence to the method to be called
urlpatterns = [
    path('', views.index),
    path('new/',views.new_products)
]