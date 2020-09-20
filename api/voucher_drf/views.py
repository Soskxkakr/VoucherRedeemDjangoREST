from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import VoucherForm
from .models import Voucher
from .serializers import VoucherSerializer

# Create your views here.
# Redeem Voucher View
def voucher_view(request):
    obj = Voucher.objects.all().values()

    if request.method == "POST":
        form = VoucherForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['voucher_code']
            check_voucher(request, entered_code)        

    form = VoucherForm()
    return render(request, 'templates/voucher.html', {'voucher' : form})

# GET ALL Vouchers json
@api_view(['GET'])
def get_vouchers(request):
    vouchers = Voucher.objects.all()
    serializer = VoucherSerializer(vouchers, many=True)
    print("LMAOOOOOOOOO ", serializer.data)
    return Response(serializer.data)

# GET Voucher json based on its id
@api_view(['GET'])
def get_voucher(request, id):
    vouchers = Voucher.objects.get(id=id)
    serializer = VoucherSerializer(vouchers)
    return Response(serializer.data)

# POST a new voucher object
@api_view(['POST'])
def add_voucher(request):
    serializer = VoucherSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# UPDATE an existing voucher object by id
@api_view(['POST'])
def update_voucher(request, id):
    voucher = Voucher.objects.get(id=id)
    serializer = VoucherSerializer(instance=voucher, data=request.data)
    print("INSTANCE: ",voucher)
    print("DATA: ", request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# DELETE a voucher (Method not allowed)
@api_view(['DELETE'])
def delete_voucher(request, id):
    voucher = Voucher.objects.get(id=id)
    # voucher.delete()
    return Response("Method Not Allowed")


# Functions
# Check if the code entered matches any voucher in database or not
def check_voucher(request, entered_code):
    voucher = loop_vouchers(request, entered_code)

    if voucher != None:
        if voucher.get('no_of_use') != 0:
            decrement_use(request, voucher)
            return messages.success(request, str(voucher.get('discount')) + "% OFF")
        else:
            return messages.error(request, "This code has been fully redeemed")
    else:
        return messages.error(request, "Invalid Code")

# Looping the voucher database
def loop_vouchers(request, entered_code):
    obj = Voucher.objects.all().values()

    for voucher in obj:
        if str(entered_code) == str(voucher.get('voucher_code')):
            return voucher

    return None

# Decrease the number of use after a correct voucher has been entered
def decrement_use(request, voucher):
    voucher['no_of_use'] = int(voucher['no_of_use']) - 1

    serializer = VoucherSerializer(instance=Voucher.objects.get(id=voucher.get('id')), data=voucher)
    if serializer.is_valid():
        serializer.save()
