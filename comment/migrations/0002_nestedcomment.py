# Generated by Django 2.2.4 on 2019-10-30 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NestedComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comment.Comment')),
                ('nested', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='yorum', to='comment.Comment')),
            ],
            bases=('comment.comment',),
        ),
    ]