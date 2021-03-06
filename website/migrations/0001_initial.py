# Generated by Django 3.0.4 on 2020-03-28 13:03

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
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('post_date', models.DateField(auto_now_add=True)),
                ('preview', models.CharField(max_length=300)),
                ('thumbnail', models.ImageField(upload_to='upload/%Y/%m/%d')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('year', models.DateField(auto_now=True)),
                ('blogpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.BlogPost')),
            ],
        ),
    ]
