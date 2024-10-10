from django.shortcuts import render
from rest_framework import viewsets
from .models import DupayAccount, DupayAsset, DupayDenomination, DupayAddress, Phase
from .serializers import DupayAccountSerializer, DupayAssetSerializer, DupayDenominationSerializer, DupayAddressSerializer, PhaseSerializer

class DupayAccountViewSet(viewsets.ModelViewSet):
    queryset = DupayAccount.objects.all()
    serializer_class = DupayAccountSerializer

class DupayAssetViewSet(viewsets.ModelViewSet):
    queryset = DupayAsset.objects.all()
    serializer_class = DupayAssetSerializer

class DupayDenominationViewSet(viewsets.ModelViewSet):
    queryset = DupayDenomination.objects.all()
    serializer_class = DupayDenominationSerializer

class DupayAddressViewSet(viewsets.ModelViewSet):
    queryset = DupayAddress.objects.all()
    serializer_class = DupayAddressSerializer

class PhaseViewSet(viewsets.ModelViewSet):
    queryset = Phase.objects.all()
    serializer_class = PhaseSerializer


