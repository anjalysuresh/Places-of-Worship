from django.shortcuts import render, redirect
from .models import Category, GroupCategory
from Community.models import Community, CommunityTypes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.

def create_group_category(request, group, community):
	categoryid = request.POST['grpcategory']
	category = Category.objects.get(pk=categoryid)
	GroupCategory.objects.create(category=category, group=group, community=community)

def category_view(request, catid, commid):
	category = Category.objects.get(pk=catid)
	community = Community.objects.get(pk=commid)
	groupscategory = GroupCategory.objects.filter(category=category, community=community)
		
	page = request.GET.get('page', 1)
	paginator = Paginator(list(groupscategory), 4)
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
		groups = paginator.page(1)
	except EmptyPage:
		groups = paginator.page(paginator.num_pages)

	return render(request, 'categoryview.html',{'groups':groups, 'category':category, 'community':community})

def update_group_category(request, group):
	groupcategory = GroupCategory.objects.get(group=group)
	categoryid = request.POST['grpcategory']
	category = Category.objects.get(pk=categoryid)
	groupcategory.category = category
	groupcategory.save()

def create_category(request):
	if request.user.is_superuser:
		if request.method == 'POST':
			name = request.POST['name']
			desc = request.POST['desc']
			commtype = request.POST['commtype']
			image = request.FILES['image']
			commtype = CommunityTypes.objects.get(pk=commtype)
			Category.objects.create(name=name, desc=desc, commtype=commtype, image=image)
			messages.success(request, name + ' category successfully created')
			return redirect('create_category')
		else:
			commtype = CommunityTypes.objects.all()
			return render(request, 'create_category.html', {'commtype':commtype})
	else:
		return redirect('home')