# Generated by Django 4.2.7 on 2023-11-13 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("btest", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="workingon", name="content",),
        migrations.RemoveField(model_name="workingon", name="price",),
        migrations.RemoveField(model_name="workingon", name="published",),
    ]