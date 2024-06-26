from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.db.models import Count
from .forms import SignUpForm
from .models import LikedFact
import requests

class IndexView(generic.View):
    # Redirect to Login View
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('login'))

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'app/signup.html'

class CustomLoginView(LoginView):
    template_name = 'app/login.html'
    next_page = 'catfacts'

@method_decorator(never_cache, name='dispatch')
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
    
@method_decorator(never_cache, name='dispatch')
class LikedFactsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/liked_facts.html'
    login_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_facts = LikedFact.objects.filter(user=self.request.user)
        context['liked_facts'] = user_facts
        return context

@method_decorator(never_cache, name='dispatch') 
class MostLikedFactsView(generic.ListView):
    template_name = 'app/most_liked_facts.html'
    context_object_name = 'most_liked_facts'

    def get_queryset(self):
        # Aggregates all facts and annotates them with the count of likes
        return LikedFact.objects.values('fact').annotate(likes=Count('id')).order_by('-likes')