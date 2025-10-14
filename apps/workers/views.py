from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Worker
from .serializers import WorkerListSerializer, WorkerDetailSerializer
from .filters import WorkerFilter
from .import_handler import import_workers_from_excel


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    filterset_class = WorkerFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return WorkerListSerializer
        return WorkerDetailSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [permissions.IsAuthenticatedOrReadOnly()]
        return [permissions.IsAdminUser()]

    @action(
        detail=False, 
        methods=['post'], 
        permission_classes=[permissions.IsAdminUser]
    )
    def import_workers(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response(
                {"error": "No file provided"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        report = import_workers_from_excel(file, request.user)
        return Response(report)