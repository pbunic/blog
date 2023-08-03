from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mdeditor.fields import MDTextField
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    """Custom manager for filtering published posts."""
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """Post publishing."""

    class Status(models.TextChoices):
        """Post status."""
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        ARCHIVED = 'AR', 'Archived'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    img_cover = models.CharField(max_length=1000)
    body = MDTextField()
    tags = TaggableManager(
        verbose_name=_('Tags'),
        help_text=_('A comma-separated tags. '
                    'Use quotes for multiple words '
                    'and lowercase letters.')
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    # Managers
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])


class Comment(models.Model):
    """Comment section."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'{self.email} | {self.post}'
