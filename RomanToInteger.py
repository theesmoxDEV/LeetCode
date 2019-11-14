if __name__=="__main__": # This make it possible to run "python RomanToInteger.py" directly in the terminal

    while True: # A infinite loop, so you can repeat the program untill you press "ctrl + c"
	
        x = str(input("Roman number to convert: ")) # The input is the roman number. The function suposses that te number is correct.

        def romanToInt(s: str) -> int:
		
	    """Converts a roman number into decimal."""
	
            total = 0
            dict ={                              # Values of each number
                "I" : 1,
                "V" : 5,
                "X" : 10,
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000
            }
            for j in range(len(s)):              # We loop over the number indices.
			
                if j == len(s)-1:                # If the number is at the end, we just add it to the total.
                    total += dict[s[j]]

		elif dict[s[j]] < dict[s[j+1]]:  # If the number is less than the next number, we substract it from the total.
                    total -= dict[s[j-1]]
                
		else:
                    total += dict[s[j]]          # If not at the end and neither less than the next number, we just add it to the total. 
            
	    return total

        print(romanToInt(x.upper()))
