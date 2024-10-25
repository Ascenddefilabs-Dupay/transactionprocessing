from django.db import models
class DupayAccount(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('asset', 'Asset'),
        ('liability', 'Liability'),
    ]
    
    account_id = models.AutoField(primary_key=True)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE_CHOICES)
    account_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class DupayAsset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(DupayAccount, on_delete=models.CASCADE, related_name='assets')
    asset_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
class DupayDenomination(models.Model):
    denomination_id = models.AutoField(primary_key=True)
    asset = models.ForeignKey(DupayAsset, on_delete=models.CASCADE, related_name='denominations')
    denomination_name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Dupay Addresses Table
class DupayAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    denomination = models.ForeignKey(DupayDenomination, on_delete=models.CASCADE, related_name='addresses')
    address_name = models.CharField(max_length=255)
    default_flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Phases Table
class Phase(models.Model):
    PHASE_CHOICES = [
        ('committed', 'Committed'),
        ('pending_incoming', 'Pending Incoming'),
        ('pending_outgoing', 'Pending Outgoing'),
    ]
    
    phase_id = models.AutoField(primary_key=True)
    phase_name = models.CharField(max_length=50, choices=PHASE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# From here connected with frontend code
class Account(models.Model):
    duc_account_id = models.AutoField(primary_key=True)
    duc_account_type = models.CharField(max_length=255)
    duc_account_name = models.CharField(max_length=255)
    duc_created_at = models.DateTimeField(auto_now_add=True)
    duc_updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'dupay_accounts'

class Asset(models.Model):
    duc_asset_id = models.AutoField(primary_key=True)
    duc_asset_name = models.CharField(max_length=255)
    duc_description = models.CharField(max_length=255, blank=True, null=True)
    duc_created_at = models.DateTimeField(auto_now_add=True)
    duc_updated_at = models.DateTimeField(auto_now=True)
    duc_account_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='assets')
    
    class Meta:
        db_table = 'dupay_assets'

class Denomination(models.Model):
    duc_denomination_id = models.AutoField(primary_key=True)
    duc_asset_id = models.ForeignKey(Asset, on_delete=models.CASCADE, null=True, blank=True, related_name='denominations')
    duc_denomination_name = models.CharField(max_length=50)
    duc_symbol = models.CharField(max_length=10)
    duc_created_at = models.DateTimeField(auto_now_add=True)
    duc_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dupay_denominations'

class Address(models.Model):
    duc_address_id = models.AutoField(primary_key=True)
    duc_denomination_id = models.ForeignKey(Denomination, on_delete=models.CASCADE, null=True, blank=True, related_name='addresses')
    duc_address_name = models.CharField(max_length=255)
    duc_default_flag = models.BooleanField(default=False)
    duc_created_at = models.DateTimeField(auto_now_add=True)
    duc_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dupay_address'

class Phases(models.Model):    
    phase_id = models.AutoField(primary_key=True)
    phase_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dupay_phases'
