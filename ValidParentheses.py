if __name__=="__main__":

    while True:
	
        x = str(input("Cadena: "))
        
        def isValid(s: str) -> bool:
            o = ['(', '{', '[']
            c = [')', '}', ']']
            r = True
            queue = []
            cont = 0
        
            if s == '':
                r = True
        
            elif len(s)%2 != 0 or s[0] in c:
                r = False
            
            else:
                for i in s:
                    if i in o:
                        queue.append(o.index(i))
                    else:
                        if i != c[queue[-1]]:
                            r = False
                            break
                        else:
                            del queue[-1]
                if queue != []:
                    r = False
            return r
            
        print(isValid(x))		