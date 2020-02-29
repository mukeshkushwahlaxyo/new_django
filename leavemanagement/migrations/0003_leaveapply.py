# Generated by Django 2.2 on 2020-02-25 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leavemanagement', '0002_auto_20200220_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveApply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reports_to', models.IntegerField(null=True)),
                ('day_status', models.CharField(max_length=255, null=True)),
                ('date_from', models.DateField(null=True)),
                ('date_to', models.DateField(null=True)),
                ('count', models.IntegerField(null=True)),
                ('reason', models.TextField(null=True)),
                ('file_path', models.CharField(max_length=255, null=True)),
                ('addr_during_leave', models.IntegerField(null=True)),
                ('contact_no', models.CharField(max_length=255, null=True)),
                ('status', models.BooleanField(null=True)),
                ('applicant_remark', models.TextField(null=True)),
                ('approver_remark', models.TextField(null=True)),
                ('hr_remark', models.TextField(null=True)),
                ('deleted_at', models.DateField(null=True)),
                ('carry_count', models.IntegerField(null=True)),
                ('paid_count', models.IntegerField(null=True)),
                ('unpaid_count', models.IntegerField(null=True)),
                ('subadmin_approval', models.BooleanField(null=True)),
                ('admin_approval', models.BooleanField(null=True)),
                ('teamlead_approval', models.BooleanField(null=True)),
                ('approver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person2persons', to=settings.AUTH_USER_MODEL)),
                ('leave_type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leavemanagement.LeaveTypeModel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
