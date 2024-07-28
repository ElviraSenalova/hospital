from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import DoctorView, ServiceView, VisitView, PatientView

router = DefaultRouter()
router.register(r'doctor', DoctorView, basename='doctor')
router.register(r'service', ServiceView, basename='service')
router.register(r'visit', VisitView, basename='visit')

urlpatterns = [
    path(
        'doctor/',
        DoctorView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),

    path(
        'doctor/<int:id>/',
        DoctorView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'doctor/<int:id>/patient',
        DoctorView.as_view({
            'get': 'list_patient',
        })
    ),

    path(
        'patient/',
        PatientView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'patient/<int:id>/',
        PatientView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),

    path('', include(router.urls)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]