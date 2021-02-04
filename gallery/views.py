from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

from .models import Book, Comment

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'gallery/index.html')


class BookList(ListView):
    model = Book
    paginate_by = 9
    ordering = ['-created']


class BookDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Book, slug=slug)



#@login_required
def like_or_dislike(request, pk):
    # print(request.resolver_match)
    user = request.user
    comment = get_object_or_404(Comment, pk=pk)
    comment_likes_users = comment.likes.all()
    count = comment_likes_users.count()

    if user.is_anonymous:
        return JsonResponse({
            'likes': count,
            'status': 'not_login',
        })

    if user in comment_likes_users:
        comment.likes.remove(user)
        count -= 1
        user_in_likes = False
    else:
        comment.likes.add(user)
        count += 1
        user_in_likes = True

    return JsonResponse({
        'status': user.is_authenticated,
        'likes': count,
        'user_in_likes': user_in_likes,
    })


def comment(request, pk):
    # print(request.resolver_match)
    user = request.user
    book = get_object_or_404(Book, pk=pk)

    print(request)
    
    
    if user.is_anonymous:
        return JsonResponse({
            'status': 'not_login',
        })
    content = request.POST.get('content')
    if content == '':
        return JsonResponse({
            'status': 'bad_content',
        })
    Comment.objects.create(
        user = user,
        book = book,
        content = content
    )
    book_comments = book.comments.all()
    count = book_comments.count()
    
    all_comments = []
    for cmmnt in book_comments:
        likers = cmmnt.likes.all()
        like_count = likers.count()
        user_in_likes = user in likers
        all_comments.append({'created': cmmnt.created_date, 'username': cmmnt.user.username, 'content': cmmnt.content, 'like_count': like_count, 'user_in_likes': user_in_likes, 'pk': cmmnt.pk})
    

    return JsonResponse({
        'status': user.is_authenticated,
        'count': count,
        'user': user.username,
        'book_comments': all_comments
    })