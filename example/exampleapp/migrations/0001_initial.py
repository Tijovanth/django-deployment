# Generated by Django 2.1.4 on 2019-01-09 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=264)),
                ('LastName', models.CharField(max_length=264)),
                ('Email', models.EmailField(max_length=264, unique=True)),
                ('Portfolio', models.URLField(blank=True)),
                ('Profilepic', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
    ]
