from django.template import loader
from django.http import HttpResponse

def products(request):
    template = loader.get_template('products.html')
    return  HttpResponse(template.render())
