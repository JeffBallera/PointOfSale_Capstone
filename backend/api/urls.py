from django.urls import path
from . import views

urlpatterns = [
    # Base Route
    path('index', views.index_view, name='index-view'),

    path('', views.Sidebar_view, name='home'),
    path('AddMaterial/', views.AddMaterial_view, name='AddMaterial'),
    path('AddProduct/', views.AddProduct_view, name='AddProduct'),
    path('ManageMaterial/', views.ManageMaterial_view, name='ManageMaterial'),
    path('ManageOrder/', views.ManageOrder_view, name='ManageOrder'),
    path('ManageProduct/', views.ManageProduct_view, name='ManageProducts'),
    path('PlaceOrder/', views.PlaceOrder_view, name='PlacedOrder'),
    path('KitchenDisplay/', views.KitchenDisplay_view, name='KitchenDisplay'),
    path('AddSupplier/', views.AddSupplier_view, name='AddSupplier'),
    path('ManageSupplier/', views.ManageSupplier_view, name='ManageSupplier'),
    path('ExpiryDates/', views.ExpiryDates_view, name='ExpiryDates'),

    path('inventory/', views.InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/', views.InventoryDetailView.as_view(), name='inventory-detail'),

    path('suppliers/', views.SupplierListCreateView.as_view(), name='supplier-list'),
    path('suppliers/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier-detail'),

    path('orders/', views.OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),

    path('productorders/', views.ProductOrdersListCreateView.as_view(), name='productorders-list'),
    path('productorders/<int:pk>/', views.ProductOrdersDetailView.as_view(), name='productorders-detail'),

    path('products/', views.ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    path('ingredients/', views.IngredientListCreateView.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', views.IngredientDetailView.as_view(), name='ingredient-detail'),
]
