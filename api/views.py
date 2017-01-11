from django.shortcuts import render
from rest_framework import generics
from api.models import Candidate, Dropdown, DropdownList
from api.serializers import CandidateSerializer, DropdownSerializer, DropdownListSerializer


class CandidateList(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class DropdownLists(generics.ListCreateAPIView):
    queryset = Dropdown.objects.all()
    serializer_class = DropdownSerializer


class DropdownDetail(generics.RetrieveUpdateAPIView):
    queryset = Dropdown.objects.all()
    serializer_class = DropdownSerializer
    lookup_field = 'field_name'


class DropdownValues(generics.ListCreateAPIView):
    queryset = DropdownList.objects.all()
    serializer_class = DropdownListSerializer

