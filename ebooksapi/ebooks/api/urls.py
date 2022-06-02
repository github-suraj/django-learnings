from django.urls import path
from ebooks.api.views import EbookListCreate

urlpatterns = [
    path("ebooks/", EbookListCreate.as_view(), name='ebook-list'),
]