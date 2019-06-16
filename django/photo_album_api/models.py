from django.db import models
from datetime import date
from user_app.models import User


class Task(models.Model):
    """Stores a task."""
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    created_by = models.CharField(max_length=200)

    # Date the task was created.
    created_on = models.DateField(default=date.today)

    # Due date.
    due_date = models.DateField(default=date.today)

    # Meta data about the database table.
    class Meta:
        # Set the table name.
        db_table = 'task'

        # Set default ordering
        ordering = ['id']

    # Define what to output when the model is printed as a string.
    def __str__(self):
        return self.title


class PhotoAlbum(models.Model):
    """ stores photo albums """
    name = models.CharField(max_length=50)
    description = models.TextField()
    create_date = models.DateField(default=date.today)
    members = models.ManyToManyField(User) #to user