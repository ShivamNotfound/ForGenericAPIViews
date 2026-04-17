from django.urls import path
from . import views
urlpatterns = [path("product_list/", views.ProductListAPIView.as_view(), name= "product_list"),
               path("product_selected_list/<int:id>", views.ProductSelectedListView.as_view(), name = "product_selected_list_view"),
               path("product_create/", views.ProductCreateAPIView.as_view(), name = "product_create"),
               path("product_update/<int:id>", views.ProductUpdateAPIView.as_view(), name = "product_update"),
               path("product_destroy/<int:id>", views.ProductDestroyAPIView.as_view(), name = "product_destroy")
               ]