from rest_framework import serializers
from .models import  DupayAccount, DupayAsset, DupayDenomination, DupayAddress, Phase
from .models import Account,Asset,Phases,Denomination,Address

# to fetch account id
class AccountIdSerializer(serializers.ModelSerializer):
    account_id = serializers.CharField()
    class Meta:
        model = Account
        fields = ['account_id', 'account_type']

# to fetch asset id
class AssetIdSerializer(serializers.ModelSerializer):
    asset_id = serializers.CharField()
    class Meta:
        model = Asset
        fields = ['asset_id', 'asset_name']

class DenominationIdSerializer(serializers.ModelSerializer):
    denomination_id = serializers.CharField()
    class Meta:
        model = Denomination
        fields = ['denomination_id', 'denomination_name']

# ============================================================

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['account_type', 'account_name']

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['asset_name', 'description','account_id']

class DenominationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denomination
        fields = ['denomination_name', 'symbol','asset_id']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_name', 'default_flag','denomination_id']

class PhasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phases
        fields = ['phase_name']

# ===========================================================
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
