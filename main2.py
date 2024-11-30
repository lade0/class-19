# program to find first and last character matching in a given word
def search(words):
    count=0
    empty=[]
    for i in words:
        if len(i)>2 and i[0]==i[-1]:
            count+=1
            empty.append(i)
    print("list of word with first and last character same\n",empty)
    return count
counter=search(['mum','898','uwkj'])
print("number of word having first and last charactre same are:",counter)