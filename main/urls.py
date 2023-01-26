from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import news_list, news_create, news_update, news_delete

urlpatterns = [
    path('', news_list, name='news_list'),
    path('create/', news_create, name='news_create'),
    path('update/<int:pk>/', news_update, name='news_update'),
    path('delete/<int:pk>/', news_delete, name='news_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
