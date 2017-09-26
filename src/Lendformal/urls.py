from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import items.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^payment/$', views.PaymentPage.as_view(), name='payment'),
    url(r'^myorders/$', views.MyordersPage.as_view(), name='myorders'),
    url(r'^details/$', views.DetailsPage.as_view(), name='details'),
    url(r'^payment/$', views.PaymentPage.as_view(), name='payment'),
    url(r'^listings/$', views.ListingsPage.as_view(), name='listings'),
    url(r'^post/$', views.PostPage.as_view(), name='post'),
    url(r'^postConfirmation/$', views.PostConfirmationPage.as_view(), name='postConfirmation'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^', include(items.urls, namespace='items')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
