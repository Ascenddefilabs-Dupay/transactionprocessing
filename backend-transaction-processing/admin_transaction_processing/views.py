from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import DupayAccount, DupayAsset, DupayDenomination, DupayAddress, Phase
from .serializers import DupayAccountSerializer, DupayAssetSerializer, DupayDenominationSerializer, DupayAddressSerializer, PhaseSerializer
from .models import Account,Asset
from .serializers import AccountSerializer,AssetSerializer,PhasesSerializer

class AccountCreateView(APIView):
    def post(self, request):
        print(request.data)
        serializer = AccountSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AssetCreateView(APIView):
    def post(self, request):
        print(request.data)
        serializer = AssetSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PhasesCreateView(APIView):
    def post(self, request):
        print(request.data)
        serializer = PhasesSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


