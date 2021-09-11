from django.urls import path
from .views import ShoppingCart, ShoppingCartUpdate

#Shop_app urls
urlpatterns = [
    path('cart-products/', ShoppingCart.as_view()),
    path('update-item/<int:item_id>', ShoppingCartUpdate.as_view()),
]
