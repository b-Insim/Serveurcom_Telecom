from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from api.models import Reference, Bars, Stock, Comptoir, Menu

def index(request):
    template = loader.get_template('api/index.html')
    return HttpResponse(template.render(request=request))

class PublisherList(ListView):
    model = Reference
    context_object_name = 'my_favorite_references'
    # model = Bars

class PublisherDetail(DetailView):
    
    model = Stock
    context_object_name = 'stock'
    template_name = 'api/stock_list.html'
    queryset = Stock.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['stock_list'] = Stock.objects.all()
        return context
    
    def get_queryset(self):
        self.ID_COMPTOIR = get_object_or_404(Stock, name=self.kwargs['ID_COMPTOIR'])
        return Stock.objects.filter(stock_list=self.ID_COMPTOIR)

class PublisherComptoiList(ListView):
    model = Comptoir
    context_object_name = 'my_list_comptoirs'

class PublisherMenuList(ListView):
    model = Menu
    context_object_name = 'my_list_references_menu'