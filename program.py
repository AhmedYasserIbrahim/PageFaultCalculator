
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

def LRU(pages, size):
    faults =0
    cache = []
    safe = [] #Use an array that keeps track of the pages that will not be removed from cache
    for i in range(len(pages)): #Easier to use indecies
        safe = [] #Reset the array in every iteration
        if pages[i] not in cache:
            if len(cache)<size:
                cache.append(int(pages[i]))
            
            else:
                for k in range(i-1,-1,-1): #Iterate from the current index in pages until 0
                    if pages[k] not in safe: #Add pages to array safe starting from page before current page
                        safe.append(pages[k]) 
                        if len(safe) == size:
                            break
                cache.remove(safe[size-1]) #Remove the last page added to the safe from array cache
                cache.append(int(pages[i])) #Add the new page to the cache
            
            faults=faults+1

    return faults

def OPT(pages, size):
    faults = 0
    cache = []
    
    for i in range(len(pages)):  # Iterate through the pages
        if pages[i] not in cache:  # If the current page is not in the cache
            if len(cache) < size:  # If the cache has available space
                cache.append(pages[i])  # Add the current page to the cache
            else:  # If the cache is full
                # Find the page in the cache that is farthest in the future
                farthest = 0
                index_to_remove = -1
                for j in range(len(cache)):
                    try:
                        index = pages[i + 1:].index(cache[j])
                    except ValueError:
                        index = float('inf')
                    if index > farthest:
                        farthest = index
                        index_to_remove = j
                
                # Remove that page from the cache
                cache.pop(index_to_remove)
                cache.append(pages[i])  # Add the new page to the cache
            faults += 1  # Increment the number of page faults
    
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

print("The number of page faults for FIFO algorithm is: " + str(OPT(pages, cacheSize)))
#Adding the hit and miss ratio would be a good feature


