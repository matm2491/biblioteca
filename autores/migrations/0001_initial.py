# Generated by Django 3.0.2 on 2020-02-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('p_apellidos', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
