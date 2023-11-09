from typing import Any
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Company
from django.http.response import JsonResponse
import json

# Descripción General: Vista Controlador de las peticiones y ls respuestas del Api


class CompanyView(View):

    
    #Metodo que obvia el CSRF
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs): 
       return super().dispatch(request, *args, **kwargs)

    
    # Metodo que permite realizar consultas All(0) o especifica(id)
    def get(self, request, id=0):
       if(id>0):
            companies=list(Company.objects.filter(id=id).values()) 
            if len(companies)>0:
                 company=companies[0]
                 datos={'message':"Success",'company':company}
            else:
                 datos={'message':"Company not found"}
            return JsonResponse(datos)

       else:
            companies=list(Company.objects.values())
            if len(companies)>0:
                datos={'message':"Success",'companies':companies}
            else:
                datos={'message':"Companies not found"}
            return JsonResponse(datos)

    # Metodo que permite realizar el guardado de una compañia
    def post(self, request):
        datos={'message':"Success"}
        jd=json.loads(request.body)
        Company.objects.create(name=jd['name'],website=jd['website'],foundation=jd['foundation'])
        return JsonResponse(datos)

    
    # Metodo que permite realizar modificacion una compañia especifica
    def put(self, request,id):
        jd=json.loads(request.body)
        companies=list(Company.objects.filter(id=id).values()) 
        if len(companies)>0:
            company = Company.objects.get(id=id)
            company.name=jd['name']
            company.website=jd['website']
            company.foundation=jd['foundation']
            company.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Company not found"}
        return JsonResponse(datos)


    # Metodo que permite Eliminar una compañia especifica
    def delete(self, request, id):
       companies=list(Company.objects.filter(id=id).values()) 
       if len(companies)>0:
           Company.objects.filter(id=id).delete()
           datos={'message':"Success"}
       else:
            datos={'message':"Company not found"}
       return JsonResponse(datos)
