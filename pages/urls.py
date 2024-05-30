from django.urls import path
from .views import AboutPageView, HomePageView, ReservationPageView, MenuePageView, OrderPageView

urlpatterns = [
    path("home", HomePageView.as_view(), name="home"),
    path("menue", MenuePageView.as_view(), name="menue"),
    path("order", OrderPageView.as_view(), name="order"),
    path("reservation", ReservationPageView.as_view(), name="reservation"),
    path("about", AboutPageView.as_view(), name="about"),
]