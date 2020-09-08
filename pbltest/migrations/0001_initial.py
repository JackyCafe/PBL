# Generated by Django 2.2.5 on 2020-08-03 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('context', models.TextField(blank=True)),
                ('context1', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('published_date', models.DateTimeField(auto_now=True, null=True)),
                ('activate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.CreateActivate')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
            options={
                'verbose_name_plural': 'Card',
            },
        ),
        migrations.CreateModel(
            name='FileCard',
            fields=[
                ('file_title', models.TextField()),
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RowCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('context', models.TextField(blank=True)),
                ('context1', models.TextField(blank=True)),
                ('context2', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('published_date', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
            options={
                'verbose_name_plural': 'row_Card',
            },
        ),
        migrations.CreateModel(
            name='UPCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/card/img/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='card/covers/')),
                ('class_material', models.CharField(max_length=100, null=True)),
                ('thumbnail', models.CharField(max_length=100, null=True)),
                ('activate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.CreateActivate')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.User')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Group')),
            ],
        ),
        migrations.CreateModel(
            name='TestCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_img', models.TextField(blank=True, null=True)),
                ('base_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pbltest.Card')),
                ('base_card1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pbltest.RowCard')),
            ],
        ),
        migrations.AddField(
            model_name='rowcard',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pbltest.UPCard'),
        ),
        migrations.AddField(
            model_name='card',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pbltest.UPCard'),
        ),
        migrations.AddField(
            model_name='card',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Group'),
        ),
    ]