# Generated by Django 4.0.2 on 2022-02-15 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_listadeprodutos_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listadeprodutos',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
    ]