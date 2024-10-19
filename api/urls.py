from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('clients/<int:client_id>/projects/', ProjectViewSet.as_view({'post': 'create', 'get': 'list'}), name='client-projects'),
]
