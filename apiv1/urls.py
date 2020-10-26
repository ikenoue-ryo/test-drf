from django.urls import path, include
from rest_framework import routers

from . import views
from .views import ArticleDetailAPIView

router = routers.DefaultRouter()
router.register('articles', views.ArticleViewSet)
router.register('writer', views.WriterViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
    path('detail_articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='detail'),
]
