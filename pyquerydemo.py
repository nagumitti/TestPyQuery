from pyquery import PyQuery as pq

def pyquery():
    tno=[];tname=[];tarr=[];tdep=[];ttype=[];
    rinfo=pq(url="http://erail.in/station/SBC?filter=4")
    for x in rinfo("table")("tr"):
        tno.append(str(rinfo(x)("a").text()))
        tname.append(str(rinfo(x)("td").eq(2).text()))
        ttype.append(str(rinfo(x)("td").eq(3).text()))
        tarr.append(str(rinfo(x)("td").eq(4).text()))
        tdep.append(str(rinfo(x)("td").eq(5).text()))
    tno.pop(0);tname.pop(0);ttype.pop(0);tarr.pop(0);tdep.pop(0)
    print tno
    print tname
    print ttype
    print tarr
    print tdep
    stationInfo=pq(url="http://erail.in/js/cmp/Stations.js")
    s=str(stationInfo("p").text())
    slist= s.split(";")
    stationList=slist[0][slist[0].find("\"")+1:-1].split(",")
    print stationList
