# Generated by Django 4.2.7 on 2023-11-13 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="projects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("satrtDate", models.DateField()),
                ("endDate", models.DateField(blank=True, null=True)),
                ("price", models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="workers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("surname", models.CharField(max_length=30)),
                ("name", models.CharField(max_length=30)),
                ("otchestvo", models.CharField(max_length=30)),
                ("pasportNumber", models.IntegerField()),
                ("pasportSerie", models.IntegerField()),
                ("INN", models.IntegerField()),
                ("birth", models.DateField()),
                ("position", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="workingOn",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(blank=True, null=True)),
                ("price", models.FloatField(blank=True, null=True)),
                ("published", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="btest.projects"
                    ),
                ),
                (
                    "worker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="btest.workers"
                    ),
                ),
            ],
        ),
    ]
