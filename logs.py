import sys


def logger(file):
    # i call python dictionaries "objects" because javascript is superior ;) thats where obj comes from
    srcIPobj = {}
    srcIPcounter = 1

    dstIPobj = {}
    dstIPcounter = 1

    ftpIPobj = {}
    ftpIPcounter = 1

    print("    LINE ------------------DATE AND TIME---------------SRC IP-----SRC PORT------DST IP-----DST PORT-----PROTOCOL-----ERROR CODE")
    for line in file:
        # line = line.rstrip()
        line = line.split(";")
        lineNum = line[0]
        time = line[1]
        srcIP = line[2]
        srcPort = line[3]
        dstIP = line[4]
        dstPort = line[5]
        proto = line[8].upper()
        code = line[9]
        codeSplit = code.split(":")
        action = codeSplit[0]
        print(action)
        if proto == "FTP" and action == "Request":
            if srcIP not in ftpIPobj:
                ftpIPobj[srcIP] = ftpIPcounter
            else:
                ftpIPobj[srcIP] += ftpIPcounter

        if srcIP not in srcIPobj:
            srcIPobj[srcIP] = srcIPcounter
        else:
            srcIPobj[srcIP] += srcIPcounter

        if dstIP not in dstIPobj:
            dstIPobj[dstIP] = dstIPcounter
        else:
            dstIPobj[dstIP] += dstIPcounter
        
        
        # print(f'{"    " + lineNum + "    " + time + "      " + srcIP +"  "+ srcPort + "       " + dstIP +"   "+ dstPort +"     "+ proto +"       "+ errorCode}')
        sortedSrcValues = sorted(srcIPobj, key=srcIPobj.get)
        sortedSrcIPDict = {}
       
        sortedDstValues = sorted(dstIPobj, key=dstIPobj.get)
        sortedDstIPDict = {}

        sortedFTPValues = sorted(ftpIPobj, key=ftpIPobj.get)
        sortedFTPIPDict = {}


        for w in sortedSrcValues:
            sortedSrcIPDict[w] = srcIPobj[w]
        for w in sortedDstValues:
            sortedDstIPDict[w] = dstIPobj[w]
        for w in sortedFTPValues:
            sortedFTPIPDict[w] = ftpIPobj[w]


    print("SRC IP'S    "+str(sortedSrcIPDict) + "\n")
    print("DST IP'S    "+str(sortedDstIPDict) + "\n")
    print("FTP IP'S    "+str(sortedFTPIPDict) + "\n")


def main():
    file_name = sys.argv[1]
    open_file = open(file_name,"r")
    print(logger(open_file))
    open_file.close()

main()
