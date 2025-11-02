from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension
from django.contrib.postgres.indexes import GinIndex

class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_thread_participants_alter_thread_created_by"),
    ]

    operations = [
        TrigramExtension(),
        migrations.AddIndex(
            model_name="message",
            index=GinIndex(
                name="msg_content_trgm",
                fields=["content"],
                opclasses=["gin_trgm_ops"],
            ),
        ),
    ]
