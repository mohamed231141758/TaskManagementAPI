from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_COMPLETE = 'complete'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETE, 'Complete'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status}) - {self.user.username}"

    class Meta:
        ordering = ['-created_at']