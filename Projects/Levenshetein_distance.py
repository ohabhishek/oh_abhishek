import sys

#Function to return the distance between two strings - Levenshtein distance


a = sys.argv[1]
b = sys.argv[2]

def lv_number(a, b):
    string1 = a
    string2 = b
    distance = 0
    n1 = len(string1)
    n2 = len(string2)
    
    if n1 >= n2:
        for i in range(n1):
            if i < n2:
                if string1[i] != string2[i]:
                    distance += 1
            else:
                distance += 1
    else:
        for i in range(n2):
            if i < n1:
                if string2[i] != string1[i]:
                    distance -= 1
            else:
                distance -= 1
    
    
        
    return distance


print "Distance: " + str(lv_number(a, b))