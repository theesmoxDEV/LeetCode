if __name__ == "__main__":
    
    def removeElement(nums, val) -> int:
        for i in nums[:]:
            if i == val:
                nums.remove(i)
            else:
                continue
        return len(nums)

    while True:

        x = input("List of numbers (separated by spaces): ").split()
        lista = [int(i) for i in x]
        n = int(input("Number you want to delete: "))
        print("List :" ,lista)
        removeElement(lista, n)
        print("New list :" ,lista)