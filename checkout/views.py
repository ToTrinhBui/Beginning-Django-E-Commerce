from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.http import HttpResponseRedirect
from checkout.forms import CheckoutForm
from checkout.models import Order, OrderItem
from checkout import checkout
from cart import cart


def show_checkout(request):
    print('------------Show checkout--------------')
    error_message = ''
    if cart.is_empty(request):
        cart_url = reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = CheckoutForm(postdata)
        if form.is_valid():
            response = checkout.process(request)
            order_number = response.get('order_number', 0)
            error_message = response.get('message', '')
            if order_number:
                request.session['order_number'] = order_number
                receipt_url = reverse('checkout_receipt')
                return HttpResponseRedirect(receipt_url)
        else:
            error_message = 'Correct the errors below'
    else:
        form = CheckoutForm()
    page_title = 'Checkout'
    context = {'page_title':page_title, 'form': form,}
    if len(error_message) != 0:
        context['error_message'] = error_message
    return render(request, "checkout/checkout.html", context)

def receipt(request):
    print('------------receipt--------------')
    order_number = request.session.get('order_number', '')
    if order_number is not None:
        order = Order.objects.filter(id=order_number)[0]
        order_items = OrderItem.objects.filter(order=order)
        del request.session['order_number']
    else:
        cart_url = reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    context = {
        'order': order,
        'order_items': order_items
    }
    return render(request, "checkout/receipt.html", context)