from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from io import StringIO, BytesIO
from hyde_web import hyde_core

# Create your views here.

class InputView(TemplateView):
    template_name = "input.html"
    warning = None
    def post(self, request, *args, **kwargs):
        if 'hidefile' in request.FILES and 'hiddenfile' in request.FILES:
            outfile = StringIO()
            hyde_core.hyde(request.FILES['hidefile'],
                    request.FILES['hiddenfile'].name,
                    request.FILES['hiddenfile'],
                    outfile)
            response = HttpResponse()
            response['Content-Disposition'] = 'attachment; filename="secret.png"'
            response.write(outfile.getvalue())
            return response
        elif 'jekfile' in request.FILES:
            outfile = BytesIO()
            hyde_core.jekyll(request.FILES['jekfile'], outfile)
            response = HttpResponse()
            response['Content-Disposition'] = 'attachment; filename="out.txt"'
            response.write(outfile.getvalue())
            return response
        self.warning = 'Some files are missing!'
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['warning'] = self.warning
        return context
