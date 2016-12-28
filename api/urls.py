from django.conf.urls import url
from api import views

urlpatterns = [
        url(r'^api/(?P<version>(v1))/candidates/$',
            views.CandidateList.as_view()),
        url(r'^api/(?P<version>(v1))/candidates/(?P<pk>[0-9]+)/$',
            views.CandidateDetail.as_view()),
        url(r'^api/(?P<version>(v1))/dropdowns/$',
            views.DropdownLists.as_view()),
        url(r'^api/(?P<version>(v1))/dropdown-values/$',
            views.DropdownValues.as_view()),
        ]

