def FIFO(pages, size):
    """
    First-In-First-Out (FIFO) Page Replacement Algorithm
    
    This function simulates the FIFO page replacement algorithm, which removes the oldest page in the cache
    when a new page needs to be added and the cache is full.
    
    Parameters:
    pages (list): List of page requests.
    size (int): Size of the cache.
    
    Returns:
    int: Number of page faults.
    """
    faults = 0
    cache = []
    for page in pages:
        if page not in cache:
            if len(cache) < size:
                cache.append(int(page))  # Add to cache if not full
            else:
                cache.pop(0)  # Remove the first item (oldest page) if cache is full
                cache.append(int(page))  # Add the new page to the end
            faults += 1  # Increment faults if page is not in cache
    return faults

def LRU(pages, size):
    """
    Least Recently Used (LRU) Page Replacement Algorithm
    
    This function simulates the LRU page replacement algorithm, which removes the least recently used page
    from the cache when a new page needs to be added and the cache is full.
    
    Parameters:
    pages (list): List of page requests.
    size (int): Size of the cache.
    
    Returns:
    int: Number of page faults.
    """
    faults = 0
    cache = []
    for i in range(len(pages)):
        if pages[i] not in cache:
            if len(cache) < size:
                cache.append(int(pages[i]))  # Add to cache if not full
            else:
                safe = []
                for k in range(i - 1, -1, -1):  # Find least recently used page
                    if pages[k] not in safe:
                        safe.append(pages[k])
                        if len(safe) == size:
                            break
                cache.remove(safe[-1])  # Remove the LRU page (last added to safe list)
                cache.append(int(pages[i]))  # Add the new page to the cache
            faults += 1  # Increment faults if page is not in cache
    return faults

def OPT(pages, size):
    """
    Optimal (OPT) Page Replacement Algorithm
    
    This function simulates the optimal page replacement algorithm, which removes the page that will not be used
    for the longest period in the future when a new page needs to be added and the cache is full.
    
    Parameters:
    pages (list): List of page requests.
    size (int): Size of the cache.
    
    Returns:
    int: Number of page faults.
    """
    faults = 0
    cache = []
    for i in range(len(pages)):
        if pages[i] not in cache:
            if len(cache) < size:
                cache.append(int(pages[i]))  # Add to cache if not full
            else:
                farthest = -1
                index_to_remove = -1
                for j in range(len(cache)):
                    try:
                        index = pages[i + 1:].index(cache[j])
                    except ValueError:
                        index = float('inf')  # Page not found in future, considered farthest
                    if index > farthest:
                        farthest = index
                        index_to_remove = j
                cache.pop(index_to_remove)  # Remove the page used farthest in the future
                cache.append(int(pages[i]))  # Add the new page to the cache
            faults += 1  # Increment faults if page is not in cache
    return faults

# Main code
print("Please enter the number of pages:")
pageNo = int(input())
print("Please enter the size of the cache:")
cacheSize = int(input())
pages = []
print("Please enter the pages(items):")
for i in range(pageNo):
    pages.append(int(input()))  # Populate the pages list with integers

print("The number of page faults for FIFO algorithm is: " + str(FIFO(pages, cacheSize)))
print("The number of page faults for LRU algorithm is: " + str(LRU(pages, cacheSize)))
print("The number of page faults for OPT algorithm is: " + str(OPT(pages, cacheSize)))
