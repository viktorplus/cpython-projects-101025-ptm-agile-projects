# Задача 5: Получение списка всех тегов и создание нового тега
# В приложении tasks удалите файл views.py, создайте модуль views.
# В модуле views создайте новый файл tag_views.py.
# В приложении tasks создайте новый модуль serializers.
# В модуле serializers создайте новый файл tag_serializers.py.
# Напишите сериализатор для работы с тегами (так как у нас всего одно поле в этой модели, сериализатор будет один на все будущие запросы).
# Напишите классовое отображение:
# Реализовать метод для получения всех объектов Tag
# для получения списка всех тегов методом get
# Для создания нового тега методом post
# Зарегистрируйте новое классовое отображение в списке эндпоинтов.
# Проверьте работу нашего классового отображения.
# Зафиксируйте все изменения, сделать запрос на слияние.
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tasks.models import Tag
from apps.tasks.serializers.tag import TagsSerializer


class TagsListCreateAPIView(APIView):


    def get(self, request):
        tags = Tag.objects.all()
        if not tags:
            return Response(data=[], status=status.HTTP_204_NO_CONTENT)
        serializer = TagsSerializer(tags, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = TagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagsDetailAPIView(APIView):

    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        serializer = TagsSerializer(tag)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        serializer = TagsSerializer(tag, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        tag = get_object_or_404(Tag, pk=pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



