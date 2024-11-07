def delta_function(y,X):
    diffs = []
    for x in X:
        diffs.append(abs(y-x))
    return diffs

def PLACE(L,X):
    if len(L) == 0:
        X.sort()
        print(X)
        return
    y = max(L)
    delta_y = delta_function(y, X)
    is_belongs_to = all(element in L for element in delta_y)
    if is_belongs_to:
        X.append(y)
        for x in delta_y:
            L.remove(x)
        PLACE(L,X)
        X.remove(y)
        for x in delta_y:
            L.append(x)
        
    else:
        y = width - y
        delta_y = delta_function(y, X)
        X.append(y)
        for x in delta_y:
            L.remove(x)
        PLACE(L,X)
        X.remove(y)
        for x in delta_y:
            L.append(x)
    return

L = [2, 2, 3 ,3, 4, 5, 6, 7, 8, 10]
width = max(L)
X = [0]
PLACE(L,X)
