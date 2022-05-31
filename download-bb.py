#!/usr/bin/env python3
import json
import os
import requests
import tempfile


def download_from_manifest(path):
    xmlfile = os.path.join(tempfile.gettempdir(), 'version.xml')
    jsonfile = os.path.join(tempfile.gettempdir(), 'version.json')

    if not os.path.exists(xmlfile):
        raw = requests.get("https://apsu.apple.com/version.xml").text
        open(xmlfile, 'w').write(raw)

    if not os.path.exists(jsonfile):
        os.system("plutil -convert json %s -o %s" % (xmlfile, jsonfile))

    for x in json.loads(open(jsonfile, "r").read())['firmwareUpdates']:
        folder = os.path.join(path, x['productID'])
        url = x['location']
        fullname = os.path.join(folder, os.path.basename(url))
        print(fullname)
        os.makedirs(folder, exist_ok=True)
        if not os.path.exists(fullname):
            os.system("curl -o %s %s" % (fullname, url))


download_from_manifest("basebinaries")

# ae54g 6.0 https://support.apple.com/kb/DL550
os.system("curl -L http://download.info.apple.com/Mac_OS_X/061-1574.20041122.ax60f/Express_6.0.basebinary -o basebinaries/102/6.0.basebinary")

# ae54g 6.1.1  https://support.apple.com/kb/DL522
os.system("curl -L https://download.info.apple.com/Mac_OS_X/061-1597.20041220.APTBs/AirPortExpressFW6.1.1.basebinary.zip -o basebinaries/102/6.1.1.basebinary.zip")
os.system("unzip basebinaries/102/6.1.1.basebinary.zip -d basebinaries/102")
os.system("mv basebinaries/102/AirPortExpressFirmware6.1.1.basebinary basebinaries/102/6.1.1.basebinary")
os.system("rm basebinaries/102/*.zip")

# ae54g 6.1 / 5.5 (unencrypted)  https://support.apple.com/kb/DL536
os.system("curl -L https://download.info.apple.com/Mac_OS_X/061-1459.20041115.m41sw/AirPort%204.1%20Update.dmg -o AirPort%204.1%20Update.dmg")
os.system("7z x AirPort%204.1%20Update.dmg")
os.system("gzcat AirPort\ 4.1\ Update/AirPortSW.pkg/Contents/Archive.pax.gz | pax -r")
os.system("cp System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/APBinary3.dat basebinaries/102/5.5.basebinary")
os.system("cp System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/APBinary4.dat basebinaries/102/6.1.basebinary")

# Axtreme 5.5.1 https://support.apple.com/kb/DL521
os.system("curl -L https://download.info.apple.com/Mac_OS_X/061-1581.20041220.PtBSE/AirPortExtremeFW5.5.1.basebinary.zip -o basebinaries/3/5.5.1.basebinary.zip")
os.system("unzip basebinaries/3/5.5.1.basebinary.zip -d basebinaries/3")
os.system("mv basebinaries/3/AirPortExtremeFW\ 5.5.1.basebinary basebinaries/3/5.5.1.basebinary")
#os.system("rm basebinaries/3/*.zip")
