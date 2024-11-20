import tkinter as tk
from PIL import Image,ImageTk,ImageDraw
import random
import math



def create_polygon(*args, **kwargs):
        global can




        if "alpha" in kwargs:         
                if "fill" in kwargs:
                        # Get and process the input data
                        fill = root.winfo_rgb(kwargs.pop("fill"))\
                               + (int(kwargs.pop("alpha") * 255),)
                        outline = kwargs.pop("outline") if "outline" in kwargs else None

                        # We need to find a rectangle the polygon is inscribed in
                        # (max(args[::2]), max(args[1::2])) are x and y of the bottom right point of this rectangle
                        # and they also are the width and height of it respectively (the image will be inserted into
                        # (0, 0) coords for simplicity)
                        image = Image.new("RGBA", (max(args[::2]), max(args[1::2])))

                        ImageDraw.Draw(image).polygon(args, fill=fill, outline=outline)



                        images.append(ImageTk.PhotoImage(image))  # prevent the Image from being garbage-collected


                        return can.create_image(0, 0, image=images[-1], anchor="nw")  # insert the Image to the 0, 0 coords
                raise ValueError("fill color must be specified!")
        return can.create_polygon(*args, **kwargs)

images = []


def draw_transparent_bg(xx,yy,x_,y_,r,col,opacity,con):



        if con==0:
                create_polygon(x_,y_, x_+xx,y_, x_+xx,y_+yy, x_,y_+yy, fill=col, alpha=opacity)

        elif con==1:



                ar=[]


                ang=270

                for a_ in range(90):


                        x=r*math.sin(math.radians(ang))+x_+r
                        y=r*math.cos(math.radians(ang))+y_+r


                        ar.append(int(x))
                        ar.append(int(y))



                        ang-=1





                ang=180

                for a_ in range(90):


                        x=r*math.sin(math.radians(ang))+x_+xx-r
                        y=r*math.cos(math.radians(ang))+y_+r


                        ar.append(int(x))
                        ar.append(int(y))



                        ang-=1




                ang=90

                for a_ in range(90):


                        x=r*math.sin(math.radians(ang))+x_+xx-r
                        y=r*math.cos(math.radians(ang))+y_+yy-r


                        ar.append(int(x))
                        ar.append(int(y))



                        ang-=1






                ang=0

                for a_ in range(90):


                        x=r*math.sin(math.radians(ang))+x_+r
                        y=r*math.cos(math.radians(ang))+y_+yy-r


                        ar.append(int(x))
                        ar.append(int(y))



                        ang-=1







                create_polygon(*ar, fill=col, alpha=opacity)




