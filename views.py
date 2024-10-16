from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator
def add_comment(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, id=blog_id)
        comment = Comment.objects.create(
            blog=blog,
            user=request.user,
            content=request.POST['content']
        )
        return redirect('blog_detail', blog_id=blog.id)


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 5)  # Show 5 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})
