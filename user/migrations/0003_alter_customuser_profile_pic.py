"""Import line"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """Class line"""
    dependencies = [
        ('users', '0002_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='nfts/'),
        ),
    ]
