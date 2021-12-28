from django.urls import path, include
from authapp import views


urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:id>', views.ProductDetail.as_view()),
]