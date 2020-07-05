# Generated by Django 3.0.5 on 2020-07-03 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('ifsc', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_data', to='api.Banks')),
            ],
        ),
        migrations.DeleteModel(
            name='Branchs',
        ),
    ]
