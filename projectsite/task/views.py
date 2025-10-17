from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Task, Category, Priority, SubTask, Note
from .forms import TaskForm, CategoryForm, PriorityForm, SubTaskForm, NoteForm


# ==============================
# DASHBOARD VIEW
# ==============================
@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request, 'dashboard.html')


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_count"] = Task.objects.count()
        context["note_count"] = Note.objects.count()
        context["category_count"] = Category.objects.count()
        context["subtask_count"] = SubTask.objects.count()
        context["priority_count"] = Priority.objects.count()
        context["recent_tasks"] = Task.objects.order_by('-created_at')[:5]
        context["recent_notes"] = Note.objects.order_by('-created_at')[:5]
        return context


# ==============================
# HELPER: Redirect if already logged in
# ==============================
def redirect_if_logged_in(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper


# ==============================
# TASK VIEWS
# ==============================
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        sort_option = self.request.GET.get("sort")

        if query:
            queryset = queryset.filter(title__icontains=query)

        if sort_option == "title_asc":
            queryset = queryset.order_by("title")
        elif sort_option == "title_desc":
            queryset = queryset.order_by("-title")
        elif sort_option == "created_asc":
            queryset = queryset.order_by("created_at")
        elif sort_option == "created_desc":
            queryset = queryset.order_by("-created_at")
        elif sort_option == "priority_asc":
            queryset = queryset.order_by("priority__name")  # assuming Priority has a 'level' field
        elif sort_option == "priority_desc":
            queryset = queryset.order_by("-priority__name")
        else:
            queryset = queryset.order_by("-created_at")
        return queryset


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("task-list")


# ==============================
# CATEGORY VIEWS
# ==============================
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class CategoryListView(ListView):
    model = Category
    context_object_name = "categories"
    template_name = "category_list.html"
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Category.objects.all()
        q = self.request.GET.get("q")
        sort = self.request.GET.get("sort")

        if q:
            queryset = queryset.filter(name__icontains=q)

        if sort == "name_asc":
            queryset = queryset.order_by("name")
        elif sort == "name_desc":
            queryset = queryset.order_by("-name")
        elif sort == "created_asc":
            queryset = queryset.order_by("created_at")
        elif sort == "created_desc":
            queryset = queryset.order_by("-created_at")

        return queryset


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("category-list")


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("category-list")


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category_confirm_delete.html"
    success_url = reverse_lazy("category-list")


# ==============================
# PRIORITY VIEWS
# ==============================
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class PriorityListView(ListView):
    model = Priority
    context_object_name = "priorities"
    template_name = "priority_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Priority.objects.all()
        q = self.request.GET.get("q")
        sort = self.request.GET.get("sort")

        if q:
            queryset = queryset.filter(level__icontains=q)

        if sort == "level_asc":
            queryset = queryset.order_by("level")
        elif sort == "level_desc":
            queryset = queryset.order_by("-level")
        elif sort == "created_asc":
            queryset = queryset.order_by("created_at")
        elif sort == "created_desc":
            queryset = queryset.order_by("-created_at")

        return queryset


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = "priority_form.html"
    success_url = reverse_lazy("priority-list")


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = "priority_form.html"
    success_url = reverse_lazy("priority-list")


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = "priority_confirm_delete.html"
    success_url = reverse_lazy("priority-list")


# ==============================
# SUBTASK VIEWS
# ==============================
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class SubTaskListView(ListView):
    model = SubTask
    context_object_name = "subtasks"
    template_name = "subtask_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = SubTask.objects.all()
        q = self.request.GET.get("q")
        sort = self.request.GET.get("sort")

        if q:
            queryset = queryset.filter(title__icontains=q)

        if sort == "title_asc":
            queryset = queryset.order_by("title")
        elif sort == "title_desc":
            queryset = queryset.order_by("-title")
        elif sort == "created_asc":
            queryset = queryset.order_by("created_at")
        elif sort == "created_desc":
            queryset = queryset.order_by("-created_at")

        return queryset
    
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"
    success_url = reverse_lazy("subtask-list")


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"
    success_url = reverse_lazy("subtask-list")


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = "subtask_confirm_delete.html"
    success_url = reverse_lazy("subtask-list")


# ==============================
# NOTE VIEWS
# ==============================
@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "note_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Note.objects.all()
        q = self.request.GET.get("q")
        sort = self.request.GET.get("sort")

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(content__icontains=q))

        if sort == "title_asc":
            queryset = queryset.order_by("title")
        elif sort == "title_desc":
            queryset = queryset.order_by("-title")
        elif sort == "created_asc":
            queryset = queryset.order_by("created_at")
        elif sort == "created_desc":
            queryset = queryset.order_by("-created_at")

        return queryset


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note-list")


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note-list")


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class NoteDeleteView(DeleteView):
    model = Note
    template_name = "note_confirm_delete.html"
    success_url = reverse_lazy("note-list")