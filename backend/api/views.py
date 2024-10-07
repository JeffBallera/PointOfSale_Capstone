from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework import views

# Renders the Sidebar page
def Sidebar_view(request):
    return render(request, 'Sidebar.html')

# Renders the AddMaterial page
def AddMaterial_view(request):
    return render(request, 'AddMaterial.html')

# Renders the AddProduct page
def AddProduct_view(request):
    return render(request, 'AddProduct.html')

# Renders the Base page (could be your base template)
def Base_view(request):
    return render(request, 'Base.html')

# Renders the ManageMaterial page
def ManageMaterial_view(request):
    return render(request, 'ManageMaterial.html')

# Renders the ManageOrder page
def ManageOrder_view(request):
    return render(request, 'ManageOrder.html')

# Renders the ManageProduct page
def ManageProduct_view(request):
    return render(request, 'ManageProduct.html')

# Renders the PlaceOrder page
def PlaceOrder_view(request):
    return render(request, 'PlaceOrder.html')

# Home view, if you have one
def home_view(request):
    return render(request, 'index.html')  # This should match your 'home' page template name

#Inventory Views
class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

# Supplier Views
class SupplierListCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# Order Views
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# ProductOrders Views
class ProductOrdersListCreateView(generics.ListCreateAPIView):
    queryset = ProductOrders.objects.all()
    serializer_class = ProductOrdersSerializer

class ProductOrdersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductOrders.objects.all()
    serializer_class = ProductOrdersSerializer

# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Ingredient Views
class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
