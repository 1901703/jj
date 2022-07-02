from datetime import timezone
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView

from qna.forms import FileUploadForm
from qna.models import Post, Comment


def qna(request):
    postlist=Post.objects.all()
    return render(request, 'qna/qna.html', {'postlist':postlist})

def new_post(request):
    if request.method == 'POST':
        post_title=request.POST['post_title']
        post_image=request.FILES['post_image']
        contents=request.POST['contents']
        post=Post(
            post_title=post_title,
            contents=contents,
            post_image=post_image,
        )
        post.save()
        return render(request, 'qna/posting.html', {'post':post})
    else:
        fileuploadForm=FileUploadForm
        context={
            'fileuploadForm':fileuploadForm,
        }
        return render(request, 'qna/new_post.html', context)

def posting(request, pk):
    post=Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post = post.pk)
    if request.method == "POST":
        comment = Comment()
        comment.post = post
        comment.body = request.POST['body']
        comment.save()
    return render(request, 'qna/posting.html', {'post':post, 'comments':comments})


#기본
def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.post_title=request.POST['post_title']
        post.post_image=request.FILES['post_image']
        post.contents=request.POST['contents']
        post.save()
        return render(request, 'qna/posting.html', {'post':post})
    else:
        fileuploadForm=FileUploadForm
        context={
            'fileuploadForm':fileuploadForm,
        }
        #return render(request, 'qna/update_post.html', {'fileuploadForm':fileuploadForm})
        return render(request, 'qna/update_post.html', context)

def remove_post(request, pk):
    postlist = Post.objects.all()
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return render(request, 'qna/qna.html', {'postlist':postlist})
    return render(request, 'qna/remove_post.html', {'post': post})
    



'''''
def posting(request, pk):
    post=Post.objects.get(pk=pk)

    if request.user == post.writer:
        post_auth = True
    else:
        post_auth = False

    context = {
        'post': post,
        'post_auth': post_auth,
    }
    return render(request, 'qna/posting.html', context)

def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        if (post.writer == request.user or request.user.level == '0'):
            form =FileUploadForm(request.POST, instance=post)
            if form.is_valid():
                post=form.save(commit=False)
                post.save()
                messages.success(request, '수정되었습니다.')
                return render(request, 'qna/posting.html', {'post':post})
    else:
        post=Post.objects.get(id=pk)
        if post.writer == request.user or request.user.level == '0':
            fileuploadForm=FileUploadForm(instance=post)
            context={
                'fileuploadForm':fileuploadForm
            }
            #return render(request, 'qna/update_post.html', {'fileuploadForm':fileuploadForm})
            return render(request, 'qna/update_post.html', context)
        else:
            messages.error(request, '본인 게시글이 아닙니다.')
            return render(request, 'qna/posting.html', {'post': post})

def remove_post(request, pk):
    postlist = Post.objects.all()
    post = Post.objects.get(pk=pk)
    if post.writer == request.user or request.user.level == '0':
        post.delete()
        messages.success(request, "삭제되었습니다.")
        return render(request, 'qna/qna.html', {'postlist':postlist})
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return render(request, 'qna/remove_post.html', {'post': post})

'''''

def detail(request,post_id):
  post_detail = get_object_or_404(Post,pk=post_id)

  return render(request,'detail.html',{'post':post_detail, })









