from django.urls import path

from . import views

app_name = 'store1'
urlpatterns = [
    path('', views.product_list, name='store1'),
    path('<int:pk>', views.product, name="product")
]
