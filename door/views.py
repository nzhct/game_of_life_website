from django.shortcuts import render


def door(request):
    return render(request, 'doortemplates/door.html')

def fail(request):
    return render(request, 'doortemplates/fail.html')