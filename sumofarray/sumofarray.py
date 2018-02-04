def sumOfArray(array):
    """
    Given an array, split and
    check if sum of each elements in each is equal
    """
    if type(array) != list:
        print "List is required. Given %s is %s" % (array, type(array))
        return False
    if len(array) <= 1:
        return False

    first = array[0]
    total = first

    for index in range(len(array)):
        if sum(array[:index]) == sum(array[index:]):
            print array[:index], array[index:]
            return True
    print "Not possible!"
    return False

if __name__ == "__main__":
    # sumOfArray("Hello")
    sumOfArray([1,2,2,1,1,1,1,5,1,1,1,1])
