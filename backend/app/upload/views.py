from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status  # , generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser

import copy
# from rest_framework.views import APIView

from upload.serializers import FileSerializer

from core.models import File

from .reports.reports import Reports

# import pandas as pd


class BaseFileAttr(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin):
    """Base viewset for user owned file attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(file__isnull=False)

        return queryset.filter(
            user=self.request.user
        ).order_by('-resource_name').distinct()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class FileUploadView(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    parser_class = (FileUploadParser,)
    queryset = File.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the files for the authenticated user"""
        resource_names = self.request.query_params.get('resource_name')
        queryset = self.queryset
        if resource_names:
            resource_names_ids = self._params_to_ints(resource_names)
            queryset = queryset.filter(
                resource_name__id__in=resource_names_ids)

        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Return appropiate serializer class"""
        # if self.action == 'upload_file':
        #     return serializers.FileSerializer

        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='resource')
    def post(self, request, *args, **kwargs):
        """POST method for uploading the file"""

        files = []
        data = []

        def user_view(request):
            current_user = request.user
            return current_user.id

        response_data = {
            'id': None,
            'report_name': None,
            'resource_name': None,
            'file': None,
            'user': None,
            'data': ''
        }

        request_data = {
            'file': {},
            'report_name': '',
            'resource_name': '',
            'encoding': '',
            '_encoding': '',
            '_mutable': True,
            '__len__': 0,
        }

        rc_obj = Reports()

        if request.FILES:
            if len(request.FILES.getlist('file')) > 0:
                for file in request.FILES.getlist('file'):
                    request_data = request.data
                    request_data['user'] = user_view(request)
                    request_data['file'] = file
                    # files.append(request_data.copy())
                    files.append(copy.copy(request_data))
            else:
                pass

        for file in files:
            file_serializer = self.serializer_class(data=file)
            if file_serializer.is_valid():
                file_serializer.save()
                data.append(file_serializer.data.copy())
            else:
                return Response(file_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        data_result = rc_obj.call_method(data)

        response_data['id'] = file_serializer.data['id']
        response_data['report_name'] = file_serializer.data['report_name']
        response_data['resource_name'] = file_serializer.data['resource_name']
        response_data['file'] = data_result['out_path']
        response_data['user'] = request.user.soeid
        response_data['data'] = data_result['data']

        return Response(response_data, status=status.HTTP_201_CREATED)

        # file_serializer = self.serializer_class(data=request.data)

        # if file_serializer.is_valid():
        #     file_serializer.save()
        #     out_path = dp_obj.call_method(file_serializer.data)
        #     response_data['id'] = file_serializer.data['id']
        #     response_data['resource_name'] = file_serializer.data['resource_name']
        #     response_data['file'] = out_path
        #     response_data['user'] = file_serializer.data['user']
        #     return Response(response_data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(methods=['POST'], detail=True, url_path='resource')
    # def upload_file(self, request):
    #     """Upload file"""
    #     file_serializer = self.serializer_class(data=request.data)

    #     if file_serializer.is_valid():
    #         file_serializer.save()
    #         # print('URL: ', file_serializer.url)
    #         print('Path: ', file_serializer.data['file'])
    #         print('Data: ', file_serializer.data)
    #         # print('User: ', request.user)
    #         return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
