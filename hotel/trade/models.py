from django.db import models

# Create your models here.
class Unit(models.Model):
    title=models.CharField(max_length=70,verbose_name='Единица измерения')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Единица измерения'
        verbose_name_plural='Единицы измерения'
        ordering=['title',]

class Operation(models.Model):
    title=models.CharField(max_length=50,verbose_name='Операция')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Операция'
        verbose_name_plural='Операции'
        ordering=['title',]

class Operator(models.Model):
    title=models.CharField(max_length=70,verbose_name='Фамилия,Имя,Отчество')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Администратор'
        verbose_name_plural='Администраторы'
        ordering=['title',]

class Category(models.Model):
    title=models.CharField(max_length=70,verbose_name='Категория')
    image = models.ImageField(upload_to='photo', blank=True,verbose_name='Картинка')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['title',]

class Pay(models.Model):
    title=models.CharField(max_length=70,verbose_name='Вид оплаты')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Вид оплаты'
        verbose_name_plural='Виды оплаты'
        ordering=['title',]

class Customer(models.Model):
    title=models.CharField(max_length=70,verbose_name='Организация')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Организация'
        verbose_name_plural='Организации'
        ordering=['title',]

class Dealer(models.Model):
    title=models.CharField(max_length=70,verbose_name='Поставщик')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Поставщик'
        verbose_name_plural='Поставщики'
        ordering=['title',]
class Good(models.Model):
    title=models.CharField(max_length=100,verbose_name='Наименование')
    unit=models.ForeignKey(Unit,on_delete=models.PROTECT,verbose_name='Единица измерения')
    category=models.ForeignKey(Category,on_delete=models.PROTECT,verbose_name='Категория')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'
        ordering=['title',]

class Doc(models.Model):
    nomerdoc=models.CharField(max_length=20,verbose_name="Номер документв")
    datadoc=models.DateField(verbose_name='Дата документа')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Создан')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Обновлен')
    dealer=models.ForeignKey(Dealer,verbose_name='Поставщик',on_delete=models.PROTECT)
    buytotal=models.FloatField(verbose_name='Итого по цене закупки',null=False,default=0)
    saletotal=models.FloatField(verbose_name='Итого по цене продажи',null=False,default=0)
    transaction=models.BooleanField(verbose_name='Проведен',default=False)
    typedoc=models.IntegerField(verbose_name='Тип документа',default=1)
    def __str__(self):
        return str(self.nomerdoc)
    class Meta:
        verbose_name='Документ'
        verbose_name_plural='Документы'


class DocJurnal(models.Model):
    iddoc=models.ForeignKey(Doc,verbose_name='Документ',on_delete=models.PROTECT)
    title=models.ForeignKey(Good,verbose_name='Наименование товара',on_delete=models.PROTECT)
    unit=models.CharField(verbose_name='Единица измерения',max_length=20)
    volume=models.FloatField(verbose_name='Количество')
    buyprice=models.FloatField(verbose_name='Цена закупки')
    percent=models.FloatField(verbose_name='Наценка,%')
    saleprice=models.FloatField(verbose_name='Цена продажи')
    buytotal=models.FloatField(verbose_name='Сумма по цене закупки',null=False,default=0)
    saletotal=models.FloatField(verbose_name='Сумма по цене продажи',null=False,default=0)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Создан')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Обновлен')

    class Meta:
        verbose_name='Наименование'
        verbose_name_plural='Наименования'
        ordering=['title',]




