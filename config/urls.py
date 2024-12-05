from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from app.views import (
    FoodApiView, FoodDetailAPIView,
    FoodUpdateAPIView, FoodDeleteAPIView, FoodUpdateDeleteAPIView, get, category, dashboard, FoodView, create_food, delete_food,update_food, category_view, reservation,
    resimage
)

schema_view = get_schema_view(
   openapi.Info(
      title="Restaurant",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dashboard, name='dashboard'),
    path('api/', include('app.urls')),
    path('api/v1/food/', FoodApiView.as_view()),
    path('', FoodDetailAPIView.as_view()),
    path('api/v1/food/update/<int:pk>/', FoodUpdateAPIView.as_view()),
    path('api/v1/food/delete/<int:pk>/', FoodDeleteAPIView.as_view()),
    path('api/v1/food/update/delete/<int:pk>/', FoodUpdateDeleteAPIView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('FoodView/', category, name='FoodView'),
    path('create_food/', create_food, name='create_food'),
    path('delete_food/<int:id>/', delete_food, name='delete_food'),
    path('update_food/<int:id>/', update_food, name='update_food'),
    path('category/', category_view, name='category-url'),
    path('reservation/', resimage, name='reservation'),
    path('resimage/', resimage, name='resimage'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)