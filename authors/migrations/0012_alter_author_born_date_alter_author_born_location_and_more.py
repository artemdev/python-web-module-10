# Generated by Django 5.0.4 on 2024-05-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0011_alter_author_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='born_date',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='born_location',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='fullname',
            field=models.CharField(unique=True),
        ),
    ]
