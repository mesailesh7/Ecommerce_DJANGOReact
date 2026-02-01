from math import trunc

from rest_framework import serializers
from .models import Product, Category, CartItem, Cart


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', decimal_places=2, max_digits=10, read_only=True)
    product_image = serializers.ImageField(source='product.image', read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = '__all__'


"""
A DRF (Django REST Framework) serializer is a crucial component that acts as a translator and validator for data in a Django API. It facilitates the conversion of complex data types, such as Django model instances and querysets, into native Python datatypes (like dictionaries), which can then be easily rendered into standard formats like JSON or XML for API responses. 

Core Functions
Serialization: Converts complex Python objects (e.g., a database model instance) into primitive, easily transportable formats like JSON for use by clients (e.g., a frontend application).

Deserialization: Takes incoming data (e.g., a JSON payload from a POST request), converts it back into complex Python objects, and validates it against defined rules and constraints before it is saved to the database.

Validation: Enforces data integrity by ensuring incoming data meets specific criteria (e.g., data types, length limits, uniqueness checks). If validation fails, the serializer returns clear error messages.

Data Control: Allows developers to explicitly control which fields are exposed in the API, including setting fields as read-only (e.g., auto-generated IDs) or write-only (e.g., passwords). 

Types of Serializers
DRF provides different classes to streamline the process of creating serializers. 

serializers.Serializer: The base class for creating serializers. It is flexible and used when you need to validate data that doesn't directly map to a Django model, or for non-model-backed data structures.

serializers.ModelSerializer: A powerful shortcut that automatically generates serializer fields and validation logic based on a Django model, significantly reducing boilerplate code. It's analogous to Django's ModelForm.

serializers.HyperlinkedModelSerializer: Similar to ModelSerializer but uses hyperlinks to represent relationships in the API instead of primary keys, promoting a more RESTful structure. 
"""
