# Generated by Django 4.0.6 on 2022-07-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='content',
            field=models.CharField(max_length=500),
        ),
    ]