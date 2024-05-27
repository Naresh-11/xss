import subprocess
import os

def fetch_katana_urls(domain):
    output_file = "katana_urls.txt"
    command = f"katana -u {domain} -silent -o {output_file}"
    subprocess.run(command, shell=True, check=True)
    
    with open(output_file, 'r') as file:
        urls = [line.strip() for line in file]
    
    os.remove(output_file)
    return urls
