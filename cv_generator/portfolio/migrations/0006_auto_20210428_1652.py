# Generated by Django 3.1.4 on 2021-04-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20210426_1752'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expereince',
            new_name='Experience',
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='skill',
            name='add_skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
