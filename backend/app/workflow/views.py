from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status  # , generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser

from workflow.serializers import WorkflowSerializer

from core.models import Workflow

from workflow.reports.AT04 import report_creation as rc


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
        ).order_by('-report_name').distinct()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class WorkflowView(viewsets.ModelViewSet):
    serializer_class = WorkflowSerializer
    parser_class = (FileUploadParser,)
    queryset = Workflow.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the files for the authenticated user"""
        report_names = self.request.query_params.get('report_name')
        queryset = self.queryset
        if report_names:
            report_names_ids = self._params_to_ints(report_names)
            queryset = queryset.filter(
                resource_name__id__in=report_names_ids)

        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        # if self.action == 'upload_file':
        #     return serializers.FileSerializer

        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='resource')
    def post(self, request, *args, **kwargs):
        """POST method for uploading the file"""

        def user_view(request):
            current_user = request.user
            return current_user.id

        response_data = {
            'id': '',
            'report_path': '',
            'report_name': '',
            'description': '',
            'message': '',
            'last_processing_date': None,
            'data': {},
            'user': None
        }

        request_data = {
            'book_date': None,
            'report_name': '',
            'user': None,
            'encoding': '',
            '_encoding': '',
            '_mutable': True,
        }

        rc_obj = rc.ReportCreation()

        request_data = request.data.copy()
        request_data['user'] = user_view(request)

        workflow_serializer = self.serializer_class(data=request_data)
        if workflow_serializer.is_valid():
            workflow_serializer.save()
        else:
            return Response(workflow_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        data_result = rc_obj.create_report(
            request_data['user'], request_data['book_date'])

        response_data['id'] = workflow_serializer.data['id']
        response_data['report_path'] = data_result['report_path']
        response_data['report_name'] = workflow_serializer.data['report_name']
        response_data['description'] = data_result['description']
        response_data['message'] = 'Successfull'
        response_data['last_processing_date'] = data_result['last_processing_date']
        response_data['user'] = request_data['user']
        response_data['data'] = data_result['data']

        return Response(response_data, status=status.HTTP_201_CREATED)
