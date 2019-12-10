if __name__ == "__main__":
    
    def removeElement(nums, val) -> int:
        for i in nums[:]:
            if i == val:
                nums.remove(i)
            else:
                continue
        return len(nums)

    while True:
        #Numbers should be typed with spaces between them.
        #No need for brackets at the beggining neither at the end
        x = input("List of numbers (separated by spaces): ").split()
        lista = [int(i) for i in x]
        n = int(input("Number you want to delete: "))
        print("List :" ,lista)
        removeElement(lista, n)
        print("New list :" ,lista)
