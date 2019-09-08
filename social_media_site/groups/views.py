from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from groups.models import Group,GroupMember
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields=('name','description')
    model=Group

class SingleGroup(generic.DetailView):
    model=Group


class ListGroups(generic.ListView):
    model=Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group=get_object_or_404(Group,slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,'Warning already a memeber')

        else:
            messages.success(self.request,'You are now a member!')

        return super().get(request,*args,**kwargs)

class MemberDetail(generic.DetailView):
    model=Group
    template_name='groups/group_member_detail.html'


class MyGroups(generic.ListView):
    model=GroupMember
    template_name='groups/mygroups.html'
    context_object_name='my_groups'




class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        try:
            membership=GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()

        except GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry you are not in this group')

        else:
            membership.delete()
            messages.success(self.request,'You have left the group')

        return super().get(request,*args,**kwargs)
