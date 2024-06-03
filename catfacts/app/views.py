from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from .models import LikedFact
import requests

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get('https://catfact.ninja/facts')
        cat_facts = response.json()['data'] if response.status_code == 200 else []
        context['cat_facts'] = cat_facts
        # Get user liked facts
        user_facts = LikedFact.objects.filter(user=self.request.user)
        # If catfacts are in user liked facts, dont show them
        context['cat_facts'] = [fact for fact in cat_facts if fact['fact'] not in [user_fact.fact for user_fact in user_facts]]
        return context

class LikeCatFactView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        fact = request.POST.get('fact')
        LikedFact.objects.create(user=request.user, fact=fact)  # Store the liked fact
        return HttpResponseRedirect(reverse_lazy('catfacts'))
    
class LikedFactsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/liked_facts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_facts = LikedFact.objects.filter(user=self.request.user)
        context['liked_facts'] = user_facts
        return context