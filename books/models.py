from django.db import models

class Book(models.Model):
    # Book ID is unique by default because it's set as the primary key
    book_id = models.AutoField(primary_key=True)  # Auto-incremented ID

    # Title and Author should not be empty
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.CharField(max_length=255, blank=False, null=False)

    # Genre (optional, but you can add constraints if needed)
    genre = models.CharField(max_length=100, blank=True, null=True)

    # Availability status should be one of these two values
    AVAILABLE = 'Available'
    CHECKED_OUT = 'Checked Out'
    AVAILABILITY_STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (CHECKED_OUT, 'Checked Out'),
    ]
    availability_status = models.CharField(
        max_length=50,
        choices=AVAILABILITY_STATUS_CHOICES,
        default=AVAILABLE,
        blank=False,  # Ensures this field cannot be left blank
        null=False,   # Ensures database doesn't store NULL value
    )

    def __str__(self):
        return f"{self.title} by {self.author}"
