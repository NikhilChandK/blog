# Generated by Django 5.0.10 on 2024-12-30 11:42

import taggit.managers
from django.db import migrations, models


def populate_active_bool(apps, schema_editor):
    Comment = apps.get_model("blog", "Comment")
    for comment in Comment.objects.all():
        # Adjust the logic based on your original data
        # For example, set True if the original active field is non-null
        comment.active_bool = bool(comment.active)  # Treat non-null values as True
        comment.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_managers_comment'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        # Step 1: Add a new boolean field
        migrations.AddField(
            model_name='comment',
            name='active_bool',
            field=models.BooleanField(default=True),
        ),
        # Step 2: Populate active_bool using the existing active field
        migrations.RunPython(populate_active_bool),
        # Step 3: Remove the original active field
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        # Step 4: Rename active_bool to active
        migrations.RenameField(
            model_name='comment',
            old_name='active_bool',
            new_name='active',
        ),
    ]
