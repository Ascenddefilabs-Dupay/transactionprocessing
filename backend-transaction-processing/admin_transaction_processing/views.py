from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import DupayAccount, DupayAsset, DupayDenomination, DupayAddress, Phase
from .serializers import AccountIdSerializer, DupayAccountSerializer, DupayAssetSerializer, DupayDenominationSerializer, DupayAddressSerializer, PhaseSerializer
from .models import Account,Asset,Denomination
from .serializers import AccountSerializer,AssetSerializer,PhasesSerializer,DenominationSerializer,AssetIdSerializer,AddressSerializer,DenominationIdSerializer

#  to fetch accounts names
class AccountNameListView(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountIdSerializer(accounts, many=True)
        return Response(serializer.data)
    
class AssetNameListView(APIView):
    def get(self, request):
        assets = Asset.objects.all()
        serializer = AssetIdSerializer(assets, many=True)
        return Response(serializer.data)
    
class DenominationNameListView(APIView):
    def get(self, request):
        denominations = Denomination.objects.all()
        serializer = DenominationIdSerializer(denominations, many=True)
        return Response(serializer.data)
    
# ==============================================================================

# to store accounts details
class AccountCreateView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  to store asset details   
class AssetCreateView(APIView):
    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#  to store Denomination details   
class DenominationCreateView(APIView):
    def post(self, request):
        serializer = DenominationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#  to store Address details   
class AddressCreateView(APIView):
    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  to store phases details  
class PhasesCreateView(APIView):
    def post(self, request):
        serializer = PhasesSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# ====================================================

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


