from django.shortcuts import render
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

from django.http import JsonResponse
from django.views import View
from django.db import connection

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



# class WalletTransactionView(View):
    
#     def get(self, request, *args, **kwargs):
#         user_id = 'DupC0001'  # Hardcoded user ID
#         wallet_id = None
#         transactions = []

#         try:
#             with connection.cursor() as cursor:
#                 # Fetch the wallet_id from the currency_converter_fiatwallet table based on user_id
#                 cursor.execute("""
#                     SELECT fiat_wallet_id 
#                     FROM currency_converter_fiatwallet 
#                     WHERE user_id = %s 
#                     ORDER BY user_id DESC LIMIT 1
#                 """, [user_id])
#                 row = cursor.fetchone()

#                 if row:
#                     wallet_id = row[0]

#                     # Fetch all transaction details from the transaction_table based on the wallet_id
#                     cursor.execute("""
#                         SELECT transaction_id, sender_mobile_number, user_phone_number, transaction_amount, transaction_fee, transaction_timestamp
#                         FROM transaction_table 
#                         WHERE wallet_id = %s
#                     """, [wallet_id])
#                     transactions = cursor.fetchall()

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#         # Format transactions into a list of dictionaries
#         transaction_data = [
#             {
#                 'transaction_id': transaction[0],
#                 'sender_mobile_number': transaction[1],
#                 'user_phone_number': transaction[2],
#                 'transaction_amount': transaction[3],
#                 'transaction_fee': transaction[4],
#                 'transaction_timestamp': transaction[5],
#             } 
#             for transaction in transactions
#         ]

#         if wallet_id:
#             return JsonResponse({
#                 'wallet_id': wallet_id,
#                 'transactions': transaction_data
#             })
#         else:
#             return JsonResponse({
#                 'message': 'No wallet found for the given user ID.'
#             }, status=404)




class WalletTransactionView(View):
 
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id')  # Get user_id from query parameters
        if not user_id:
            return JsonResponse({'error': 'User ID is required.'}, status=400)
            
        wallet_id = None
        transactions = []

        try:
            with connection.cursor() as cursor:
                # Fetch the wallet_id from the currency_converter_fiatwallet table based on user_id
                cursor.execute("""
                    SELECT fiat_wallet_id 
                    FROM currency_converter_fiatwallet 
                    WHERE user_id = %s 
                    ORDER BY user_id DESC LIMIT 1
                """, [user_id])
                row = cursor.fetchone()

                if row:
                    wallet_id = row[0]

                    # Fetch all transaction details from the transaction_table based on the wallet_id
                    cursor.execute("""
                        SELECT transaction_id, sender_mobile_number, user_phone_number, transaction_amount, transaction_fee, transaction_timestamp
                        FROM transaction_table 
                        WHERE wallet_id = %s
                    """, [wallet_id])
                    transactions = cursor.fetchall()

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

        # Format transactions into a list of dictionaries
        transaction_data = [
            {
                'transaction_id': transaction[0],
                'sender_mobile_number': transaction[1],
                'user_phone_number': transaction[2],
                'transaction_amount': transaction[3],
                'transaction_fee': transaction[4],
                'transaction_timestamp': transaction[5],
            } 
            for transaction in transactions
        ]

        if wallet_id:
            return JsonResponse({
                'wallet_id': wallet_id,
                'transactions': transaction_data
            })
        else:
            return JsonResponse({
                'message': 'No wallet found for the given user ID.'
            }, status=404)