# Generated by Django 2.1.5 on 2019-03-07 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('global_listing', '0005_propertyaddress_propertyimages_roomflooring'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='phonenumber_user_id', to='global_listing.User')),
            ],
        ),
    ]
