# Generated by Django 5.0.3 on 2024-03-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_userprofilephoto_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.DeleteModel(
            name='UserProfilePhoto',
        ),
    ]
