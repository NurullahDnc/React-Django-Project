# from django.http import HttpResponse,JsonResponse
# from django.shortcuts import get_object_or_404, render
# from .models import project

# def anasayfa(request):
#     kurslar=project.objects.filter(isActive=1)
#     return render(request,'pages/anasayfa.html',{
#                   'kategoiler':kurslar,
#                   })

# def iletisim(request):
#     cars = project.objects.all()
#     car_list = [{"id": car.id, "title": car.title, "model": car.text} for car in cars]
#     return JsonResponse({"cars": car_list})



# def hakkimizda(request):
#     return render(request,"pages/hakkimizda.html")

# def details(request,slug):
#     detay_=get_object_or_404(project,slug=slug)
#     context={
#         'detay':detay_
#     }
#     return render(request,'pages/details.html',context)