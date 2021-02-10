from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from account.forms import RegisterForm
from account.mixins import LoggedInRedirectMixin, AccessUserMixin

from gallery.models import Book


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


class Login(LoggedInRedirectMixin, LoginView):
    pass

class Logout(LoginRequiredMixin, LogoutView):
    pass

class Register(LoggedInRedirectMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('gallery:login')

# class BookList(LoginRequiredMixin, ListView):
#     template_name = 'gallery/home.html'
#     def get_queryset(self):
#         return Book.objects.filter(user=self.request.user)
#     paginate_by = 9
#     ordering = ['-created']


# class PostDelete(AccessUserMixin, DeleteView):
#     model = Post
#     success_url = reverse_lazy('gallery:home')


# class PostCreate(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ('title', 'description', 'photo')
#     success_url = reverse_lazy('gallery:home')

#     def form_valid(self, form):
#         self.obj = form.save(commit=False)
#         self.obj.user = self.request.user

#         return super(PostCreate, self).form_valid(form)


# class PostUpdate(AccessUserMixin, UpdateView):
#     model = Post
#     fields = ('title', 'description', 'photo')
#     success_url = reverse_lazy('gallery:home')


@login_required
def cart_add(request, id):
    print(request)
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.add(product=product)
    return redirect("gallery:cart_detail")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.remove(product)
    return redirect("gallery:cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.add(product=product)
    return redirect("gallery:cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("gallery:cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("gallery:cart_detail")


@login_required
def cart_detail(request):
    cart = Cart(request)
    total_price = 0
    for c in cart.cart:
        total_price += cart.cart[c]['quantity'] * float(cart.cart[c]['price'])

    return render(request, 'gallery/shoppingcart.html', context={'sum_price': total_price})