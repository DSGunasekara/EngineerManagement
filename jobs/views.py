from django.db.models import manager
from django.shortcuts import render, redirect
from .models import Job
from users.models import Profile
from .forms import JobAddForm
from django.contrib import messages


def engineers(request):
    context = {
        'engineers': Profile.objects.filter(role="field_engineer")
    }
    return render(request, 'engineer/home.html', context)


def jobs(request):
    context = {
        'jobs': Job.objects.all()
    }
    return render(request, 'engineer/jobs.html', context)


def add_job(request):
    if request.method == 'POST':
        form = JobAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job Created!')
            return redirect('profile')
    else:
        form = JobAddForm()
    return render(request, 'engineer/addJob.html', {'form': form})
