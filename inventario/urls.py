from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('create/product/', views.create_product, name='create_product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



