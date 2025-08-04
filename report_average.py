from tabulate import tabulate


def generate_average_report(stats):
    report_data = []
    for url, data in stats.items():
        count = data['count']
        avg_time = data['total_time'] / count if count else 0
        report_data.append([url, count, round(avg_time, 4)])
    report_data.sort(key=lambda x: x[0])

    return tabulate(
        report_data,
        headers=['handler', 'total', 'avg_response_time'],
        tablefmt='grid'
    )
