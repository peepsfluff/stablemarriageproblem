from Marriage import Marriage
from itertools import permutations



class Solution:

    def __init__(self, number, men, women):
        """
        :param number: The number of members
        :param men: The preference list of men, as a dictionary.
        :param women: The preference list of the women, as a dictionary.
        """
        self.num = number
        self.men = men
        self.women = women
        self.stable_matchings = []


    def output_stable_matchings(self):
        """
        This method both computes and returns the stable matchings
        :return: the list of stable matchings
        """

        pair1 = (list(permutations(range(1, self.num + 1))))

        dict1 = {}  # womens preferences
        dict2 = {}  # mens preferences
        finalpotlist = []  # possible stable match
        l2 = []
        l1 = []

        q = Queue()

        for x in range(0, len(pair1)):
            for y in range(0, self.num):
                value = pair1[x][y]
                q.enqueue(value)

            for i in range(1, self.num+1):
                ccheck = 0

                popped = q.dequeue()  # MEN preference
                                                            #WOMEN preference
                tup = (popped, i)                           #man to woman
                finalpotlist.append(tup)


                #print(((self.women[popped]).index(i)))
                more2 = ((self.women[popped]).index(i))     #what women they would leave their partner for (index inside dict given)
                if more2 != 0:

                    for z in range(0, more2+1):

                        if (z < (more2)):

                            putin2 = ((self.women[popped])[z])#append the key and the value(s) into a list
                            l2.append(putin2)
                            dict2[popped]=l2

                           # dict2[popped] = l2.append(putin2)
                        else:

                            l2 = []


                        #dict2[popped] = q1.enqueue(putin2)
                else:
                    #the woman they are matched with is there first preference
                    dict2[popped] = [0] #no preference, append key and value 0 into a list



                more1 = ((self.men[i]).index(popped))   #WOMEN
                if more1 != 0:
                    #q2 = Queue()

                    for z in range(0, more1+1):

                        if (z<(more1)):
                            putin1 = ((self.men[i])[z])
                            l1.append(putin1)
                            dict1[i] = l1


                        else:



                            l1=[]

                            i=+1

                else:
                    # the men they are matched with is there first preference
                    dict1[i] = [0]



       
            for i in dict1:

                for k in dict2:
                    ccheck = 0


                    if (dict2=={}):
                        break
                    if ((i in dict2[k])):

                        ccheck += 1

                        if k in dict1[i]:
                            ccheck += 1

                      
                            dict1={}
                            dict2={}
                            finalpotlist=[]
                            break


            if ccheck!=2:
                ccheck=0
                #print(self.stable_matchings)

                if(finalpotlist!=[]):
                    (self.stable_matchings).append(finalpotlist)
                finalpotlist = []
                dict1 = {}
                dict2 = {}

            if ccheck==2:

                finalpotlist = []
                dict1 = {}
                dict2 = {}


        return self.stable_matchings






class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)