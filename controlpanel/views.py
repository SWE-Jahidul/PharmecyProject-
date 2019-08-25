from django.shortcuts import render, redirect
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers


# login .
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username.strip() != '' and password.strip() != '':
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('manage')
            else:
                return render(request, 'cpanel/index.html', {'error': 'Login Failed!'})
        else:
            return render(request, 'cpanel/index.html', {'error': 'You must enter username and password!'})
    else:
        return render(request, 'cpanel/index.html')

@login_required(login_url='loginpage')

def controlpanel(request):
    if request.method == 'POST':
        pass 
    else:
        return render(request, 'cpanel/homepage.html')

@login_required(login_url='loginpage')

def add(request):
    categories = models.Category.objects.all()
    generic = models.Generic.objects.all()
    mtypes = models.Mtypes.objects.all()

    if request.method == 'POST':
        name = request.POST['m_name']
        cat = request.POST['medicine_catagory']
        brand = request.POST['brand_name']
        generic =request.POST['generic']
        price = request.POST['price']
        expire = request.POST['expired_date']
        mtype = request.POST['mtype']
       
        if name.strip() != '' and cat.strip() != '' and brand.strip() != '' and price.strip() !='' and expire.strip() != '':
            medicine = models.Medicine()
            medicine.name = name
            medicine.category = cat
            medicine.brandName = brand
            medicine.generic = generic
            medicine.pricePerTablet = price
            medicine.expireDate = expire
            medicine.mtype = mtype
            medicine.save()
            return render(request, 'cpanel/add.html', {'categories': categories, 'generics':generic, 'mtypes':mtypes, 'success': 'New Medicine Added Successfully'})
        else:
            return render(request, 'cpanel/add.html', {'categories': categories, 'generics':generic, 'mtypes':mtypes, 'error': 'You must fill up all information!'})
    else:
        return render(request, 'cpanel/add.html', {'categories': categories, 'generics':generic, 'mtypes':mtypes})

@login_required(login_url='loginpage')

def category(request):
    available = models.Category.objects.all()

    print(available)
    if request.method == 'POST':
        catName = request.POST['cname']

        if catName.strip() != '':
            category = models.Category()
            category.name = catName
            category.save()
            return render(request, 'cpanel/category.html', {'success': 'New Category added Successfully', 'available': available})
        else:
            return render(request, 'cpanel/category.html', {'error': 'You must give me a category name', 'available': available})

    else:
        return render(request, 'cpanel/category.html', {'available': available})


def generic(request):
    available = models.Generic.objects.all()

    print(available)
    if request.method == 'POST':
        genName = request.POST['gname']

        if genName.strip() != '':
            generic = models.Generic()
            generic.name = genName
            generic.save()
            return render(request, 'cpanel/generic.html', {'success': 'New Category added Successfully', 'available': available})
        else:
            return render(request, 'cpanel/generic.html', {'error': 'You must give me a category name', 'available': available})

    else:
        return render(request, 'cpanel/generic.html', {'available': available})


def medicine(request):
    available = models.Medicine.objects.all()
    return render(request, 'cpanel/allMedicineDetails.html', {'available': available})

def sale(request):
    available = models.Medicine.objects.all()
    return render(request, 'cpanel/sale.html', {'medicine': available})

def mdetails(request, mid):
    medicine = models.Medicine.objects.get(id=mid)
    medicine_serialized = serializers.serialize('json', medicine)
    return JsonResponse(medicine_serialized, safe=False) 

@login_required(login_url='loginpage')
def logoutNow(request):
    logout(request)
    return redirect('loginpage')