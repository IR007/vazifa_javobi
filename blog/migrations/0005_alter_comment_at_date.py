# Generated by Django 4.2.5 on 2023-10-09 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_at_date_alter_comment_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='at_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
