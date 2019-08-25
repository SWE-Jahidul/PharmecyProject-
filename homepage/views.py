from django.shortcuts import render
from controlpanel.models import Medicine, Category

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        
        searchby = request.POST['sorting']
        searchfor = request.POST['s_name']

        if searchby == 'brand':
            getItembyBrand = Medicine.objects.filter(brandName=searchfor)
            return render(request, 'index.html', {'medicines': getItembyBrand})

        elif searchby == 'category':
            getItemByCategory = Medicine.objects.filter(category=searchfor)
            return render(request, 'index.html', {'medicines': getItemByCategory})
        
        elif searchby == 'generic':
            getItemByGeneric = Medicine.objects.filter(generic=searchfor)
            return render(request, 'index.html', {'medicines': getItemByGeneric})
        else:
            target = Medicine.objects.get(name=searchfor)

            getAllCategorizeItem = Medicine.objects.filter(category=target.category)
            return render(request, 'index.html', {'medicines': getAllCategorizeItem})
    else: 
        allmedicine = Medicine.objects.all()
        return render(request, 'index.html', {'medicines': allmedicine})