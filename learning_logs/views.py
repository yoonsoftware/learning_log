from django.shortcuts import render, redirect
from django.template import context
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import Http404

# Create your views here.
def index(request):
    """학습 로그 홈페이지"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """주제를 모두 보여 줍니다"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)    

@login_required
def topic(request, topic_id):
    """주제를 하나 표시하고 연관된 항목을 모두 표시 합니다"""
    topic = Topic.objects.get(id=topic_id)
    # 해당 주제가 현재 사용자의 소유인지 확인합니다.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)   

@login_required
def new_topic(request):
    """새 주제를 추가 합니다"""
    if request.method !='POST':
        #데이터가 전송되지 않았으므로 빈 폼을 만듭니다.
        form = TopicForm()
    else:
        #POST 데이터가 전송되었으므로 데이터를 처리합니다.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    #빈 폼이나 에러 폼을 표시합니다.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)           

@login_required
def new_entry(request, topic_id):
    """주제에 연결된 새 항목을 추가합니다"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #데이터가 전송되지 않았으므로 빈 폼을 만듭니다.
        form = EntryForm()
    else:
        #POST 데이터가 전송되었으므로 데이터를 처리합니다
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    #빈 폼이나 에러 폼을 표시합니다.
    context = {'topic': topic, 'form' : form}
    return render(request, 'learning_logs/new_entry.html', context)  

@login_required
def edit_entry(request, entry_id):
    """기존 항목을 수정합니다"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #최초 요청이므로 폼에 현재 항목 내용을 채웁니다.
        form = EntryForm(instance=entry)
    else:
        # POST  데이터가 전송되었으므로 데이터를 처리합니다.
        form = EntryForm(instance=entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry':entry, 'topic':topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)                
