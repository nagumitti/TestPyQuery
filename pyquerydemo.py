from pyquery import PyQuery as pq

def pyquery():
    rinfo=pq(url="http://erail.in/station/SBC?filter=4")
    for x in rinfo("table")("tr"):
        print "Train No.- "+str(rinfo(x)("a").text())+" Train Name- "+str(rinfo(x)("td").eq(2).text())+" Type- "+str(rinfo(x)("td").eq(3).text())
