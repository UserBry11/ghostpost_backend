from django.db import models
from django.utils import timezone


class BoastRoast(models.Model):
    title = models.CharField(max_length=30)
    boolean = models.BooleanField()
    content = models.TextField()
    upvotes = models.PositiveIntegerField(default=0, blank=True)
    downvotes = models.PositiveIntegerField(default=0, blank=True)
    post_date = models.DateTimeField(default=timezone.now)

    @property
    def vote_score(self):
        total = self.upvotes - self.downvotes
        return total

    def __str__(self):
        return self.title
