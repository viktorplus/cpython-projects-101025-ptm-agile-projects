from rest_framework.serializers import ModelSerializer


from apps.tasks.models import Task




class AllTasksSerializer(ModelSerializer):
   class Meta:
       model = Task
       fields = ['id', 'name', 'status', 'priority']