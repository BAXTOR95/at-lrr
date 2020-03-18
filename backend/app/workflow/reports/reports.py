"""Reports module"""

from .AT04 import report_creation as rc_at04


REPORTS_CHOICES = [
    'AT01', 'AT02', 'AT03', 'AT04', 'AT05', 'AT06', 'AT07', 'AT08',
    'AT09', 'AT10', 'AT11', 'AT12', 'AT13', 'AT14', 'AT15', 'AT16',
    'AT17', 'AT18', 'AT19', 'AT20', 'AT21', 'AT23', 'AT24', 'AT25',
    'AT26', 'AT27', 'AT29', 'AT30', 'AT31', 'AT32', 'AT33', 'AT34',
    'AT35', 'AT36', 'AT37', 'AT38',
]


class Reports():
    """Reports Class for every report"""

    at04_obj = rc_at04.ReportCreation()

    def call_method(self, data):
        """Call the method corresponding to the data's report name provided"""

        data_results = {}
        report_name = data['report_name']

        if report_name in REPORTS_CHOICES:

            if report_name == 'AT04':
                data_results = self.at04_obj.create_report(data)

        return data_results
