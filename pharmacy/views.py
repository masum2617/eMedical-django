from django.shortcuts import render
from .models import Cardiovascular
# Create your views here.
def pharmacy(request):
    cardiovascular = Cardiovascular.objects.order_by('-id')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            cardiovascular = cardiovascular.filter(drug_name__icontains=keywords)

    if 'drugCategory' in request.GET:
        drugCategory = request.GET['drugCategory']
        if drugCategory:
            cardiovascular = cardiovascular.filter(drug_category__iexact=drugCategory)
    
    context = {
        'cardiovascular':cardiovascular,
    }
    return render(request, 'pharmacy/pharmacy.html', context)

