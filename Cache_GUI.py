#import tkinter as tk
#from tkinter import ttk
from tkinter import *
from Cache_Algorithm import Cache_Algorithm
 
class Window:
    def __init__(self, master):

        title1 = Label(master, text= "CSC512C/GO2 - Cache Simulation", font=("Arial Black",25), bg="#243e36", fg="white", padx= 700,anchor = CENTER)
        subtitle1 = Label(master, text= "4-Way Block Set Associative (Least Recently Used)", font=("Arial",15), bg="#7ca982", fg="white", padx= 700,anchor = CENTER)
        subtitle2 = Label(master, text= "Calamiong, Yno Andrei | Santiago, Charl Joseph", font=("Arial",8), bg="#7ca982", fg="white", padx= 700,anchor = CENTER)

        title1.pack(side="top")
        subtitle1.pack(side="top")
        subtitle2.pack(side="bottom")

        lowerframe = Frame(master)
        detailsframe = Frame(lowerframe, background="#f1f7ed",width=30)
        detailsframe.pack(expand = False, fill = Y, side=LEFT)


        ##################################
        specs_frame = Frame(detailsframe, background="#f1f7ed",width=30)
        specs_frame.pack(expand = False, fill = BOTH, side=TOP)
        info = Label(specs_frame, text = "SPECIFICATIONS",font=("Arial Black",20,'bold'),bg='#243e36',fg='white').pack(fill=X)
        info1 = Label(specs_frame, text = "Number of cache blocks: 32 blocks",font=("Arial",10,'bold'),anchor=W).pack(fill=X)
        info2 = Label(specs_frame, text = "Number of memory blocks: 1024 blocks",font=("Arial",10,'bold'),anchor=W).pack(fill=X)
        info3 = Label(specs_frame, text = "Cache line: 16 words",font=("Arial",10,'bold'),anchor=W).pack(fill=X)
        info4 = Label(specs_frame, text = "Read policy: Non Load-Through",font=("Arial",10,'bold'),anchor=W).pack(fill=X)

        ##################################
        step_by_step_var = BooleanVar()
        step_by_step_checkbox = Checkbutton(detailsframe, text="Step-by-Step Animation", variable=step_by_step_var, 
                                            background="#f1f7ed",font=("Arial",10,'bold')).pack(fill=X)

        ##################################
        space_frame = Frame(detailsframe, background="#f1f7ed",width=30,height=10).pack(fill=X,side=TOP)

        simulation_button_frame = Frame(detailsframe, background="#f1f7ed",width=35)
        simulation_button_frame.pack(expand = False, fill = BOTH, side=TOP,anchor=CENTER)
        sequential_button = Button(simulation_button_frame, relief=GROOVE, 
                                   text="Sequential",height=2, width=11, bg="#243e36", fg="white",  font=("Arial",10,'bold'),
                                   command=lambda: self.run_simulation("Sequential", step_by_step_var.get())).pack(side=LEFT)
        
        random_button = Button(simulation_button_frame, relief=GROOVE, 
                               text="Random",height=2, width=11, bg="#243e36", fg="white",  font=("Arial",10,'bold'),
                               command=lambda: self.run_simulation("Random", step_by_step_var.get())).pack(side=LEFT)

        midrange_button = Button(simulation_button_frame, relief=GROOVE, 
                                 text="Mid-Repeat",height=2, width=11, bg="#243e36", fg="white",  font=("Arial",10,'bold'),
                                 command=lambda: self.run_simulation("Mid-Repeat", step_by_step_var.get())).pack(side=LEFT)


        ##################################
        reset_button = Button(detailsframe, relief=GROOVE, 
                              text="Reset",height=1, width=30, bg="#243e36", fg="white",  font=("Arial Black",10),
                              command=self.reset_display)
        reset_button.pack(expand = False, fill = BOTH, side=TOP,anchor=CENTER)

        ##################################
        space_frame = Frame(detailsframe, background="#f1f7ed",width=30,height=10).pack(fill=X,side=TOP)

        output_frame = Frame(detailsframe, background="#f1f7ed",width=30)
        output_frame.pack(expand = True, fill = BOTH, side=TOP)
        out = Label(output_frame, text = "OUTPUT",font=("Arial Black",20,'bold'),bg='#243e36',fg='white').pack(fill=X)
        out1 = Label(output_frame, text = "Memory Access Count:",font=("Arial",10,'bold'),anchor=W).pack(fill=X)
        self.res1_var = StringVar()
        res1 = Label(output_frame, textvariable=self.res1_var, font=("Arial",10,),anchor=W,background="#f1f7ed").pack(fill=X)
        out2 = Label(output_frame, text = "Cache Hit Count: 1024 blocks",font=("Arial",10,'bold'),anchor=W).pack(fill=X)
        self.res2_var = StringVar()
        res2 = Label(output_frame, textvariable=self.res2_var, font=("Arial",10,),anchor=W,background="#f1f7ed").pack(fill=X)
        out3 = Label(output_frame, text = "Cache Miss Count",font=("Arial",10,'bold'),anchor=W).pack(fill=X)
        self.res3_var = StringVar()
        res3 = Label(output_frame, textvariable=self.res3_var, font=("Arial",10,),anchor=W,background="#f1f7ed").pack(fill=X)
        out4 = Label(output_frame, text = "Cache Hit Rate",font=("Arial",10,'bold'),anchor=W).pack(fill=X)
        self.res4_var = StringVar()
        res4 = Label(output_frame, textvariable=self.res4_var, font=("Arial",10,),anchor=W,background="#f1f7ed").pack(fill=X)
        out5 = Label(output_frame, text = "Cache Miss Rate",font=("Arial",10,'bold'),anchor=W).pack(fill=X)
        self.res5_var = StringVar()
        res5 = Label(output_frame, textvariable=self.res5_var, font=("Arial",10,),anchor=W,background="#f1f7ed").pack(fill=X)
        out6 = Label(output_frame, text = "Average Memory Access Time",font=("Arial",10,'bold'),anchor=W).pack(fill=X)
        self.res6_var = StringVar()
        res6 = Label(output_frame, textvariable=self.res6_var, font=("Arial",10,),anchor=W,background="#f1f7ed").pack(fill=X)
        out7 = Label(output_frame, text = "Total Memory Access Time",font=("Arial",10,'bold'),anchor=W).pack(fill=X)
        self.res7_var = StringVar()
        res7 = Label(output_frame, textvariable=self.res7_var, font=("Arial",10,),anchor=W,background="#f1f7ed").pack(fill=X)


        ##################################
        subframe2 = Frame(lowerframe, background="#f1f7ed")
        subframe2.pack(expand=True, fill=BOTH, side=LEFT,padx=10)
        scrollbar = Scrollbar(subframe2, orient=VERTICAL)
        self.result_text = Text(subframe2,background="#f1f7ed",state=DISABLED,width=10,yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.result_text.pack(expand=True, fill=BOTH, side=LEFT)


 
        subframe3 = Frame(lowerframe, background="#f1f7ed")
        seq_table = Label(subframe3, text= "Sequence Hit/Miss Block")
        seq_table.place(relx=0.5, rely=0.5,anchor=CENTER)
        subframe3.pack(expand=True, fill=BOTH, side=LEFT, padx = 5)
        
        lowerframe.pack(expand = True, fill = BOTH ,padx=10,pady=5, side = "bottom")

    def run_simulation(self, test_case, state):
        self.result_text["state"]=NORMAL
        
        self.result_text.delete(1.0, END)
        simulator = Cache_Algorithm(8, 64, 'non-load-through', 8, 4)

        simulator.run_simulation(test_case, state)
        if state:
            for cache_snapshot in simulator.trace:
                self.result_text.insert(END, cache_snapshot)
        else:
            self.result_text.insert(END, "".join(simulator.trace))

        self.result_text.insert(END, "Simulation Completed!\n")
        self.result_text["state"]=DISABLED
        self.res1_var.set(simulator.access_count)
        self.res2_var.set(simulator.hit_count)
        self.res3_var.set(simulator.miss_count)
        self.res4_var.set(simulator.hit_rate)
        self.res5_var.set(simulator.miss_rate)
        self.res6_var.set(simulator.avg_access_time)
        self.res7_var.set(simulator.total_access_time)


    def reset_display(self):
        self.result_text["state"]=NORMAL
        self.result_text.delete(1.0, END)
        self.result_text["state"]=DISABLED

if __name__ == "__main__":
    root = Tk()
    root.geometry('1000x750')
    root.configure(bg='#f1f7ed')

    root.title("CSC512C/GO2 - Cache Simulation")
    window = Window(root)
    root.mainloop()
