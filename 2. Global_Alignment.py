seq1 = "CTCGCAGC"
seq2 = "CAGGCCCT"

len1 = len(seq1)
len2 = len(seq2)

swapped = False

if len1 < len2:
    len1, len2 = len2, len1
    seq1, seq2 = seq2, seq1
    swapped = True

gap_cost = -5
mismatch_cost = -2
match_cost = 10

rows = len1 + 1
cols = len2 + 1

table = [[0 for _ in range(cols)]for _ in range(rows)]

def build_table():
    for i in range (rows):
        table[i][0] = i * gap_cost

    for j in range(cols):
        table[0][j] = j * gap_cost

    for i in range(1, rows):
        for j in range(1,cols):
            table[i][j] = max(table[i-1][j-1]+evaluate(seq1[i-1],seq2[i-1]),table[i-1][j]+gap_cost, table[i][j-1]+gap_cost)

def evaluate(a,b):
    if a==b:
        return match_cost
    elif a=="-" or b=="-":
        return gap_cost
    else:
        return mismatch_cost

def traceback(seqA,seqB):
    ansAlignA = ""
    ansAlignB = ""
    i =  len(seqA)
    j = len(seqB)
    while i>0 or j>0:
        if i>0 and j>0 and table[i][j]==table[i-1][j-1]+evaluate(seqA[i-1],seqB[j-1]):
            ansAlignA += seqA[i-1]
            ansAlignB += seqB[j-1]
            i += -1
            j += -1

        elif i>0 and table[i][j] == table[i-1][j]+gap_cost:
            ansAlignA += seqA[i-1]
            ansAlignB += "-"
            i += -1

        else:
            ansAlignA += "-"
            ansAlignB += seqB[j-1]
            j += -1
    return ansAlignA,ansAlignB

build_table()
for row in table:
    print(row)

ref_str,align_str = traceback(seq1,seq2)
ref_str = ref_str[::-1]
align_str = align_str[::-1]

if swapped is True:
    ref_str, align_str = align_str, ref_str

print(ref_str)
print(align_str)


srt_len = len(ref_str)
score = 0
for i in range(srt_len):
    score = score + evaluate(ref_str[i],align_str[i])

print(score)