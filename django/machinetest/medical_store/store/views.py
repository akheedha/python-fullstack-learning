from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine
from .forms import MedicineForm, SignupForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# 🔐 SIGNUP VIEW
def signup_view(request):
    form = SignupForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('medicine_list')

    return render(request, 'signup.html', {'form': form})


# 🚪 LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('login')


# ➕ ADD MEDICINE (MAX 5 LIMIT)
@login_required
def add_medicine(request):
    count = Medicine.objects.filter(user=request.user).count()

    if count >= 5:
        return render(request, 'error.html', {
            'message': 'Limit reached! Only 5 medicines allowed.'
        })

    form = MedicineForm(request.POST or None)

    if form.is_valid():
        med = form.save(commit=False)
        med.user = request.user
        med.save()
        return redirect('medicine_list')

    return render(request, 'add_medicine.html', {'form': form})


# 📋 LIST + SEARCH + PAGINATION
@login_required
def medicine_list(request):
    query = request.GET.get('q')

    medicines = Medicine.objects.filter(user=request.user)

    if query:
        medicines = medicines.filter(name__icontains=query)

    paginator = Paginator(medicines, 3)  # 3 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'medicine_list.html', {
        'page_obj': page_obj
    })


# ✏️ EDIT MEDICINE
@login_required
def edit_medicine(request, id):
    med = get_object_or_404(Medicine, id=id, user=request.user)

    form = MedicineForm(request.POST or None, instance=med)

    if form.is_valid():
        form.save()
        return redirect('medicine_list')

    return render(request, 'add_medicine.html', {'form': form})


# 🗑️ DELETE MEDICINE
@login_required
def delete_medicine(request, id):
    med = get_object_or_404(Medicine, id=id, user=request.user)
    med.delete()
    return redirect('medicine_list')