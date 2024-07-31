#recursive function to call the sum of the series
def rec_func(l,i,sum):
    if(i==len(l)):
        return sum
    sum=sum+l[i]
    return rec_func(l,i+1,sum)

list=[1,2,3,4,5]
print(rec_func(list,0,0))
