from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class GalleryPageView(TemplateView): 
    template_name = 'gallery.html'