# Generated by Django 4.1.2 on 2022-10-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_post_seo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='seo_tag',
            field=models.ManyToManyField(default=None, to='blog.seoproperty'),
        ),
    ]
