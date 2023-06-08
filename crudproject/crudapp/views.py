from django.shortcuts import render,redirect
from .models import Item
from django.views.generic import ListView,DetailView

# Create your views here.



def create(request):
    item1=Item.objects.all()
    if request.method=="POST":
        num=request.POST.get('slno','')
        name=request.POST.get('item','')
        description=request.POST.get('desc','')
        item=Item(num=num,name=name,description=description)
        item.save()
    return render(request,"index.html",{'item':item1})

def delete(request,itemid):
    item=Item.objects.get(id=itemid)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    return render(request,"delete.html")

    

def update(request,id):
    item=Item.objects.get(id=id)

    if request.method=='POST':
        item.num = request.POST['slno']
        item.name = request.POST['item']
        item.description = request.POST['description']
        item.save()
        return redirect('/',) 

    return render(request, "update.html", {'item': item})


# class ItemList(ListView):
#     model=Item
#     template_name="index.html"
