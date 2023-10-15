from django.urls import path
from .views import exchange_page_view


urlpatterns = [
    path("", exchange_page_view, name="exchange")
]
