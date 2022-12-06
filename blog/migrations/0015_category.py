# Generated by Django 4.1.2 on 2022-10-24 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
            ],
        ),
    ]