from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm

class IndexView(generic.TemplateView):
    template_name = 'app/index.html'

class SingUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'app/signup.html'
