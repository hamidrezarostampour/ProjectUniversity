from django.db import models
from account.models import User
from uuslug import uuslug as slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True) #, verbose_name='آدرس پست')
    title = models.CharField(max_length=200) #, verbose_name='عنوان')
    photo = models.ImageField(upload_to="cat_images")
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, instance=self)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return '{}'.format(self.title)


class Book(models.Model):
    title = models.CharField(max_length=200) #, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True) #, verbose_name='آدرس پست')
    description = models.TextField() # verbose_name="محتوا")
    photo = models.ImageField(upload_to="images") #, verbose_name='تصویر')
    # user = models.ForeignKey(User, on_delete=models.CASCADE) #, verbose_name='کاربر')
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
    # stars = models.ManyToManyField(User, blank=True, related_name='stars')
    number_of_pages = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=0,default=0)
    category = models.ManyToManyField(Category)    

    def get_avg_stars_percent(self):
        book_stars = Star.objects.filter(book=self)
        book_stars_scores = [bs.score for bs in book_stars]
        if len(book_stars) == 0:
            avg = 0
        else:
            avg = sum(book_stars_scores) / len(book_stars)
        return int((avg/5)*100)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, instance=self)
        super(Book, self).save(*args, **kwargs)
        
    def __str__(self):
        return '{} - {}'.format(self.title, self.author)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def __str__(self):
        return '{} - {}'.format(self.book.title, self.user.username)
    
    class Meta:
        ordering = ['-created_date']


class Star(models.Model):
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='stars')
    def __str__(self):
        return '{} - {} - {}'.format(self.score, self.book.title, self.user.username)
