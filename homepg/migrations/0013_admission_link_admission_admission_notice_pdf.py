# Generated by Django 4.2.5 on 2023-09-20 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepg', '0012_admission'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='link_admission',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='notice_pdf',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
