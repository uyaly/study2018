#似乎marker只能一个一个点添加，不能以数组形式添加
#http://lbs.amap.com/api/javascript-api/guide/quickstart/#t1
#https://wiki.python.org/moin/Templating
#http://www.jb51.net/article/84425.htm
#http://www.yeolar.com/note/2012/08/28/mako-syntax/
#Python打开HTML文件需要引用webbrowser
import webbrowser
from mako.template import Template                         #导入模板对象
import codecs                                              #导入转义库
import pandas as pd

#经纬度已经在R+Python中下载过，这里就不重复下载
df_lonlat=pd.read_table(r'result.txt',sep=",",header=None)
df_lonlat.head(5)           #查看前5行

def get_dic_lonlat(df):      #<---将lonlat转成字典,title:lon,lat--->
    count_df=len(df)                          #df的行号,用以循环
    i=0                                       #初始化变量
    title=[]                                  #初始化变量
    lonlat=[]                                 #初始化变量
    dic={}                                    #初始化变量
    while i<count_df-1:                        #循环
        title.append(df.ix[i,0])               #获取标题
        lon=round(df.ix[i,3],4)                #获取lon
        lat=round(df.ix[i,4],4)                #获取lat
        lonlat.append(str(lon)+","+str(lat))   #lon,lat
        # print title,lonlat
        dic=dict(zip(title,lonlat))            #写入字典,title:lonlat
        i=i+1
    return dic                                 #返回字典

def getInterAmap(str_city_center,dic_lonlat):      #<---获取动态高德地图--->
    # sh = '121.472644,31.231706'  # 上海中心点
    #高德地图-->静态地图API地址
    url = r'map.html'
    tmple=Template(filename=url,input_encoding='utf-8')        #根据amap构建模板对象
    result=tmple.render(Locat=str_city_center, Pt=dic_lonlat)                          #将location传递给mako的template
    # result=tmple.render(Locat='121.74,31.24')                 #test only
    print(result)                                               #显示结果
    f=codecs.open("map.html",'w',"utf-8")                   #另存为文件
    f.write(result)                                            #写入信息
    f.close()                                                  #关闭文件
    url_1=r'map.html'                                       #文件名
    webbrowser.open(url_1)                                     #打开本地html

if __name__=='__main__':         #<---主程序--->
    dic_lonlat=get_dic_lonlat(df_lonlat)                      #返回字典
    for key,value in dic_lonlat.items():
        print(key,'-->',value)                            #观察字典内容
    str_city_center = '121.47,31.23'            #城市中心点lonlat
    result=getInterAmap(str_city_center, dic_lonlat)              #获取地图