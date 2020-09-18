from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import VoucherForm
from .models import Voucher
from .serializers import VoucherSerializer

# Create your views here.

def sample(request):
    return HttpResponse("Hello World!")

def voucher_view(request):
    obj = Voucher.objects.all().values()

    if request.method == "POST":
        form = VoucherForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['voucher_code']
            check_voucher(request, entered_code)        

    form = VoucherForm()
    return render(request, 'templates/voucher.html', {'voucher' : form})

@api_view(['GET'])
def get_vouchers(request):
    vouchers = Voucher.objects.all()
    serializer = VoucherSerializer(vouchers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_voucher(request, id):
    vouchers = Voucher.objects.get(id=id)
    serializer = VoucherSerializer(vouchers)
    return Response(serializer.data)

@api_view(['POST'])
def add_voucher(request):
    serializer = VoucherSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def update_voucher(request, id):
    voucher = Voucher.objects.get(id=id)
    serializer = VoucherSerializer(instance=voucher, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_voucher(request, id):
    voucher = Voucher.objects.get(id=id)
    # voucher.delete()
    return Response("Method Not Allowed")

# Functions
def check_voucher(request, entered_code):
    obj = Voucher.objects.all().values()

    for voucher in obj:
        if str(entered_code) == str(voucher.get('voucher_code')):
            return messages.success(request, voucher.get('discount'))
        else:
            return messages.error(request, "This code is either used or invalid")