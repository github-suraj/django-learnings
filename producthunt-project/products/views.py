from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Products

# Create your views here.
def homepage(request):
    products = Products.objects.all()
    data_dict = dict(products=products)
    return render(request, 'products/home.html', data_dict)

@login_required(login_url='/users/signup')
def create(request):
    if request.method == 'POST':
        product = Products()
        product.title = request.POST['title']
        product.content = request.POST['content']
        product.url = request.POST['url']
        product.icon = request.FILES['icon']
        product.image = request.FILES['image']
        product.pub_date = timezone.datetime.now()
        product.user = request.user
        product.save()
        return redirect('/products/' + str(product.id))
    else:
        return render(request, 'products/create.html')

def product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    data_dict = dict(product=product)
    return render(request, 'products/product.html', data_dict)

@login_required(login_url='/users/signup')
def upvote(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    product.votes_total += 1
    product.save()
    return redirect('/products/' + str(product.id))
