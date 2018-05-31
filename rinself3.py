# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, subprocess

ririn = LINE("EtZdCJUsZytwdEcoXea1.rCWrtE6UfnNgoLxTqXzdSq.5CEzXyh1pnynfuaOyg4mwnShvaKWj6f9g2QnC2ipnmU=")
#ririn = LINE("TOKENMU")

ririnMid = ririn.profile.mid
ririnProfile = ririn.getProfile()
ririnSettings = ririn.getSettings()
ririnPoll = OEPoll(ririn)
botStart = time.time()

msg_dict = {}

wait = {
    "autoAdd": True,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "autoRespon": True,
    "autoResponPc": False,
    "autoJoinTicket": True,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "leaveRoom": True,
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "Protectcancel": True,
    "Protectgr": True,
    "Protectinvite": True,
    "Protectjoin": False,
    "setKey": False,
    "sider": False,
    "unsendMessage": True
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ DNA BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════")
    
wait["myProfile"]["displayName"] = ririnProfile.displayName
wait["myProfile"]["statusMessage"] = ririnProfile.statusMessage
wait["myProfile"]["pictureStatus"] = ririnProfile.pictureStatus
coverId = ririn.getProfileDetail()["result"]["objectId"]
wait["myProfile"]["coverId"] = coverId

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    ririn.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                ririn.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@dee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    ririn.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if wait["setKey"] == True:
        if pesan.startswith(wait["keyCommand"]):
            cmd = pesan.replace(wait["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def helpmessage():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpMessage =   "╔════════════════════╗" + "\n" + \
                    "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "    ✪ 🅷🅴🅻🅿 🅼🅴🆂🆂🅰🅶🅴 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ʜᴇʟᴘ " + "\n" + \
                    "╠❂➣ " + key + "ᴛᴛs " + "\n" + \
                    "╠❂➣ " + key + "ᴛʀᴀɴsʟᴀᴛᴇ " + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "               ✪ 🆂🆃🅰🆃🆄🆂 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ʀᴇsᴛᴀʀᴛ" + "\n" + \
                    "╠❂➣ " + key + "ʀᴜɴᴛɪᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "sᴘ" + "\n" + \
                    "╠❂➣ " + key + "sᴘᴇᴇᴅ" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴀᴛᴜs" + "\n" + \
                    "╠❂➣ ᴍʏᴋᴇʏ" + "\n" + \
                    "╠❂➣ sᴇᴛᴋᴇʏ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "           ✪ 🆂🅴🆃🆃🅸🅽🅶🆂 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏᴀᴅᴅ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏᴊᴏɪɴ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏᴊᴏɪɴᴛɪᴄᴋᴇᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʟᴇᴀᴠᴇ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇᴀᴅ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇsᴘᴏɴ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴀᴜᴛᴏʀᴇsᴘᴏɴᴘᴄ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴄᴏɴᴛᴀᴄᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴘᴏsᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋsᴛɪᴄᴋᴇʀ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴜɴsᴇɴᴅᴄʜᴀᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                    ✪ 🆂🅴🅻🅵 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ʙᴀᴄᴋᴜᴘᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇʙɪᴏ:「ǫᴜᴇʀʏ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇɴᴀᴍᴇ:「ǫᴜᴇʀʏ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʟᴏɴᴇᴘʀᴏғɪʟᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇᴘɪᴄᴛᴜʀᴇᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴍɪᴅ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏɴᴀᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏʙɪᴏ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴘɪᴄᴛᴜʀᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "ᴍʏᴄᴏᴠᴇʀ" + "\n" + \
                    "╠❂➣ " + key + "ʀᴇsᴛᴏʀᴇᴘʀᴏғɪʟᴇ" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴄᴏɴᴛᴀᴄᴛ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴍɪᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟɴᴀᴍᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟʙɪᴏ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴘɪᴄᴛᴜʀᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "sᴛᴇᴀʟᴄᴏᴠᴇʀ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "             ✪ 🆂🅿🅴🅲🅸🅰🅻 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ʟᴜʀᴋɪɴɢ" + "\n" + \
                    "╠❂➣ " + key + "ʟᴜʀᴋɪɴɢ「ᴏɴ/ᴏғғ/ʀᴇsᴇᴛ」" + "\n" + \
                    "╠❂➣ " + key + "ᴍᴇɴᴛɪᴏɴ" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄᴀᴅᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄᴅᴇʟ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴍɪᴍɪᴄʟɪsᴛ" + "\n" + \
                    "╠❂➣ " + key + "sɪᴅᴇʀ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                 ✪ 🅶🆁🅾🆄🅿 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴀɴɢᴇɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴄʀᴇᴀᴛᴏʀ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘɪᴅ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘɴᴀᴍᴇ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴛɪᴄᴋᴇᴛ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴛɪᴄᴋᴇᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘᴍᴇᴍʙᴇʀʟɪsᴛ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘɪɴғᴏ" + "\n" + \
                    "╠❂➣ " + key + "ɢʀᴏᴜᴘʟɪsᴛ" + "\n" + \
                    "╠❂➣ " + key + "ɪɴᴠɪᴛᴇɢᴄ「ᴀᴍᴏᴜɴᴛ」" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                  ✪ 🅼🅴🅳🅸🅰 ✪" + "\n" + \
                    "╠════════════════════╝" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴅᴀᴛᴇ「ᴅᴀᴛᴇ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋʟᴏᴄᴀᴛɪᴏɴ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴘʀᴀʏᴛɪᴍᴇ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴡᴇᴀᴛʜᴇʀ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
                    "╠❂➣ " + key + "ᴄʜᴇᴄᴋᴡᴇʙsɪᴛᴇ「ᴜʀʟ」" + "\n" + \
                    "╠❂➣ " + key + "ɪɴsᴛᴀɪɴғᴏ 「ᴜsᴇʀɴᴀᴍᴇ」" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴀʀᴄʜɪᴍᴀɢᴇ 「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴀʀᴄʜʟʏʀɪᴄ 「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴀʀᴄʜᴍᴜsɪᴄ 「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╠❂➣ " + key + "sᴇᴀʀᴄʜʏᴏᴜᴛᴜʙᴇ「sᴇᴀʀᴄʜ」" + "\n" + \
                    "╠════════════════════╗" + "\n" + \
                    "                ᴄʀᴇᴅɪᴛs ʙʏ : ᴅ̶ᴇ̶ᴇ̶ ✯" + "\n" + \
                    "╚════════════════════╝" + "\n" + \
                    "╔════════════════════╗" + "\n" + \
                    "                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰" + "\n" + \
                    "╚════════════════════╝"
    return helpMessage

def helptexttospeech():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "          ◄]·✪·ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ·✪·[►" + "\n" + \
                        "╠════════════════════╝ " + "\n" + \
                        "╠❂➣ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "╠❂➣ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜ : ᴄʜɪɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜʏᴜᴇ : ᴄʜɪɴᴇsᴇ (ᴄᴀɴᴛᴏɴᴇsᴇ)" + "\n" + \
                        "╠❂➣ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴀᴜ : ᴇɴɢʟɪsʜ (ᴀᴜsᴛʀᴀʟɪᴀ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴜᴋ : ᴇɴɢʟɪsʜ (ᴜᴋ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴜs : ᴇɴɢʟɪsʜ (ᴜs)" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ (ᴄᴀᴍʙᴏᴅɪᴀɴ)" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇsᴇs : sᴘᴀɴɪsʜ (sᴘᴀɪɴ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇsᴜs : sᴘᴀɴɪsʜ (ᴜs)" + "\n" + \
                        "╠❂➣ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "╠❂➣ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "╠════════════════════╗" + "\n" + \
                        "               ᴄʀᴇᴅɪᴛs ʙʏ : ©ᴅ̶ᴇ̶ᴇ̶ ✯" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "ᴄᴏɴᴛᴏʜ : " + key + "sᴀʏ-ɪᴅ ʀɪʀɪɴ"
    return helpTextToSpeech

def helptranslate():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTranslate = "╔════════════════════╗" + "\n" + \
                        "                     ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "             ◄]·✪·ᴛʀᴀɴsʟᴀᴛᴇ·✪·[►" + "\n" + \
                        "╠════════════════════╝" + "\n" + \
                        "╠❂➣ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "╠❂➣ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀᴍ : ᴀᴍʜᴀʀɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀᴢ : ᴀᴢᴇʀʙᴀɪᴊᴀɴɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴜ : ʙᴀsǫᴜᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʙᴇ : ʙᴇʟᴀʀᴜsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ʙs : ʙᴏsɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɢ : ʙᴜʟɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴇʙ : ᴄᴇʙᴜᴀɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ɴʏ : ᴄʜɪᴄʜᴇᴡᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜᴄɴ : ᴄʜɪɴᴇsᴇ (sɪᴍᴘʟɪғɪᴇᴅ)" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜᴛᴡ : ᴄʜɪɴᴇsᴇ (ᴛʀᴀᴅɪᴛɪᴏɴᴀʟ)" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴏ : ᴄᴏʀsɪᴄᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴛ : ᴇsᴛᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʏ : ғʀɪsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢʟ : ɢᴀʟɪᴄɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴀ : ɢᴇᴏʀɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴜ : ɢᴜᴊᴀʀᴀᴛɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴛ : ʜᴀɪᴛɪᴀɴ ᴄʀᴇᴏʟᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴀ : ʜᴀᴜsᴀ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴀᴡ : ʜᴀᴡᴀɪɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴡ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "╠❂➣ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴍɴ : ʜᴍᴏɴɢ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ɪɢ : ɪɢʙᴏ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴀ : ɪʀɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴡ : ᴊᴀᴠᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴋɴ : ᴋᴀɴɴᴀᴅᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴋ : ᴋᴀᴢᴀᴋʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴜ : ᴋᴜʀᴅɪsʜ (ᴋᴜʀᴍᴀɴᴊɪ)" + "\n" + \
                        "╠❂➣ " + key + "ᴋʏ : ᴋʏʀɢʏᴢ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴏ : ʟᴀᴏ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴛ : ʟɪᴛʜᴜᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟʙ : ʟᴜxᴇᴍʙᴏᴜʀɢɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɢ : ᴍᴀʟᴀɢᴀsʏ" + "\n" + \
                        "╠❂➣ " + key + "ᴍs : ᴍᴀʟᴀʏ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʟ : ᴍᴀʟᴀʏᴀʟᴀᴍ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴛ : ᴍᴀʟᴛᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɪ : ᴍᴀᴏʀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʀ : ᴍᴀʀᴀᴛʜɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɴ : ᴍᴏɴɢᴏʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʏ : ᴍʏᴀɴᴍᴀʀ (ʙᴜʀᴍᴇsᴇ)" + "\n" + \
                        "╠❂➣ " + key + "ɴᴇ : ɴᴇᴘᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘs : ᴘᴀsʜᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғᴀ : ᴘᴇʀsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴀ : ᴘᴜɴᴊᴀʙɪ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴍ : sᴀᴍᴏᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴅ : sᴄᴏᴛs ɢᴀᴇʟɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴛ : sᴇsᴏᴛʜᴏ" + "\n" + \
                        "╠❂➣ " + key + "sɴ : sʜᴏɴᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴅ : sɪɴᴅʜɪ" + "\n" + \
                        "╠❂➣ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "╠❂➣ " + key + "sʟ : sʟᴏᴠᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴏ : sᴏᴍᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "sᴜ : sᴜɴᴅᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "╠❂➣ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛɢ : ᴛᴀᴊɪᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴇ : ᴛᴇʟᴜɢᴜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴜʀ : ᴜʀᴅᴜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴢ : ᴜᴢʙᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "╠❂➣ " + key + "xʜ : xʜᴏsᴀ" + "\n" + \
                        "╠❂➣ " + key + "ʏɪ : ʏɪᴅᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ʏᴏ : ʏᴏʀᴜʙᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴢᴜ : ᴢᴜʟᴜ" + "\n" + \
                        "╠❂➣ " + key + "ғɪʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴇ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "╠════════════════════╗" + "\n" + \
                        "              ᴄʀᴇᴅɪᴛs ʙʏ : ©ᴅ̶ᴇ̶ᴇ̶ ✯" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "ᴄᴏɴᴛᴏʜ : " + key + "ᴛʀ-ɪᴅ ʀɪʀɪɴ"
    return helpTranslate
    
def ririnBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] Succes")
            return

        if op.type == 5:
            print ("[ 5 ] Add Contact")
            if wait["autoAdd"] == True:
                ririn.findAndAddContactsByMid(op.param1)
            ririn.sendMessage(op.param1, "╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n       ʜᴀʟʟᴏ, ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅ ᴍᴇ\n\n                    ᴏᴘᴇɴ ᴏʀᴅᴇʀ :\n               ✪ sᴇʟғʙᴏᴛ ᴏɴʟʏ ✪\n            ✪ sᴇʟғʙᴏᴛ + ᴀssɪsᴛ ✪\n                ✪ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ✪\n              「ᴀʟʟ ʙᴏᴛ ᴘʏᴛʜᴏɴ з」\n\n         ᴍɪɴᴀᴛ ᴘᴄ ᴀᴋᴜɴ ᴅɪ ʙᴀᴡᴀʜ :\n        [line.me/ti/p/ppgIZ0JLDW]")

        if op.type == 13:
            print ("[ 13 ] Invite Into Group")
            if ririnMid in op.param3:
                if wait["autoJoin"] == True:
                    ririn.acceptGroupInvitation(op.param1)
                dan = ririn.getContact(op.param2)
                tgb = ririn.getGroup(op.param1)
                sendMention(op.param1, "ʜᴀʟᴏ @!      , ᴛʜx ғᴏʀ ɪɴᴠɪᴛᴇ ᴍᴇ".format(str(tgb.name)),[op.param2])
                ririn.sendContact(op.param1, op.param2)
                ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                
        if op.type == 15:
        	dan = ririn.getContact(op.param2)
        	tgb = ririn.getGroup(op.param1)
        	sendMention(op.param1, "ɴᴀʜ ᴋᴀɴ ʙᴀᴘᴇʀ @!      , ɢᴀᴋ ᴜsᴀʜ ʙᴀʟɪᴋ ᴅɪ {} ʟᴀɢɪ ʏᴀ\nsᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ᴅᴀɴ sᴇᴍᴏɢᴀʜ ᴛᴇɴᴀɴɢ ᴅɪʟᴜᴀʀ sᴀɴᴀ 😘😘😘".format(str(tgb.name)),[op.param2])
        	ririn.sendContact(op.param1, op.param2)
        	ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        	
        if op.type == 17:
        	dan = ririn.getContact(op.param2)
        	tgb = ririn.getGroup(op.param1)
        	sendMention(op.param1, "ʜᴏʟᴀ @!         ,\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ {} \nᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴄʜᴇᴄᴋ ɴᴏᴛᴇ ʏᴀ \nᴀᴡᴀs ᴋᴀʟᴀᴜ ʙᴀᴘᴇʀᴀɴ 😘😘😘".format(str(tgb.name)),[op.param2])
        	ririn.sendContact(op.param1, op.param2)
        	ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))

        if op.type == 22:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)

        if op.type == 24:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)

        if op.type == 25:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = wait["keyCommand"].title()
                if wait["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != ririn.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            if cmd == "help":
                                helpMessage = helpmessage()
                                ririn.sendMessage(to, str(helpMessage),contentMetadata = {'AGENT_ICON': 'https://photos.app.goo.gl/qgLZTAPqR9ShYVhf2', 'AGENT_NAME': 'Help.', 'AGENT_LINK': 'line.me/ti/p/ppgIZ0JLDW'})
                                ririn.sendContact(to, "ueca4120a9d7b0e4a9e7f4f1b1b96a436")
                            elif cmd == "tts":
                                helpTextToSpeech = helptexttospeech()
                                ririn.sendMessage(to, str(helpTextToSpeech))
                                ririn.sendContact(to, "ueca4120a9d7b0e4a9e7f4f1b1b96a436")
                            elif cmd == "translate":
                                helpTranslate = helptranslate()
                                ririn.sendMessage(to, str(helpTranslate))
                                ririn.sendContact(to, "ueca4120a9d7b0e4a9e7f4f1b1b96a436")
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#





















#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                    elif msg.contentType == 1:
                        if wait["changePictureProfile"] == True:
                            path = ririn.downloadObjectMsg(msg_id)
                            wait["changePictureProfile"] = False
                            ririn.updateProfilePicture(path)
                            ririn.sendMessage(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ᴘʀᴏғɪʟᴇ")
                        if msg.toType == 2:
                            if to in wait["changeGroupPicture"]:
                                path = ririn.downloadObjectMsg(msg_id)
                                wait["changeGroupPicture"].remove(to)
                                ririn.updateGroupPicture(to, path)
                                ririn.sendMessage(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ɢʀᴏᴜᴘ")
                    elif msg.contentType == 7:
                        if wait["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔════[ sᴛɪᴄᴋᴇʀ ɪɴғᴏ ] "
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(stk_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇs ɪᴅ : {}".format(pkg_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(stk_ver)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                            ririn.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if wait["checkContact"] == True:
                            try:
                                contact = ririn.getContact(msg.contentMetadata["mid"])
                                if ririn != None:
                                    cover = ririn.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    ririn.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔═══[ ᴅᴇᴛᴀɪʟs ᴄᴏɴᴛᴀᴄᴛ ]"
                                ret_ += "\n╠❂➣ ɴᴀᴍᴀ : {}".format(str(contact.displayName))
                                ret_ += "\n╠❂➣ ᴍɪᴅ : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠❂➣ ʙɪᴏ : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴘʀᴏғɪʟᴇ : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴄᴏᴠᴇʀ : {}".format(str(cover))
                                ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                ririn.sendMessage(to, str(ret_))
                            except:
                                ririn.sendMessage(to, "ᴋᴏɴᴛᴀᴋ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ")
                    elif msg.contentType == 16:
                        if wait["checkPost"] == True:
                            try:
                                ret_ = "╔════[ ᴅᴇᴛᴀɪʟs ᴘᴏsᴛ ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = ririn.getContact(sender)
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠❂➣ ᴜʀʟ : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠❂➣ sᴛɪᴄᴋᴇʀ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠❂➣ ɴᴏᴛᴇ : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚════[ ✯ ᴅɴᴀ ʙᴏᴛ ✯ ]"
                                ririn.sendMessage(to, str(ret_))
                            except:
                                ririn.sendMessage(to, "ɪɴᴠᴀʟɪᴅ ᴘᴏsᴛ")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26:
            msg = op.message
            if wait["autoResponPc"] == True:
                if msg.toType == 0:
                    ririn.sendChatChecked(sender,msg_id)
                    contact = ririn.getContact(sender)
                    cName = contact.displayName
                    balas = ["╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nᴍᴏʜᴏɴ ᴍᴀᴀғ sᴀʏᴀ sᴇᴅᴀɴɢ sɪʙᴜᴋ, ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘᴇsᴀɴ ᴏᴛᴏᴍᴀᴛɪs, ᴊɪᴋᴀ ᴀᴅᴀ ʏᴀɴɢ ᴘᴇɴᴛɪɴɢ ᴍᴏʜᴏɴ ʜᴜʙᴜɴɢɪ sᴀʏᴀ ɴᴀɴᴛɪ, ᴛᴇʀɪᴍᴀᴋᴀsɪʜ...","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nsᴀʏᴀ ʟᴀɢɪ sɪʙᴜᴋ ʏᴀ ᴋᴀᴋ ᴊᴀɴɢᴀɴ ᴅɪɢᴀɴɢɢᴜ","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nsᴀʏᴀ sᴇᴅᴀɴɢ ᴛɪᴅᴜʀ ᴋᴀᴋ"]
                    dee = "" + random.choice(balas)
                    ririn.sendImageWithURL(sender, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                    ririn.sendMessage(sender,dee)
                
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != ririn.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if wait["autoRead"] == True:
                        ririn.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in wait["mimic"]["target"] and wait["mimic"]["status"] == True and wait["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            ririn.sendMessage(msg.to,text)
                    if wait["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                ririn.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                ririn.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if wait["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = ririn.findGroupByTicket(ticket_id)
                                    ririn.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    ririn.sendMessage(to, "sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴛᴇʀᴇᴅ ᴛʜᴇ ɢʀᴏᴜᴘ %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if ririnMid in mention["M"]:
                                    if wait["autoRespon"] == True:
                                    	ririn.sendChatChecked(sender,msg_id)
                                    	contact = ririn.getContact(sender)
                                    	ririn.sendImageWithURL(sender, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                                    	sendMention(sender, "ᴏɪ ᴍʙʟᴏ @!      ,\nɴɢᴀᴘᴀɪɴ ᴛᴀɢ ᴛᴀɢ ɢᴡ", [sender])
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if wait["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = ririn.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ."
                                ret_ += "\nsᴇɴᴅᴇʀ : @!      "
                                ret_ += "\nsᴇɴᴅ ᴀᴛ : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nᴛʏᴘᴇ : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nᴛᴇxᴛ : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            ririn.sendMessage(at,"sᴇɴᴛᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ,ʙᴜᴛ ɪ ᴅɪᴅɴ'ᴛ ʜᴀᴠᴇ ʟᴏɢ ᴅᴀᴛᴀ.\nsᴏʀʀʏ > <")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
                    
        if op.type == 55:
        	try:
        		group_id = op.param1
        		user_id=op.param2
        		subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
        	except Exception as e:
        		print(e)
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = ririn.getContact(op.param2).displayName
                            dan = ririn.getContact(op.param2)
                            tgb = ririn.getGroup(op.param1)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        sendMention(op.param1, "ᴡᴏʏ ☞ @!       ☜\nᴅɪ {} ᴋᴏᴋ ᴅɪᴇᴍ ᴅɪᴇᴍ ʙᴀᴇ...\nsɪɴɪ ɪᴋᴜᴛ ɴɢᴏᴘɪ".format(str(tgb.name)),[op.param2])
                                        ririn.sendContact(op.param1, op.param2)
                                        ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                                    else:
                                        sendMention(op.param1, "ᴍʙʟᴏ ☞ @!       ☜\nɴɢɪɴᴛɪᴘ ᴅᴏᴀɴɢ ʟᴜ ᴅɪ {} \nsɪɴɪ ɢᴀʙᴜɴɢ ᴍᴀ ᴋɪᴛᴀ".format(str(tgb.name)),[op.param2])
                                        ririn.sendContact(op.param1, op.param2)
                                        ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                                else:
                                    sendMention(op.param1, "ʜɪʟɪʜ ☞ @!       ☜\nɴɢᴀᴘᴀɪɴ ʟᴜ...\nɢᴀʙᴜɴɢ ᴄʜᴀᴛ sɪɴɪ ᴅɪ {} ".format(str(tgb.name)),[op.param2])
                                    ririn.sendContact(op.param1, op.param2)
                                    ririn.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
                
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = ririnPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                ririnBot(op)
                ririnPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)