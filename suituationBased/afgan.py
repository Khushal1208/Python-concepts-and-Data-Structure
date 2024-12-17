# tag = "21a45e"
tag = "22w35xc"
# tag = "2g3y34k4"
# tag = "2k2l2p2"

for i in range(len(tag)-1):
    if tag[i].lower() in ('a','e','i','o','u'):
        print("bhagakar goli maro isko")

    else:
        if (tag[i].isdigit() and tag[i+1].isdigit()):
            if((int(tag[i]) + int(tag[i+1]))%2 == 0):
                print("apna bhai hai , aane do.")
            else:
                print("bhagakar goli maro isko")