from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DupayAccountViewSet, DupayAssetViewSet, DupayDenominationViewSet, DupayAddressViewSet, PhaseViewSet
from .views import AccountCreateView,AssetCreateView,PhasesCreateView, AccountNameListView,DenominationCreateView,AssetNameListView,AddressCreateView,DenominationNameListView

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
    path('DupayDenomination/', DenominationCreateView.as_view(), name='Denomination-create'),
    path('DupayAddress/', AddressCreateView.as_view(), name='Address-create'),
    path('DupayPhases/', PhasesCreateView.as_view(), name='Phases-create'),


    path('account_names/', AccountNameListView.as_view(), name='account-name-list'),
    path('asset_names/', AssetNameListView.as_view(), name='asset-name-list'),
    path('denomination_names/', DenominationNameListView.as_view(), name='denomination-name-list'),
    
]
