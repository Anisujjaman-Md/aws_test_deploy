from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
import psutil
from datetime import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import add 


class ServerStatusSerializer(serializers.Serializer):
    server_status = serializers.CharField()
    current_time = serializers.DateTimeField()
    cpu_usage_percent = serializers.ListField(child=serializers.FloatField(), allow_empty=False)
    cpu_cores = serializers.IntegerField()
    total_memory = serializers.IntegerField()
    available_memory = serializers.IntegerField()
    used_memory = serializers.IntegerField()
    memory_usage_percent = serializers.FloatField()
    disk_total = serializers.IntegerField()
    disk_used = serializers.IntegerField()
    disk_free = serializers.IntegerField()
    disk_usage_percent = serializers.FloatField()


class ServerStatus(APIView):
    def get(self, request):
        try:
            cpu_cores = psutil.cpu_count(logical=False)  # Number of physical CPU cores
            total_memory = psutil.virtual_memory().total  # Total available memory in bytes
            available_memory = psutil.virtual_memory().available  # Available memory in bytes
            used_memory = psutil.virtual_memory().used  # Used memory in bytes
            disk_usage = psutil.disk_usage('/')  # Disk usage information for the root directory

            data = {
                'server_status': 'Server is running',
                'current_time': datetime.now().isoformat(),
                'cpu_usage_percent': psutil.cpu_percent(interval=1, percpu=True),
                'cpu_cores': cpu_cores,
                'total_memory': total_memory,
                'available_memory': available_memory,
                'used_memory': used_memory,
                'memory_usage_percent': psutil.virtual_memory().percent,
                'disk_total': disk_usage.total,
                'disk_used': disk_usage.used,
                'disk_free': disk_usage.free,
                'disk_usage_percent': disk_usage.percent,
            }
            serializer = ServerStatusSerializer(data)
            return Response(serializer.data)
        except Exception as e:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)
        


class CeleryTaskView(APIView):
    def get(self, request):
        result = add.delay(4, 4)
        return Response({'task_id': result.id}, status=status.HTTP_200_OK)