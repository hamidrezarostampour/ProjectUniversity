from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

from .models import Book, Comment, Star, Category

from django.shortcuts import render


# Create your views here.



def about(request):
    return render(request, 'gallery/about.html')


class CategoryList(ListView):
    model = Category
    template_name = 'gallery/index.html'


class AboutList(ListView):
    model = Category
    template_name = 'gallery/about.html'


class RahnamaList(ListView):
    model = Category
    template_name = 'gallery/rahnama.html'


class OfferList(ListView):
    model = Category
    template_name = 'gallery/offer.html'


class BookList(ListView):
    model = Book

    def get_queryset(self):
        global cat
        slug = self.kwargs.get('cat_slug')
        cat = get_object_or_404(Category, slug=slug)
        cat_books = Book.objects.filter(category=cat)
        return cat_books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = cat
        return context

    paginate_by = 12
    ordering = ['-created']


class BookDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Book, slug=slug)


# @login_required
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

    # print(request)

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
        user=user,
        book=book,
        content=content
    )
    book_comments = book.comments.all()
    count = book_comments.count()

    all_comments = []
    for cmmnt in book_comments:
        likers = cmmnt.likes.all()
        like_count = likers.count()
        user_in_likes = user in likers
        all_comments.append({'created': cmmnt.created_date, 'username': cmmnt.user.username, 'content': cmmnt.content,
                             'like_count': like_count, 'user_in_likes': user_in_likes, 'pk': cmmnt.pk})

    return JsonResponse({
        'status': user.is_authenticated,
        'count': count,
        'user': user.username,
        'book_comments': all_comments
    })


def star(request, pk, score):
    # print(request.resolver_match)
    user = request.user
    book = get_object_or_404(Book, pk=pk)

    book_stars = Star.objects.filter(book=book)
    book_stars_users = [bs.user for bs in book_stars]
    book_stars_scores = [bs.score for bs in book_stars]

    if len(book_stars) == 0:
        avg = 0
    else:
        avg = sum(book_stars_scores) / len(book_stars)
    avg = int((avg / 5) * 100)

    if user.is_anonymous:
        return JsonResponse({
            'avg': avg,
            'status': 'not_login',
        })
    if score not in [0, 1, 2, 3, 4, 5]:
        return JsonResponse({
            'avg': avg,
            'status': 'bad_content',
        })

    user_in_stars = True
    if user in book_stars_users:
        user_index = book_stars_users.index(user)
        book_stars_scores[user_index] = score
        Star.objects.filter(user=user, book=book).update(score=score)
    else:
        Star.objects.create(
            user=user,
            book=book,
            score=score
        )
        book_stars_users.append(user)
        book_stars_scores.append(score)

    avg = sum(book_stars_scores) / len(book_stars_users)
    avg = int((avg / 5) * 100)
    return JsonResponse({
        'status': user.is_authenticated,
        'avg': avg,
        'user_in_stars': user_in_stars,
        'user_score': score
    })
