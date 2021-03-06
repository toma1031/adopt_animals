# Generated by Django 2.2.17 on 2021-04-08 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, verbose_name='Animal Category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=300, verbose_name='State')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('photo', models.ImageField(upload_to='images', verbose_name='Photo')),
                ('sex', models.IntegerField(verbose_name='Sex')),
                ('weight', models.IntegerField(verbose_name='Weight')),
                ('story', models.TextField(max_length=300, verbose_name='Story')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopt_animals.Tag', verbose_name='Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
