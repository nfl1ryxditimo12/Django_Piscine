# Generated by Django 3.2.5 on 2021-08-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex07', '0002_alter_movies_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]