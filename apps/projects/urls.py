from django.urls import path


from .views.projects import get_all_projects, get_all_tasks, get_all_tags, get_tag_by_id, update_required_tag


urlpatterns = [
   path('projects/', get_all_projects),
   path('tasks/', get_all_tasks),
   path('tags/', get_all_tags),
   path('tags/<int:tag_id>/', get_tag_by_id),
   path('tags/<int:tag_id>/update/', update_required_tag),
]
