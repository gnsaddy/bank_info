from django.conf.urls import url
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from src import views
from src.views import ListView

urlpatterns = [
    path('', views.bankUsingIfsc, name="index"),
    url(r'^import/', views.ImportView.as_view(), name='import'),
    # url(r'^ifsc/(?P<ifsc>[A-Za-z]{4}\w{7})$', DetailView.as_view()),
    url(r'^branches/(?P<city>.*)/(?P<bank>.*)$', ListView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
