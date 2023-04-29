

from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponse
#
from app.models import Category,Product,contact_us,Order,Brand,DetailsOfUser
from django.contrib.auth import authenticate,login
from app.models import UserCreateForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User
from django.contrib import messages
from grocery_store.forms import ProductForm


def Master(request):
    return render(request,'master.html')

def Index(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    product = Product.objects.all()
    categoryID = request.GET.get('category')

    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product=Product.objects.filter(brand = brandID).order_by('-id')
    else:
        product = Product.objects.all()





    context = {
        'category' : category,
        'product':product,
        'brand':brand,
    }

    return render(request,'index.html',context)



def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user= authenticate(
                username= form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
               
            )
            login(request,new_user)
            return redirect('details')
    else:
        form = UserCreateForm()

    context = {
        'form': form,

    }

    return render(request,'registration/signup.html',context)


def details(request):
    
    if request.method == 'POST':
        
        details = DetailsOfUser(
              first_name = request.POST.get('first_name'),
              last_name = request.POST.get('last_name'),
              city = request.POST.get('city'),
              phone = request.POST.get('phone'),
              pincode = request.POST.get('pincode'),
              address = request.POST.get('address'),
            )
        details.save()
        return redirect('index')
    #     context = {
    #     'details': details,

    # }
    return render(request,'details.html')
    # return redirect('index')

        
      
    # return HttpResponse("this is checkout")

        

@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')




def contact_page(request):
    if request.method=='POST':
        contact = contact_us(
            name = request.POST.get('name'),
            email=request.POST.get('email'),
            subject= request.POST.get('subject'),
            message=request.POST.get('message'),

        )
        contact.save()

    return render(request,'contact.html')




def CheckOut(request):
    if request.method == 'POST':

        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)
       

     
        # if res>1:
        
        #     return render(request,)
        


        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a* b

        
            
             

            
            
            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                total= total,
                # val= cart[i]['stock'] - cart[i]['quantity'] ,
            )
            order.save()


        request.session['cart'] ={}
        # context = {
        #     'stock': val
        # }
        return redirect('index')
    return HttpResponse("this is checkout")


def Your_Order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)


    order = Order.objects.filter(user=user)
    context = {
        'order': order,
    }
    print(user,order)


    return render(request,'order.html',context)

def Blog(request):
    return render(request,'blog.html')

def Product_page(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    product = Product.objects.all()
    categoryID = request.GET.get('category')

    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
        'category':category,
        'brand':brand,
        'product':product

    }
    return render(request,'product.html',context)
def Product_Detail(request,id):
    product = Product.objects.filter(id=id).first()
    context = {
        'product':product
    }
    return render(request,'product_detail.html',context)

def Search(request):
    query = request.GET['query']
    product = Product.objects.filter(name__icontains = query)
    context = {
        'product':product,
    }
    return render(request,'search.html',context)



def admin_login(request):
   if request.user.is_authenticated:
      return redirect('seller_page')
   else:
      if request.method == "POST":
         username = request.POST.get('username')
         password = request.POST.get('password')
         print(username, password)
      # check if user has entered correct credentials
         user = authenticate(username=username, password=password)
         if username=="sagar" and password=="12345":
            login(request,user)
            return redirect('seller_page')
         elif user is not None:
            #A backend authenticated the credentials
            login(request, user)
            return redirect('index')
        #  else:
        #     #No backend authenticated the credentials
        #     # messages.info(request, 'Username OR password is incorrect')
            # return render(request, 'seller/admin_login.html')
      return render(request, 'seller/admin_login.html')

    
   

def admin_register(request):
    return render(request,'admin_register')


@login_required(login_url="/accounts/login/")
def seller(request):
    return render(request,'admin_index.html')

@login_required(login_url="/accounts/login/")
def products_list(request):
    product = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('products_list')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
    }
    # context = {
    #     'form': form,

    # }

    return render(request, 'products_list.html', context)


@login_required(login_url="/accounts/login/")
def orders_list(request):
    order = Order.objects.all()
    context = {
        'order': order,
    }
    return render(request,'orders_list.html', context)


@login_required(login_url="/accounts/login/")
# @allowed_users(allowed_roles=['Admin'])
def products_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('products_list')
    context = {
        'item': item
    }
    return render(request, 'products_delete.html', context)


@login_required(login_url="/accounts/login/")
def products_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'products_edit.html', context)
