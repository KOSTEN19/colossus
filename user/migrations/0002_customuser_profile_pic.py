"""Import line"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """Class line"""
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
