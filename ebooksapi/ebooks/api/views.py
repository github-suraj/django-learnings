from rest_framework import generics, mixins
from ebooks.models import Ebook
from ebooks.api.serializers import EbookSerializer

class EbookListCreate(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
