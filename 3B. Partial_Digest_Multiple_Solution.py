def delta_function(y, X):
    diffs = []
    for x in X:
        diffs.append(abs(y - x))
    return diffs

def PLACE(L, X):
    if len(L) == 0:
        X.sort()
        solutions.append(X.copy()) 
        return
    
    y_val = max(L)
    all_possible_y = [y_val,width-y_val]

    for y in all_possible_y:
        delta_y = delta_function(y, X)
        is_belongs_to = all(element in L for element in delta_y)
        
        if is_belongs_to:
            X.append(y)
            for x in delta_y:
                L.remove(x)
            PLACE(L, X)  
            X.remove(y)
            for x in delta_y:
                L.append(x)
            
    return

L = [2, 2, 3 ,3, 4, 5, 6, 7, 8, 10]
#L = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 10, 11, 12]
width = max(L)
X = [0]
solutions = []
PLACE(L, X)
for solution in solutions:
    print(solution)
