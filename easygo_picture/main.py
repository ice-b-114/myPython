# -*- coding: utf-8 -*-
import Merge_data_set
import data
import class_cut
import os
'''
try:
    
except:
        print("发生异常")
        
        '''
filepath = r"C:/Users\JSKJ\Desktop\shenhe"#总文件夹所在的上级目录的路径
files = os.listdir(filepath)
for name in files:
    Merge_data_set.main(filepath,name)
    data.main(filepath,name)
    class_cut.main(filepath,name)
print("完成")