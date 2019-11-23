from django.urls import include, path

from . import views

urlpatterns = [
    path('<slug:short>', views.RedirectView.as_view(), name='short-url'),
]