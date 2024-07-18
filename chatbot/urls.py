from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatbotSettingsViewSet, ChatbotInteractionViewSet

router = DefaultRouter()
router.register(r'settings', ChatbotSettingsViewSet)
router.register(r'interactions', ChatbotInteractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
