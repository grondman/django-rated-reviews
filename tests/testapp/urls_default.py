from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^', include('reviews.urls')),

    # Provide the auth system login and logout views
    url(r'^accounts/login/$', LoginView.as_view(template_name='login.html')),
    url(r'^accounts/logout/$', LogoutView.as_view()),
]
