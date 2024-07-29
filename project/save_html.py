def save(path , content):
    with open(path, 'w', encoding="utf-8") as fp:
        fp.write(content)

def read(path):
    html = ""
    with open(path, encoding="utf-8") as fp:
        html = fp.read()
    return html


if __name__=="__main__":
    print(__name__)