from django.db import modelsfrom django.contrib.auth.models import Userfrom BasicArticle.models import Articles,get_file_pathclass Law(models.Model):	article = models.OneToOneField(Articles,on_delete=models.CASCADE)	upvote = models.PositiveIntegerField(default=0)	downvote = models.PositiveIntegerField(default=0)	def __str__(self):		return self.article.titleclass Voting(models.Model):	article = models.ForeignKey(Articles,on_delete=models.CASCADE)	user = models.ForeignKey(User,on_delete=models.CASCADE)	upflag = models.BooleanField(default=False)	downflag = models.BooleanField(default=False)	def __str__(self):		return self.article.title + "-" + self.user.username