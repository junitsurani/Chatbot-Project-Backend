from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatInteractionListCreate, ChatbotSettingsView

router = DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/chatbot-settings/', ChatbotSettingsView.as_view(), name='chatbot-settings'),
    path('api/chat-interactions/', ChatInteractionListCreate.as_view(), name='chat-interactions'),


]


# urlpatterns = [
#     path('', include(router.urls)),
#     path('snippet/', get_js_snippet),
#      path('settings/', ChatbotSettingsListCreateView.as_view(), name='settings-list-create'),
#     path('settings/<int:pk>/', ChatbotSettingsUpdateView.as_view(), name='settings-update'),
# ]
