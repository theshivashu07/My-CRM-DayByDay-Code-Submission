# Generated by Django 3.1.7 on 2021-06-11 06:37

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
                ('userName', models.CharField(max_length=15)),
                ('emailId', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('fullName', models.CharField(max_length=25)),
                ('Age', models.CharField(max_length=2)),
                ('mobileNumber', models.CharField(max_length=10)),
            ],
        ),
    ]
