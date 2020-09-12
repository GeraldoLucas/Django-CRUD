from django.urls import path
from core.views import IndexView, \
    CreateProduct, UpdateProduct, DeleteProduct

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateProduct.as_view(), name='add_product'),
    path('<int:pk>/update/', UpdateProduct.as_view(), name='upd_product'),
    path('<int:pk>/delete/', DeleteProduct.as_view(), name='del_product'),
]
