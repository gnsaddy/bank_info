# Generated by Django 3.0.5 on 2020-07-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='ifsc',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]