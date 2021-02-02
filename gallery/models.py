from django.db import models
from account.models import User
from uuslug import uuslug as slugify
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200) #, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True) #, verbose_name='آدرس پست')
    description = models.TextField() # verbose_name="محتوا")
    photo = models.ImageField(upload_to="images") #, verbose_name='تصویر')
    user = models.ForeignKey(User, on_delete=models.CASCADE) #, verbose_name='کاربر')
    created = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, instance=self)
        super(Post, self).save(*args, **kwargs)
        
    def __str__(self):
        return '{} - {}'.format(self.title, self.user)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.post.title, self.user.username)
    
    class Meta:
        ordering = ['-created_date']