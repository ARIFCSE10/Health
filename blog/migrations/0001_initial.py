# Generated by Django 2.1.4 on 2019-04-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=5000)),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'db_table': 'blog',
            },
        ),
    ]
