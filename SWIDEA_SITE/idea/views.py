from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Idea, DevTool, IdeaStar
from .forms import IdeaForm, DevToolForm

def idea_list(request):
    sort_by = request.GET.get('sort', 'star')  # 기본 정렬을 찜하기순으로 설정
    
    if sort_by == 'star':
        ideas = Idea.objects.annotate(
            star_count=Count('ideastar')
        ).order_by('-star_count', '-id')
    elif sort_by == 'name':
        ideas = Idea.objects.all().order_by('title')
    elif sort_by == 'created':
        ideas = Idea.objects.all().order_by('id')
    elif sort_by == 'latest':
        ideas = Idea.objects.all().order_by('-id')
    else:
        ideas = Idea.objects.all().order_by('-id')
    
    # 더미 사용자 ID 사용 (로그인 기능이 없으므로)
    user_id = 1
    user_starred_ideas = list(IdeaStar.objects.filter(user_id=user_id).values_list('idea_id', flat=True))
    
    # 페이지네이션
    paginator = Paginator(ideas, 4)  # 페이지당 4개 아이디어
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'idea/idea_list.html', {
        'page_obj': page_obj,
        'sort_by': sort_by,
        'user_starred_ideas': user_starred_ideas,
    })

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            messages.success(request, '아이디어가 성공적으로 등록되었습니다.')
            return redirect('idea:idea_detail', idea_id=idea.id)
    else:
        form = IdeaForm()
    
    return render(request, 'idea/idea_form.html', {
        'form': form, 
        'title': '아이디어 등록',
    })

def idea_detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    
    # 더미 사용자 ID 사용 (로그인 기능이 없으므로)
    user_id = 1
    is_starred = IdeaStar.objects.filter(idea=idea, user_id=user_id).exists()
    
    return render(request, 'idea/idea_detail.html', {
        'idea': idea,
        'is_starred': is_starred,
    })

def idea_edit(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            messages.success(request, '아이디어가 성공적으로 수정되었습니다.')
            return redirect('idea:idea_detail', idea_id=idea.id)
    else:
        form = IdeaForm(instance=idea)
    
    return render(request, 'idea/idea_form.html', {'form': form, 'title': '아이디어 수정'})

def idea_delete(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    idea.delete()
    messages.success(request, '아이디어가 성공적으로 삭제되었습니다.')
    return redirect('idea:idea_list')

def devtool_list(request):
    devtools = DevTool.objects.all().order_by('name')
    paginator = Paginator(devtools, 10)  # 페이지당 10개 항목
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'idea/devtool_list.html', {'page_obj': page_obj})

def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            devtool = form.save()
            messages.success(request, '개발툴이 성공적으로 등록되었습니다.')
            return redirect('idea:devtool_detail', devtool_id=devtool.id)
    else:
        form = DevToolForm()
    
    return render(request, 'idea/devtool_form.html', {
        'form': form, 
        'title': '개발툴 등록',
    })

def devtool_detail(request, devtool_id):
    devtool = get_object_or_404(DevTool, id=devtool_id)
    
    return render(request, 'idea/devtool_detail.html', {
        'devtool': devtool,
    })

def devtool_edit(request, devtool_id):
    devtool = get_object_or_404(DevTool, id=devtool_id)
    
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            devtool = form.save()
            messages.success(request, '개발툴이 성공적으로 수정되었습니다.')
            return redirect('idea:devtool_detail', devtool_id=devtool.id)
    else:
        form = DevToolForm(instance=devtool)
    
    return render(request, 'idea/devtool_form.html', {'form': form, 'title': '개발툴 수정'})

def devtool_delete(request, devtool_id):
    devtool = get_object_or_404(DevTool, id=devtool_id)
    devtool.delete()
    messages.success(request, '개발툴이 성공적으로 삭제되었습니다.')
    return redirect('idea:devtool_list')

def toggle_star(request, idea_id):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, id=idea_id)
        
        # 더미 사용자 ID 사용 (로그인 기능이 없으므로)
        user_id = 1
        
        # 찜 상태 토글
        try:
            star = IdeaStar.objects.get(idea=idea, user_id=user_id)
            star.delete()
        except IdeaStar.DoesNotExist:
            IdeaStar.objects.create(idea=idea, user_id=user_id)
        
        # 원래 페이지로 리다이렉트
        return redirect(request.META.get('HTTP_REFERER', 'idea:idea_list'))
    
    return redirect('idea:idea_list')

def change_interest(request, idea_id, action):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, id=idea_id)
        
        if action == 'up':
            idea.interest += 1
        elif action == 'down' and idea.interest > 0:
            idea.interest -= 1
        
        idea.save()
        
        # 원래 페이지로 리다이렉트
        return redirect(request.META.get('HTTP_REFERER', 'idea:idea_list'))
    
    return redirect('idea:idea_list')