# Generated by Django 3.0.5 on 2020-07-01 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'bank',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=30)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Bank')),
            ],
            options={
                'db_table': 'branch',
                'ordering': ['state', 'city', 'district', 'branch'],
            },
        ),
    ]
