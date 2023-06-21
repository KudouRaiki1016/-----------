from django.shortcuts import render

def top_page(request):
    context = {}
    return render(request, 'points_save/top_page.html', context)