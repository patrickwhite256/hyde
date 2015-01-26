from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from io import BytesIO
from hyde_web import hyde_core

# Create your views here.

class InputView(TemplateView):
    template_name = "input.html"
    warning = None
    def post(self, request, *args, **kwargs):
        if 'hidefile' in request.FILES and 'hiddenfile' in request.FILES:
            #TODO: what is security
            hidefile_data = request.FILES['hidefile'].read()
            hiddenfile_data = request.FILES['hiddenfile'].read()
            try:
                out_bytes = hyde_core.hyde(
                        (request.FILES['hidefile'].name, hidefile_data),
                        (request.FILES['hiddenfile'].name, hiddenfile_data))
            except hyde_core.HydeException as e:
                self.warning = e.msg
                return self.get(request, *args, **kwargs)
            response = HttpResponse()
            response['Content-Disposition'] = 'attachment; filename="secret.png"'
            response.write(out_bytes)
            return response
        elif 'jekfile' in request.FILES:
            file_data = request.FILES['jekfile'].read()
            try:
                out_bytes, filename = hyde_core.jekyll(
                        (request.FILES['jekfile'].name, file_data))
            except hyde_core.HydeException as e:
                self.warning = e.msg
                return self.get(request, *args, **kwargs)
            response = HttpResponse()
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(
                    filename)
            response.write(out_bytes)
            return response
        self.warning = 'Some files are missing!'
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['warning'] = self.warning
        return context
