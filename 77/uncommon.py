def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    myset = set(my_cities)
    otherset = set(other_cities)
    myset.symmetric_difference_update(otherset)
    return len(myset)
    
