from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectsViewSet

# Crear un enrutador y registrar la vista del proyecto
router = DefaultRouter()
router.register(r'projects', ProjectsViewSet)

# Incluir las rutas del enrutador en la URL principal
urlpatterns = [
    path('api/', include(router.urls)),  # Rutas de la API
]
