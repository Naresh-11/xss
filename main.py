from scanner.tester import test_vulnerabilities
from scanner.wayback_urls import fetch_wayback_urls
from scanner.katana import fetch_katana_urls
from utils.cli import get_args

def main():
    args = get_args()
    domain = args.target
    output_file = args.output
    verbose = args.verbose

    urls = [domain]
    if args.fetch_urls:
        urls.extend(fetch_wayback_urls(domain))
        if verbose:
            print(f"Found {len(urls)} URLs using Wayback Machine")

    if args.use_katana:
        katana_urls = fetch_katana_urls(domain)
        urls.extend(katana_urls)
        if verbose:
            print(f"Found {len(katana_urls)} URLs using Katana")

    urls = list(set(urls))  # Remove duplicates
    if verbose:
        print(f"Total unique URLs to scan: {len(urls)}")

    payload_files = [
        ("payloads/xss_payloads.txt", "XSS"),
        ("payloads/lfi_payloads.txt", "LFI"),
        ("payloads/sql_payloads.txt", "SQL Injection"),
        ("payloads/cmdi_payloads.txt", "Command Injection"),
        ("payloads/redirect_payloads.txt", "Open Redirect")
    ]

    all_vulnerabilities = []
    for url in urls:
        vulnerabilities = test_vulnerabilities(url, payload_files)
        if vulnerabilities:
            all_vulnerabilities.extend(vulnerabilities)

    if all_vulnerabilities:
        with open(output_file, 'w') as f:
            for vuln in all_vulnerabilities:
                output = f"Vulnerability Found: {vuln[1]} in {vuln[0]} with payload {vuln[2]}"
                print(f"\033[92m{output}\033[0m")
                f.write(output + "\n")
    else:
        print(f"\033[91mNo vulnerabilities found.\033[0m")

if __name__ == "__main__":
    main()
