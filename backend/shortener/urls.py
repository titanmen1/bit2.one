from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from shortener import views

appname = "shortener"

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="home"),
    path("create_short_url", views.CreateShortUrlView.as_view(), name="create_short_url"),
    path(
        'r/<str:shortened_part>',
        views.RedirectUrlView.as_view(),
        name='redirect'
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
