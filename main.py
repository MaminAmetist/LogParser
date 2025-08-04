import argparse
from parser import parse_logs
from report_registry import get_report


def main():
    parser = argparse.ArgumentParser(description='Log report generator')
    parser.add_argument('--file', nargs='+', required=True, help='Path to log file(s)')
    parser.add_argument('--report', required=True, help='Report name')
    parser.add_argument('--date', required=False, help='Filter by date YYYY-MM-DD')

    args = parser.parse_args()

    stats = parse_logs(args.file, args.date)

    try:
        report_func = get_report(args.report)
        report = report_func(stats)
        print(report)
    except Exception as exc:
        print(f'Отчёт {args.report} не найден: {exc}')


if __name__ == "__main__":
    main()
