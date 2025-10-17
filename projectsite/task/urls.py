from django.urls import path, include
from task import views
from allauth.account.views import LoginView

urlpatterns = [
    # Allauth (login, signup, etc.)
    path('accounts/', include('allauth.urls')),

    # Root URL - protected dashboard
    path('', views.DashboardView.as_view(), name='dashboard'),

    # Task Management
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/add/', views.TaskCreateView.as_view(), name='task-add'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),

    # Categories
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    # Priorities
    path('priorities/', views.PriorityListView.as_view(), name='priority-list'),
    path('priorities/add/', views.PriorityCreateView.as_view(), name='priority-add'),
    path('priorities/<int:pk>/update/', views.PriorityUpdateView.as_view(), name='priority-update'),
    path('priorities/<int:pk>/delete/', views.PriorityDeleteView.as_view(), name='priority-delete'),

    # Subtasks
    path('subtasks/', views.SubTaskListView.as_view(), name='subtask-list'),
    path('subtasks/add/', views.SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtasks/<int:pk>/update/', views.SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtasks/<int:pk>/delete/', views.SubTaskDeleteView.as_view(), name='subtask-delete'),

    # Notes
    path('notes/', views.NoteListView.as_view(), name='note-list'),
    path('notes/add/', views.NoteCreateView.as_view(), name='note-add'),
    path('notes/<int:pk>/update/', views.NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note-delete'),

    #Pwa
    path('', include('pwa.urls')),
]