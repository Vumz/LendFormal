from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class ListingsPage(generic.TemplateView):
    template_name = "listings.html"

class PaymentPage(generic.TemplateView):
    template_name = "payment.html"

class MyordersPage(generic.TemplateView):
    template_name = "myorders.html"

class DetailsPage(generic.TemplateView):
    template_name = "details.html"

class PostPage(generic.TemplateView):
    template_name = "ListingForm.html"

class PostConfirmationPage(generic.TemplateView):
    template_name = "ListingConfirmation.html"
