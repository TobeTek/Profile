from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import Response
from .forms import ResponseForm

# Create your views here.

class HomePageView(generic.CreateView):
	model = Response
	form_class = ResponseForm
	template_name = 'home_page.html'
	success_url = reverse_lazy('home-page')