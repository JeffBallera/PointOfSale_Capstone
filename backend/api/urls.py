from django.urls import path
from . import views

urlpatterns = [
    # Base Route
     path('home/', views.home_view, name='home-view'),  # Home page view
    
    path('', views.Sidebar_view, name='sidebar'),  # Sidebar
    path('AddMaterial/', views.AddMaterial_view, name='add-material'),
    path('AddProduct/', views.AddProduct_view, name='add-product'),
    path('Base/', views.Base_view, name='base'),
    path('ManageMaterial/', views.ManageMaterial_view, name='manage-material'),
    path('ManageOrder/', views.ManageOrder_view, name='manage-order'),
    path('ManageProduct/', views.ManageProduct_view, name='manage-product'),
    path('PlaceOrder/', views.PlaceOrder_view, name='place-order'),

    path('inventory/', views.InventoryListCreateView.as_view(), name='inventory-list'),
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
