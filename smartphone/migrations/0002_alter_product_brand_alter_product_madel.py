# Generated by Django 4.0.5 on 2022-06-28 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='smartphone.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='madel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='smartphone.madel'),
        ),
    ]
