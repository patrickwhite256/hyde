from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class InputView(TemplateView):
    template_name = "input.html"
