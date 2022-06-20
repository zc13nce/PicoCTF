encodedFlag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"
decodedFlag = ""

for i in encodedFlag:
    char1 = chr((ord(i) >>  8))
    char2 = chr((ord(i) - (ord(char1) << 8)))
    decodedFlag = decodedFlag + char1 + char2

print(decodedFlag)
