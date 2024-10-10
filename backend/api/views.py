from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework import views
from .forms import Inventory

def index_view(request):
    return render(request, 'index.html')

def Sidebar_view(request):
    return render(request, 'Sidebar.html')

def PlaceOrder_view(request):
    return render(request, 'PlacedOrder.html')

def ManageOrder_view(request):
    return render(request, 'ManageOrder.html')

def AddMaterial_view(request):
    form=Inventory()
    if request.method == 'POST':
        print('Printing Post:', request.POST)
    context={'form':form}
    return render(request, 'AddMaterial.html', context)

def ManageMaterial_view(request):
    return render(request, 'ManageMaterial.html')

def AddProduct_view(request):
    return render(request, 'AddProduct.html')

def ManageProduct_view(request):
    return render(request, 'ManageProducts.html')

def KitchenDisplay_view(request):
    return render(request, 'KitchenDisplay.html')

def AddSupplier_view(request):
    return render(request, 'AddSupplier.html')
def ManageSupplier_view(request):
    return render(request, 'ManageSupplier.html')

def ExpiryDates_view(request):
    return render(request, 'ExpiryDates.html')
#Inventory Views
class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    lookup_field = 'pk'  # This uses the primary key for lookup

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
