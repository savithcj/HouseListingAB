# Generated by Django 2.1.5 on 2019-03-13 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('global_listing', '0019_remove_propertyimages_property_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyimages',
            name='property_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='propertyimages_property_id', to='global_listing.Property'),
        ),
    ]
