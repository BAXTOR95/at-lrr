# from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status  # , generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser
# from rest_framework.views import APIView

from upload.serializers import FileSerializer

from core.models import File

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

    def post(self, request, *args, **kwargs):
        """POST method for uploading the file"""
        file_serializer = self.serializer_class(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            # print('URL: ', file_serializer.url)
            print('Path: ', file_serializer.data['file'])
            # print('User: ', request.user)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(methods=['POST'], detail=True, url_path='upload-file')
    # def upload_file(self, request):
    #     """Upload file"""
    #     file_serializer = self.serializer_class(data=request.data)

    #     if file_serializer.is_valid():
    #         file_serializer.save()
    #         # print('URL: ', file_serializer.url)
    #         print('Path: ', file_serializer.data['file'])
    #         # print('User: ', request.user)
    #         return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
