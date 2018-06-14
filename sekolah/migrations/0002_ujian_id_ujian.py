# Generated by Django 2.0 on 2018-06-12 14:26

from django.db import migrations, models
import uuid

def create_uuid(apps, schema_editor):
    Ujian = apps.get_model('sekolah', 'Ujian')
    for ujian in Ujian.objects.all():
        ujian.id_ujian = uuid.uuid4()
        ujian.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ujian',
            name='id_ujian',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.RunPython(create_uuid),
        migrations.AlterField(
            model_name='ujian',
            name='id_ujian',
            field=models.UUIDField(unique=True),
        ),
    ]