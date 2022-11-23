from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.forms.models import model_to_dict

from .models import Account
import ipdb


class AccountView(APIView):
    def get(self, request, account_id):
        try:
            account = Account.objects.get(pk=account_id)
        except Account.DoesNotExist:
            return Response({"error": "account not found"}, 404)

        account_dict = model_to_dict(account)

        ipdb.set_trace()

        return Response(account_dict)


class AccountCreateView(APIView):
    def post(self, request):
        account = Account.objects.create(**request.data)
        account_dict = model_to_dict(account)

        return Response(account_dict, status.HTTP_201_CREATED)
