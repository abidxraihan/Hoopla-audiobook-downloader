# -*- coding: utf-8 -*-
# Module: KEYS-L3
# Created on: 11-10-2021
# Authors: -∞WKS∞-
# Version: 1.1.0

# Modified by: CrymanChen
# Modified on: April 7, 2023

import base64, requests, sys, xmltodict
import headers

# Added a third-party library pyperclip, the purpose is to quickly copy the key (sometimes multiple keys) to the clipboard
import pyperclip
from pywidevine.L3.cdm import cdm, deviceconfig
from base64 import b64encode
from pywidevine.L3.getPSSH import get_pssh
from pywidevine.L3.decrypt.wvdecryptcustom import WvDecrypt

pssh = sys.argv[1]
lic_url = sys.argv[2]


def WV_Function(pssh, lic_url, cert_b64=None):
    wvdecrypt = WvDecrypt(
        init_data_b64=pssh,
        cert_data_b64=cert_b64,
        device=deviceconfig.device_android_generic,
    )
    widevine_license = requests.post(
        url=lic_url, data=wvdecrypt.get_challenge(), headers=headers.headers
    )
    # Explanation:
    # Line 24 needs to be adjusted according to different License types, it is not fixed, for example:
    # ① Check the cURL of the License request, convert it to a Python-compatible statement, if the last line is like this:
    # response = requests.post('Here is the License URL', headers=headers, data=data,)
    # Then line 24 does not need to be modified, just copy the headers to headers.py, note that the content type (Content-Type) of the message body is sometimes not application/x-www-form-urlencoded
    # ② If the last line is like this:
    # response = requests.post('Here is the License URL', headers=headers, data=data, params=params)
    # Then you need to add parameters (params), the general solution is to add ", json=params" after "headers=headers.headers", so that the parameters are sent in json format, otherwise it usually returns HTTP 400/403/502
    license_b64 = b64encode(widevine_license.content)
    wvdecrypt.update_license(license_b64)
    Correct, keyswvdecrypt = wvdecrypt.start_process()
    if Correct:
        return Correct, keyswvdecrypt


correct, keys = WV_Function(pssh, lic_url)

print()
for key in keys:
    print("--key " + key)

# Create a key_string string, so that all keys are transformed as follows: ① Add the prefix "--key" ② Make each key with the prefix connected with a space (convenient for one-click copying when there are multiple keys)
key_string = " ".join([f"--key {key}" for key in keys])
# Use the imported pyperclip library to copy the key_string string to the clipboard, saving the trouble of manually selecting "--key {key}", copying, and pasting
pyperclip.copy(key_string)
