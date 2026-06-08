from django.urls import path,include



urlpatterns =[
    path('projects/', include('apps.projects.urls')),
    path('tasks/', include('apps.tasks.urls')),
]