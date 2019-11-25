if __name__=="__main__":

    while True:
        x = str(input("Haystack: "))
        y = str(input("Needle: "))
        
        def strStr(haystack: str, needle: str) -> int:
            if not needle:
                return 0
            if not haystack:
                return -1
            for i in range(len(haystack)):
                if haystack[i:(i+(len(needle)))] == needle:
                    return i
                elif ((i+(len(needle)-1))>=((len(haystack))-1)):
                    return -1
                else:
                    continue
                
        print("Output: " + str(strStr(x,y)))