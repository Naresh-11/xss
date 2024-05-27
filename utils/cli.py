import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Vulnerability Scanner Tool")
    parser.add_argument("-t", "--target", required=True, help="Target domain or URL to scan")
    parser.add_argument("-o", "--output", help="Output file to save results", default="output.txt")
    parser.add_argument("--fetch-urls", action="store_true", help="Fetch URLs using Wayback Machine")
    parser.add_argument("--use-katana", action="store_true", help="Fetch URLs using Katana")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
    return parser.parse_args()
