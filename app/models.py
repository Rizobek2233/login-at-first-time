from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.name


class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100)
    text =  models.CharField(max_length=100)
    title_1 = models.CharField(max_length=100)
    title_2 = models.CharField(max_length=100)
    work_time = models.DateTimeField()
    image = models.ImageField(upload_to='back_img', null=True)

    def __str__(self) -> str:
        return self.name
    

class FoodCategory(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name
    

class Food(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food/', null=True)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    discont = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    is_food = models.BooleanField(default=False)


    def __str__(self) -> str:   
        return self.name 


    def discounted_price(self):
        if self.discount_present:
            discounted_price = self.price - self.discount_precent*self.price/100 
            return discounted_price


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self) -> str:
        return self.name

class BookTable(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    i_name = models.CharField(max_length=100)
    i_number = models.CharField(max_length=100)
    i_date = models.IntegerField()
    i_time = models.DateTimeField()
    button = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name      


class Contact(models.Model):
    name = models.CharField(max_length=100)
    title_1 = models.CharField(max_length=100)
    title_2 = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name


class BookTable_2(models.Model):
    text = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    button = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.text

class GalleryInfo(models.Model):
    name = models.CharField(max_length=100)
    title_1 = models.CharField(max_length=100)
    title_2 = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Gallery(models.Model):
    images = models.ImageField(upload_to='images', null=True)


    def __str__(self) -> str:
        return self.images


class WorkShop(models.Model):
    name = models.CharField(max_length=100)
    title_1 = models.CharField(max_length=100)
    title_2 = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name
    

class WorkShopInfo(models.Model):
    title_one = models.CharField(max_length=255)
    title_two = models.CharField(max_length=255)
    title_three = models.CharField(max_length=255)
    title_button = models.CharField(max_length=255)
    title_number = models.IntegerField()


    def __str__(self) -> str:
        return self.title_one
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    contact = models.ImageField(upload_to='icon', null=True)


    def __str__(self) -> str:
        return self.name

class WorkShopDetail(models.Model):
    date = models.DateField()
    teacher = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    

class Shop(models.Model):
    name = models.CharField(max_length=100)
    title_one = models.CharField(max_length=100)
    title_two = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name
    

class ShopCard(models.Model):
    image = models.ImageField(upload_to='card_image', null=True)
    button = models.CharField(max_length=100)
    title_one = models.CharField(max_length=100)
    title_two = models.CharField(max_length=100)
    title_three = models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.title_two
    

class Blog(models.Model):
    name = models.CharField(max_length=100)
    title_one = models.CharField(max_length=100)
    title_two = models.CharField(max_length=100)

    
    def __str__(self) -> str:
        return self.name
    

class BlogCard(models.Model):
    image = models.ImageField(upload_to='blog_image', null=True)
    date = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    paragrph = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.text
    

class BlogPost(models.Model):
    date = models.DateField()
    title_one = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.date
    

class BlogPostInfo(models.Model):
    text = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_post_images')
    text_two = models.CharField(max_length=255)
    description_two = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.text