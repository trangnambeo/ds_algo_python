#!/usr/bin/python

###############################################################################
## Run length encode
##
## @param string string to be encoded
##
## @return encoded string, e.x., "aaaabbbccddddde" --> "4a3b2c5d1e"
###############################################################################
def runLengthEncode(string):
    result = ''
    curChar = string[0]
    rlCnt = 1
    for i in xrange(1, len(string)):
        if string[i] == curChar:
            rlCnt = rlCnt + 1
        else:
            result += (str(rlCnt) + curChar)
            curChar = string[i]
            rlCnt = 1
    # Append the last character
    result += (str(rlCnt) + curChar)

    return result

###############################################################################
## Run length decode
##
## @param string string to be decoded
##
## @return decoded string, e.x., "4a3b2c5d1e" --> "aaaabbbccddddde"
###############################################################################
def runLengthDecode(string):
    result = ''
    curChar = string[0]
    rlCnt = 1
    index = 0
    while index <= (len(string) - 1):
        if (index % 2 == 0):
            curLength = int(string[index])
            curChar = string[index + 1]
            for i in xrange(0, curLength):
                result += curChar
        index += 1
    return result


###############################################################################
## Output Nth hear-say number
##
## @param N number to determine
##
## @remarks start from 1,e.x., 1, 11, 21, 1211, 111221, 312211...
###############################################################################
def hearSay(N):
    result = "1"
    for i in xrange(1, N):
        result = runLengthEncode(result)
    print("Hear-Say number of N = {} is {}\n".format(N, result))

###############################################################################
## Main program
###############################################################################
if __name__ == "__main__":
    # Run length encode
    data = "aaaabbbccddddeeeeeee"
    print("Run Length Encode of {} is {}\n".format(data,
          runLengthEncode(data)))

    # Run length decode
    data = "4a3b2c5d1e"
    print("Run Length Decode of {} is {}\n".format(data,
         runLengthDecode(data)))

    # Hear-say problem
    hearSay(5)
    hearSay(6)
    hearSay(7)

