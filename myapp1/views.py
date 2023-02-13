
from django.http import HttpResponse
from .models import Type, Item
from django.shortcuts import get_list_or_404,render
from datetime import datetime
from django.views.generic import View

def index(request):

        item_list = Item.objects.all().order_by('-price')[:10]
        return render(request, 'myapp1/index.html', {'item_list': item_list})
        response = HttpResponse()
        heading1 = '<p>' + 'Different Types: ' + '</p>'
        response.write(heading1)
        for item in item_list:
            para = '<p>' + str(item.price) + ': ' + str(item) + '</p>'
            response.write(para)
        return response

def about(request,year,month):
    month_name = datetime.strftime(datetime(2000, month, 1), '%B')
    response = HttpResponse()
    response.write(f'<p>This is an Online Grocery Store - {month_name} {year}</p>')
    return response

def detail(request, type_no):
    item_list = get_list_or_404(Item, type=type_no)
    response = HttpResponse()
    for item in item_list:
        response.write('<p>' + item.name + '</p>')
    return response

# FBV(function -based - view)
# Simple to write and understand.
# Good for basic logic.
def type_list(request):
    types = Type.objects.all()
    response = HttpResponse()
    for typ in types:
        response.write('<p>' + typ.name + '</p>')
    return response

# CBV(class-based-view)
# Can be inherited
# Reusable
# can handle complex logic
class TypeListView(View):
    def get(self, request):
        types = Type.objects.all()
        response = HttpResponse()
        for typ in types:
            response.write('<p>' + typ.name + '</p>')
        return response