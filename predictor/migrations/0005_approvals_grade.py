# Generated by Django 3.0.2 on 2020-01-15 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0004_remove_approvals_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvals',
            name='grade',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]