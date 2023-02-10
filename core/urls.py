from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Define as rotas para a aplicação
urlpatterns = [
    path('', include('main.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
