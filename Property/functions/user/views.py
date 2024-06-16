from django.shortcuts import render, get_object_or_404
from main.models import Good

def user_goods_list(request):
    goods = Good.objects.all()
    return render(request, 'functions/user_goods_list.html', {'goods': goods})

def user_good_detail(request, pk):
    good = get_object_or_404(Good, pk=pk)
    return render(request, 'functions/user_good_detail.html', {'good': good})
