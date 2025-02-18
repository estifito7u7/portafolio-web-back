from rest_framework import serializers
from .models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = [
            'id',
            'name',
            'photo',
            'category',
            'description',
            'start_date',
            'end_date',
            'github_link',
            'website_link',
            'date_created',
            'get_thumbnail'
        ]