# Generated by Django 2.2 on 2021-06-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0003_change_field_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(max_length=1000, null=True, verbose_name='Комментарий от покупателя'),
        ),
    ]
