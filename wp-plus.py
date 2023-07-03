import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
import pathlib


script_version = '4.1.0 beta'
window_title = f"WARP-PLUS-CLOUDFLARE By ALIILAPRO (version {script_version})"
os.system('title ' + window_title if os.name ==
          'nt' else 'PS1="\[\e]0;' + window_title + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')
print("            *********************************")
print("            WARP-PLUS-CLOUDFLARE By ALIILAPRO")
print("            *********************************")
print("")
print("[+] ABOUT SCRIPT:")
print("[-] With this script, you can getting unlimited GB on Warp+.")
print(f"[-] Version: {script_version}")
print("--------")
print("[+] THIS SCRIPT CODDED BY ALIILAPRO")
print("[-] SITE: aliilapro.github.io")
print("[-] TELEGRAM: aliilapro")
print("--------")


proxy_url = 'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt'
response = urllib.request.urlopen(proxy_url)
proxy_list = response.read().decode('utf-8').splitlines()

proxy_file = 'proxy.txt'
with open(proxy_file, 'w') as file:
	for proxy in proxy_list:
		file.write(proxy + '\n')

with open(proxy_file, 'r') as file:
	proxy_list = [line.strip() for line in file]


def newID():
	while True:
		referrer = input("[#] Enter the WARP+ ID: ")
		user_input = input(f"[?] Your ID = ({referrer}) is it correct? (y/n):")
		if user_input == "y":
			save_id = input("[?] Do you want to save your ID? (y/n):")
			if save_id == "y":
				with open("referrer.txt", "w") as file:
					file.write(referrer)
				return referrer
			elif save_id == "n":
				return referrer
			else:
				print(f"\"{save_id}\" is not a valid parameter.")
		elif user_input == "n":
			user_input = None
		else:
			print(f"\"{user_input}\" is not a valid parameter.")


def progressBar():
	animation = ["[□□□□□□□□□□]", "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
              "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]"]
	progress_anim = 0
	save_anim = animation[progress_anim % len(animation)]
	percent = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(f"\r[+] Waiting response...  " +
			                 save_anim + f" {percent}%")
			sys.stdout.flush()
			time.sleep(0.075)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write("\r[+] Request completed... [■■■■■■■■■■] 100%")
			break


def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)


def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))
	except Exception as error:
		print(error)

url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'


def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
                    "install_id": install_id,
                    "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                    "referrer": referrer,
                    "warp_enabled": False,
                    "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                    "type": "Android",
                    "locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
                    'Host': 'api.cloudflareclient.com',
                    'Connection': 'Keep-Alive',
                    'Accept-Encoding': 'gzip',
                    'User-Agent': 'okhttp/3.12.1'
             }
		req = urllib.request.Request(url, data, headers)
		response = urllib.request.urlopen(req)
		status_code = response.getcode()
		return status_code
	except Exception as error:
		print("")
		print(error)


if pathlib.Path("referrer.txt").exists():
	while True:
		user_input = input("[?] Do you want to use saved WARP+ ID? (y/n):")
		if user_input == "y":
			with open("referrer.txt", "r") as file:
				referrer = file.read().strip()
			break
		elif user_input == "n":
			referrer = newID()
			break
		else:
			print(f"\"{user_input}\" is not a valid parameter.")
else:
	referrer = newID()

g = 0
b = 0

for proxy_url in proxy_list:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("            *********************************")
	print("            WARP-PLUS-CLOUDFLARE By ALIILAPRO")
	print("            *********************************")
	print("")
	try:
		print(f"[#] Total: Good {g}  Bad {b}")
		sys.stdout.write("\r[+] Sending request...   [□□□□□□□□□□] 0%")
		sys.stdout.flush()
		proxy_handler = urllib.request.ProxyHandler(
			{'http': proxy_url, 'https': proxy_url})
		opener = urllib.request.build_opener(proxy_handler)
		urllib.request.install_opener(opener)
		result = run()
		if result == 200:
			g += 1
			progressBar()
		else:
			b += 1
	except Exception as e:
		print(f"Proxy: {proxy_url} - Error: {str(e)}")
