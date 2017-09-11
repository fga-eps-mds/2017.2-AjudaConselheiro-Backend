from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from counselors.models import Counselor
from counselors.permissions import IsCounselorOwner
from counselors.serializers import CounselorSerializer

class CounselorViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Counselor.objects.all()
    serializer_class = CounselorSerializer

    def get_permissions(self):
        if (self.request.method in permissions.SAFE_METHODS):
            return (permissions.AllowAny(),)

        if (self.request.method == 'POST'):
            return (permissions.AllowAny(),)
        
        return (permissions.IsAuthenticated(), IsCounselorOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)

        if (serializer.is_valid()):
            Counselor.objects.create_user(**serializer.validated_data)
            
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(
        {
            'status': 'Bad request',
            'message': 'Counselor could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)