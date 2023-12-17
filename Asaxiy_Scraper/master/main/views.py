import sys
sys.path.append(r'C:\Users\....\....\django-json-fetch-master\scraping_projects')
import json
from postgress_db import *
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

@csrf_exempt
def data(request):
    #print(all_data())
    if request.method == 'POST':
        received_data = json.loads(request.body)
        if received_data == 'give_data':
            data_title = all_data()
            return JsonResponse(data_title, safe=False)
    return render(request, '404.html')  


def product_list(request): 
    return render(request, 'index.html')    
