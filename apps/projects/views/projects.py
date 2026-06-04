from rest_framework.request import Request
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from apps.projects.serializers.project import AllProjectsSerializer
from apps.tasks.serializers.task import AllTasksSerializer
from apps.tasks.serializers.tag import TagsSerializer

from apps.projects.models.project import Project
from apps.tasks.models.task import Task
from apps.tasks.models.tag import Tag





@api_view(['GET',])
def get_all_projects(request: Request) -> JsonResponse:
   all_projects = Project.objects.all()


   if not all_projects.exists():
       return JsonResponse(
           [],
           status=status.HTTP_204_NO_CONTENT,
           safe=False
       )
   else:
       serialized_data = AllProjectsSerializer(
           all_projects, many=True
       )


       return JsonResponse(
           serialized_data.data,
           status=status.HTTP_200_OK,
           safe=False
       )


@api_view(['GET',])
def get_all_tasks(request: Request) -> JsonResponse:
   project_name = request.query_params.get('project')


   if not project_name:
       all_tasks = Task.objects.all()


   else:
       all_tasks = Task.objects.filter(project__name=project_name)


   if not all_tasks.exists():
       return JsonResponse(
           data=[],
           status=status.HTTP_204_NO_CONTENT,
           safe=False
       )


   serialized_data = AllTasksSerializer(all_tasks, many=True)


   return JsonResponse(
       data=serialized_data.data,
       status=status.HTTP_200_OK,
       safe=False
   )


@api_view(['GET',])
def get_all_tags(request: Request) -> JsonResponse:
   tags = Tag.objects.all()


   if not tags.exists():
       return JsonResponse(
           data=[],
           status=status.HTTP_204_NO_CONTENT,
           safe=False
       )


   serialized_data = TagsSerializer(tags, many=True)


   return JsonResponse(
       data=serialized_data.data,
       status=status.HTTP_200_OK,
       safe=False
   )


@api_view(['GET',])
def get_tag_by_id(request: Request, tag_id: int) -> JsonResponse:
   try:
       tag = Tag.objects.get(id=tag_id)


   except Tag.DoesNotExist:
       return JsonResponse(
           data={},
           status=status.HTTP_204_NO_CONTENT
       )


   serialized_data = TagsSerializer(tag)


   return JsonResponse(
       data=serialized_data.data,
       status=status.HTTP_200_OK,
   )


@api_view(['PUT',])
def update_required_tag(request: Request, tag_id: int) -> JsonResponse:
   try:
       tag = Tag.objects.get(id=tag_id)
   except Tag.DoesNotExist:
       return JsonResponse(
           {},
           status=status.HTTP_204_NO_CONTENT
       )


   validated_data = TagsSerializer(tag, request.data)


   if validated_data.is_valid(raise_exception=True):
       validated_data.save()


       return JsonResponse(
           validated_data.data,
           status=status.HTTP_200_OK,
       )
