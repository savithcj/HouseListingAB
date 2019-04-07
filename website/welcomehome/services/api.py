from .models import *

from .serializers import *

from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

class CompanyAPI(ObjectMultipleModelAPIViewSet):
    querylist = [
        {'queryset': Company.objects.all(), 'serializer_class': CompanySerializer},
        {'queryset': CompanyAddress.objects.all(), 'serializer_class': CompanyAddressSerializer},
        {'queryset': Service.objects.all(), 'serializer_class': ServiceSerializer}
    ]