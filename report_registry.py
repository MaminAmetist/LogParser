from report_average import generate_average_report

REPORTS = {
    'average': generate_average_report
}


def get_report(name):
    return REPORTS.get(name)
