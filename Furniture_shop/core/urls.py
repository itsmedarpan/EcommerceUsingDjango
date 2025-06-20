from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views
from django.urls import path, include
from .views import homepage, about, shop, signup, myaccount, edit_myaccount
from product.views import product

urlpatterns = [
    path('',homepage, name='homepage'),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('cart/', include('cart.urls')),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)