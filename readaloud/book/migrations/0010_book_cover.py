# Generated by Django 4.1.4 on 2023-02-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0009_alter_book_categories"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="cover",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
