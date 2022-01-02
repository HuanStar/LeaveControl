import requests
import bs4

url = "https://gitee.com/HuanStar23/LeaveControl"

head = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/65.0.3325.181 Safari/537.36'
}


res = requests.get(url, headers=head)
res.encoding = "UTF-8"
soup = bs4.BeautifulSoup(res.text, "html.parser")
targets = soup.find_all(name="div", class_="desc")


now_ver = 1.1
vers = "1.1"

def versions():
    global vers
    return vers

def update(now_ver):
    global targets, vers
    i = 0
    for n in targets:
        if i == 4:
            vers = ver = n.text[-4:-1]
            version = float(ver)
            if version <= now_ver:
                return False
            else:
                return True
            # print(version > now_ver)
            # print(version)
            # print(n.text)
        i += 1


# if __name__ == "__main__":
#     update(1.1)