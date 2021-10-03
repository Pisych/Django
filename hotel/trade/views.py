from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.views.generic import ListView, CreateView,UpdateView,DeleteView # новый
from django.urls import reverse_lazy
from django.template import RequestContext
from django.db.models import Sum
from django.core import paginator# новый
# Страницы справочников*****************************************
global unitmode,stringForm,lastDocPk

def tradePage(request):
    return render(request,'trade/TradePage.html')
def listPage(request):
    return render(request,'trade/ListPage.html')
def VuePage(request):
    return render(request,'trade/VuePage.html')

#Список номенклатуры
class GoodList(ListView):
    model = Good
    template_name = 'trade/GoodPage.html'
    context_object_name = 'data'
def GoodListByCategory(request):
    Cat=Category.objects.all()
    good=Good.objects.all()
    context={'Category':Cat,'Good':good}
    return render(request,'trade/GoodPage.html',context)
#Список категорий
class CategoryList(ListView):
    model = Category
    template_name = 'trade/CategoryPage.html'
    context_object_name = 'data'

# Список единиц измерений
def CreateUnit(request):
        form=UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('UnitPage')
        else:
            form=UnitForm()
            data=Unit.objects.all()
            context = {'data': data, 'form': form}
            return render(request, "trade/NewUnit.html", context)

def UpdateUnit(request,pk):
    unit=Unit.objects.get(id=pk)
    if request.method == 'POST':
        form=UnitForm(request.POST,instance=unit)
        if form.is_valid():
            form.save()
            return redirect('UnitPage')
    else:
        unit = Unit.objects.get(id=pk)
        form = UnitForm(instance=unit)
        data = Unit.objects.all()
        context = {'data': data, 'form': form,'unit':unit}
        return render(request, "trade/UpdateUnit.html", context)

