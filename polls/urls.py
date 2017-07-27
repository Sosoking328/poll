from django.conf.urls import url
from myFirstSite import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from . import views


urlpatterns=[
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^results/$', views.ResultsView.as_view(), name='results'),
    url(r'^votes/$', views.votes, name='votes'),
]


urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
