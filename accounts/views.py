from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict

from .models import Account


class AccountView(APIView):
    def get(self, request, account_id):
        try:
            account = Account.objects.get(pk=account_id)
        except Account.DoesNotExist:
            return Response({"error": "account not found"}, 404)

        account_dict = model_to_dict(account)

        return Response(account_dict)
