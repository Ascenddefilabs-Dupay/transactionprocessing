from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DupayAccountViewSet, DupayAssetViewSet, DupayDenominationViewSet, DupayAddressViewSet, PhaseViewSet

router = DefaultRouter()
router.register(r'accounts', DupayAccountViewSet)
router.register(r'assets', DupayAssetViewSet)
router.register(r'denominations', DupayDenominationViewSet)
router.register(r'addresses', DupayAddressViewSet)
router.register(r'phases', PhaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
