from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def post_list(request):
    return HttpResponse("list")

@csrf_exempt
def post_detail(request):
    if request.method == "POST":
        id = request.POST.get("id")
        context = {"title":"post1"}
        return render(request, template_name:'blog/post_detail.html', context=context)
    return HttpResponse(error)

