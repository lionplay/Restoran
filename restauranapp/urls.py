from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('about', views.about_page, name="about"),
    path('registration', views.registration_user, name="registration"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    
    path('contact_us', views.contact_us, name="contact_us"),

    #path('contact',views.contact,name='contact'),

    path('allproducts/',views.allproducts,name='allproducts'),
    
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail, name='cart_detail'),
    

]