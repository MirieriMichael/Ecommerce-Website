# Generated by Django 5.1 on 2024-08-18 21:08

from django.db import migrations, models
from django.utils.text import slugify

def generate_unique_slugs(apps, schema_editor):
    Item = apps.get_model('item', 'Item')
    for item in Item.objects.all():
        if not item.slug:
            unique_slug = slugify(item.name)
            counter = 1
            # Ensure uniqueness of the slug
            while Item.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slugify(item.name)}-{counter}"
                counter += 1
            item.slug = unique_slug
            item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RunPython(generate_unique_slugs),
    ]
