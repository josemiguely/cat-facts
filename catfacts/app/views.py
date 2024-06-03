from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.TemplateView):
    template_name = 'app/index.html'

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'app/signup.html'

class CustomLoginView(LoginView):
    template_name = 'app/login.html'
    next_page = 'catfacts'
    
class CatFactsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/catfacts.html'
    login_url = reverse_lazy('login')