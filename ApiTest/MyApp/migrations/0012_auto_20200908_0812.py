# Generated by Django 2.2 on 2020-09-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0011_auto_20200813_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_apis',
            name='last_api_body',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='db_apis',
            name='last_body_method',
            field=models.CharField(max_length=20, null=True),
        ),
    ]