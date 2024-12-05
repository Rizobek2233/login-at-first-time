from django import forms


from .models import Food

class CreateFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'about', 'category', 'price', 'discont', 'is_food')

