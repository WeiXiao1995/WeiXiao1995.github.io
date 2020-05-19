import json,os
path='D:\Cs_about\WebSite\SN&XW v1.1\images\index\gallery'
yearList=[];
ImgStructDict={}
dirlist = os.listdir(path)
for dirs in dirlist:
    if os.path.isdir(path+"\\"+dirs):
        pathList=[];
        locList=[];
        yearList.append(dirs)
        subdir=os.listdir(path+"\\"+dirs);
        for img in subdir:
            if not os.path.isdir(path+"\\"+dirs+"\\"+img):
##                print(path+"\\"+dirs+"\\"+img)
                pathList.append(dirs+"/"+img)
                suffix=os.path.splitext(img)[-1]
                ind=img.find('(')
                if ind==-1:
                    ind=img.find(suffix)
                locList.append(img[0:ind])
        ImgStructDict['loc'+dirs]=locList#location+year
        ImgStructDict['path'+dirs]=pathList#path+year
    ##        ImgStruct{end+1}=imgname;
    ##        pathcell{end+1}=locfind(imgname);

fw=open('D:\Cs_about\WebSite\SN&XW v1.1\img_info.json','w',encoding='utf-8')   #打开一个名字为‘user_info.json’的空文件
json.dump(ImgStructDict,fw,ensure_ascii=False,indent=4)#字典转成json,字典转换成字符串,不需要写文件，自己帮你将转成的json字符串写入到‘user_info.json’的文件中 
fw.close()
