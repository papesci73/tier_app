from django.db import models
from django.conf import settings


class ShorterModelItem(models.Model):
    """Model to contain the data to trandform and trace URLs"""
    long_url = models.CharField(max_length=4096, unique=True)
    hits = models.PositiveIntegerField(default='0', editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        indexes = [
            models.Index(fields=['long_url'])
        ]

    def __str__(self):
        """return the model urls"""
        return self.long_url
