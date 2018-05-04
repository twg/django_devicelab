import datetime
from rest_framework import mixins
from rest_framework import generics
from api.models import Device, Employee
from api.serializers import DeviceSerializer, EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class DeviceListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class EmployeeListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.filter(active=True)
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@api_view(['GET'])
def checkout_device(request):
    employee_id = request.GET.get('employee_id')
    device_id = request.GET.get('device_id')
    if not employee_id or not device_id:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    employee = Employee.objects.filter(id=employee_id).first()
    device = Device.objects.filter(id=device_id).first()

    if not employee or not device:
        return Response('fuck right off', status=status.HTTP_400_BAD_REQUEST)

    # is device available?
    if (Ledger.objects.filter(device=device, return_date=None).count() > 0):
        return Response('device already checked out')

    ledger_entry = Ledger.objects.create(
        employee=employee, device=device, checkout_date=datetime.datetime.now()
    )

    return Response('device checked out', status=status.HTTP_200_OK)    
    