def DeleteUnit(request,pk):
    unit = Unit.objects.get(id=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            try:
                unit.delete()
                return redirect('UnitPage')
            except:
                return redirect('UnitPage')
    else:
        unit = Unit.objects.get(id=pk)
        form = UnitForm(instance=unit)
        data = Unit.objects.all()
        context = {'data': data, 'form': form, 'unit': unit}
        return render(request, "trade/DeleteUnit.html", context)

def UnitList(request):
    data = Unit.objects.all()
    context = {'data': data, }
    return render(request, "trade/UnitPage.html", context)

# Организации
def CreateCustomer(request):
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CustomerPage')
        else:
            form=CustomerForm()
            data=Customer.objects.all()
            context = {'data': data, 'form': form}
            return render(request, "trade/CreateCustomer.html", context)

def UpdateCustomer(request,pk):
    unit=Customer.objects.get(id=pk)
    if request.method == 'POST':
        form=CustomerForm(request.POST,instance=unit)
        if form.is_valid():
            form.save()
            return redirect('CustomerPage')
    else:
        unit = Customer.objects.get(id=pk)
        form = CustomerForm(instance=unit)
        data = Unit.objects.all()
        context = {'data': data, 'form': form,'unit':unit}
        return render(request, "trade/UpdateCustomer.html", context)

def DeleteCustomer(request,pk):
    unit = Customer.objects.get(id=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=unit)
        if form.is_valid():
            try:
                unit.delete()
                return redirect('CustomerPage')
            except:
                return redirect('CustomerPage')
    else:
        unit = Customer.objects.get(id=pk)
        form = CustomerForm(instance=unit)
        data = Customer.objects.all()
        context = {'data': data, 'form': form, 'unit': unit}
        return render(request, "trade/DeleteCustomer.html", context)

def CustomerList(request):
    data = Customer.objects.all()
    context = {'data': data }
    return render(request, "trade/CustomerPage.html", context)

# Поставщики
def CreateDealer(request):
        form=DealerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('DealerPage')
        else:
            form=DealerForm()
            data=Dealer.objects.all()
            context = {'data': data, 'form': form}
            return render(request, "trade/CreateDealer.html", context)

def UpdateDealer(request,pk):
    unit=Dealer.objects.get(id=pk)
    if request.method == 'POST':
        form=DealerForm(request.POST,instance=unit)
        if form.is_valid():
            form.save()
            return redirect('DealerPage')
    else:
        unit = Dealer.objects.get(id=pk)
        form = DealerForm(instance=unit)
        data = Dealer.objects.all()
        context = {'data': data, 'form': form,'unit':unit}
        return render(request, "trade/UpdateDealer.html", context)

def DeleteDealer(request,pk):
    unit = Dealer.objects.get(id=pk)
    if request.method == 'POST':
        form = DealerForm(request.POST, instance=unit)
        if form.is_valid():
            try:
                unit.delete()
                return redirect('DealerPage')
            except:
                return redirect('DealerPage')
    else:
        unit = Dealer.objects.get(id=pk)
        form = DealerForm(instance=unit)
        data = Dealer.objects.all()
        context = {'data': data, 'form': form, 'unit': unit}
        return render(request, "trade/DeleteDealer.html", context)

def DealerList(request):
    data = Dealer.objects.all()
    context = {'data': data }
    return render(request, "trade/DealerPage.html", context)

# Виды оплаты
def CreatePay(request):
        form=PayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PayPage')
        else:
            form=PayForm()
            data=Pay.objects.all()
            context = {'data': data, 'form': form}
            return render(request, "trade/CreatePay.html", context)

def UpdatePay(request,pk):
    unit=Pay.objects.get(id=pk)
    if request.method == 'POST':
        form=PayForm(request.POST,instance=unit)
        if form.is_valid():
            form.save()
            return redirect('PayPage')
    else:
        unit = Pay.objects.get(id=pk)
        form = PayForm(instance=unit)
        data = Pay.objects.all()
        context = {'data': data, 'form': form,'unit':unit}
        return render(request, "trade/UpdatePay.html", context)

def DeletePay(request,pk):
    unit = Pay.objects.get(id=pk)
    if request.method == 'POST':
        form = PayForm(request.POST, instance=unit)
        if form.is_valid():
            try:
                unit.delete()
                return redirect('PayPage')
            except:
                return redirect('PayPage')
    else:
        unit = Pay.objects.get(id=pk)
        form = PayForm(instance=unit)
        data = Pay.objects.all()
        context = {'data': data, 'form': form, 'unit': unit}
        return render(request, "trade/DeletePay.html", context)

def PayList(request):
    data = Pay.objects.all()
    context = {'data': data }
    return render(request, "trade/PayPage.html", context)

# Администраторы
def CreateOperator(request):
        form=OperatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('OperatorPage')
        else:
            form=OperatorForm()
            data=Operator.objects.all()
            context = {'data': data, 'form': form}
            return render(request, "trade/CreateOperator.html", context)

def UpdateOperator(request,pk):
    unit=Operator.objects.get(id=pk)
    if request.method == 'POST':
        form=OperatorForm(request.POST,instance=unit)
        if form.is_valid():
            form.save()
            return redirect('OperatorPage')
    else:
        unit = Operator.objects.get(id=pk)
        form = OperatorForm(instance=unit)
        data = Operator.objects.all()
        context = {'data': data, 'form': form,'unit':unit}
        return render(request, "trade/UpdateOperator.html", context)

def DeleteOperator(request,pk):
    unit = Operator.objects.get(id=pk)
    if request.method == 'POST':
        form = OperatorForm(request.POST, instance=unit)
        if form.is_valid():
            try:
                unit.delete()
                return redirect('OperatorPage')
            except:
                return redirect('OperatorPage')
    else:
        unit = Operator.objects.get(id=pk)
        form = OperatorForm(instance=unit)
        data = Operator.objects.all()
        context = {'data': data, 'form': form, 'unit': unit}
        return render(request, "trade/DeleteOperator.html", context)

def OperatorList(request):
    data = Operator.objects.all()
    context = {'data': data }
    return render(request, "trade/OperatorPage.html", context)


# Категории
def CreateCategory(request):
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('CategoryPage')
        else:
            form=CategoryForm()
            data=Category.objects.all()
            context = {'data': data, 'form': form}
            return render(request, "trade/CreateCategory.html", context)

def UpdateCategory(request,pk):
    unit=Category.objects.get(id=pk)
    if request.method == 'POST':
        form=CategoryForm(request.POST,request.FILES,instance=unit)
        if form.is_valid():
            form.save()
            return redirect('CategoryPage')
    else:
        unit = Category.objects.get(id=pk)
        form = CategoryForm(instance=unit)
        data = Category.objects.all()
        context = {'data': data, 'form': form,'unit':unit}
        return render(request, "trade/UpdateCategory.html", context)

def DeleteCategory(request,pk):
    unit = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=unit)
        if form.is_valid():
            try:
                unit.delete()
                return redirect('CategoryPage')
            except:
                return redirect('CategoryPage')
    else:
        unit = Category.objects.get(id=pk)
        form = CategoryForm(instance=unit)
        data = Category.objects.all()
        context = {'data': data, 'form': form, 'unit': unit}
        return render(request, "trade/DeleteCategory.html", context)

