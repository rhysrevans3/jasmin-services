# Generated by Django 2.0.6 on 2018-06-11 15:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jasmin_metadata', '0002_auto_20170125_1755'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('jasmin_services', '0005_remove_group_dn_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='role name')),
                ('description', models.CharField(blank=True, max_length=250)),
                ('hidden', models.BooleanField(default=True, help_text='Prevents the role appearing in listings unless the user has an active grant or request for it.')),
                ('position', models.PositiveIntegerField(default=9999, help_text='Number defining where the role appears in listings. Roles are ordered first by their service, then in ascending order by this field, then alphabetically.')),
            ],
            options={
                'ordering': ('service__category__position', 'service__category__long_name', 'service__position', 'service__name', 'position', 'name'),
                'permissions': (('view_users_role', 'Can view users with role'), ('send_message_role', 'Can send messages to users with role')),
            },
        ),
        migrations.CreateModel(
            name='RoleObjectPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_pk', models.CharField(help_text='Primary key of the object to which the permission applies.', max_length=150, verbose_name='Object primary key')),
                ('content_type', models.ForeignKey(help_text='Content type of the object to which the permission applies.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Object content type')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object_permissions', related_query_name='object_permission', to='jasmin_services.Role')),
            ],
        ),
        migrations.AlterModelOptions(
            name='behaviour',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='grant',
            options={'get_latest_by': 'granted_at', 'ordering': ('role__service__category__position', 'role__service__category__long_name', 'role__service__position', 'role__service__name', 'role__position', 'role__name', '-granted_at')},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'get_latest_by': 'requested_at', 'ordering': ('role__service__category__position', 'role__service__category__long_name', 'role__service__position', 'role__service__name', 'role__position', 'role__name', '-requested_at'), 'permissions': (('decide_request', 'Can make decisions on requests'),)},
        ),
        migrations.RenameField(
            model_name='grant',
            old_name='role',
            new_name='role_old',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='role',
            new_name='role_old',
        ),
        migrations.RemoveField(
            model_name='service',
            name='manual_intervention_required',
        ),
        migrations.AddField(
            model_name='role',
            name='behaviours',
            field=models.ManyToManyField(related_name='roles', related_query_name='role', to='jasmin_services.Behaviour'),
        ),
        migrations.AddField(
            model_name='role',
            name='metadata_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='jasmin_metadata.Form'),
        ),
        migrations.AddField(
            model_name='role',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', related_query_name='role', to='jasmin_services.Service'),
        ),
        migrations.AddField(
            model_name='grant',
            name='role_new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grants', related_query_name='grant', to='jasmin_services.Role'),
        ),
        migrations.AddField(
            model_name='request',
            name='role_new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', related_query_name='request', to='jasmin_services.Role'),
        ),
        migrations.AlterUniqueTogether(
            name='roleobjectpermission',
            unique_together={('role', 'permission', 'content_type', 'object_pk')},
        ),
        migrations.AlterUniqueTogether(
            name='role',
            unique_together={('service', 'name')},
        ),
    ]