from django.shortcuts import render

# Create your views here.
def company_list(request):
    return render(request, 'corp/company_list.html', {})