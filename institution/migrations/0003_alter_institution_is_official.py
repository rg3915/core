# Generated by Django 3.2.12 on 2023-01-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0002_auto_20230127_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='is_official',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no'), ('unknow', 'unknow')], max_length=6, null=True, verbose_name='Is official'),
        ),
    ]
