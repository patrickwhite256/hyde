from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class InputView(TemplateView):
    template_name = "input.html"
    warning = None
    def post(self, request, *args, **kwargs):
        if 'hidefile' in request.FILES and 'hiddenfile' in request.FILES:
            pass
        elif 'jekfile' in request.FILES:
            pass
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['warning'] = self.warning
        return context
