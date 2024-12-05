from django.contrib import admin
from .models import RestaurantInfo, FoodCategory, Food, Reservation, BookTable, Contact

admin.site.register(RestaurantInfo)
admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(Reservation)
admin.site.register(BookTable)
admin.site.register(Contact)
