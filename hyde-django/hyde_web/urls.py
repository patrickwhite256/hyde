from django.conf.urls import patterns,url
from hyde_web import views as h_v

urlpatterns = patterns('',
        url(r'^$', h_v.InputView.as_view()),
)
