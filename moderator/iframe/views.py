from django.views.generic import TemplateView


class DesktopView(TemplateView):
    template_name = 'iframe/desktop.html'
