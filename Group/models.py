from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group as Roles
from BasicArticle.models import Articles
import os, uuid
from Media.models import Media

# Create your models here.
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('group', filename)

class Group(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField()
	image = models.ImageField(null=True,upload_to=get_file_path)
	visibility = models.BooleanField()
	created_at = models.DateTimeField(null=True, auto_now_add=True)
	created_by = models.ForeignKey(User,null =True, related_name='groupcreator')

	def __str__(self):
		return self.name

class GroupMembership(models.Model):
	group = models.ForeignKey(Group, related_name='groupmembership')
	user = models.ForeignKey(User, related_name='groupmembership')
	role = models.ForeignKey(Roles, null=True, related_name='groupmembership')

class GroupArticles(models.Model):
	article = models.ForeignKey(Articles, related_name='grouparticles')
	user = models.ForeignKey(User, related_name='grouparticles')
	group = models.ForeignKey(Group, null=True, related_name='grouparticles')
	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('article_view', kwargs={'pk': self.article_id})

class GroupInvitations(models.Model):
    invitedby = models.ForeignKey(User, related_name='groupinvitationsinvitedby')
    invitedat = models.DateTimeField(null=True, auto_now_add=True)
    user = models.ForeignKey(User, related_name='groupinvitations')
    role = models.ForeignKey(Roles, null=True, related_name='groupinvitations')
    status = models.CharField(null=True, max_length=100)
    group = models.ForeignKey(Group, related_name='groupinvitations')

class GroupMedia(models.Model):
	media = models.ForeignKey(Media, null=True, related_name='groupmedia')
	user = models.ForeignKey(User, null=True, related_name='groupmedia')
	group = models.ForeignKey(Group, null=True, related_name='groupmedia')	