from datetime import timezone, datetime

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.projects.models import Project
from apps.projects.serializers.project import AllProjectsSerializer, CreateProjectSerializer


# Задача 7: Получение списка проектов и создание нового проекта
# В приложении projects создайте модули serializers, views, удалить файл views.py.
# В модуле serializers создайте файл project_serializers.py.
# В только что созданном файле создайте первый сериализатор AllProjectsSerializer на получения информации о всех проектах. Отображаемые поля:
# id
# name
# created_at
# В модуле views создайте файл project_views.py, напишите классовое отображение:
# Реализуйте метод на получение списка всех проектов:
# Получить из query_params значения дат date_from, date_to
# Если никаких значений передано не было - получить список полностью всех проектов
# Если были переданы значения для временного диапазона - сконвертировать полученные значения по текущей временной зоне (поможет метод make_aware() и модуль timezone в django)
# Провести фильтрацию по диапазону дат date_from date_to
# Реализуйте метод get на отображение списка всех проектов, добавьте фильтрацию через request_params на получение проектов в определённом временном промежутке, например с 2020-01-01 по 2024-01-01
# Реализуйте метод на создание нового проекта
# Зарегиструйте новое отображение в файле urls.py в приложении projects.
# Проверьте работу нашего классового отображения.
# Зафиксируйте все изменения, сделать запрос на слияние.


class ProjectsListCreateAPIView(APIView):
    def post(self, request):
        serializer = CreateProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        if not (date_from and date_to):
            projects = Project.objects.all()
        else:
            date_from = timezone.make_aware(datetime.strptime(date_from, '%Y-%m-%d'),
                                            timezone.get_default_timezone())
            date_to = timezone.make_aware(datetime.strptime(date_to, '%Y-%m-%d'),
                                          timezone.get_default_timezone())

            projects = Project.objects.filter(created_at__range=(date_from, date_to))
        if not projects:
            return Response(data=[], status=status.HTTP_204_NO_CONTENT)
        serializer = AllProjectsSerializer(projects, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



