from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def process_order(request,prod_id):
    if request.method == "POST":
        if 'total_charge' and 'quantity_from_form' not in request.session:
            request.session['quantity_from_form'] = 0
            request.session['creditcard_charge'] = 0
            request.session['total_charge'] = 0
        
        p_price = {}
        for item in Product.objects.all().values():
            p_price[str(item['id'])] = item['price']
        print("dict p_price!!!!!!!!!!!!!!!!!!!!!!!!!!",p_price)

        request.session['quantity_from_form'] = int(request.POST["quantity"])
        request.session['creditcard_charge'] = int(request.POST["quantity"]) * float(p_price[str(prod_id)])
        request.session['total_charge'] += request.session['creditcard_charge']

        print("Charging credit card...")
        Order.objects.create(quantity_ordered=request.session['quantity_from_form'], total_price=request.session['total_charge'])
        return redirect('/checkout')

def checkout(request):
    return render(request, "store/checkout.html")