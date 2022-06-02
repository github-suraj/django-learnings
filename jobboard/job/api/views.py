from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from job.models import JobOffer
from job.api.serializers import JobOfferSerializer

class JobOfferList(APIView):

    def get(self, request):
        job_offers = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(job_offers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobOfferDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(JobOffer, pk=pk)

    def get(self, request, pk):
        job_offer = self.get_object(pk)
        serializer = JobOfferSerializer(job_offer)
        return Response(serializer.data)

    def put(self, request, pk):
        job_offer = self.get_object(pk)
        serializer = JobOfferSerializer(job_offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        job_offer = self.get_object(pk)
        job_offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
