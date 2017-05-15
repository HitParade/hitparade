from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

from hitparade import views
from utils import v_url

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^account/social/accounts/$", TemplateView.as_view(template_name="account/social.html"), name="account_social_accounts"),
    url(r"^account/social/", include("social_django.urls", namespace="social")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(v_url('teams/$'), views.team_list),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
