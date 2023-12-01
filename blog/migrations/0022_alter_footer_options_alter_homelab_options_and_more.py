# Generated by Django 4.2 on 2023-11-15 20:55

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_homelab_homelabelement_alter_footer_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footer',
            options={'ordering': ['link_section'], 'verbose_name_plural': 'Footer Map'},
        ),
        migrations.AlterModelOptions(
            name='homelab',
            options={'verbose_name_plural': 'Homelab Space'},
        ),
        migrations.AlterModelOptions(
            name='homelabelement',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Homelab Hardware'},
        ),
        migrations.RemoveField(
            model_name='homelab',
            name='lab_image_one',
        ),
        migrations.RemoveField(
            model_name='homelab',
            name='lab_image_three',
        ),
        migrations.RemoveField(
            model_name='homelab',
            name='lab_image_two',
        ),
        migrations.AddField(
            model_name='homelab',
            name='body',
            field=mdeditor.fields.MDTextField(default='body'),
            preserve_default=False,
        ),
    ]
