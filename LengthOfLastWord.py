if __name__ == "__main__":

    def lengthOfLastWord(s) -> int:
        lista = s.split()
        if lista == []:
            return 0
        else:
            return len(lista[-1])
            
    while True:
        i = input("Phrase: ")
        print(lengthOfLastWord(i))