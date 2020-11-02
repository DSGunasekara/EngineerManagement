from django.shortcuts import render, redirect
from jobs.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST, prefix="user")
        p_form = ProfileCreateForm(request.POST, prefix="profile")
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(
                request, f'Account was created! You can now log in')
            return redirect('login')
    else:
        u_form = UserRegisterForm(prefix="user")
        p_form = ProfileCreateForm(prefix="profile")
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your account has been updated successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/updateProfile.html', context)
