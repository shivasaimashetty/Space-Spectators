from django.contrib import admin
from groups.models import Group,GroupMember
from groups import models
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model=models.GroupMember

admin.site.register(Group)
admin.site.register(GroupMember)
