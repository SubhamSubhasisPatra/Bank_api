from django.shortcuts import render
from django.db.models import Q
# Create your views here.

from rest_framework import generics
from rest_framework import filters

from .models import Banks, Branches
from .serializers import BankSerializer, BranchSerializer

from .filter import BranchFilter


class BranchView(generics.ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['ifsc']

    # def get_queryset(self):
    #     b = self.request.


class MultiBranchFilter(generics.ListAPIView):
    # data = Bank.objects.filter(name='STATE BANK OF INDIA')

    queryset = Branches.objects.filter()
    serializer_class = BranchSerializer
    filter_class = BranchFilter
