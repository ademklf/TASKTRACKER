# Generated by Django 4.1.4 on 2022-12-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('priority', models.SmallIntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default=3)),
                ('is_done', models.BooleanField(default=False)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
