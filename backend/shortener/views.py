from django.shortcuts import render
from django.http import HttpResponseRedirect
from shortener.models import Shortener
from shortener.forms import ShortenerForm
from django.views.generic import CreateView
from django.views import View


class CreateShortUrlView(CreateView):
    model = Shortener
    template_name = 'shortener/home.html'
    form_class = ShortenerForm

    def form_valid(self, form):
        form.save()

        shortened_object = form.instance
        new_url = self.request.build_absolute_uri('/') + shortened_object.short_url
        full_url = shortened_object.full_url

        return render(
            self.request,
            self.template_name,
            self.get_context_data(
                form=form,
                new_url=new_url,
                full_url=full_url
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_url'] = kwargs.get('new_url')
        context['long_url'] = kwargs.get('full_url')
        return context


class RedirectUrlView(View):
    def get(self, request, *args, **kwargs):

        shortener = Shortener.objects.get(short_url=kwargs['shortened_part'])
        shortener.save()

        return HttpResponseRedirect(shortener.full_url)
