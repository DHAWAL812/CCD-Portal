# Generated by Django 3.0.3 on 2020-02-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_candidate_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='company_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
