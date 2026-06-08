from rest_framework.serializers import ModelSerializer


from apps.projects.models import Project




class AllProjectsSerializer(ModelSerializer):
   class Meta:
       model = Project
       fields = ['id', 'name','created_at']



class CreateProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields=['name','description']
