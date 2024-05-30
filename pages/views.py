from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class MenuePageView(TemplateView):
    template_name = "pages/menue.html"

class OrderPageView(TemplateView):
    template_name = "pages/order.html"

class ReservationPageView(TemplateView):
    template_name = "pages/reservation.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"