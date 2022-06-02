from django.urls import path
from job.api.views import JobOfferList, JobOfferDetail

urlpatterns = [
    path('jobs', JobOfferList.as_view(), name='job-list'),
    path('jobs/<int:pk>', JobOfferDetail.as_view(), name='job-detail'),
]