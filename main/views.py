from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news_form.html', {'form': form})



def news_update(request, pk):
    news = News.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_form.html', {'form': form})

def news_delete(request, pk):
    if request.method == 'POST':
        News.objects.get(pk=pk).delete()
        return redirect('news_list')
    else:
        news = News.objects.get(pk=pk)
        return render(request, 'news_confirm_delete.html', {'news': news})



def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news_list.html', {'news_list': news_list})