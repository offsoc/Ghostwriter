from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.views import defaults as default_views

urlpatterns = [
     # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("ghostwriter.users.urls", namespace="users")),
    path("home/", include("ghostwriter.home.urls", namespace="home")),
    path("accounts/", include("allauth.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("rolodex/", include("ghostwriter.rolodex.urls", namespace="rolodex")),
    path("shepherd/", include("ghostwriter.shepherd.urls", namespace="shepherd")),
    path("reporting/", include("ghostwriter.reporting.urls", namespace="reporting")),
    path("", RedirectView.as_view(pattern_name="home:dashboard"), name="home"),
    path("tinymce/", include("tinymce.urls")),
	path("oplog/", include("ghostwriter.oplog.urls", namespace="oplog")),

    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
