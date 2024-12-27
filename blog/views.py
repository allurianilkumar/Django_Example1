from django.shortcuts import render

def index(request):
    # Logic to display all blog posts
    return render(request, 'blog/index.html')

def detail(request, post_id):
    # Logic to display a specific blog post by its ID
    return render(request, 'blog/detail.html', {'post_id': post_id})

def comments(request, post_id):
    # Logic to display comments for a specific post
    return render(request, 'blog/comments.html', {'post_id': post_id})
