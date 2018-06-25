"""The Model Class for my application.
"""
import uuid
from django.db import models
from django.urls import reverse


class User(models.Model):

    """Model representing a given user

    Attributes:
        created_at (datetime): The time at which a user is created
        email (string): The email id for a given user
        name (string): username
        updated_at (datetime): The time at which a user's record is updated
        uuid (uuid): Unique id representing a given user - the primary key for our table
    """

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                               editable=False)
    email = models.EmailField()
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the model object

        Returns:
            str: Return the name and email for a given user
        """
        return '{0} ({1})'.format(self.name, self.email)

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this user
        """
        return reverse('user_detail', args=[str(self.user_id)])
