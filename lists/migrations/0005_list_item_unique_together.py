# Generated by Django 4.0.1 on 2022-02-06 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_remove_list_items_item_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]