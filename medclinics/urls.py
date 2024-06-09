from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppealViewSet, ServiceViewSet, DiagnosisViewSet
from . import views
from . import dash_app

router = DefaultRouter()
router.register(r'appeals', AppealViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'diagnoses', DiagnosisViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dash/', views.dash_example, name='dash-example'),
    path('django_plotly_dash/', include('django_plotly_dash.urls'))
]
