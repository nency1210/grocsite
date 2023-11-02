# from django.shortcuts import render, get_object_or_404
# from django.views import View
# from django.shortcuts import redirect
# from django.urls import reverse
# from django.http import HttpResponse, HttpResponseRedirect
# from myapp1.models import Type, Item, OrderItem
# from datetime import datetime
# from myapp1.forms import OrderItemForm, InterestForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required, user_passes_test
#
# @login_required
# def index(request):
#     type_list = Type.objects.all().order_by('id')[:7]
#     return render(request, 'myapp1/index0.html', {'type_list': type_list})
#
#
# # def index(request):
# #     price_list = Item.objects.all().order_by('-price')[:10]
# #     response = HttpResponse()
# #     heading1 = '<p>' + 'Different Types: ' + '</p>'
# #     response.write(heading1)
# #
# #     for i in price_list:
# #         para = '<p>' + str(i.price) + ': ' + str(i) + '</p>'
# #         response.write(para)
# #     return response
#
# def about_date(request, year, month):
#     month_name = datetime.strptime(str(month), '%m').strftime('%B')
#     message = "This is an online grocery store - {} {}.".format(month_name, year)
#     return HttpResponse(message)
#
#
# def about(request):
#     return render(request, 'myapp1/about0.html', {'message': 'This is an online grocery store'})
#
#
# # def detail(request, type_no):
# #     type = get_object_or_404(Type, pk=type_no)
# #     items = Item.objects.filter(type=type).order_by('-price')
# #     response = HttpResponse()
# #     heading = '<p>' + 'Items for type: ' + str(type) + '</p>'
# #     response.write(heading)
# #     for item in items:
# #         para = '<p>' + str(item.name) + ': ' + str(item.price) + '</p>'
# #         response.write(para)
# #     return response
#
# def detail(request, type_no):
#     type = get_object_or_404(Type, pk=type_no)
#     items = Item.objects.filter(type=type).order_by('-price')
#     return render(request, 'myapp1/detail0.html', {'type': type, 'items': items})
#
#
# # Function-Based View (FBV)
# def my_fbv(request):
#     context = {
#         'message': 'Hello, this is my Function-Based View (FBV)!'
#     }
#     return render(request, 'myapp1/my_template.html', context)
#
#
# # Class-Based View (CBV)
# class MyCBV(View):
#     def get(self, request):
#         context = {
#             'message': 'Hello, this is my Class-Based View (CBV)!'
#         }
#         return render(request, 'myapp1/my_template.html', context)
#
#
#
# '''
#
#         CBVs utilize classes and extend the Django View class, whereas FBVs are just functions.
#         To manage different HTTP methods, FBVs rely on the request.method attribute,
#         whereas CBVs utilize the http_method_names attribute to indicate supported methods.
#         In FBVs, the request is provided as an argument to the view function,
#         but in CBVs it can be accessed through the self.request attribute.
#
#
#         #Yes, we are passing the 'posts' variable to the template to display the latest 10 posts.
#
#             #No, we don't need to pass any extra context variables to the about0.html template.'''
#
# @login_required
# def items(request):
#     item_list = Item.objects.all().order_by('id')[:20]
#     return render(request, 'myapp1/items.html', {'item_list': item_list})
#
#
# # def place_order(request):
# #     form = OrderItemForm(request.POST)
# #     if form.is_valid():
# #         form.save()
# #         form = OrderItemForm()
# #
# #     form1 = InterestForm(request.POST)
# #     if form1.is_valid():
# #         form.save()
# #         form1 = InterestForm()
# #
# #     context = {
# #         'form': form,
# #         'form1': form1
# #     }
# #
# #     return render(request, 'myapp1/place_order.html', context)
#
# @login_required
# def place_order(request):
#     msg = ''
#     item_list = Item.objects.all()
#     if request.method == 'POST':
#         form = OrderItemForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             #print(f"\n{order.__dict__}\n")
#             if order.items_ordered <= order.item.stock:
#                 order.save()
#                 #update the stock of item
#                 order.item.stock -= order.items_ordered
#                 order.item.save()
#                 msg = 'Your order has been placed successfully.'
#             else:
#                 msg = 'We do not have sufficient stock to fill your order.'
#         else:
#             msg = 'Please fill in all the required fields.'
#         return render(request, 'myapp1/order_response.html', {'msg': msg})
#     else:
#         form = OrderItemForm()
#     return render(request, 'myapp1/place_order.html', {'form': form, 'msg': msg, 'item_list': item_list})
#
# @login_required
# def itemdetail(request, item_id):
#     item = Item.objects.get(id=item_id)
#     interested = item.interested
#     if request.method == 'POST':
#         form = InterestForm(request.POST)
#         if form.is_valid():
#             interested = form.cleaned_data['interested']
#             quantity = form.cleaned_data['quantity']
#             comments = form.cleaned_data['comments']
#             if interested:
#                 item.interested.add(request.user)
#             else:
#                 item.interested.remove(request.user)
#             item.save()
#             # msg = 'Thanks for your interest!'
#     else:
#         form = InterestForm()
#     return render(request, 'myapp1/itemdetail.html', {'item': item, 'interested': interested, 'form': form})
#
#
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('myapp1:index'))
#             else:
#                 return HttpResponse('Your account is disabled.')
#         else:
#             return HttpResponse('Invalid login details.')
#     else:
#         return render(request, 'myapp1/login.html')
#
# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('myapp1:user_login'))
#
# @login_required
# def myorder(request):
#     if request.user.is_active:
#         orders = OrderItem.objects.filter(client=request.user)
#         return render(request, 'myapp1/myorder.html', {'orders': orders})
#     else:
#         message = 'You are not a active client!'
#         return render(request, 'myapp1/myorder.html', {'message': message})
