from rest_framework import serializers
from .models import  DupayAccount, DupayAsset, DupayDenomination, DupayAddress, Phase
from .models import Account,Asset,Phases

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['account_type', 'account_name']

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['asset_name', 'description']

class PhasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phases
        fields = ['phase_name']


class DupayAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupayAccount
        fields = '__all__'

class DupayAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupayAsset
        fields = '__all__'

class DupayDenominationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupayDenomination
        fields = '__all__'

class DupayAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupayAddress
        fields = '__all__'

class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = '__all__'
