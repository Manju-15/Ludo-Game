class Ludo:
    size = 3
    cp = [1,0]
    p1 = [1,0]
    p2 = [1,0]
    def disp(self,player):
        a = []
        for i in range(3):
            l = []
            for j in range(3):
                if (i == self.p2[0] and j == self.p2[1]):
                    l.append("p2")
                elif (i == self.p1[0] and j == self.p1[1]):
                    l.append("p1")
                else:
                    l.append(0)
            a.append(l)
        print("position of", player, "is :")
        for i in range(3):
            for j in range(3):
                print(a[i][j], end=" ")
            print()
    def Left(self,steps,player):
        if player=='p1':
            p = self.p1
            while(self.p1[1]<3 and steps!=0 and self.p1[1]>0):
                self.p1[1]-=1
                steps -= 1
            if steps == 0:
                self.disp(player)
            elif steps == 1:
                print("P1 wins the game!!!!!!!!!!")
                ob.flag=False
            elif steps==2 or steps==3:
                self.p1 = p
                print("You need to get 1")
        elif player=='p2':
            p = self.p2
            while(self.p2[1]<3 and steps!=0 and self.p2[1]>0):
                self.p2[1]-=1
                steps -= 1
            if steps == 0:
                self.disp(player)
            elif steps==1:
                print("P2 wins the game!!!!!!!!!")
                self.flag = False
            elif steps==2 or steps==3:
                self.p2 = p
                print("You need to get 1")
    def Up(self,steps,player):
        if player=='p1':
            while(self.p1[0]<3 and steps!=0 and self.p1[0]>0):
                self.p1[0]-=1
                steps -= 1
            if steps == 0:
                self.disp(player)
            else:
                self.Left(steps,player)
        elif player=='p2':
            while(self.p2[0]<3 and steps!=0 and self.p2[0]>0):
                self.p2[0]-=1
                steps -= 1
            if steps == 0:
                self.disp(player)
            else:
                self.Left(steps,player)
    def right(self,steps,player):
        if player=='p1':
            while(self.p1[1]<2 and steps!=0 and self.p1[0]==2):
                self.p1[1]+=1
                steps -= 1
            if steps == 0:
                self.disp(player)
            else:
                self.Up(steps, player)
        elif player=='p2':
            while(self.p2[1]<2 and steps!=0 and self.p2[0]==2):
                self.p2[1]+=1
                steps -= 1
            if steps == 0:
                self.disp(player)
            else:
                self.Up(steps,player)
    def down(self,steps,player):
        if player=='p1':
            while(self.p1[0]<2 and self.p1[0]>0 and steps!=0 and self.p1[1]==0):
                self.p1[0]+=1
                steps -= 1
            if steps == 0:
                print("P1")
                self.disp(player)
            else:
                self.right(steps, player)
        elif player=='p2':
            while(self.p2[0]<2 and self.p2[0]>0 and steps!=0 and self.p2[1]==0):
                self.p2[0]+=1
                steps -= 1
            if steps == 0:
                print("P2")
                self.disp(player)
            else:
                self.right(steps,player)
ob = Ludo()
ob.flag = True
while(ob.flag):
    p = input("Enter player as p1 or p2 alternatively : ")
    n = int(input("Enter the dice = "))
    ob.down(n,p)
    if p == "p1" and ob.flag:
        if ob.p1 == ob.p2 and (ob.p1 !=[1,2] and ob.p2 != [1,2]):
            print("P2 will move to the start position")
            ob.p2 = ob.cp
            ob.disp(p)
    elif ob.flag:
        if ob.p1 == ob.p2 and (ob.p1 !=[1,2] and ob.p2 != [1,2]):
            print("P1 will move to the start position")
            ob.p1 = ob.cp
            ob.disp(p)

