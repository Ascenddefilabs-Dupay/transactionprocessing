from rest_framework import serializers
from .models import  DupayAccount, DupayAsset, DupayDenomination, DupayAddress, Phase
from .models import Account,Asset,Phases,Denomination,Address

# to fetch account id
class AccountIdSerializer(serializers.ModelSerializer):
    duc_account_id = serializers.CharField()
    class Meta:
        model = Account
        fields = ['duc_account_id', 'duc_account_type']

# to fetch asset id
class AssetIdSerializer(serializers.ModelSerializer):
    duc_asset_id = serializers.CharField()
    class Meta:
        model = Asset
        fields = ['duc_asset_id', 'duc_asset_name']

class DenominationIdSerializer(serializers.ModelSerializer):
    duc_denomination_id = serializers.CharField()
    class Meta:
        model = Denomination
        fields = ['duc_denomination_id', 'duc_denomination_name']

# ============================================================

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['duc_account_type', 'duc_account_name']

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['duc_asset_name', 'duc_description','duc_account_id']

class DenominationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denomination
        fields = ['duc_denomination_name', 'duc_symbol','duc_asset_id']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['duc_address_name', 'duc_default_flag','duc_denomination_id']

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
