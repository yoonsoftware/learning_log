from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """새 사용자를 등록합니다."""
    if request.method != 'POST':
        # 빈 등록 폼을 표시 합니다
        form = UserCreationForm()
    else:
        # 완성된 폼을 처리합니다.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 사용자를 로그인 시키고 홈페이지로 보냅니다
            login(request, new_user)
            return redirect('learning_logs:index')

    # 빈 폼이나 에러 폼을 표시합니다
    context = {'form': form}
    return render(request, 'registration/register.html', context)