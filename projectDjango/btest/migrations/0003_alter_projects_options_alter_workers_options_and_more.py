# Generated by Django 4.2.7 on 2023-11-20 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("btest", "0002_remove_workingon_content_remove_workingon_price_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="projects",
            options={
                "ordering": ["satrtDate"],
                "verbose_name": "Проекты",
                "verbose_name_plural": "Проект",
            },
        ),
        migrations.AlterModelOptions(
            name="workers",
            options={
                "ordering": ["surname"],
                "verbose_name": "Сотрудники",
                "verbose_name_plural": "Сотрудник",
            },
        ),
        migrations.AlterModelOptions(
            name="workingon",
            options={
                "verbose_name": "Участия в проектах",
                "verbose_name_plural": "Участие в проектах",
            },
        ),
        migrations.AlterField(
            model_name="projects",
            name="endDate",
            field=models.DateField(
                blank=True, null=True, verbose_name="Дата окончания"
            ),
        ),
        migrations.AlterField(
            model_name="projects",
            name="price",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Объём финансирования"
            ),
        ),
        migrations.AlterField(
            model_name="projects",
            name="satrtDate",
            field=models.DateField(verbose_name="Дата начала"),
        ),
        migrations.AlterField(
            model_name="projects",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="workers",
            name="INN",
            field=models.IntegerField(verbose_name="ИНН"),
        ),
        migrations.AlterField(
            model_name="workers",
            name="birth",
            field=models.DateField(verbose_name="Дата рождения"),
        ),
        migrations.AlterField(
            model_name="workers",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="workers",
            name="otchestvo",
            field=models.CharField(max_length=30, verbose_name="Отчество"),
        ),
        migrations.AlterField(
            model_name="workers",
            name="pasportNumber",
            field=models.IntegerField(verbose_name="Номер паспорта"),
        ),
        migrations.AlterField(
            model_name="workers",
            name="pasportSerie",
            field=models.IntegerField(verbose_name="Серия паспорта"),
        ),
        migrations.AlterField(
            model_name="workers",
            name="position",
            field=models.CharField(max_length=50, verbose_name="Должность"),
        ),
        migrations.AlterField(
            model_name="workers",
            name="surname",
            field=models.CharField(max_length=30, verbose_name="Фамилия"),
        ),
        migrations.AlterField(
            model_name="workingon",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="btest.projects",
                verbose_name="Проект",
            ),
        ),
        migrations.AlterField(
            model_name="workingon",
            name="worker",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="btest.workers",
                verbose_name="Сотрудник",
            ),
        ),
    ]
