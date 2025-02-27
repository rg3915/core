# Generated by Django 3.2.12 on 2023-03-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researcher', '0002_auto_20230123_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher',
            name='gender',
            field=models.CharField(choices=[('F', 'Mujer'), ('M', 'Hombre')], max_length=1, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='lattes',
            field=models.TextField(blank=True, null=True, verbose_name='Lattes'),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='orcid',
            field=models.TextField(blank=True, null=True, verbose_name='ORCID'),
        ),
    ]
