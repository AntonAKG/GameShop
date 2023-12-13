from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'main_page/main.html'
