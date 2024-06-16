from django.shortcuts import render, get_object_or_404, redirect
from .models import Good
from .forms import GoodForm

def admin_goods_list(request):
    goods = Good.objects.all()
    return render(request, 'admin/goods_list.html', {'goods': goods})

def admin_good_detail(request, pk):
    good = get_object_or_404(Good, pk=pk)
    return render(request, 'admin/good_detail.html', {'good': good})

def admin_good_new(request):
    if request.method == "POST":
        form = GoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:admin_goods_list')
    else:
        form = GoodForm()
    return render(request, 'admin/good_add.html', {'form': form})

def admin_good_edit(request, pk):
    good = get_object_or_404(Good, pk=pk)
    if request.method == "POST":
        form = GoodForm(request.POST, request.FILES, instance=good)
        if form.is_valid():
            form.save()
            return redirect('main:admin_good_detail', pk=good.pk)
    else:
        form = GoodForm(instance=good)
    return render(request, 'admin/good_edit.html', {'form': form, 'good': good})

def admin_good_delete(request, pk):
    good = get_object_or_404(Good, pk=pk)
    if request.method == "POST":
        good.delete()
        return redirect('main:admin_goods_list')
    return render(request, 'admin/good_delete.html', {'good': good})
