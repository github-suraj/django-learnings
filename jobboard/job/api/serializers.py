from rest_framework import serializers
from job.models import JobOffer

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        exclude = ("id", )

    def validate(self, data):
        if data['job_title'] == data['job_description']:
            raise serializers.ValidationError("Job Title and Descriptions must be different from one another!")
        return data

    def validate_job_description(self, value):
        if len(value) < 100:
            raise serializers.ValidationError("Job Description must be 100 chars long!")
        return value
