from django.urls import path
from . import views as gallery_view
from account import views as account_view

app_name = 'gallery'

urlpatterns = [
    
    path('', gallery_view.CategoryList.as_view(), name='index'),
    path('about', gallery_view.about, name='about'),
    path('rahnama', gallery_view.rahnama, name='rahnama'),
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



    path('cart/add/<int:id>/', account_view.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', account_view.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         account_view.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         account_view.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', account_view.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',account_view.cart_detail,name='cart_detail'),
]