from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from account.forms import RegisterForm
from account.mixins import LoggedInRedirectMixin, AccessUserMixin

from gallery.models import Post


class Login(LoggedInRedirectMixin, LoginView):
    pass

class Logout(LoginRequiredMixin, LogoutView):
    pass

class Register(LoggedInRedirectMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('gallery:login')

class PostList(LoginRequiredMixin, ListView):
    template_name = 'gallery/home.html'
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)
    paginate_by = 9
    ordering = ['-created']


class PostDelete(AccessUserMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('gallery:home')


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'description', 'photo')
    success_url = reverse_lazy('gallery:home')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.user = self.request.user

        return super(PostCreate, self).form_valid(form)


class PostUpdate(AccessUserMixin, UpdateView):
    model = Post
    fields = ('title', 'description', 'photo')
    success_url = reverse_lazy('gallery:home')
