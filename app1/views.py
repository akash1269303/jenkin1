from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from app1.forms import ProductForm
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

class Insert_Product(View):
    def post(self,request):
        b_data=request.body 
        s_data= io.BytesIO(b_data) 
        d_data=JSONParser().parse(s_data)
        ps=ProductForm(data=d_data)
        if ps.is_valid():
            ps.save()
            message={"sucess":"data is saved"}
        else:
            message={"error":ps.errors}
            json_data=JSONRenderer().render(message)
        return HttpResponse(json_data,content_type="application/json")
