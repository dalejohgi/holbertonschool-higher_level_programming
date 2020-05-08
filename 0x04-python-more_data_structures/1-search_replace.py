#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def searcher(element):
        return (element if element is not search else replace)
    return list(map(searcher, my_list))
