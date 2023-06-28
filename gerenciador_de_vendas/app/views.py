from django.template import loader
from django.http import HttpResponse
from .models import Products, Order

def products(request):
    myproducts = Products.objects.all().values()
    template = loader.get_template('all_products.html')
    context = {
        'myproducts': myproducts
    }
    return  HttpResponse(template.render(context, request))


def details(request, id):
  myproduct = Products.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myproduct': myproduct
  }
  return HttpResponse(template.render(context, request))

def all_orders(request):
   myorder = Order.objects.all().values()
   template = loader.get_template('all_order.html')
   context = {
      'myorder': myorder
   }
   return HttpResponse(template.render(context,request))