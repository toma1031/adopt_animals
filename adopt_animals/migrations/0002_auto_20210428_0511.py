# Generated by Django 2.2.17 on 2021-04-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt_animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='Weight'),
        ),
    ]
