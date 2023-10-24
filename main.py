import tkinter as tk
from tkmacosx import CircleButton
from PIL import ImageTk, Image
import time
from ctypes import *
root = tk.Tk()

root.geometry('1000x1000')

class App(object):
    def __init__(self, master):
        self._master = master
        self._btn_matrix = []
        self._menu_matrix=[]
        self.rounds = 0
        self.rounds_list = []
        self.mix_counter=0
        
        self.done_mix = False
        self.done = " "
        self.round_count=1
        self.color_counter=0
        self.timespeed= 0 
        self.index=[]
        self.mix_indicator=''
        self.color = " "

        self.m=[]
        self.mix_list=[]
        

        self.frame2 = tk.LabelFrame(master,bg="white",padx=30, pady=30)
        self.frame2.place (x = 310, y = 0 )

        
        self.frame_replay= tk.Frame(padx=15, pady=15)
        self.frame_replay.place(x=820,y=25)

        replay_button = CircleButton(self.frame_replay, bg='red',fg='white', text='Replay')
        replay_button['command']=self.replay_function
        replay_button.pack()



        self.frame_clear = tk.Frame(padx=15, pady=15)
        self.frame_clear.place(x=1020,y=25)
        clear_button = CircleButton(self.frame_clear,bg='blue',fg='white',text='Clear board')
        clear_button['command']=self.clear_function
        clear_button.pack()

        self.frame_end_replay = tk.Frame(padx=15, pady=15)
        self.frame_end_replay.place(x=920,y=25)
        end_replay_btn = CircleButton(self.frame_end_replay,bg='green',fg='white',text='End replay')
        end_replay_btn['command']=self.back
        end_replay_btn.pack()

        self.frame3 = tk.LabelFrame(padx=15, pady=15, text= "GENERATE")
        self.frame3.place(x=830, y=220)

        self.generate_button = tk.Button(text='Generate')
        self.generate_button['command'] = self.show_Index
        self.generate_button.place(x=830, y=150)

        self.generate_label = tk.Text(self.frame3, height=12, width = 20)
        self.generate_label.pack_forget()

        self.clgenerate_button = tk.Button(text = "Clear Generate", command=lambda: self.generate_label.delete(1.0,tk.END))

        self.clgenerate_button.place(x=920, y= 150)
    
        frame4 = tk.LabelFrame(master, fg="black" )
        frame4.place(x=80,y=50)
        self.label1_color = tk.Button(frame4,text = "Color",bg = "white",fg = "black",height=1,width=9, font = ("Arial Bold", 9))
        self.label1_color.grid(row =0,column=0)
        self.label2_color = tk.Button(frame4, text = "Speed", bg ="white",fg = "black",height=1,width=9, font = ("Arial Bold", 9))
        self.label2_color.grid(row= 0, column=1 )
        self.label3_color = tk.Button (frame4, bg = "#7df208",height=1,width=9)
        self.label3_color.grid(row =1, column=0)
        self.label3_color['command']= self.get_color1
        self.label4_color = tk.Button(frame4,bg = "#ffe838",height=1,width=9)
        self.label4_color.grid(row =2, column =0)
        self.label4_color['command']= self.get_color2
        self.label5_color = tk.Button(frame4,bg = "#88c4fc",height=1,width=9)
        self.label5_color.grid(row =3, column =0)
        self.label5_color['command']= self.get_color3
        self.label6_color = tk.Button(frame4,bg = "#f79b5f",height=1,width=9)
        self.label6_color.grid(row =4, column =0)
        self.label6_color['command']= self.get_color4
        self.label7_color = tk.Button(frame4,bg = "#ff9696",height=1,width=9)
        self.label7_color.grid (row =5, column =0)
        self.label7_color['command']= self.get_color5
        self.label_color = tk.Button(frame4, bg = "white",height=1,width=9)
        self.label_color.grid (row =6, column =0)
        self.label_color['command']= self.get_color6
        self.label8_color = tk.Entry (frame4, bg = "white",width=9)
        self.label8_color.insert(0, 20)
        self.label8_color.grid (row =1, column =1)
        self.label9_color = tk.Entry(frame4,bg = "white",width=9)
        self.label9_color.insert(0, 30)
        self.label9_color.grid (row =2, column =1)
        self.label10_color = tk.Entry(frame4,bg = "white", width=9)
        self.label10_color.insert(0, 50)
        self.label10_color.grid (row =3, column =1)
        self.label11_color = tk.Entry(frame4,bg = "white", width=9)
        self.label11_color.insert(0, 500)
        self.label11_color.grid (row =4, column =1)
        self.label12_color = tk.Entry(frame4,bg = "white", width=9)
        self.label12_color.insert(0, 200)
        self.label12_color.grid (row =5, column =1)


        

        for col in range(0,12):
            row_matrix = []
            for row in range(0,12):
                btn = tk.Button(self.frame2, bg = 'white', image=self.asphalt_photo_new, text= " ",command =lambda x=row, y=col : self.update(x,y), highlightthickness=0)    
                btn.grid(row = row, column = col, padx=0, pady=0)
                
                row_matrix.append(btn)                    
            self._btn_matrix.append(row_matrix)
         
        
        for col in range(0,12):
            menu_rowmatrix=[]
            for row in range(0,12):
                my_menu=tk.Menu(master, tearoff=False)
                my_menu.add_command(label="Mix", command=lambda a=row, b=col: self.mix(a,b))
                my_menu.add_command(label="Escape", command=lambda a=row, b=col: self.escape(a,b))
                my_menu.add_command(label="Dispense", command=lambda a=row, b=col: self.dispense(a,b))
                my_menu.add_command(label="Start", command=lambda a=row, b=col: self.start(a,b))
                my_menu.add_command(label="End", command=lambda a=row, b=col: self.end(a,b))
                my_menu.add_command(label="Clear", command=lambda a=row, b=col: self.clear(a,b))
                my_menu.add_command(label="Exit", command=root.quit)
                self._btn_matrix[col][row].bind("<Button-3>", lambda evt, x=row, y=col: self.my_popup(evt,x,y))
                menu_rowmatrix.append(my_menu)
                
              
            
            self._menu_matrix.append(menu_rowmatrix)

    def get_color1(self):
            self.color = "#7df208"
    def get_color2(self):
            self.color = "#ffe838"
    def get_color3(self):
            self.color = "#88c4fc"
    def get_color4(self):
            self.color = "#f79b5f"
    def get_color5(self):
            self.color = "#ff9696"
    def get_color6(self):
            self.color = "white"
            
    
    frame1= tk.Frame(padx=0, pady=0)

    frame1.place(x=80, y=270)
    
    key_photo=Image.open("key.png")

    key_photo2=key_photo.resize((150,140))

    key_photo_new=ImageTk.PhotoImage(key_photo2)

    label=tk.Label(frame1, image=key_photo_new)

    label.pack()

    m_photo=Image.open("m.png")

    m_photo2=m_photo.resize((30,30))

    m_photo_new=ImageTk.PhotoImage(m_photo2)

    E_photo=Image.open("E.png")

    E_photo2=E_photo.resize((30,30))

    E_photo_new=ImageTk.PhotoImage(E_photo2)

    tri_photo=Image.open("delta.png")

    tri_photo2=tri_photo.resize((30,30))

    tri_photo_new=ImageTk.PhotoImage(tri_photo2)

    dispense_photo=Image.open("alpha2.png")

    dispense_photo2=dispense_photo.resize((30,30))

    dispense_photo_new=ImageTk.PhotoImage(dispense_photo2)

 

    asphalt_photo=Image.open("asfalt-light.png")

    asphalt_photo2=asphalt_photo.resize((30,30))

    asphalt_photo_new=ImageTk.PhotoImage(asphalt_photo2)

    leftarrow_photo=Image.open("leftarrow.png")

    leftarrow_photo2=leftarrow_photo.resize((30,30))

    downarrow_photo2= leftarrow_photo2.rotate(90)
    
    rightarrow_photo2 = downarrow_photo2.rotate(90)

    uparrow_photo2 = rightarrow_photo2.rotate(90)

    leftarrow_photo_new=ImageTk.PhotoImage(leftarrow_photo2)

    downarrow_photo_new =ImageTk.PhotoImage(downarrow_photo2)

    uparrow_photo_new = ImageTk.PhotoImage(uparrow_photo2)

    rightarrow_photo_new =ImageTk.PhotoImage(rightarrow_photo2)

    dot_photo=Image.open("blackdot.png")

    dot_photo_2=dot_photo.resize((30,30))

    dot_photo_new=ImageTk.PhotoImage(dot_photo_2)


    x_photo=Image.open("x.png")

    x_photo2=x_photo.resize((30,30))

    x_photo_new=ImageTk.PhotoImage(x_photo2)

    

    def num_rounds(self): 
        total_time = float(self.total_entry.get()) * 1000
        step_time = float(self.step_entry.get())
        self.rounds = float(total_time/(step_time*4))
        self.rounds=int(self.rounds)
        self.rounds_list.append(self.rounds)
        round_label = tk.Label(fg="white", bg="blue", text = "Rounds: " + str(self.rounds) )
        round_label.place(x=611, y=552)

   
    
    def mix(self, row, col):
        # self._btn_matrix[col][row].config(image=self.m_photo_new)

        self.clockwise_button_up = tk.Button(bg = "white", text = "Clockwise Up",height=2,width=20, command = lambda x=row, y=col: self.clockwise_up(x,y))
          
        self.counter_clockwise_button_up = tk.Button(bg='white',text='Counter-clockwise Up', height=2, width=20, command=lambda x=row, y=col: self.counter_clockwise_up(x,y) )

        self.clockwise_button_down = tk.Button(bg = "white", text = "Clockwise Down",height=2,width=20, command = lambda x=row, y=col: self.clockwise_down(x,y))
          
        self.counter_clockwise_button_down = tk.Button(bg='white',text='Counter-clockwise Down', height=2, width=20, command = lambda x=row, y=col: self.counter_clockwise_down(x,y)) 

        self.clockwise_button_up.place(x=370,y=600)
        
        self.counter_clockwise_button_up.place(x=570,y=600)
        
        self.clockwise_button_down.place(x=370, y=650)

        self.counter_clockwise_button_down.place(x=570,y=650)

        self.step_label = tk.Label(fg="black", bg="white", text = "Step Time (ms): ")

        self.step_label.place(x=370, y=505)

        self.step_entry = tk.Entry(fg="black", bg="white", width=5)

        self.step_entry.place(x=470, y=505)

        self.total_label = tk.Label(fg="black", bg="white", text="Total Time (s): ")

        self.total_entry = tk.Entry(fg="black", bg="white", width=5)

        self.total_label.place(x=370, y=555)

        self.total_entry.place(x=470, y=555)

        self.mix_button = tk.Button(fg="white", bg="red", text="Mix", height =2 , width=10)

        self.mix_button.place(x=600, y= 500)

        self.mix_button['command'] = self.num_rounds

       
        
    # canvas = tk.Canvas(width=1000, height=1000)

    # canvas.pack()
    

    def escape(self, row, col):
        self._btn_matrix[col][row].config(image=self.E_photo_new)

    def dispense(self, row, col):
        self._btn_matrix[col][row].config(image=self.dispense_photo_new )

    def start(self, row, col):
        self._btn_matrix[col][row].config(image=self.tri_photo_new )

    def end(self, row, col):
        self._btn_matrix[col][row].config(image=self.x_photo_new )
    
    def clear(self, row, col):
        self._btn_matrix[col][row].config(image=self.asphalt_photo_new)

    def clearMix(self, row, col):
        self._btn_matrix[col][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col][row-1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row-1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row-1].config(image=self.asphalt_photo_new)
        
        self.mix_list.clear()
    
    
    
    
    def show_Index(self):
        self.generate_label.config(state=tk.NORMAL)
        self.generate_label.delete(1.0,tk.END)
        
        index_list=[]
        for i in range(0, len(self.index)):
            col = self.index[i][0]
            row = self.index[i][1]
            color = self.index[i][2]
            time = 0
            index = 12*row + col
            
            if color=='#7df208':
                time=float(self.label8_color.get())
            elif color=="#ffe838":
                time=float(self.label9_color.get())
            elif color=="#88c4fc":
                time=float(self.label10_color.get())
            elif color=="#f79b5f":
                time=float(self.label11_color.get())
            elif color=="#ff9696":
                time=float(self.label12_color.get())
            
            if time>1000:
                seconds = int(time/1000)
                ms = time - seconds 
                cs = int(ms/10)
                new_list=[]
                new_list.append(index)
                new_list.append(',')
                new_list.append(seconds)
                new_list.append(',')
                new_list.append(cs)
                new_list.append(',')
                index_list.append(new_list)
                
            else:
                new_list_two=[]
                new_time = int(time/10)
                new_list_two.append(index)
                new_list_two.append(',')
                new_list_two.append(0)
                new_list_two.append(',')
                new_list_two.append(new_time)
                new_list_two.append(',')
                index_list.append(new_list_two)
        
        
                
        
        for i in range(0, len(index_list)):
            self.generate_label.insert(tk.END, index_list[i])
            self.generate_label.insert(tk.END, '\n')
        
    

        
        self.generate_label.pack()
    

    
        


            
        
    
    


            
    
    
    
    def clockwise_up(self, row, col):
        self._btn_matrix[col][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col][row-1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row-1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row-1].config(image=self.asphalt_photo_new)
       
        self._btn_matrix[col][row].config(image=self.uparrow_photo_new)
        self._btn_matrix[col][row-1].config(image=self.rightarrow_photo_new)
        self._btn_matrix[col+1][row-1].config(image=self.downarrow_photo_new)
        self._btn_matrix[col+1][row].config(image=self.leftarrow_photo_new)
        
        mixx_list=[]
        mixx_list.append([col,row,self._btn_matrix[col][row].cget('bg'),self.uparrow_photo_new])
        mixx_list.append([col,row-1,self._btn_matrix[col][row-1].cget('bg'),self.rightarrow_photo_new])
        mixx_list.append([col+1,row-1,self._btn_matrix[col+1][row-1].cget('bg'),self.downarrow_photo_new])
        mixx_list.append([col+1,row,self._btn_matrix[col+1][row].cget('bg'),self.leftarrow_photo_new]) 
        mixx_list.append([col,row,self._btn_matrix[col][row].cget('bg'),self.uparrow_photo_new])
        self.mix_list.append(mixx_list)


    #----
    def counter_clockwise_up(self, row, col):
        self._btn_matrix[col][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col][row-1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row-1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row-1].config(image=self.asphalt_photo_new)
        

        self._btn_matrix[col][row].config(image=self.uparrow_photo_new)
        self._btn_matrix[col][row-1].config(image=self.leftarrow_photo_new)
        self._btn_matrix[col-1][row-1].config(image=self.downarrow_photo_new)
        self._btn_matrix[col-1][row].config(image=self.rightarrow_photo_new)
       
        mixx_list=[]
        mixx_list.append([col,row,self._btn_matrix[col][row].cget('bg'),self.uparrow_photo_new])
        mixx_list.append([col,row-1,self._btn_matrix[col][row-1].cget('bg'),self.leftarrow_photo_new])
        mixx_list.append([col-1,row-1,self._btn_matrix[col-1][row-1].cget('bg'),self.downarrow_photo_new])
        mixx_list.append([col-1,row,self._btn_matrix[col-1][row].cget('bg'),self.rightarrow_photo_new])
        mixx_list.append([col,row,self._btn_matrix[col][row].cget('bg'),self.uparrow_photo_new])
        self.mix_list.append(mixx_list)
        

        
    
    def counter_clockwise_down(self, row, col):
        self._btn_matrix[col][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col][row-1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row-1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row-1].config(image=self.asphalt_photo_new)

        self._btn_matrix[col][row].config(image=self.downarrow_photo_new)
        self._btn_matrix[col][row+1].config(image=self.rightarrow_photo_new)
        self._btn_matrix[col+1][row+1].config(image=self.uparrow_photo_new)
        self._btn_matrix[col+1][row].config(image=self.leftarrow_photo_new)

        mixx_list=[]
        mixx_list.append([col,row,self._btn_matrix[col][row].cget('bg'),self.downarrow_photo_new])
        mixx_list.append([col,row+1,self._btn_matrix[col][row+1].cget('bg'),self.rightarrow_photo_new])
        mixx_list.append([col+1,row+1,self._btn_matrix[col+1][row+1].cget('bg'),self.uparrow_photo_new])
        mixx_list.append([col+1,row,self._btn_matrix[col+1][row].cget('bg'),self.leftarrow_photo_new])
        mixx_list.append([col,row,self._btn_matrix[col][row].cget('bg'),self.downarrow_photo_new])
        self.mix_list.append(mixx_list)
        

    def clockwise_down(self, row, col):
        # self._btn_matrix[col][row].config(text = "Clockwise Down")
        self._btn_matrix[col][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col][row-1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row-1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row].config(image=self.asphalt_photo_new)
        self._btn_matrix[col-1][row+1].config(image=self.asphalt_photo_new)
        self._btn_matrix[col+1][row-1].config(image=self.asphalt_photo_new)

       
        self._btn_matrix[col][row].config(image=self.downarrow_photo_new,)
        self._btn_matrix[col][row+1].config(image=self.leftarrow_photo_new)
        self._btn_matrix[col-1][row+1].config(image=self.uparrow_photo_new)
        self._btn_matrix[col-1][row].config(image=self.rightarrow_photo_new)

        mixx_list=[]
        mixx_list.append([col,row,self._btn_matrix[col][row].cget('bg'),self.downarrow_photo_new])
        mixx_list.append([col,row+1,self._btn_matrix[col][row+1].cget('bg'),self.leftarrow_photo_new])
        mixx_list.append([col-1,row+1,self._btn_matrix[col-1][row+1].cget('bg'),self.uparrow_photo_new])
        mixx_list.append([col-1,row,self._btn_matrix[col-1][row].cget('bg'), self.rightarrow_photo_new])
        mixx_list.append([col,row,self._btn_matrix[col][row].cget('bg'),self.downarrow_photo_new])

        self.mix_list.append(mixx_list)

    

   
        







    def my_popup(self, event, row, col):
        self._menu_matrix[col][row].tk_popup(event.x_root, event.y_root)
            
           
    
    def update(self, row, col):
        
        # if(self._btn_matrix[col][row].cget("bg")=='white'):
        #     self._btn_matrix[col][row].config( bg = '#7df208' )
        if(self._btn_matrix[col][row].cget("bg")=='white'):
            self.color_counter=self.color_counter+1
            self._btn_matrix[col][row].config( text = self.color_counter )
        self._btn_matrix[col][row].config( bg = self.color )

        if self.color == "white":
            self.color_counter = self.color_counter-1
            self._btn_matrix[col][row].config(text='' ) 

        # elif(self._btn_matrix[col][row].cget("bg")=='#7df208'):
        #     self._btn_matrix[col][row].config( bg = '#ffe838' )
        # elif(self._btn_matrix[col][row].cget("bg")=='#ffe838'):
        #     self._btn_matrix[col][row].config( bg = '#88c4fc' )
        # elif(self._btn_matrix[col][row].cget("bg")=='#88c4fc'):
        #     self._btn_matrix[col][row].config( bg = '#f79b5f' )
        # elif(self._btn_matrix[col][row].cget("bg")=='#f79b5f'):
        #     self._btn_matrix[col][row].config( bg = '#ff9696' )
        # elif(self._btn_matrix[col][row].cget("bg")=='#ff9696'):
        #     self._btn_matrix[col][row].config( bg = 'white' )
        #     self.color_counter=self.color_counter-1
    
    def replay_function(self):
        self.index.clear()
        count=1
        while(count<=self.color_counter):
            for col in range(0,12):
                for row in range(0,12):
                    if self._btn_matrix[col][row].cget('text')==count:
                        color = self._btn_matrix[col][row].cget('bg')
                        image = self._btn_matrix[col][row].cget('image')
                        self.index.append([col,row,color,image])
            count=count+1
    
    

        # self._master.after(500, self.replay_flash)
        for col in range (0,12):
            for row in range(0,12):
                self._btn_matrix[col][row].config(image=self.asphalt_photo_new)
                self._btn_matrix[col][row].config(bg='gray')
        self.frame1.config(bg='gray')
        self.frame2.config(bg='gray')
        self.frame3.config(bg='gray')
        self.frame_clear.config(bg='gray')
        self.frame_replay.config(bg='gray')
        self.frame_end_replay.config(bg='gray')
        root.config(bg='gray')
        
        i=0
        k=0
        self._master.after(1000, self.time, i, k)
    
    

            

    def time(self, i,k):
        if len(self.mix_list)>0:
            for a in range(0,len(self.mix_list)):
                for b in range(0,len(self.mix_list[0])):
                    coll=self.mix_list[a][b][0]
                    rww=self.mix_list[a][b][1]
                    self.mix_list[a][b][2]= self._btn_matrix[coll][rww].cget('bg')
        button= self.index[i]
        self.coll=button[0]
        self.roww = button[1]
        colorr = button[2]
        img = button[3]
        if colorr=='#7df208':
            self.timespeed = int(self.label8_color.get())
        elif colorr=="#ffe838":
            self.timespeed=int(self.label9_color.get())
        elif colorr=="#88c4fc":
            self.timespeed=int(self.label10_color.get())
        elif colorr=="#f79b5f":
            self.timespeed=int(self.label11_color.get())
        elif colorr=="#ff9696":
            self.timespeed=int(self.label12_color.get())
        self._btn_matrix[self.coll][self.roww].config(image = self.dot_photo_new, bg= colorr) 

        if i>0:
            past_btn= self.index[i-1]
            past_col=past_btn[0]
            past_row = past_btn[1]
            past_bg=past_btn[2]
            past_img = past_btn[3]
            self._btn_matrix[past_col][past_row].config(image = past_img, bg = past_bg)
            
            # if (past_col==self.mix_list[1][0] and past_row==self.mix_list[1][1] and past_col) or (past_col==self.mix_list[2][0] and past_row==self.mix_list[2][1]) or (past_col==self.mix_list[3][0] and past_row==self.mix_list[3][1]):
            #     if(past_col<self.coll) or (past_row<self.roww):
            #         self._btn_matrix[past_col][past_row].config(image = self.asphalt_photo_new)
            
        
        if len(self.mix_list)>0:
            if k<len(self.mix_list):
                self.m = self.mix_list[k]
                mix_start_col = self.m[0][0]
                mix_start_row = self.m[0][1]
                if self.roww==mix_start_row and self.coll==mix_start_col:
                    self.time2(1,i,k)
                else:
                    if ((i+1)<len(self.index)):
                        self._btn_matrix[self.coll][self.roww].after(self.timespeed, self.time, i+1, k)     
            else:
                if ((i+1)<len(self.index)):
                    self._btn_matrix[self.coll][self.roww].after(self.timespeed, self.time, i+1, k)
        else:
            if ((i+1)<len(self.index)):
                    self._btn_matrix[self.coll][self.roww].after(self.timespeed, self.time, i+1, k)

        self.round_count=1




    def back(self):
        self.frame1.config(bg='white')
        self.frame2.config(bg='white')
        self.frame3.config(bg='white')
        self.frame_clear.config(bg='white')
        self.frame_replay.config(bg='white')
        self.frame_end_replay.config(bg="white")
        root.config(bg='white')
        for col in range (0,12):
            for row in range(0,12):
                self._btn_matrix[col][row].config(image=self.asphalt_photo_new)
                self._btn_matrix[col][row].config(bg='white')
        for w in self.index:
            clll=w[0]
            rwww = w[1]
            clrrr = w[2]
            imggg = w[3]
            self._btn_matrix[clll][rwww].config(bg=clrrr, image = imggg)
        for a in range(0,len(self.mix_list)):
            for b in range(1, 4):
                cllll=self.mix_list[a][b][0]
                rwwww = self.mix_list[a][b][1]
                clrrrr = self.mix_list[a][b][2]
                imgggg = self.mix_list[a][b][3]
                self._btn_matrix[cllll][rwwww].config(image = imgggg)
            
        
        
    
   
    def time2(self,j,i,k):
            btn = self.m[j]
            self.cl=btn[0]
            self.rw = btn[1]
            clrr=btn[2]
            imgg=btn[3]
            self._btn_matrix[self.cl][self.rw].config(image=self.dot_photo_new)
            #mouse-heree
            if j>0:
                past_btnn = self.m[j-1]
                past_cll=past_btnn[0]
                past_rww = past_btnn[1]
                past_clrr = past_btnn[2]
                past_imgg=past_btnn[3]
                self._btn_matrix[past_cll][past_rww].config(image=past_imgg)
            j=j+1
            
            if(j<len(self.m)):
                self._btn_matrix[self.cl][self.rw].after(self.step_entry.get(), self.time2, j,i,k)
            elif self.round_count<self.rounds_list[k]:
                self.round_count=self.round_count+1
                j=1
                self._btn_matrix[self.cl][self.rw].after(self.step_entry.get(), self.time2, j,i,k)
            else:
                # self.done="done"
                if ((i+1)<len(self.index)) and k<len(self.mix_list):
                    self._btn_matrix[self.coll][self.roww].after(self.timespeed, self.time, i+1, k+1)
    
    

    def clear_function(self):
        for col in range(0,12):
            for row in range(0,12):
                self._btn_matrix[col][row].config(text=' ')
                self._btn_matrix[col][row].config(image=self.asphalt_photo_new)
                self._btn_matrix[col][row].config(bg='white')
        self.mix_list.clear()
                




    

 
if __name__ == '__main__':
    app =App(root)
    root.mainloop()