def CategoryList(request):
    data = Category.objects.all()
    context = {'data': data }
    return render(request, "trade/CategoryPage.html", context)
#Номенклатура
def CreateGood(request):
     form = GoodForm(request.POST)
     if form.is_valid():
       form.save()
       return redirect('GoodPage')
     else:
         form = GoodForm()
         good = Good.objects.all()
         cat=Category.objects.all()
         context = {'Good': good, 'form': form,'Category':cat}
         return render(request, "trade/CreateGood.html", context)

def UpdateGood(request,pk):
    unit=Good.objects.get(id=pk)
    if request.method == 'POST':
        form=GoodForm(request.POST,instance=unit)
        if form.is_valid():
            form.save()
            return redirect('GoodPage')
    else:
        unit = Good.objects.get(id=pk)
        form = GoodForm(instance=unit)
        good = Good.objects.all()
        cat = Category.objects.all()
        context = {'Good': good, 'form': form, 'Category': cat}
        return render(request, "trade/UpdateGood.html", context)

def DeleteGood(request,pk):
    unit = Good.objects.get(id=pk)
    if request.method == 'POST':
        form = GoodForm(request.POST, instance=unit)
        if form.is_valid():
            try:
                unit.delete()
                return redirect('GoodPage')
            except:
                return redirect('GoodPage')
    else:
        unit = Good.objects.get(id=pk)
        form = GoodForm(instance=unit)
        good = Good.objects.all()
        cat = Category.objects.all()
        context = {'Good': good, 'form': form, 'Category': cat}
        return render(request, "trade/DeleteGood.html", context)

# Форма нового документа
def CreateDoc(request):

    form = DocForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('DocList')
       # return render(request, "trade/DocPage.html", context)
    else:
        form = DocForm()
        doc = Doc.objects.all()
        context = {'Doc': doc, 'form': form, }
        return render(request, "trade/AddDocPage.html", context)

# Форма табличной части
def CreateDocTable(request):
    lastdoc = Doc.objects.latest('created_at')
    doctable = DocJurnal.objects.filter(iddoc=lastdoc)
    sumsaletotal=DocJurnal.objects.filter(iddoc=lastdoc).aggregate(Sum('saletotal'))
    form=AddDocTableForm(request.POST,initial={'iddoc':lastdoc.id})
    if form.is_valid():
        form.save()
        lastdoc = Doc.objects.latest('created_at')

        context = {'lastdoc': lastdoc, 'form': form, 'doctable': doctable,'saletotal':sumsaletotal}
        print(doctable)
        return render(request, "trade/DocTablePage.html",context)
    else:
        form = AddDocTableForm(initial={'iddoc':lastdoc.id})

        lastdoc = Doc.objects.latest('created_at')
        doctable = DocJurnal.objects.all()
        context = {'lastdoc': lastdoc, 'form': form,'doctable':doctable }
        print(doctable)

        return render(request, "trade/AddTablePage.html", context)

# функция добавления документа*************************


#Список приходных документов
class DocList(ListView):
    model = Doc
    template_name = 'trade/DocPage.html'
    context_object_name = 'data'
    ordering = ['-created_at']
    paginate_by = 15
def DocView(request):
    lastdoc = Doc.objects.latest('created_at')
    doctable = DocJurnal.objects.filter(iddoc=lastdoc.id)
    sumsale = DocJurnal.objects.filter(iddoc=lastdoc).aggregate(Sum('saletotal'))
    sumbuy = DocJurnal.objects.filter(iddoc=lastdoc).aggregate(Sum('buytotal'))
    context = {'lastdoc': lastdoc, 'doctable': doctable,'sumsale':sumsale,'sumbuy':sumbuy}
    print(doctable)
    return render(request, "trade/DocTablePage.html", context)
def UpdateDocTable(request,pk):
    lastdoc=Doc.objects.get(id=pk)
    doctable = DocJurnal.objects.filter(iddoc=lastdoc.id)
    sumsale = DocJurnal.objects.filter(iddoc=lastdoc).aggregate(Sum('saletotal'))
    sumbuy = DocJurnal.objects.filter(iddoc=lastdoc).aggregate(Sum('buytotal'))
    print(sumsale)
    context = {'lastdoc':lastdoc,'doctable':doctable,'sumsale':sumsale,'sumbuy':sumbuy}
    print(context)
    return render(request, "trade/DocTablePage.html", context)

def Test(request,pk):
    return HttpResponse(pk)