from django.shortcuts import render
from .models import Post, Like, Comment
from django.http import JsonResponse

def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    # 댓글 닉네임 가공: 첫 번째 luckyclody, 두 번째 hamzzi, 나머지는 익명
    for post in posts:
        for i, comment in enumerate(post.comments.all()):
            if comment.author is None:
                if i == 0:
                    comment.display_name = 'luckyclody'
                elif i == 1:
                    comment.display_name = 'hamzzi'
                else:
                    comment.display_name = '익명'
            else:
                comment.display_name = comment.author.username
    return render(request, 'pirostagram/feed.html', {'posts': posts, 'user': request.user})

def like_toggle(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        post = Post.objects.get(id=post_id)
        user = request.user if request.user.is_authenticated else None

        liked = Like.objects.filter(post=post, user=user)
        if liked.exists():
            liked.delete()
            liked_status = False
        else:
            Like.objects.create(post=post, user=user)
            liked_status = True

        like_count = post.likes.count()
        return JsonResponse({"liked": liked_status, "like_count": like_count})
    return JsonResponse({"error": "Invalid request"}, status=400)

def comment_add(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        content = request.POST.get("content")
        post = Post.objects.get(id=post_id)
        user = request.user if request.user.is_authenticated else None

        comment = Comment.objects.create(post=post, author=user, content=content)
        return JsonResponse({
            "id": comment.id,
            "author": comment.author.username if comment.author else "익명",
            "content": comment.content,
            "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M")
        })
    return JsonResponse({"error": "Invalid request"}, status=400)

def comment_delete(request):
    if request.method == "POST":
        comment_id = request.POST.get("comment_id")
        try:
            comment = Comment.objects.get(id=comment_id)
            # 익명 댓글은 누구나 삭제 가능, 유저 댓글은 본인만 삭제
            if comment.author is None or (request.user.is_authenticated and comment.author == request.user):
                comment.delete()
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "error": "권한이 없습니다."})
        except Comment.DoesNotExist:
            return JsonResponse({"success": False, "error": "댓글이 존재하지 않습니다."})
    return JsonResponse({"error": "Invalid request"}, status=400)