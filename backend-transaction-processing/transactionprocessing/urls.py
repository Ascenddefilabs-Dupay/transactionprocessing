from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet ,WalletTransactionView

router = DefaultRouter()

router.register(r'projects',ProjectViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('wallet-transactions/', WalletTransactionView.as_view(), name='wallet-transactions'),
]
