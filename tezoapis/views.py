from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Employee
from .serializers import EmployeeSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


from django_filters import rest_framework
from .models import Employee

class EmployeeFilter(rest_framework.FilterSet):
    class Meta:
        model = Employee
        fields = {
            'empid': ['exact', 'icontains'],
            'firstname': ['exact', 'icontains' , 'istartswith'],
            'lastname': ['exact', 'icontains' , 'istartswith'],
            'DOB': ['exact', 'year', 'month', 'day'],
            'emailid': ['exact', 'icontains' , 'istartswith'],
            'mobile': ['exact'],
            'joining': ['exact', 'year', 'month', 'day'],
            'location': ['exact', 'icontains'],
            'jobtitle': ['exact', 'icontains'],
            'Department': ['exact', 'icontains'],
            'AssignManager': ['exact', 'icontains'],
            'AssignProject': ['exact', 'icontains'],
            'profilepath': ['exact', 'icontains'],
            'status': ['exact', 'icontains'],
        }


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = EmployeeFilter
    search_fields = ['empid', 'firstname', 'lastname']
    ordering_fields = ['empid', 'firstname', 'lastname', 'DOB', 'emailid', 'mobile', 'joining', 'location', 'jobtitle', 'Department', 'AssignManager', 'AssignProject', 'profilepath', 'status']
    pagination_class = StandardResultsSetPagination