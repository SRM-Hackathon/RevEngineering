from django.conf.urls import url
from webcam import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    #url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^webcam/$', views.webcam, name='webcam'),
    #url(r'^predict/$', views.PredictPageView.as_view(), name='predict'),
#    url(r'^upload/$', views.UploadPageView.as_view(), name='upload'),
    url(r'^output/$', views.output1, name='output'),
    url(r'^imgdata/$', views.imgdata, name='imgdata'),
    url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
    url(r'^emotion/$', views.emotion, name='emotion'),
    url(r'^textinput/$', views.textinput, name='textinput'),

    #path('output', views.output, name='output'),
]
