from django.urls import path
from .views import (InventoryListCreateView, InventoryDetailView,
                    SupplierListCreateView, SupplierDetailView,
                    OrderListCreateView, OrderDetailView,
                    ProductOrdersListCreateView, ProductOrdersDetailView,
                    ProductListCreateView, ProductDetailView,
                    IngredientListCreateView, IngredientDetailView)

urlpatterns = [
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),

]