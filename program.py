
def FIFO(pages, size):
    faults =0
    cache = []
    for page in pages:
        if page not in cache:
            if len(cache) < size:
                cache.append(int(page)) #Only add and do not remove an item if the cache is not full

            else:
                cache.pop(0) #Remove the first item in the list
                cache.append(int(page)) #Add the new item to the end of the list
            faults = faults+1 #increment the fault number if the page is not in the cache for both cases

    return faults
    
#**Main code**
print("Please enter the number of pages:")
pageNo = int(input())
print("Please enter the size of the cache:")
cacheSize = int(input())
pages = []
print("Please enter the pages(items): ")
for i in range(pageNo): #Fill the pages list with the page numbers
    pages.append(int(input())) #Make sure to convert from String to int before populating the list

print("The number of page faults for FIFO algorithm is: " + str(FIFO(pages, cacheSize)))

