from django.urls import path
from django.conf.urls.static import static
from .views import *
urlpatterns=[
    path('',tradePage,name='tradePage'),
    path('listPage',listPage,name='listPage'),

    path('UnitPage', UnitList, name='UnitPage'),
    path('CreateUnit', CreateUnit, name='CreateUnit'),
    path('UpdateUnit/<str:pk>',UpdateUnit,name='UpdateUnit'),
    path('DeleteUnit/<str:pk>',DeleteUnit,name='DeleteUnit'),

    path('OperatorPage',OperatorList,name='OperatorPage'),
    path('CreateOperator', CreateOperator, name='CreateOperator'),
    path('UpdateOperator/<str:pk>', UpdateOperator, name='UpdateOperator'),
    path('DeleteOperator/<str:pk>', DeleteOperator, name='DeleteOperator'),

    path('PayPage',PayList,name='PayPage'),
    path('CreatePay', CreatePay, name='CreatePay'),
    path('UpdatePay/<str:pk>', UpdatePay, name='UpdatePay'),
    path('DeletePay/<str:pk>', DeletePay, name='DeletePay'),

    path('DealerPage',DealerList,name='DealerPage'),
    path('CreateDealer', CreateDealer, name='CreateDealer'),
    path('UpdateDealer/<str:pk>', UpdateDealer, name='UpdateDealer'),
    path('DeleteDealer/<str:pk>', DeleteDealer, name='DeleteDealer'),

    path('CustomerPage',CustomerList, name='CustomerPage'),
    path('CreateCustomer', CreateCustomer, name='CreateCustomer'),
    path('UpdateCustomer/<str:pk>', UpdateCustomer, name='UpdateCustomer'),
    path('DeleteCustomer/<str:pk>', DeleteCustomer, name='DeleteCustomer'),

    path('CategoryPage',CategoryList,name='CategoryPage'),
    path('CreateCategory', CreateCategory, name='CreateCategory'),
    path('UpdateCategory/<str:pk>', UpdateCategory, name='UpdateCategory'),
    path('DeleteCategory/<str:pk>', DeleteCategory, name='DeleteCategory'),

    path('GoodPage',GoodListByCategory,name='GoodPage'),
    path('CreateGood', CreateGood, name='CreateGood'),
    path('UpdateGood/<str:pk>', UpdateGood, name='UpdateGood'),
    path('DeleteGood/<str:pk>', DeleteGood, name='DeleteGood'),


    path('AddDoc',CreateDoc,name='AddDoc'),
    path('DocList',DocList.as_view(),name='DocList'),
    path('UpdateDocTable/<str:pk>',UpdateDocTable,name='UpdateDocTable'),
    path('DocTable',CreateDocTable,name='DocTable'),
    path('DocView',DocView,name='DocView')

]