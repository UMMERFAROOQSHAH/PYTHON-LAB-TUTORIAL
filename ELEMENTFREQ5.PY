array = [1,1,1,2,2,3,4,4,4,5,5,6]
counted = []
for i in array:#ITERATES THROUGH ARRAY:-
    if i not in counted:
        count = 0
        for j in array:#COUNTS OCCURANCE OF ELEMENTS:-
            if i == j:
                count += 1
        counted.append(i)
        print(f"Element {i} occurs {count} times.")