global first1,last1,first2,last2
first1 = int(input("числитель первой дроби: ")) #24
last1 = int(input("знаменатель первой дроби: ")) #24
first2 = int(input("числитель второй  дроби: ")) #24
last2 = int(input("знаменатель второй дроби: ")) #24

def cout_znam():
    #global znam,chislitel
#    znam = 0
    if(last1 == last2):
        znamenatel = last1
        chislitel = first1 + first2
    else:
        if (last2 % last1 == 0):
            znamenatel = (last2//last1)*last1
            chislitel = (znamenatel//last1*first1)+(znamenatel//last2*first2)
        elif (last1%last2==0):
            znamenatel = (last1//last2)*last2
            #chislitel = (znamenatel//last1*first1)+(znamenatel//last2*first2)
        else:
            znamenatel = last1 * last2
        chislitel = (znamenatel//last1*first1)+(znamenatel//last2*first2)
    
    
    if(chislitel>znamenatel):
        print(True)
        z = True
        while z:
            for i in range(2,int(znamenatel)):
                if (znamenatel % i == 0) and (chislitel % i == 0):
                    chislitel //=i
                    znamenatel //=i
                    break
            else:
                z= False
                break
    if(znamenatel>chislitel):
        print(False)
        z = True
        while z:
            for i in range(2,int(chislitel)):
                if(znamenatel % i == 0) and (chislitel % i == 0):
                    chislitel //= i
                    znamenatel //=i
                    break
            else:
                z = False
                break


    if (chislitel>znamenatel):
        if (znamenatel == 1):
            return (f"Ваш результат: {chislitel}")
        elif(chislitel % znamenatel == 0):
                return (f"Ваш результат: {chislitel/znamenatel}")
        else:
            z1=chislitel//znamenatel
            z2=chislitel-z1*znamenatel
            return (f"Ваш результат: {z1} {z2}/{znamenatel}")

             
    res = str(chislitel)+"/"+str(znamenatel)
    return (f"Ваша результат: {res}")
    
        
if __name__ == '__main__':
    print(cout_znam())
    input("нажмите <Return> то бы выйти")
