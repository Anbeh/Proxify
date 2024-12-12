from requests import get
from base64 import b64decode

mtproto_links = [
    'https://mtpro.xyz/api/?type=mtproto',
    'https://mtpro.xyz/api/?type=socks'
]

v2ray_links = [
        "https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/BeVpn.txt",
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/mix",
        "https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt",
        "https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/reality",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vless",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vmess",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/trojan",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/shadowsocks",
        "https://raw.githubusercontent.com/ts-sf/fly/main/v2",
        "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2",
        "https://mrpooya.top/SuperApi/BE.php",
        "https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/BeVpn.txt"
    ]

proxy_links = {
    'socks5': [
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/socks5.txt',
        'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/refs/heads/main/proxies/socks5.txt',
        'https://raw.githubusercontent.com/hookzof/socks5_list/refs/heads/master/proxy.txt',
        'https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Socks5.txt',
        'https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks5/data.txt',
        'https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/socks5_proxies.txt',
        'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/refs/heads/main/socks5.txt',
        'https://raw.githubusercontent.com/elliottophellia/proxylist/refs/heads/master/results/socks5/global/socks5_checked.txt',
        'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/refs/heads/main/socks5.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/SOCKS5_RAW.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks5.txt',
        'https://raw.githubusercontent.com/sunny9577/proxy-scraper/refs/heads/master/generated/socks5_proxies.txt'
        'https://raw.githubusercontent.com/r00tee/Proxy-List/main/Socks5.txt'
    ],
    'socks4': [
        'https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks4/data.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
        'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks4.txt',
        'https://raw.githubusercontent.com/sunny9577/proxy-scraper/refs/heads/master/generated/socks4_proxies.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/socks4.txt',
        'https://raw.githubusercontent.com/r00tee/Proxy-List/main/Socks4.txt',
        'https://proxyspace.pro/socks4.txt'

    ],
    'http': [
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/http.txt',
        'https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/http/data.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/http.txt',
        'https://raw.githubusercontent.com/sunny9577/proxy-scraper/refs/heads/master/generated/http_proxies.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/http.txt',
        'https://api.openproxylist.xyz/http.txt',
        'https://alexa.lr2b.com/proxylist.txt',
        'https://rootjazz.com/proxies/proxies.txt',
        'https://proxy-spider.com/api/proxies.example.txt',
        'https://multiproxy.org/txt_all/proxy.txt',
        'https://proxyspace.pro/http.txt'

    ],
    'https': [
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/https.txt',
        'https://raw.githubusercontent.com/claude89757/free_https_proxies/refs/heads/main/https_proxies.txt',
        'https://raw.githubusercontent.com/r00tee/Proxy-List/main/Https.txt',
        'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/refs/heads/master/https.txt',
        'https://raw.githubusercontent.com/SevenworksDev/proxy-list/refs/heads/main/proxies/https.txt',
        'https://proxyspace.pro/https.txt'
    ],
    'mtproto': [
        'https://raw.githubusercontent.com/soroushmirzaei/telegram-proxies-collector/refs/heads/main/proxies'
    ]
}


def get_proxy(type):
    with open(f'{type}.txt', 'w') as output:
        for link in proxy_links[type]:
            data = get(link).text
            if data == '404: Not Found':
                continue
            else:
                for line in data.splitlines():
                    if line.startswith('socks5://') or line.startswith('socks4://') or line.startswith('http://') or line.startswith('https://'):
                        line = line.removeprefix('socks5://')
                        line = line.removeprefix('socks4://')                        
                        line = line.removeprefix('http://')
                        line = line.removeprefix('https://')
                    output.write(line + '\n')
        output.close()


def get_v2ray():
    with open('v2ray.txt', 'wb') as output:
        for link in v2ray_links:
            data = get(link).text
            if data == '404: Not Found':
                continue
            else:
                data = b64decode(data)
                output.write(data)
                output.write(b'\n')
        output.close()


def get_mtproto(link_index):
    if link_index == 0:
        with open('mtproto-tg.txt', 'w') as output:
            data = get(mtproto_links[0]).json()
            for proxy in data:
                output.write(f"https://t.me/proxy?server={proxy['host']}&port={proxy['port']}&secret={proxy['secret']}\n")
            output.close()
    elif link_index == 1:
            with open('socks5-tg.txt', 'w') as output:
                data = get(mtproto_links[1]).json()
                for proxy in data:
                    output.write(f"https://t.me/proxy?server={proxy['ip']}&port={proxy['port']}\n")
                output.close()


get_proxy('socks4')
get_proxy('socks5')
get_proxy('http')
get_proxy('https')
get_mtproto(1)
get_mtproto(0)
get_v2ray()