from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
import csv

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.views import View
from django.views.generic import TemplateView
from .models import Bank, Branch
from .serializers import BranchSerializer
from .forms import BankForm
import json

class ImportView(View):
    @staticmethod
    def get(request):
        return render(request, 'upload.html')

    @staticmethod
    def post(request):
        csv_file = request.FILES.get('csv_file')
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        count = 0
        for row in reader:
            bank_name = row.get('bank_name')
            ifsc = row.get('ifsc')
            branch = row.get('branch')
            address = row.get('address')
            city = row.get('city')
            district = row.get('district')
            state = row.get('state')
            print("IFSC-- {}".format(ifsc))
            if not ifsc:
                break
            bank_object, created = Bank.objects.get_or_create(
                name=bank_name
            )
            branch_defaults = {
                'branch': branch,
                'bank': bank_object,
                'address': address,
                'city': city,
                'district': district,
                'state': state
            }

            branch_object, created = Branch.objects.update_or_create(
                ifsc=ifsc, defaults=branch_defaults
            )
            if created:
                print("row created{}".format(branch_defaults))

            count += 1
        messages.success(request, "{} rows imported.".format(count))

        return render(request, 'index.html')


def bankUsingIfsc(request):
    if request.POST:
        # search_ifsc = request.GET.get('ifsc')
        bank = request.POST.get('bank')
        city = request.POST.get('city')
        try:
            # branch = Branch.objects.filter(ifsc__iexact=search_ifsc)
            branch_qset = Branch.objects.filter(
                Q(city__iexact=city),
                Q(bank__name__icontains=bank)
            )
        except ObjectDoesNotExist:
            raise NotFound('Branch not found for given IFSC code')
        # serializerIFSC = BranchSerializer(branch, many=True)
        serializerCity = BranchSerializer(branch_qset, many=True)
        x = JsonResponse(serializerCity.data, safe=False)
        print(x.json())
        return render(request, 'index.html', {"data_city": serializerCity})
    else:
        return render(request, 'index.html')


class DetailView(View):
    @staticmethod
    def get(request, ifsc):
        ifsc_queryset = Branch.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BranchSerializer(ifsc_queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class ListView(View):
    @staticmethod
    def get(request, city, bank):
        branch_queryset = Branch.objects.filter(
            city__iexact=city, bank__name__icontains=bank)
        serializer = BranchSerializer(branch_queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
