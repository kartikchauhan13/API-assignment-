from django.urls import path,include
from .serializers import CartItemSerializer
from .models import CartItem
from .views import CartItemViews


urlpatterns = [
    path('cart-items/', CartItemViews.as_view() ),
    path('cart-items/<int:id>/', CartItemViews.as_view() ),
]