def max_consecultive_seq(v):
    global_max = 0
    suffix_max = 0
    a = b = 0

    for i in range(len(v)):

        # updates the suffix max
        if v[i]+suffix_max > global_max:
            suffix_max += v[i]
            global_max = suffix_max
            b = i
        else:
            if v[i]+suffix_max > 0:
                suffix_max += v[i]
            else:
                suffix_max = 0
                a = i+1

    #check whether just one element is greater than the sum of any other sequence
    if a > b:
        return (a,a)

    return (a,b)

v = [-2,1,3,-1,4,2,-3,-10, 9,-7]
print(max_consecultive_seq(v))