#######################################################
# Name:       Michael Cunningham
# Class:      CIS-1400
# Assignment: Homework 9 fall 2021
# File:       Homework_09.py
# Purpose: sort names
######################################################
def sort_list(name_list):
    for i in range(len(name_list)):
        for j in range(0,len(name_list)-i-1):
            if name_list[j]>name_list[j+1]:
                temp = name_list[j]
                name_list[j] = name_list[j+1]
                name_list[j+1] = temp

def binary_search(names,search_name):
    l = 0
    r = len(names)-1
    lookups = 0
    while l <= r:
        mid = l + (r - l)//2;
        lookups += 1
        if names[mid] == search_name:
            return mid,lookups
        elif names[mid] < search_name:
            l = mid + 1
        else:
            r = mid - 1
    return -1,lookups

def search(names):
    while True:
        print("Enter a name to search for <or enter to exit>")
        search_name=input()
        if len(search_name) == 0:
            break
        index,lookups=binary_search(names,search_name)
        if index!=-1:
            print("Name found: {}".format(search_name))
            print("Positions: {}".format(index))
            print("Lookups: {}".format(lookups))
        else:
            print("Name not found")
            print("Lookups: {}".format(lookups))

def main():
    names_array = (['']*20)

    print("Please enter 20 names:")
    for i in range(20):
        name = input("{0}: ".format(i+1))
        names_array[i] = name

    sort_list(names_array)
    print("The sorted names are:")
    for name in names_array:
        print(name)
    search(names_array)
main()