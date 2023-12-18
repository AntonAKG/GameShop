from django.views.generic import ListView, DetailView, TemplateView

from .models import Game, GalleryGame


class HomeView(ListView):
    template_name = 'main_page/main.html'
    model = Game
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class DetailGameView(DetailView):
    model = Game
    template_name = 'main_page/game_detail.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super(DetailGameView, self).get_context_data()

        game_id = self.kwargs['pk']
        context['title'] = 'about game'
        context['game'] = Game.objects.get(pk=game_id)
        context['gallery'] = GalleryGame.objects.filter(game_id=game_id)

        return context


class About(TemplateView):
    template_name = 'main_page/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data()

        context['title'] = 'About'

        return context
