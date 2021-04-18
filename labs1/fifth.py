# For a given list of strings write a function that
# returns a sorted list with all strings starting with the
# character x at the beginning (define two lists)

unsorted_list = ['xh', 'xd', 'xu', 'auss', 'sidu', 'xkdi', 'xkall']
sorted_list = sorted([n for n in unsorted_list if n[0] == 'x'])
print(", ".join(unsorted_list)+'\n'+", ".join(sorted_list))
