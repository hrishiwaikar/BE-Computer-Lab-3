#------code by @Hrishikesh Waikar@ -----#


def decimaltobinary(no):
    #returns the binary representation of the decimal no in the form of a list
    b=[] #b will hold the binary no as it forms
    print('in decimal to binary , no'+str(no))
    while no!=0:
        remainder = no%2
        #print remainder
        b.append(remainder)
        no=no//2

    print('b'+str(b))
    b.reverse()
    return b

def binarytodecimal(no):
    #returns decimal of no
    no.reverse()
    sum=0
    for i,bit in enumerate(no):
        if bit==1:
            sum=sum+2**i

    return sum

def twoscomplement(bin_no):  #for negative nos
    #twos complement helps represent a negative binary number
    #eg. -3 can be represented as twos complement of 3
    # 3=>011 , 2's complement of 3 => 101
    binary_no=list(bin_no)
    change=False
    for i,digit in reversed(list(enumerate(binary_no))):
        #print 'index'+str(i)
        if change==True:
            if digit==1:
                binary_no[i]=0
            else:
                binary_no[i]=1
        if digit==1:
            change=True

    return binary_no

def add(no1,no2) :
    # add two binary nos, assuming the two nos. are of same length
    #for booths it is important that the sum of two numbers have the same length as the input nos
    no=[] #the new addition will be in this list

    carry=0
    for i,digit in reversed(list(enumerate(no1))):
        sum=no1[i]+no2[i]+carry
        if sum==2:
            sum=0
            carry=1
        elif sum==3:
            sum=1
            carry=1
        else:
            carry=0
        no.append(sum)
    no.reverse()
    return no



def asr(no):  #arithmetic shift right
    #shift the bits of the binary no to right by 1 digit
    #the left most new bit being the same as previous left most bit

    shiftedno=[]
    shiftedno.append(no[0]) #add the first leftmost bit same as previous
    #then copy the rest of the string - last element which will be garbaged
    for i in range(0,len(no)-1):
        shiftedno.append(no[i])

    return shiftedno


def extendlarger(no):
    no.reverse()
    no.append(0)
    no.append(0)
    no.reverse()
    return no

def extendsmaller(no,by):
    no.reverse()
    for i in range(by):
        no.append(0)
    no.reverse()
    return no

#MAIN FUNCTION TO CALCULATE THE BOOTHS MULTIPLICATION OF TWO NUMBERS


def boothmultiplication(mdecimal,rdecimal):
    mdecimal= int(mdecimal)
    rdecimal = int(rdecimal)
    #print(mdecimal)
    #print(rdecimal)
    m=decimaltobinary(abs(mdecimal))
    r=decimaltobinary(abs(rdecimal))
    #print(m)
    #print(r)
    original_m=list(m)
    original_r=list(r)

    if len(r)>len(m):
        r=extendlarger(r)
        m =extendsmaller(m,len(r)-len(m))
    elif len(m)>len(r):
        m=extendlarger(m)
        r=extendsmaller(r,len(m)-len(r))
    else:
        m=extendlarger(m)
        r=extendlarger(r)

    if mdecimal<0:
        m=twoscomplement(m)

    if rdecimal<0:
        r=twoscomplement(r)

    #print " m "+str(m)
    #print " r "+str(r)

    #now we have got m and r
    # -m
    minusm=twoscomplement(m)

    #There are three components in booths : A, S, P
    # A = m 00..len(m) 0
    # S = -m 00...len(-m) 0
    # P = 00...len(r) r 0

    #let e be empty list of length(m)+1 size
    e=[]
    for i in range(len(m)+1):
       e.append(0)

    A = m+e
    S = minusm+e
    e.pop()
    P = e+r
    P.append(0)

    print("A "+str(A))
    print("S "+str(S))
    print ("P "+str(P))

    x=len(m)
    #print "last two bits "+str(A[len(A)-2:])
    lasttwo=[]
    originalP=list(P)
    # NOW THE ORIGINAL BOOTHS ALGORITHM

    steplist=[]
    messagelist=[]
    step=''

    for i in range(x):
        lasttwo=P[len(P)-2:]

        if lasttwo[0]==lasttwo[1]:  # if last two bits are 00 or 11
            #only arithmetic shift right =asr
            P = asr(P)
            step='Step ' + str(i+1) + ' Only Arithmetic Shift Right'
            messagelist.append(step)
        elif lasttwo[0]==0:
            #basically last two bits are 01 , now P=P+A then asr
            P=add(P,A)
            P=asr(P)
            step='Step '+str(i+1)+' Add P and A followed by Arithmetic Shift Right'
            messagelist.append(step)
        else:
            #last two bits are 10 , P=P+S , then asr
            P=add(P,S)
            P=asr(P)
            step = 'Step ' + str(i+1) + ' Add P and S followed by Arithmetic Shift Right'
            messagelist.append(step)
        steplist.append(list(P))
        #print "\n"+str(i+1)+"  P "+str(P)


    L=P
    L.pop()

    finalbinaryans=L

    #print("\nfinalbinaryans "+str(finalbinaryans))

    # ------code by @Hrishikesh Waikar@ -----#

    if not ((mdecimal>0 and rdecimal>0) or (mdecimal<0 and rdecimal<0)) :
        finalbinaryans = twoscomplement(finalbinaryans)
        ans = binarytodecimal(finalbinaryans)
        ans=ans*(-1)
    else:
        k =list(finalbinaryans)
        ans = binarytodecimal(k)
    print(ans)

    for i in range(len(steplist)):
        print(messagelist[i])
        print(steplist[i])
        print('\n')

    contextdata={
        'm':original_m,
        'r':original_r,
        'P':originalP,
        'A':A,
        'S':S,
        'messagelist':messagelist,
        'steplist':steplist,
        'finalbinans':finalbinaryans,
        'ans':ans
    }

    return contextdata

#boothmultiplication(3,4)

#------code by @Hrishikesh Waikar@ -----#
