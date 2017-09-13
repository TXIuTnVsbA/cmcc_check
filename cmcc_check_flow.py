# -*- coding: utf-8 -*-
import requests,re,sys,os,commands,time
reload(sys)
sys.setdefaultencoding("utf-8")
requests.packages.urllib3.disable_warnings()
session = requests.Session()
session.headers.update({'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
                        'Referer': 'http://wap.10086.cn/s/index.html'})

def get():
    proxies = {'http':'http://10.0.0.172:80','https':'https://10.0.0.172:80'}
    session.get("http://wap.10086.cn/ywcx/ywcx.jsp",proxies=proxies)
    R = session.get("http://wap.10086.cn/ywcx/tcylcx.jsp",proxies=proxies)
    R.encoding = "utf-8"
    req = R.text
    fl=flow(req)
    #print "===================================="
    print "剩余:"+fl[0],"总量:"+fl[1]
    print "====================================" 
    
    '''
    session.get("http://wap.10086.cn/ywcx/ywcx.jsp")
    R = session.get("http://wap.10086.cn/ywcx/tcylcx.jsp")
    '''

def flow(T):
    list = re.findall('\d+.?\d+MB', T)
    residue = 0.0
    allflow = 0.0
    # 0,2,4,....N+2;剩余#residue
    for i in range(0, len(list), 2):
        residue = residue + float(list[i].split('MB')[0])
    # 1,3,5,....N+2;总量#all
    for i in range(1, len(list), 2):
        allflow = allflow + float(list[i].split('MB')[0])
    return str(residue),str(allflow)

def rainy_check():
    #os.system('clear')
    print "===================================="
    wk="netcfg|grep -v /0|grep -v lo|grep UP|awk '{print $1}'"
    wk=commands.getstatusoutput(wk)[1]
    xx="cat /proc/net/dev|grep -w "+wk+"|awk '{print $2}'"
    xx=commands.getstatusoutput(xx)[1]
    sx="cat /proc/net/dev|grep -w "+wk+"|awk '{print $10}'"
    sx=commands.getstatusoutput(sx)[1]
    up="echo $(awk -v x="+xx+" -v y=1048576 'BEGIN {printf \"%.2f\",x/y}')"
    up=commands.getstatusoutput(up)[1]
    down="echo $(awk -v x="+sx+" -v y=1048576 'BEGIN {printf \"%.2f\",x/y}')"
    down=commands.getstatusoutput(down)[1]
    print "上传:"+down,"下载:"+up
    #print "===================================="

while(1):
    rainy_check()#搬运rainy的查询模块
    get()#查询流量模块
    time.sleep(5)#单位秒
