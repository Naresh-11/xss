from .fetcher import fetch_parameters
from .injector import inject_payloads, load_payloads

def test_vulnerabilities(url, payload_files):
    parameters = fetch_parameters(url)
    vulnerabilities = []

    for param_url, method, params in parameters:
        for payload_file, vuln_type in payload_files:
            payloads = load_payloads(payload_file)
            is_vulnerable, payload = inject_payloads(param_url, method, params, payloads)
            if is_vulnerable:
                vulnerabilities.append((param_url, vuln_type, payload))

    return vulnerabilities
