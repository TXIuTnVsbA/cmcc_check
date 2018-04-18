# cmcc_check

环境：安卓、wap接入点

APP：Qpython2.7

原理：

    利用wap接入点访问wap.10086.cn存储cookie实现免密登录，
    
    再自定义请求浏览http://wap.10086.cn/ywcx/tcylcx.jsp 查询流量
    
    利用正则表达式分块提取套餐流量，最后计算出总流量和剩余流量
    
    函数rainy_check()：利用os.system执行shell命令来查看主要网卡的流量信息
