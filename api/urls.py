from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, CallRequestViewSet

# Set up the router for API endpoints
router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'calls', CallRequestViewSet)

# Connect the router to URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
