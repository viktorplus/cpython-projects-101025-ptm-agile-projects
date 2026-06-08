from django.urls import path
from apps.tasks.views.tag_views import TagsListCreateAPIView, TagsDetailAPIView

urlpatterns = [
    path('tags/', TagsListCreateAPIView.as_view() ,name='tags_list_create'),
    path('tags/<int:pk>/', TagsDetailAPIView.as_view(),name='tags_detail'),
]