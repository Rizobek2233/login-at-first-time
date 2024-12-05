from rest_framework import serializers
from .models import Food, Category, Reservation, BookTable, Contact, BookTable_2, GalleryInfo, Gallery, WorkShop, WorkShopInfo, Teacher, WorkShopDetail, Shop, ShopCard, Blog, BlogCard, BlogPost, BlogPostInfo


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)
    class Meta:
        depth = 1
        model = Food
        fields = '__all__'

    def discounted_price(self, obj):
        if obj.discounted_price is not None:
            return obj.discounted_price
        return None
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['discounted_price'] is None:
            data.pop('discounted_price')
        return data


class BookTable(serializers.ModelSerializer):
    class Meta:
        model = BookTable
        fields = '__all__'


class Contact(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class Teacher(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class BookTable_2(serializers.ModelSerializer):
    class Meta:
        model = BookTable_2
        fields = '__all__'

    
class GalleryInfo(serializers.ModelSerializer):
    class Meta:
        model = GalleryInfo
        fields = '__all__'


class Gallery(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class WorkShop(serializers.ModelSerializer):
    class Meta:
        model = WorkShop
        fields = '__all__'


class WorkShopInfo(serializers.ModelSerializer):
    class Meta:
        model = WorkShopInfo
        fields = '__all__'


class WorkShopDetail(serializers.ModelSerializer):
    class Meta:
        model = WorkShopDetail
        fields = '__all__'


class Shop(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopCard(serializers.ModelSerializer):
    class Meta:
        model = ShopCard
        fields = '__all__'


class Blog(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogPost(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostInfo(serializers.ModelSerializer):
    class Meta:
        model = BlogPostInfo
        fields = '__all__'


class BlogCard(serializers.ModelSerializer):
    class Meta:
        model = BlogCard
        fields = '__all__'



