# Generated by Django 3.1.7 on 2021-03-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50, verbose_name='Login')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('firstname', models.CharField(max_length=50, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=50, verbose_name='Last Name')),
            ],
        ),
    ]
