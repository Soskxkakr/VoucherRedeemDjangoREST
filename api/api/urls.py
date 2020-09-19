from django.contrib import admin
from django.urls import path

from voucher_drf import views

urlpatterns = [
    path('', views.voucher_view),
    path('get-vouchers/', views.get_vouchers),
    path('get-voucher/<str:id>/', views.get_voucher),
    path('add-voucher/', views.add_voucher),
    path('update-voucher/<str:id>/', views.update_voucher),
    path('delete-voucher/<str:id>/', views.delete_voucher),
    path('site-admin/', admin.site.urls),
]
