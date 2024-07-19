from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import ChatbotSettings, ChatInteraction
from .serializers import ChatbotSettingsSerializer, ChatInteractionSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser



# Create your views here.

class ChatbotSettingsViewSet(viewsets.ModelViewSet):
    queryset = ChatbotSettings.objects.all()
    serializer_class = ChatbotSettingsSerializer

class ChatbotSettingsView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        settings = ChatbotSettings.objects.first()
        if not settings:
            return Response({'error': 'Settings not found'}, status=404)
        serializer = ChatbotSettingsSerializer(settings)
        return Response(serializer.data)

    def put(self, request, format=None):
        settings = ChatbotSettings.objects.first()
        if not settings:
            return Response({'error': 'Settings not found'}, status=404)

        # Handle file fields
        data = request.data.copy()
        for field in ['launcher_icon', 'assistant_image', 'send_icon']:
            if field in data and isinstance(data[field], str) and data[field] == '':
                data.pop(field)

        serializer = ChatbotSettingsSerializer(settings, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class ChatInteractionListCreate(generics.ListCreateAPIView):
    queryset = ChatInteraction.objects.all()
    serializer_class = ChatInteractionSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_js_snippet(request):
    snippet = """
    <div id="chatbot"></div>
    <script>
        (function() {
            var script = document.createElement('script');
            script.src = 'http://localhost:3000/static/js/main.js';
            document.getElementById('chatbot').appendChild(script);
        })();
    </script>
    """
    return JsonResponse({'snippet': snippet})

