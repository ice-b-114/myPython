# -*- coding: UTF-8 -*-
import requests
import re

def download(img_url,pname):
    print("Downloading...")
    r = requests.get(img_url)
    #print(r.status_code) # 返回状态码
    if r.status_code == 200:
        open(pname+'.jpg', 'wb').write(r.content) # 将内容写入图片
        print("Done")
    else:
        print("Fail")
def main(limit,*tag):
    tags = '+'.join(tag)
    res=requests.get(url='http://yande.re/post.xml?limit='+str(limit)+'&tags='+tags)
    print(res.text)
    pic_address = re.findall(r'jpeg_url="(.+?)"', res.text, )
    pic_name = re.findall(r'<post id="(.+?)"', res.text, )
    for i in range(0,limit):
        download(pic_address[i],pic_name[i])
if __name__ == '__main__':
    main(1,"order%3Arandom")#order%3Arandom