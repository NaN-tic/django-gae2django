from django.db import models
from django.contrib.auth.models import User


class CodereviewProfile(models.Model):
    # Link to the user model
    user = models.OneToOneField(User, related_name='profile', unique=False)
    main_reviewer = models.BooleanField(u"Main Reviewer", default=False,
                                        blank=True, help_text="Designates that\
                                        this user receive all mails from\
                                        codereviews uploads and comments")

    def __str__(self):
        return "%s's profile" % self.user


# Create your models here.
