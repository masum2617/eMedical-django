from django.shortcuts import render
from .models import Category, Drug
from .choices import category
# Create your views here.
# def pharmacy(request):

    # cardiovascular = Cardiovascular.objects.order_by('-id')

    # cardio_condition = Cardiovascular.objects.values_list('condition', flat=True).distinct()

    # if 'keywords' in request.GET:
    #     keywords = request.GET['keywords']
    #     if keywords:
    #         cardiovascular = cardiovascular.filter(drug_name__icontains=keywords)

    # if 'drugCategory' in request.GET:
    #     drugCategory = request.GET['drugCategory']
    #     if drugCategory:
    #         cardiovascular = cardiovascular.filter(drug_category__iexact=drugCategory)
    
    # context = {
    #     'category': category,
        
    # }
    # return render(request, 'pharmacy/pharmacy.html', context)

def pharmacy(request):
    drugs = Drug.objects.order_by('-id')
    cardio_condition = Drug.objects.values_list('condition', flat=True).distinct()

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            drugs = drugs.filter(drug_name__icontains=keywords)
    
    if 'drugCategory' in request.GET:
        drugCategory = request.GET['drugCategory']
        if drugCategory:
            drugs = drugs.filter(category__drug_category__icontains=drugCategory)

    if 'condition' in request.GET:
        condition = request.GET['condition']
        if condition:
            drugs = drugs.filter(condition__iexact=condition)

    context = {
        'drugs': drugs,
        'category': category,
        'cardio_condition':cardio_condition,
    }    
    return render(request, 'pharmacy/pharmacy.html', context)