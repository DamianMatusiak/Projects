from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Tag(models.Model):
    tag_name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.tag_name


class Entry(models.Model):
    title = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    user_likes = models.ManyToManyField(
        User, related_name="posts_liked", blank=True,
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_similar_entries(self):
        return (Entry.objects.all()
                .filter(tags__in=self.tags.all())
                .exclude(pk=self.pk)
                .annotate(tag_number=Count('tags'))
                .order_by('-tag_number', '-pub_date')[:3])

    def get_absolute_url(self):
        return reverse("entry-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Entry, on_delete=models.CASCADE)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body_text[:30] + \
            ("..." if len(self.body_text) > 30 else "")


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
    tags_followed = models.ManyToManyField(Tag)

    def get_entries_for_tags(self):
        return (Entry.objects.all()
                .filter(tags__in=self.tags_followed.all())
                .annotate(tag_number=Count('tags'))
                .order_by('-tag_number', '-pub_date')[:3])
