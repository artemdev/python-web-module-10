# Generated by Django 5.0.4 on 2024-05-01 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_rename_name_quote_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='tags',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]