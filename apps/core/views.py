from django.views.generic import ListView

from .models import District


__all__ = (
    'HomeView',
)


class HomeView(ListView):
    model = District
    template_name = 'core/index.html'
    context_object_name = 'districts'
