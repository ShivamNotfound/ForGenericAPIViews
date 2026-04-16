from django.urls import path
from . import views
urlpatterns = [path("product_list/", views.ProductListAPIView.as_view(), name= "product_list"),
               path("product_selected_list/<int:id>", views.ProductSelectedListView.as_view(), name = "product_selected_list_view")]