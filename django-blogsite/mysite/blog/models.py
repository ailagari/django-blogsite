from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse #for reverse method to track back urls(Canonical URLs)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
            self).get_queryset()\
                .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft' , 'DRAFT'),
        ('published', 'PUBLISHED'),  
    )  #This is a tuple with first element in each tuple is the actual value to be set on the model, 
        #and the second element is the human-readable name.
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    def get_absolute_url(self):
        return reverse('blog:post_detail',
        args=[self.publish.year,
        self.publish.month,
        self.publish.day, self.slug])
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title