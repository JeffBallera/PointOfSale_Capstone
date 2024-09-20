from django.db import models

# Inventory Model
class Inventory(models.Model):
    Inventory_ID = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=255)
    ItemDescription = models.TextField()
    ItemCategory = models.CharField(max_length=100)
    PurchasePrice = models.DecimalField(max_digits=10, decimal_places=2)
    Supplier_ID = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    MinStockLevel = models.IntegerField()
    ItemExpiry = models.DateField()
    Created_At = models.DateTimeField(auto_now_add=True)

# Supplier Model
class Supplier(models.Model):
    Supplier_ID = models.AutoField(primary_key=True)
    SupplierName = models.CharField(max_length=255)
    SupplierDesc = models.TextField()
    SupplierNumber = models.CharField(max_length=15)
    Order_ID = models.ForeignKey('Order', on_delete=models.CASCADE)
    Status = models.CharField(max_length=50)
    MinOrderQty = models.IntegerField()
    PaymentTerms = models.CharField(max_length=100)
    DeliveryTerms = models.CharField(max_length=100)
    ContractStart = models.DateField()
    ContractEnd = models.DateField()

# Order Model
class Order(models.Model):
    Order_ID = models.AutoField(primary_key=True)
    Items = models.CharField(max_length=255)
    Quantity = models.IntegerField()
    OrderStatus = models.CharField(max_length=50)
    Created_At = models.DateTimeField(auto_now_add=True)

# ProductOrders Model
class ProductOrders(models.Model):
    ProductOrder_ID = models.AutoField(primary_key=True)
    OrderStatus = models.CharField(max_length=50)
    OrderNumber = models.CharField(max_length=50)
    CustomerName = models.CharField(max_length=255)
    TableNumber = models.CharField(max_length=10)
    Products_ID = models.ForeignKey('Product', on_delete=models.CASCADE)
    OrderPrice = models.DecimalField(max_digits=10, decimal_places=2)
    EstimatedPrepTime = models.IntegerField()

# Product Model
class Product(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255)
    ProductDescription = models.TextField()
    ProductCategory = models.CharField(max_length=100)
    ProductImage = models.ImageField(upload_to='product_images/')
    PurchasePrice = models.DecimalField(max_digits=10, decimal_places=2)
    Ingredient_ID = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    Created_At = models.DateTimeField(auto_now_add=True)

# Ingredient Model
class Ingredient(models.Model):
    Ingredient_ID = models.AutoField(primary_key=True)
    IngredientName = models.CharField(max_length=255)
    ItemUnitMeasure = models.CharField(max_length=50)
    MeasureCount = models.IntegerField()
    Inventory_ID = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    Created_At = models.DateTimeField(auto_now_add=True)
