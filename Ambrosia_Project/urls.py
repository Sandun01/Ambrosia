from django.conf.urls import url
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name="home"),

    path('ViewAllUsers', views.view_AllUsers, name="view_all_users"),
    path('ViewAllUsers/EditUser', views.ShowUser, name="update_user"),
    path('ViewAllUsers/UpdateUserdetails', views.UpdateUser, name="update_user_details"),
    path('ViewAllUsers/', views.DeleteUser, name="delete_user"),
    path('AddUser', views.registration, name='register'),


    path('Factory', views.factoryHomepage, name='factory_home'),
    path('Shop', views.teashopHomepage, name='teashop_home'),


    path('Shop/InventoryHome', views.inventoryhome, name="inventoryhome"),

    #salesManagement

    path('Shop/SalesHomeIncome/SalesCreateInvoice', views.SalesCreateInvoice, name="SalesCreateInvoice"),
    path('Shop/SalesHomeIncome/DeleteSalesCreateInvoice', views.BillRowDelete, name="BillRowDelete"),
    path('Shop/SalesHomeIncome/SalesCreateInvoice/SalesViewBill', views.SalesViewBill, name="SalesViewBill"),

    path('Shop/SalesHomeIncome/SalesTransaction', views.SalesTransaction, name="SalesTransaction"),
    path('Shop/SalesHomeIncome/SalesTransaction/SalesViewBill', views.SalesViewBill, name="SalesViewBill"),
    path('Shop/SalesHomeIncome/SalesTransaction/BillPDF', GenerateBill.as_view(), name="SalesBill"),

    # path('Shop/SalesHomeIncome/SalesTransaction/SalesViewBill/Vdelete', views.Vdelete, name="Vdelete"),
    path('Shop/SalesHomeIncome/SalesPriceTable', views.SalesPriceTable, name="SalesPriceTable"),

    path('Shop/SalesHomeIncome/SalesPriceTable/ShopPriceTableEdit', views.ShopPriceTableEdit, name="ShopPriceTableEdit"),
    path('Shop/SalesHomeIncome/SalesPriceTable/ShopPriceTableUpdate', views.ShopPriceTableUpdate, name="ShopPriceTableUpdate"),

    path('Shop/SalesHomeIncome', views.SalesHomeIncome, name="SalesHomeIncome"),
    path('Shop/SalesHomeIncome/IncomeMonthlyGeneratePDF', GeneratePDFInvoiceMonthly.as_view(), name="generateIncomePdfMonthly"),
    path('Shop/SalesHomeIncome/AnnualIncomeGeneratePDF', GeneratePDFInvoiceAnnually.as_view(), name="SalesHomeAnnuallyIncome"),


]

