# Generated by Django 5.1.7 on 2025-03-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_availability_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='availability_status',
            field=models.CharField(choices=[('Available', 'Available'), ('Checked Out', 'Checked Out')], default='Available', max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
