if __name__=="__main__":

    while True:
        #you have to type the words separated by spaces
        y = input("Words list: ")
        
        x = [str(i) for i in y.split()]
    
    def longestCommonPrefix(strs) -> str:
            prefix = strs[0] if strs else ""
            max_len = len(prefix)
            for word in strs[1:]:
                for i in range(max_len+1):
                    prefix = prefix[0:max_len-i]
                    if prefix == word[0:max_len-i]:
                        break

            return prefix
          
        print("Longest common prefix: " + str(longestCommonPrefix(x)))