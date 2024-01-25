#!/usr/bin/python3
"""Log parsing project"""

import sys


def process_line(line, metrics):
    """Parse the line using the provided format"""
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
    except (ValueError, IndexError):
        """Skip the line if the format is not as expected"""
        return metrics

    """Update metrics"""
    metrics['total_size'] += file_size
    metrics['line_count'] += 1
    metrics['status_counts'][status_code] += 1

    return metrics


def print_metrics(metrics):
    """Print the metrics"""
    print(f"Total file size: {metrics['total_size']}")
    for status_code in sorted(metrics['status_counts']):
        count = metrics['status_counts'][status_code]
        print(f"{status_code}: {count}")


def main():
    """Entry point"""
    metrics = {
        'total_size': 0,
        'line_count': 0,
        'status_counts': {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                          405: 0, 500: 0}
    }

    try:
        for line in sys.stdin:
            metrics = process_line(line.strip(), metrics)

            if metrics['line_count'] % 10 == 0:
                print_metrics(metrics)

    except KeyboardInterrupt:
        """Handle keyboard interruption (CTRL + C)"""
        print_metrics(metrics)


if __name__ == "__main__":
    main()
