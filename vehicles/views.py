from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import Vehicle
from django import forms
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView



class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields =  '__all__'


class VehicleList(View):
    def get(self, request):
        rooms =  list(Vehicle.objects.all().values())
        data =  dict()
        data['rooms'] = rooms
        return JsonResponse(data)


class VehicleDetail(View):
    def get(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        data =  dict()
        data['vehicles'] = model_to_dict(vehicle)
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class  VehicleCreate(CreateView):
    def  post(self, request):
        data =  dict()
        form = VehicleForm(request.POST)
        if form.is_valid():
            room = form.save()
            data['vehicles'] = model_to_dict(room)
        else:
            data['error'] =  "form not valid!"
        return JsonResponse(data)


class  VehicleUpdate(View):
    def  post(self, request, pk):
        data =  dict()
        room = Vehicle.objects.get(pk=pk)
        form = VehicleForm(instance=room, data=request.POST)
        if form.is_valid():
            room = form.save()
            data['room'] = model_to_dict(room)
        else:
            data['error'] =  "form not valid!"
        return JsonResponse(data)


class  VehicleDelete(View):
    def  post(self, request, pk):
        data =  dict()
        room = Vehicle.objects.get(pk=pk)
        if room:
            room.delete()
            data['message'] =  "Vehicle deleted!"
        else:
            data['message'] =  "Error!"
        return JsonResponse(data)
