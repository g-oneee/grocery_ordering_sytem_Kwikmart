from django.db import models



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
import datetime



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def  __str__(self):
        return self.name




class Sub_Category(models.Model):
    name = models.CharField(max_length=150)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    # Availability = (('In Stock ','In Stock' ),('Out of Stock','Out of Stock'))
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='ecomerce/pimg')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    # Availability = models.CharField(choices=Availability,null=True,max_length=100)
    date = models.DateField(auto_now_add= True)
    stock= models.IntegerField()
    threshold_value = models.IntegerField()
    def __str__(self):
        return self.name


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Email',error_messages={'exists':'This Already Exists'})
    class Meta:
        model = User
        # fields = ('username','email','password1','password2','first_name','last_name','city','phone','pincode', 'address')
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password1'
        self.fields['password2'].widget.attrs['placeholder'] = ' Confirm Password'

        # self.fields['first_name'].widget.attrs['placeholder'] = ' Full name'
        # self.fields['last_name'].widget.attrs['placeholder'] = ' first name'
        # self.fields['phone'].widget.attrs['placeholder'] = ' Phone'
        # self.fields['pincode'].widget.attrs['placeholder'] = ' pincode'
        # self.fields['address'].widget.attrs['placeholder'] = ' adrress'



    def save(self,commit=True):
        user = super(UserCreateForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_massage['exists'])
        return self.cleaned_data['email']


class contact_us(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField(max_length=50)

    subject =models.CharField(max_length=200)

    message =models.TextField(max_length=200)

    def __str__(self):
        return self.name



class Order(models.Model):
    image = models.ImageField(upload_to='ecomerce/order/image')
    product = models.CharField(max_length=1000,default='')
   
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=10)
    price = models.IntegerField()
    total = models.CharField(max_length=100,default='')
    date = models.DateField(default=datetime.datetime.today)


    def __str__(self):
        return self.product

class DetailsOfUser(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
    address = models.TextField()
    def __str__(self):
        return self.first_name
