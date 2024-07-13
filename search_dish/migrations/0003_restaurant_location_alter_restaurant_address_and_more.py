# Generated by Django 4.2.6 on 2024-07-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_dish', '0002_alter_restaurant_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.CharField(default='NA', max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]