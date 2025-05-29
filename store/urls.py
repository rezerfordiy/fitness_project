from django.urls import path, include, re_path
from .views import index, product_tab, cart, index_with_order

urlpatterns = [

    path('page/<int:page>', index, name='home'),
    path('page/<int:page>/catalog/', index_with_order),  # Без сортировки
    path('page/<int:page>/catalog/<str:sort_command>/', index_with_order),  # С сортировкой
    path('product/<int:product_id>/', product_tab),
    
    path('cart/', cart),
]
#'products/<int:productid>/