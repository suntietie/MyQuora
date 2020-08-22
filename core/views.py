from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.conf import settings

class IndexTemplateView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        # remove not before deployment
        if not settings.DEBUG:
            template_name = "index-dev.html"
        else:
            template_name = "index.html"
        return template_name
    
    