# Generated by Django 5.0.4 on 2024-04-19 09:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0005_course_price_lesson_price_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="updated_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="последнее обновление"
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="updated_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="последнее обновление"
            ),
        ),
    ]
