from django.urls import path

urlpatterns = [
    path(r'^$', 'index', name='home'),
    path(r'^(?P<short_id>\w{6})$', 'redirect_original', name='redirectoriginal'),
    path(r'^makeshort/$', 'shorten_url', name='shortenurl')
]
