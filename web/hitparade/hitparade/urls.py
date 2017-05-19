from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

from hitparade import views
from utils import v_url

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(v_url('teams'), views.TeamListView)

# TODO: Make sure the `base_name` here is correct
router.register(v_url('games'), views.GameListView, base_name='games')
router.register(v_url('players'), views.PlayerListView, base_name='players')


urlpatterns = [
    # Admin
    url(r'^grappelli/', include('grappelli.urls')),
    url(r"^admin/", include(admin.site.urls)),

    # HitParade
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),

    # Hit Parade API
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # django-account
    url(r"^account/", include("account.urls")),
    url(r"^account/social/accounts/$", TemplateView.as_view(template_name="account/social.html"), name="account_social_accounts"),
    url(r"^account/social/", include("social_django.urls", namespace="social")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
