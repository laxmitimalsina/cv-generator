# Generated by Django 3.1.4 on 2021-04-26 14:57

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('url', models.URLField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='education',
            old_name='institute',
            new_name='educational_institute',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='name',
            new_name='add_skills',
        ),
        migrations.AddField(
            model_name='education',
            name='country',
            field=django_countries.fields.CountryField(default='Nepal', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.CharField(default='added text', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='title',
            field=models.CharField(default='added title', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
