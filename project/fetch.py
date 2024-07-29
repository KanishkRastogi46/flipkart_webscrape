import requests as re


def fetch(url):
    res = re.get(url)
    res.encoding = "utf-8"
    return res


if __name__=="__main__":
    print(__name__)