def findNextCellToFill(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False








def intro():
        
        global can,state,can,width,height,cnt,view_pos_moves

        view_pos_moves=0

        state=0
        can.delete("all")

        can.create_arc(width/2-80-15,height-20-30, width/2-80+15,height-20,style="arc",outline="#000000",start=90,extent=180)
        can.create_arc(width/2+80-15,height-20-30, width/2+80+15,height-20,style="arc",outline="#000000",start=270,extent=180)

        can.create_line(width/2-80,height-20-30, width/2+80,height-20-30,fill="#000000")
        can.create_line(width/2-80-1,height-20, width/2+80,height-20,fill="#000000")

        can.create_text(width/2,height-20-15,text="New Game", font=("FreeMono",13),fill="#000000")


        if cnt==1:


                can.create_arc(width/2-80-15,height-20-30-40, width/2-80+15,height-20-40,style="arc",outline="#000000",start=90,extent=180)
                can.create_arc(width/2+80-15,height-20-30-40, width/2+80+15,height-20-40,style="arc",outline="#000000",start=270,extent=180)

                can.create_line(width/2-80,height-20-30-40, width/2+80,height-20-30-40,fill="#000000")
                can.create_line(width/2-80-1,height-20-40, width/2+80,height-20-40,fill="#000000")

                can.create_text(width/2,height-20-15-40,text="Continue", font=("FreeMono",13),fill="#000000")



def b1(e):
        global state,cnt
        global width,height
        global sel,sel2
        global viewable,my_solutions,solution,possible_sol
        global view_pos_moves
        global game_mode
        global mistakes
        global write_st,write_st2,write_ar
        global ava_no





        if state==0:

                if width/2-80<=e.x<=width/2+80 and height-20-30<=e.y<=height-20:

                        sel_game_mode()

                cx,cy=width/2-80,height-20-30+15

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        sel_game_mode()



                cx,cy=width/2+80,height-20-30+15

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        sel_game_mode()



                if cnt==1:



                        if width/2-80<=e.x<=width/2+80 and height-20-30-40<=e.y<=height-20-40:
                                load()

                                main()

                        cx,cy=width/2-80,height-20-30+15-40

                        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                        if r<=15:
                                load()
                                main()



                        cx,cy=width/2+80,height-20-30+15-40

                        r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                        if r<=15:
                                load()
                                main()

        elif state==1:




                yv=(height-(40)*5)/2

                #40



                if width/2-80<=e.x<=width/2+80 and yv<=e.y<=yv+30:

                        game_mode="easy"

                        gen(0)

                        mistakes=0

                        main()

                cx,cy=width/2-80,yv+15

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        game_mode="easy"
                        gen(0)
                        mistakes=0
                        main()



                cx,cy=width/2+80,yv+15

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        game_mode="easy"
                        gen(0)
                        mistakes=0
                        main()


















                #35


                if width/2-80<=e.x<=width/2+80 and yv+40<=e.y<=yv+30+40:
                        game_mode="medium"

                        gen(1)
                        mistakes=0

                        main()

                cx,cy=width/2-80,yv+15+40

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        game_mode="medium"
                        gen(1)
                        mistakes=0
                        main()



                cx,cy=width/2+80,yv+15+40

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        game_mode="medium"
                        gen(1)
                        mistakes=0
                        main()














                #30

                if width/2-80<=e.x<=width/2+80 and yv+40*2<=e.y<=yv+30+40*2:
                        game_mode="hard"

                        gen(2)
                        mistakes=0

                        main()

                cx,cy=width/2-80,yv+15+40*2

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        game_mode="hard"
                        gen(2)
                        mistakes=0
                        main()



                cx,cy=width/2+80,yv+15+40*2

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        game_mode="hard"
                        gen(2)
                        mistakes=0
                        main()


















                #25

                if width/2-80<=e.x<=width/2+80 and yv+40*3<=e.y<=yv+30+40*3:
                        game_mode="expert"

                        gen(3)
                        mistakes=0

                        main()

                cx,cy=width/2-80,yv+15+40*3

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        game_mode="expert"

                        gen(3)
                        mistakes=0
                        main()



                cx,cy=width/2+80,yv+15+40*3

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        game_mode="expert"

                        gen(3)
                        mistakes=0
                        main()













                #20

                if width/2-80<=e.x<=width/2+80 and yv+40*4<=e.y<=yv+30+40*4:

                        game_mode="nightmare"


                        gen(4)
                        mistakes=0

                        main()

                cx,cy=width/2-80,yv+15+40*4

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        game_mode="nightmare"
                        gen(4)
                        mistakes=0
                        main()



                cx,cy=width/2+80,yv+15+40*4

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:
                        game_mode="nightmare"
                        gen(4)
                        mistakes=0
                        main()



        elif state==2:


                w_=width-20
                sz=w_/9


                if 10<=e.x<=10+w_:
                        if 40<=e.y<=40+w_:


                                x=e.x-10
                                y=e.y-40

                                x=int(x/sz)
                                y=int(y/sz)





                                sel=[x,y]



                                ar=viewable

                                for _ in my_solutions:


                                        if solution[_[1]][_[0]]==_[-1]:
                                                ar[_[1]][_[0]]=_[-1]



                                if not ar[y][x]==0:
                                        sel2=ar[y][x]
                                else:
                                        sel2=0




                                main()

                                return



                if 10<=e.x<=10+w_:
                        if height-10-sz<=e.y<=height-10:

                                x=e.x-10

                                val=int(x/sz)+1


                                try:
                                        v=ava_no.index(val)



                                        if sel!=0 and viewable[sel[1]][sel[0]]==0:




                                                if write_st==1:

                                                        

                                                        for _ in range(len(possible_sol)):

                                                                if sel[0]==possible_sol[_][0] and sel[1]==possible_sol[_][1]:



                                                                        write_ar.append([sel[0],sel[1],val])

                                                                        main()
                                                                        return



                                                                pass



                                                else:


                                                        for _ in range(len(my_solutions)):
                                                                v=my_solutions[_]

                                                                if v[0]==sel[0] and v[1]==sel[1]:
                                                                        my_solutions.pop(_)

                                                        my_solutions.append([sel[0],sel[1],val] )

                                                        if solution[sel[1]][sel[0]]!=val:
                                                                mistakes+=1
                                                        else:
                                                                sel2=val

                                                        
                                                        sel=0

                                                        possible_sol_()

                                                        

                                                        main()


                                                        return

                                        sel=0
                                        sel2=val
                                        main()
                                        return

                                except:
                                        pass








                if 5<=e.x<=55:
                        if height-122.77777777777777<=e.y<=height-64.77777777777777:

                                p="x"



                                for v in range(len(my_solutions)):

                                        v_=my_solutions[v]

                                        if v_[0]==sel[0] and v_[1]==sel[1]:


                                                p=v
                                                break



                                if not p=="x":


                                        my_solutions.pop(p)


                                        sel=0
                                        main()


                                return







                if 65<=e.x<=115:
                        if height-122.77777777777777<=e.y<=height-64.77777777777777:


                                if view_pos_moves==0:
                                        view_pos_moves=1

                                        

                                elif view_pos_moves==1:
                                        view_pos_moves=0
                                        write_st2=1
                                        write_st=0


                                main()
                                return






                if 125<=e.x<=175:
                        if height-122.77777777777777<=e.y<=height-64.77777777777777:

                                if view_pos_moves==1:

                                        if write_st==0:
                                                write_st=1

                                        elif write_st==1:
                                                write_st=0


                                        main()
                                        return








                cx,cy=width-10-30+15,5+15

                r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

                if r<=15:

                        my_solutions=[]
                        view_pos_moves=0
                        write_st=0

                        sel=0
                        sel2=0



                        write_st2=0
                        write_ar=[]
                        ava_no=[]



                        try:


                                with open('data/save.txt', 'r') as file:

                                        
                                        if file.read()=="":
                                                cnt=0
                                        else:
                                                cnt=1

                        except:
                                cnt=0


                        intro()



                        return






                sel=0
                sel2=0
                main()





        elif state==3:

                xx,yy=200,100

                x_=(width-xx)/2
                y_=(height-yy)/2



                if x_<=e.x<=x_+xx:
                        if y_+yy-40<=e.y<=y_+yy:

                                my_solutions=[]
                                view_pos_moves=0
                                write_st=0

                                sel=0
                                sel2=0

                                write_st2=0
                                write_ar=[]
                                ava_no=[]

                                intro()








def gen(gm):

        global solution,viewable

        solution=[]

        ar=[]

        while len(ar)!=9:

                val=random.randint(1,9)

                try:

                        v=ar.index(val)
                except:
                        ar.append(val)



        solution.append(ar)

        for _ in range(8):
                solution.append([0,0,0,0,0,0,0,0,0])


        solveSudoku(solution)



        if gm==0:
                n=40
        elif gm==1:
                n=35
        elif gm==2:
                n=30
        elif gm==3:
                n=25
        elif gm==4:
                n=20

        ar=[]

        while len(ar)!=n:


                x=random.randint(0,8)
                y=random.randint(0,8)

                try:
                        v=ar.index([x,y])
                except:
                        ar.append([x,y])


        

        viewable=[]

        for y in range(9):

                ar_=[]
                for x in range(9):

                        try:
                                v=ar.index([x,y])
                                ar_.append(solution[y][x])
                        except:
                                ar_.append(0)


                viewable.append(ar_)




        
        #for _ in viewable:
        #        print(_)


        


def possible_sol_():
        global possible_sol,viewable,my_solutions,solution,write_st,write_ar,write_st2 ,ava_no

        possible_sol=[]


        ar=viewable

        for _ in my_solutions:


                if solution[_[1]][_[0]]==_[-1]:
                        ar[_[1]][_[0]]=_[-1]

        def get_possible_values(board, row, col):
            """Find all possible values for a specific cell in the Sudoku board."""
            if board[row][col] != 0:
                return []  # The cell is already filled

            # Collect numbers already in the row, column, and 3x3 subgrid
            used_numbers = set()

            # Check the row
            used_numbers.update(board[row])

            # Check the column
            for i in range(9):
                used_numbers.add(board[i][col])

            # Check the 3x3 subgrid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    used_numbers.add(board[i][j])

            # Possible values are numbers not in the used_numbers set
            return [num for num in range(1, 10) if num not in used_numbers]



        for y in range(9):
                for x in range(9):

                        if ar[y][x]==0:


                                ava=get_possible_values(ar, y, x)


                                possible_sol.append([x,y,ava])

        ava_no=[]


        for v in possible_sol:

                for _ in v[-1]:

                        try:
                                vv=ava_no.index(_)
                        except:
                                ava_no.append(_)












        if write_st2==1:

                write_st2=0
                write_ar=[]
        else:

                for w in write_ar:

                        x_,y_=w[:2]
                        val=w[-1]

                        for _ in range(len(possible_sol)):

                                x,y=possible_sol[_][:2]

                                if x_==x and y_==y:


                                        try:
                                                v=possible_sol[_][-1].index(val)

                                                possible_sol[_][-1].pop(v)



                                        except:

                                                try:

                                                        ar_=get_possible_values(ar, y, x)
                                                        v=ar_.index(val)
                                                        possible_sol[_][-1].append(val)
                                                except:
                                                        pass











        return possible_sol

def check_win():
        global viewable,my_solutions,solution

        con=0

        ar=viewable

        for _ in my_solutions:


                if solution[_[1]][_[0]]==_[-1]:
                        ar[_[1]][_[0]]=_[-1]




        if ar==solution:
                con=1

        return con



def main():
        global solution,viewable,my_solutions

        global state,can,width,sel,sel2

        global eraser
        global notes,notes2,write,write2,write_st,write_st2

        global view_pos_moves,possible_sol
        global game_mode
        global mistakes
        global exit
        global cnt

        can.delete("all")

        possible_sol_()

        state=2


        can.create_text(10,20,text=game_mode,font=("FreeMono",13,"bold"),fill="#000000",anchor="w")
        can.create_text(width/2,20,text="mistakes - "+str(mistakes),font=("FreeMono",13),fill="#000000",anchor="c")

        exit_=can.create_image(width-10-30,5,image=exit,anchor="nw")





        w_=width-20

        can.create_rectangle(10-2,40-2,10+w_+2,40+w_+2,fill="#ffffff",outline="#000000",width=3)
        can.create_rectangle(10,40,10+w_,40+w_,fill="#ffffff",outline="#ffffff")











        sz=w_/9






        xx=10+sz
        for x in range(9):

                if x==2 or x==5:
                        w=3
                else:
                        w=1

                can.create_line(xx,40,xx,40+w_,fill="#000000",width=w)


                xx+=sz


        yy=40+sz
        for x in range(9):

                if x==2 or x==5:
                        w=3
                else:
                        w=1

                can.create_line(10,yy,10+w_,yy,fill="#000000",width=w)


                yy+=sz




        if not sel==0:
                can.create_rectangle(10+sel[0]*sz,40+sel[1]*sz, 10+sel[0]*sz+sz,40+sel[1]*sz+sz,fill="#000000",outline="#000000")











        







        #viewable

        for y in range(9):
                for x in range(9):



                        if viewable[y][x]!=0:

                                col="#000000"

                                if viewable[y][x]==sel2:
                                        can.create_rectangle(10+x*sz,40+y*sz, 10+x*sz+sz,40+y*sz+sz,fill="#000000",outline="#000000")

                                        col="#ffffff"


                                can.create_text(10+x*sz+sz/2,40+y*sz+sz/2,text=str(viewable[y][x]),font=("FreeMono",14),fill=col)






        for v in my_solutions:


                col="blue"



                if sel2==v[-1]:
                        col="cyan"


                if solution[v[1]][v[0]]!=v[-1]:
                        col="red"












                can.create_text(10+v[0]*sz+sz/2,40+v[1]*sz+sz/2,text=v[-1],fill=col, font=("FreeMono",14))




        can.create_line(10,height-10, 10+w_,height-10,fill="#000000",width=2)

        n=1

        for _ in range(9):

                try:
                        v=ava_no.index(n)

                        can.create_text(10+_*sz+sz/2,height-10-sz/2,text=str(n),font=("FreeMono",14),fill="#000000")
                except:
                        pass

                n+=1






        can.create_image(10+5,height-10-sz-20-30-10,image=eraser,anchor="nw")


        notes__=notes
        col1="#000000"

        if view_pos_moves==1:
                notes__=notes2
                col1="#00A546"
        can.create_image(10+30+20+5+10,height-10-sz-20-30-10,image=notes__,anchor="nw")


        write_=write
        col2="#000000"

        if write_st==1:
                write_=write2
                col2="#00A546"


        can.create_image(10+30+20+5+10+60,height-10-sz-20-30-10,image=write_,anchor="nw")







        can.create_text(10+30+20+5+10+60+15,height-10-sz-20+2,text="write",font=("FreeMono",13),anchor="c",fill=col2)

        can.create_text(10,height-10-sz-20+2,text="erase",font=("FreeMono",13),anchor="w")

        can.create_text(10+50+10,height-10-sz-20+2,text="notes",font=("FreeMono",13),anchor="w",fill=col1)

        

        if view_pos_moves==1:
                


                

                for _ in possible_sol:

                        




                        con=0
                        for ms in my_solutions:

                                if _[:2]==ms[:2]:
                                        con=1
                        
                        if con==1:
                                continue




                        vv=sz/3

                        for v in _[-1]:

                                x=10+_[0]*sz
                                y=40+_[1]*sz




                                if v==1:
                                        x+=vv/2
                                        y+=vv/2
                                elif v==2:
                                        x+=vv/2+vv
                                        y+=vv/2
                                elif v==3:
                                        x+=vv/2+vv*2
                                        y+=vv/2
                                elif v==4:
                                        x+=vv/2
                                        y+=vv/2+vv
                                elif v==5:
                                        x+=vv/2+vv
                                        y+=vv/2+vv
                                elif v==6:
                                        x+=vv/2+vv*2
                                        y+=vv/2+vv
                                elif v==7:
                                        x+=vv/2
                                        y+=vv/2+vv*2
                                elif v==8:
                                        x+=vv/2+vv
                                        y+=vv/2+vv*2
                                elif v==9:
                                        x+=vv/2+vv*2
                                        y+=vv/2+vv*2


                                col="#999999"

                                if sel!=0:


                                        if sel[0]==_[0] and sel[1]==_[1]:
                                                col="#ffffff"


                                if v==sel2:
                                        can.create_rectangle(x-vv/2,y-vv/2, x+vv-vv/2,y+vv-vv/2, fill="#000000",outline="#000000")
                                        col="#ffffff"





                                can.create_text(x,y,text=str(v),font=("FreeMono",9),fill=col)














        save()

        


        
        cw=check_win()

        cw=1
        

        

        if cw==1:
                state=3


                draw_transparent_bg(width,height,0,0,15,"#000000",0.5,0)



                xx,yy=200,100

                x_=(width-xx)/2
                y_=(height-yy)/2



                draw_transparent_bg(xx,yy,x_,y_,15,"#000000",0.9,1)

                can.create_line(x_,y_+yy-40, x_+xx,y_+yy-40,fill="#ffffff")
                can.create_text(x_+xx/2,y_+yy-20,text="Quit",fill="red",font=("FreeMono",13))
                can.create_text(x_+xx/2,y_+(yy-40)/2,text="Completed!",fill="#ffffff",font=("FreeMono",13))



                file = open("data/save.txt", "w")
                file.write("")
                file.close()

                cnt=0



def load():
        global solution,viewable,my_solutions,write_ar
        global sel,sel2,view_pos_moves,write_st,write_st2,mistakes,game_mode

        ar=[]

        with open('data/save.txt', 'r') as file:

                for line in file:

                        ar.append(line.strip())



        #solution

        solution=[]


        count=0

        

        for y in range(9):

                ar_=[]

                for n in range(9):

                        ar_.append(int(ar[0][count]))

                        count+=1


                solution.append(ar_)









        #solution

        viewable=[]


        count=0

        

        for y in range(9):

                ar_=[]

                for n in range(9):

                        ar_.append(int(ar[1][count]))

                        count+=1


                viewable.append(ar_)






        #my_solutions

        my_solutions=[]

        ar_=ar[2].split("x")

        ar_.pop(-1)

        if len(ar_)==0:
                my_solutions=[]
        else:

                for _ in ar_:

                        my_solutions.append([int(_[0]),int(_[1]),int(_[2])])




        







        #write_ar

        write_ar=[]

        ar_=ar[3].split("x")

        ar_.pop(-1)

        if len(ar_)==0:
                write_ar=[]
        else:

                for _ in ar_:

                        write_ar.append([int(_[0]),int(_[1]),int(_[2])])







        if ar[4]=="0":
                sel=0
        else:
                sel=[int(ar[4][0]),int(ar[4][1])]


        sel2=int(ar[5])
        view_pos_moves=int(ar[6])
        write_st=int(ar[7])
        write_st2=int(ar[8])
        mistakes=int(ar[9])
        game_mode=ar[10]










def save():
        global solution,viewable,my_solutions,write_ar
        global sel,sel2,view_pos_moves,write_st,write_st2,mistakes,game_mode


        file = open("data/save.txt", "w")
        L = []

        d=""

        for y in solution:
                for x in y:
                        d+=str(x)

        d+="\n"

        L.append(d)






        d=""

        for y in viewable:
                for x in y:
                        d+=str(x)

        d+="\n"

        L.append(d)






        d=""


        for _ in my_solutions:

                d+=str(_[0])
                d+=str(_[1])

                d+=str(_[-1])



                d+="x"

        d+="\n"

        L.append(d)




        d=""


        for _ in write_ar:

                d+=str(_[0])
                d+=str(_[1])

                d+=str(_[-1])

                d+="x"

        d+="\n"

        L.append(d)




        if sel==0:

                L.append(str(sel)+"\n")
        else:
                L.append(str(sel[0])+str(sel[1])+"\n")
        L.append(str(sel2)+"\n")
        L.append(str(view_pos_moves)+"\n")
        L.append(str(write_st)+"\n")        
        L.append(str(write_st2)+"\n")
        L.append(str(mistakes)+"\n")        
        L.append(str(game_mode)+"\n")
        L.append(str(sel2)+"\n")
        L.append(str(view_pos_moves)+"\n")
        L.append(str(write_st)+"\n")        
        L.append(str(write_st2)+"\n")
        L.append(str(mistakes)+"\n")        
        L.append(str(game_mode)+"\n")


        file.writelines(L)
        file.close()

def sel_game_mode():
        global can,state
        global width,height

        state=1


        can.delete("all")


        yv=(height-(40)*5)/2



        can.create_arc(width/2-80-15,yv, width/2-80+15,yv+30, style="arc",outline="#000000",start=90,extent=180)
        can.create_arc(width/2+80-15,yv, width/2+80+15,yv+30, style="arc",outline="#000000",start=270,extent=180)

        can.create_line(width/2-80,yv, width/2+80,yv,fill="#000000")
        can.create_line(width/2-80-1,yv+30, width/2+80,yv+30,fill="#000000")

        can.create_text(width/2,yv+15,text="Easy",font=("FreeMono",13),fill="#000000")








        can.create_arc(width/2-80-15,yv+40, width/2-80+15,yv+30+40, style="arc",outline="#000000",start=90,extent=180)
        can.create_arc(width/2+80-15,yv+40, width/2+80+15,yv+30+40, style="arc",outline="#000000",start=270,extent=180)

        can.create_line(width/2-80,yv+40, width/2+80,yv+40,fill="#000000")
        can.create_line(width/2-80-1,yv+30+40, width/2+80,yv+30+40,fill="#000000")

        can.create_text(width/2,yv+15+40,text="Medium",font=("FreeMono",13),fill="#000000")









        can.create_arc(width/2-80-15,yv+40*2, width/2-80+15,yv+30+40*2, style="arc",outline="#000000",start=90,extent=180)
        can.create_arc(width/2+80-15,yv+40*2, width/2+80+15,yv+30+40*2, style="arc",outline="#000000",start=270,extent=180)

        can.create_line(width/2-80,yv+40*2, width/2+80,yv+40*2,fill="#000000")
        can.create_line(width/2-80-1,yv+30+40*2, width/2+80,yv+30+40*2,fill="#000000")

        can.create_text(width/2,yv+15+40*2,text="Hard",font=("FreeMono",13),fill="#000000")






        can.create_arc(width/2-80-15,yv+40*3, width/2-80+15,yv+30+40*3, style="arc",outline="#000000",start=90,extent=180)
        can.create_arc(width/2+80-15,yv+40*3, width/2+80+15,yv+30+40*3, style="arc",outline="#000000",start=270,extent=180)

        can.create_line(width/2-80,yv+40*3, width/2+80,yv+40*3,fill="#000000")
        can.create_line(width/2-80-1,yv+30+40*3, width/2+80,yv+30+40*3,fill="#000000")

        can.create_text(width/2,yv+15+40*3,text="Expert",font=("FreeMono",13),fill="#000000")





        can.create_arc(width/2-80-15,yv+40*4, width/2-80+15,yv+30+40*4, style="arc",outline="#000000",start=90,extent=180)
        can.create_arc(width/2+80-15,yv+40*4, width/2+80+15,yv+30+40*4, style="arc",outline="#000000",start=270,extent=180)

        can.create_line(width/2-80,yv+40*4, width/2+80,yv+40*4,fill="#000000")
        can.create_line(width/2-80-1,yv+30+40*4, width/2+80,yv+30+40*4,fill="#000000")

        can.create_text(width/2,yv+15+40*4,text="Nightmare",font=("FreeMono",13),fill="#000000")


def init_im():
        global eraser,notes,notes2,exit,write,write2

        eraser=ImageTk.PhotoImage(file="data/eraser.png")
        notes=ImageTk.PhotoImage(file="data/notes.png")
        notes2=ImageTk.PhotoImage(file="data/notes2.png")

        write=ImageTk.PhotoImage(file="data/write.png")
        write2=ImageTk.PhotoImage(file="data/write2.png")

        exit=ImageTk.PhotoImage(file="data/exit.png")


cnt=0


solution=[]
viewable=[]
my_solutions=[]
possible_sol=[]

sel=0
sel2=0

eraser=0
notes=0

eraser_=0
notes_=0

view_pos_moves=0

game_mode=""
mistakes=0

exit=0
exit_=0

notes2=0
write2=0


write_st=0
write_st2=0
write_ar=[]

ava_no=[]

root=tk.Tk()

wd=root.winfo_screenwidth()
ht=root.winfo_screenheight()


width=450
height=600

root.geometry(str(width)+"x"+str(height)+"+"+str(int((wd-450)/2))+"+0")
root.title("Sudoku")

root.resizable(0,0)
root.iconbitmap("data/icon.ico")


can=tk.Canvas(width=width,height=height,relief="flat",highlightthickness=0,border=0,bg="#ffffff")
can.place(in_=root,x=0,y=0)
can.bind("<Button-1>",b1)


try:


        with open('data/save.txt', 'r') as file:

                
                if file.read()=="":
                        cnt=0
                else:
                        cnt=1

except:
        cnt=0




init_im()

intro()
root.mainloop()



