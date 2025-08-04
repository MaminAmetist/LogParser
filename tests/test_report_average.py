from pytest import main
from report_average import generate_average_report


def test_generate_average_report_basic():
    stats = {
        "/api/a": {"count": 2, "total_time": 0.4},
        "/api/b": {"count": 1, "total_time": 0.2},
    }

    result = generate_average_report(stats)
    assert "/api/a" in result
    assert "0.2" in result  # avg 0.4 / 2
    assert "/api/b" in result
    assert "0.2" in result  # avg 0.2 / 1


if __name__ == '__main__':
    main(['-v'])
