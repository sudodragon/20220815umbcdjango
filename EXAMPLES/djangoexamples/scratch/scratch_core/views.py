from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.



# example without template (only used in class -- always use templates in real life):
# def home(request):
#     return HttpResponse("Welcome to Scratch Core")

# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to Scratch Core" }
#     return render(request, 'scratch_core/home.html', context)

class ContextMixin(View):
    template_name = self.EXTRA.pop('template')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if hasattr(self, 'extra_data'):
            context.update(self.extra_data)
        return context

class Hello1(ContextMixin, TemplateView):
    EXTRA = dict(color='blue', template='hello1.html')

class Hello2(ContextMixin, TemplateView):
    EXTRA = dict(color='orange', template='hello2.html')

class Hello3(ContextMixin, TemplateView):
    EXTRA = dict(color='orange', template='hello3.html')
