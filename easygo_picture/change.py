# -*- coding: utf-8 -*-
import os
import xml.etree.cElementTree as ET
def gci(filepath):
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        elif 'xml' in fi:
            changee(fi_d)

def changee(xml):
    root = ET.parse(xml)
    depth = root.find("size").find("depth").text
    assert depth == "3"
    for ob in root.findall("object"):
        if  int(float(ob.find("bndbox").find("ymin").text)) < 0 :
            ob.find("bndbox").find("ymin").text = '0'
            print("success")
    root.write(xml, encoding="utf-8")
        

xml_path = r"C:/Users/JSKJ/Desktop/shenhe/"
gci(xml_path)