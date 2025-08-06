from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # if we used globally then we can comment this
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

# In settings we initialized the authentication classess to used them globally
# If we want to used seperate then we do this
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]