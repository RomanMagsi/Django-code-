from django.http import HttpResponse
from django.shortcuts import render
from estore.Models.Product import Product
from estore.Models.Category import Category
from estore.Models.Customer import Customer
from django.contrib.auth.hashers import make_password,check_password
#action
def index(request):
    cat=request.GET.get('category')
    print('Got id ',cat)
    if cat:
        prds=Product.get_products_by_category(cat)
    else:
        prds=Product.get_all_products()
    ctrs=Category.get_all_categories()
    return render(request,"home.html",{'products':prds,'category':ctrs})

def about(request):
    return render(request,'about.html')

def contact(request):
    return HttpResponse("<h1>Contact Us Section</h1>")

def login(request):
    print('Login Function Called')
    if request.method=="GET":
        print('GET Method Called')
        return render(request,'Login.html')
    else:
        print('POST METHOD Called')
        post=request.POST;
        email=post.get('email')
        passw=post.get('pass')
        error=''
        if not email:
            error='email cannot be empty'
        elif not passw:
            error='password cannot be empty'
        else:
            customer=Customer.customer_by_email(email)
            if customer:
                print(customer.email)
                if check_password(passw,customer.password):
                    print('Password matched')
                else:
                    print('Password not matched')
                print('Customer found')
            else:
                print('Customer not found')


        return render(request,'Login.html',{'error':error})

def signup(request):
    if request.method=="GET":
        print('GET request Called')
        return render(request,'signup.html')
    else:
        error=''
        post_req = request.POST
        c=Customer()
        c.name=post_req.get('name')
        c.email=post_req.get('email')
        c.phone=post_req.get('phone')
        password=post_req.get('pass')
        c_password=post_req.get('passa')
        valued = {
            'fname':c.name,
            'email':c.email,
            'phone':c.phone
        }
        if password!=c_password:
            error="Password does not match"
        elif len(password) < 8:
            error += "\nPassword should be 8 characters long"
        elif not c.name:
            error="Name should not blank"
        elif not c.email:
            error='Email should not blank'
        elif c.ifExists():
            error='Account Already Existed, Please Login'
        else:
            c.password=make_password(password)
            c.register()
            error="Account Created Successfully"
        print('POST request Called')
        data={
            'error':error,
            'value':valued
        }
        return render(request, 'signup.html',data)

