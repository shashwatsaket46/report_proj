from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Salesr
from .forms import SalesSearchForm
# Create your views here.
def home_view(request):
    form=SalesSearchForm(request.POST or None)
    if request.method=='POST':
        date_from=request.POST.get('date_from')
        date_to=request.POST.get('date_to')
        chart_type=request.POST.get('chart_type')
        print(date_from,date_to,chart_type)
    context={
        'form':form,
    }
    return render(request,'salesr/home.html',context)
class SalesListView(ListView):
    model=Salesr
    template_name='salesr/main.html'
class SalesDetailView(DetailView):
    model=Salesr
    template_name='salesr/detail.html'
def sale_list_view(request):
    qs=Salesr.object.all()
    return render(request,'salesr/main.html',{'object':qs})
def sale_detail_view(request,**kwargs):
    pk=kwargs.get('pk')
    obj=Salesr.objects.get(pk=pk)
    return render(request,'salesr/detail.html',{'object':obj})

