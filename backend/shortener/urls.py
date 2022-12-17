from django.urls import path
from shortener import views

appname = "shortener"

urlpatterns = [
    path("", views.CreateShortUrlView.as_view(), name="home"),
    path('<str:shortened_part>', views.RedirectUrlView.as_view(), name='redirect'),
]
