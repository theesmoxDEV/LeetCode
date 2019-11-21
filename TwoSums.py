if __name__=="__main__":
    while True:
        #Input: Numbers separated by spaces
        n = str(input("Number list: "))
        x = [int(i) for i in n.split()]
        y = int(input("Sum target: "))
          
        def twoSum(nums, target):
            for i in range(0,len(nums)):
                for j in range(0,len(nums)):
                    if nums[i]+nums[j]==target:
                        if i==j:
                            continue
                        else:
                            return [i,j]
                
        print("Indices that sum "+ str(y)+ ": " + str(twoSum(x,y)))