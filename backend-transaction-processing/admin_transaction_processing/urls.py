from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DupayAccountViewSet, DupayAssetViewSet, DupayDenominationViewSet, DupayAddressViewSet, PhaseViewSet
from .views import AccountCreateView,AssetCreateView,PhasesCreateView

router = DefaultRouter()
router.register(r'accounts', DupayAccountViewSet)
router.register(r'assets', DupayAssetViewSet)
router.register(r'denominations', DupayDenominationViewSet)
router.register(r'addresses', DupayAddressViewSet)
router.register(r'phases', PhaseViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('DupayAccounts/', AccountCreateView.as_view(), name='account-create'),
    path('DupayAssets/', AssetCreateView.as_view(), name='Assets-create'),
    path('DupayPhases/', PhasesCreateView.as_view(), name='Phases-create'),
]
