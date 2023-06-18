from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="homeurl"),
    path("about/", views.about, name="abouturl"),
    path("addstock/", views.add_stock, name="addstockurl"),
    path("delete/<int:stock_id>", views.delete, name="deleteurl"),
    path("delete_stock/", views.delete_stock, name="deletestockurl")
]