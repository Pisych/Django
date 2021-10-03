from django import forms
from django.forms.fields import DateField
from .models import *
# Единицы измерения**************************************************************
class UnitForm(forms.ModelForm):
   class Meta:
    model=Unit
    fields=['title']
    widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control'}),
    }


# Номенклатура**************************************************************
class GoodForm(forms.ModelForm):
    class Meta:
        model=Good
        #fields='__all__'
        fields=['title','unit','category']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'unit':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),

        }




# Администраторы **********************************************************************

class OperatorForm(forms.ModelForm):
    class Meta:
        model=Operator
        #fields='__all__'
        fields=['title',]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'})
        }

#Поставщики
class DealerForm(forms.ModelForm):
    class Meta:
        model=Dealer
        #fields='__all__'
        fields=['title',]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'})
        }

#Организации
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        #fields='__all__'
        fields=['title',]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'})
        }
#Виды оплаты
class PayForm(forms.ModelForm):
    class Meta:
        model=Pay
        #fields='__all__'
        fields=['title',]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'})
        }


# Категории
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        #fields='__all__'
        fields=['title','image',]
        widgets={
           'title':forms.TextInput(attrs={'class':'form-control'}),
           'image':forms.FileInput()
        }




# Документы**************************************************************
class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%d-%m-%Y'

class DocForm(forms.ModelForm):
    class Meta:
        model=Doc
        #fields='__all__'
        fields=['nomerdoc','datadoc','dealer']
        widgets={
            'nomerdoc':forms.TextInput(attrs={'class':'form-control'}),
            'datadoc':MyDateInput(attrs={'class':'form-control '}),
            'dealer':forms.Select(attrs={'class':'form-control'}),
        }


class AddDocTableForm(forms.ModelForm):

    class Meta:
        model=DocJurnal
        fields=['iddoc','title','volume','buyprice','saleprice','percent','buytotal','saletotal']
        labels={'title':'Наименование'}
        widgets={'iddoc':forms.HiddenInput(attrs={'class':'form-control'}),
         'volume':forms.NumberInput(attrs={'class':'form-control','min':0,'value':1,
         'oninput':'getResult()',}),
        'title':forms.Select(attrs={'class':'form-control'}),
        'buyprice':forms.NumberInput(
        attrs={'class': 'form-control','min':0,'value':1,'oninput':'getResult()'}),
        'saleprice': forms.NumberInput(
        attrs={'class': 'form-control', 'min': 0, 'value': 1,'oninput':'getResult()' }),
        'percent': forms.NumberInput(
        attrs={'class': 'form-control', 'min': 0, 'value': 20,'oninput':'getResult()' }),
        'buytotal': forms.NumberInput(
        attrs={'class': 'form-control', 'min': 0, 'value': 1,  }),
        'saletotal': forms.NumberInput(
        attrs={'class': 'form-control', 'min': 0, 'value': 1, }),
        }










