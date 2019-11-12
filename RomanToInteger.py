if __name__=="__main__":

    while True:
	
        x = str(input("Roman number to convert: "))

        def romanToInt(s: str) -> int:
            total = 0
            dict ={
                "I" : 1,
                "V" : 5,
                "X" : 10,
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000
            }
            for j in range(len(s)):
                if j == len(s)-1:
                    total += dict[s[j]]
                elif dict[s[j]] < dict[s[j+1]]:
                    total -= dict[s[j-1]]
                else:
                    total += dict[s[j]]
            return total

        print(romanToInt(x.upper()))