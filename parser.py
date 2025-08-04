import json
from collections import defaultdict


def parse_logs(files, date_filter=None):
    stats = defaultdict(lambda: {'count': 0, 'total_time': 0.0})
    try:
        for file_path in files:
            with open(file_path, encoding='utf-8') as f:
                for line in f:
                    try:
                        log = json.loads(line.strip())
                        if date_filter:
                            log_date = log['@timestamp'].split('T')[0]
                            if log_date != date_filter:
                                continue
                        url = log.get('url')
                        response_time = log.get('response_time', 0.0)
                        stats[url]['count'] += 1
                        stats[url]['total_time'] += response_time
                    except (json.JSONDecodeError, KeyError):
                        continue
    except Exception as exc:
        print(f'Файл {files} не найден: {exc}.')

    return stats
