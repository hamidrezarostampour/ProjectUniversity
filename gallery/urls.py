from django.urls import path
from . import views as gallery_view
from account import views as account_view

app_name = 'gallery'

urlpatterns = [
    
    path('', gallery_view.CategoryList.as_view(), name='index'),
    path('about', gallery_view.AboutList.as_view(), name='about'),
    path('rahnama', gallery_view.RahnamaList.as_view(), name='rahnama'),
    path('offer', gallery_view.OfferList.as_view(), name='offer'),
    path('shoppingcart', gallery_view.ShoppingCart.as_view(), name='shoppingcart'),
    path('books/<slug:cat_slug>', gallery_view.BookList.as_view(), name='books'),
    path('search', gallery_view.SearchResultsView.as_view(), name='search_results'),

    path('login', account_view.Login.as_view(), name='login'),
    path('logout', account_view.Logout.as_view(), name='logout'),
    path('register', account_view.Register.as_view(), name='register'),

    path('api/<int:pk>/like_or_dislike', gallery_view.like_or_dislike, name='like_or_dislike'),
    path('api/<int:pk>/comment', gallery_view.comment, name='comment'),
    path('api/<int:pk>/star/<int:score>', gallery_view.star, name='star'),

    # path('home', account_view.PostList.as_view(), name='home'),
    # path('create', account_view.PostCreate.as_view(), name='create'),
    path('book/<slug:slug>', gallery_view.BookDetail.as_view(), name='detail'),
    # path('delete/<int:pk>', account_view.PostDelete.as_view(), name="delete"),
    # path('update/<int:pk>', account_view.PostUpdate.as_view(), name="update"),
]