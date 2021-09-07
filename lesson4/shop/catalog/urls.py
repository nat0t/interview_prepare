from django.urls import path

from catalog import views

app_name = 'catalog'
urlpatterns = [
    path('catalog/', views.get_catalog, name='catalog'),
    path('product/', views.add_product, name='product'),
]
