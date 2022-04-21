# GUI

import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import control

E = tk.E
W = tk.W
N = tk.N
S = tk.S

class ControlsApplication(tk.Frame):
    def __init__(self):
        # Lay out the master grid
        master = tk.Tk()
        master.geometry("1000x750")
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Control Systems Design")
        tx_lbls = np.array(['Plant Numerator', 'Plant Denominator', 'Controller Numerator', 'Controller Denominator',\
                         'Gain (K)','Wn/Zeta','Poles/Zeros', 'L(s)', 'TF', 'Stability'])
        btn_lbls = np.array(['Calculate', 'Root Locus' ,'Bode Plot', 'Nyquist Plot', 'Step-Response'])
        
        # Configure rows
        for r in range(5):
            self.master.rowconfigure(r, weight=1)  
            
        # Configure columns
        column = 5 # Design with 5 columns
        # Labels for input
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            tx = tk.Text(master,bg='purple',fg='white')
            tx.grid(row=0,column=c,sticky=W+E+N+S)
            tx.insert('1.0',tx_lbls[c])
            tx.configure(state="disabled")
        
        
        # Text boxes for input
        txIns = []
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            tx = tk.Text(master)
            tx.grid(row=1,column=c,sticky=W+E+N+S)
            if c == 1:
                tx.insert('1.0','1,1,0')
            else:
                tx.insert('1.0','1')
            txIns.append(tx)
        
        # Labels for output
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            tx = tk.Text(master,bg='green',fg='yellow')
            tx.grid(row=2,column=c,sticky=W+E)
            tx.insert('1.0',tx_lbls[c+column])
            tx.configure(state="disabled")
            
        # Text boxes for output
        txOuts = []
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            tx=tk.Text(master)
            tx.grid(row=3,column=c,sticky=W+E+N+S)
            txOuts.append(tx)
            tx.insert('1.0','[calc]')
            
            
        for c in range(1):
            self.fig = Figure(figsize=(8,10))
            fig_plot= self.fig.add_subplot(111)
            canvas = FigureCanvasTkAgg(self.fig, master)
            
            canvas = FigureCanvasTkAgg(self.fig, master)
            plot_widget = canvas.get_tk_widget()
            plot_widget.grid(row=4,column=c, columnspan=5, sticky=E+W+S+W)
            canvas.draw();
            
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            if c == 0:
                btn = tk.Button(master, text=btn_lbls[c],\
                                command = lambda:Calculate(),fg="red");
            elif c == 1:
                btn = tk.Button(master, text=btn_lbls[c],\
                                command = lambda:RootLocus(),fg="red")
            elif c == 2:
                btn = tk.Button(master, text=btn_lbls[c],\
                                command = lambda:Bode(),fg="red")
            elif c == 3:
                btn = tk.Button(master, text=btn_lbls[c],\
                                command = lambda:Nyquist(),fg="red")
            else:
                btn = tk.Button(master, text=btn_lbls[c],\
                                command = lambda:StepResp(),fg="red")
            btn.grid(row=6,column=c,sticky=E+W)
        
        # Function for TF
        def GetTF():
            num = txIns[0].get("1.0", "end-1c")
            num = np.array(num.split(',')).astype(float)
            print(num)
            den = txIns[1].get("1.0", "end-1c")
            den = np.array(den.split(',')).astype(float)
            print(den)
            cnum = txIns[2].get("1.0", "end-1c")
            cnum = np.array(cnum.split(',')).astype(float)
            print(cnum)
            cden = txIns[3].get("1.0", "end-1c")
            cden = np.array(cden.split(',')).astype(float)
            print(cden)
            G = control.tf(num,den);Dc = control.tf(cnum,cden)
            tf = control.minreal(G*Dc)
            return tf
        
        # Function to calculate poles/zeros/wn/z
        def Calculate():
            tf = GetTF()
            K = float(txIns[4].get("1.0", "end-1c"))
            tf_cl = control.minreal(K*tf/(1+K*tf))
            zeros = control.zero(tf)
            poles = control.pole(tf)
            cl_poles = control.pole(tf_cl)
            pid = 0;
            if np.sum(np.iscomplex(cl_poles)) > 0:
                pid = np.nonzero(np.iscomplex(cl_poles))[0][0]
            txOuts[0].delete('1.0','end')
            txOuts[1].delete('1.0','end')
            wn = np.abs(cl_poles[pid])
            wn = np.round(wn,2)
            zeta = np.abs(np.math.cos(np.angle(cl_poles[pid])))
            zeta = np.round(zeta,2)
            str1 = 'wn: ' + str(wn) + ' zeta: ' + str(zeta)
            str2 = 'poles: ' + str(poles) + ' zeros: ' + str(zeros)
            txOuts[0].insert('1.0',str1)
            txOuts[1].insert('1.0',str2)
            txOuts[2].delete('1.0','end')
            txOuts[2].insert('1.0',str(tf))
            txOuts[3].delete('1.0','end')
            txOuts[3].insert('1.0',str(tf_cl))
            
            ##########FROM HW5##################
            # Calculate departures and arrivals 
            n = len(poles)
            p_angs=np.zeros(n) 
            m = len(zeros)
            z_angs=np.zeros(m) 
             
            # Departure angles at poles 
            for i in range(0,n): 
                ang = np.concatenate((np.angle(poles[i]-zeros), -np.angle(poles[i]-poles))) #concatenate 
                ang = np.sum(ang)*180/np.pi -180 -360*(i) #sum 
                ang = np.round(np.mod(ang,360),2) 
                p_angs[i] = ang

            # Arrival angles at zeros 
            for i in range(0,m): 
                ang = np.concatenate((np.angle(zeros[i]-poles), -np.angle(zeros[i]-zeros)))  #concatenate 
                ang = np.sum(ang)*180/np.pi +180 +360*(i) #sum 
                ang = np.round(np.mod(ang,360),2) 
                z_angs[i] = ang 
            print('pole deps: ', p_angs) 
            print ('zero arrivs: ',z_angs) 
             
            # Calculate the n-m asymptotes  
            # Location 
            asym_loc = (np.sum(poles)-np.sum(zeros))/(n-m) #sum 
            asym_loc = np.round(np.real( asym_loc),2) 
            # Angles of n-m branches 
            asym_angs = np.zeros(n-m) 
            print('asymptote alpha: ', asym_loc) 
            for i in range(0,n-m): 
                asym_angs[i] = (180 + 360*i)/(n-m) 
            print('asymptote angles: ', asym_angs) 
             
            # Calculate multiple roots 
            num = np.squeeze(tf.num)
            den = np.squeeze(tf.den)
            num_df = np.polyder(num)
            den_df = np.polyder(den) 
            df = np.polyadd(np.convolve(num_df,den), -np.convolve(den_df,num)) #convolve 
            mroots=np.round(np.roots(df),2) 
            mroots=(mroots[~np.iscomplex(mroots)]) 
            mroots = np.unique(mroots)
            print('multiple roots:', mroots)
            
            
            
        # Function to create the rootlocus
        def RootLocus():
            tf = GetTF()
            print(tf)
            plt.figure()
            control.rlocus(tf,grid=True, print_gain=True)
            canvas.draw()
        
        # Function for Bode plot
        def Bode():
            tf = GetTF()
            print(tf)
            plt.figure()
            control.bode_plot(tf,grid=True)
            canvas.draw()
            
        # Function for Nyquist plot
        def Nyquist():
            return;
            
        # Function to compute and display the step-response
        def StepResp():
            tf = GetTF()
            K = float(txIns[4].get("1.0", "end-1c"))
            tf = control.minreal(K*tf/(1+K*tf))
            print(tf)
            t = np.arange(0,100,.1)
            y0 = control.step_response(tf,t)
            fig_plot.clear()
            fig_plot.plot(t,y0[1])
            fig_plot.set_xlabel('time (s)')
            fig_plot.set_ylabel ('y(t)')
            fig_plot.grid('on')
            self.fig.tight_layout()
            canvas.draw()
        
        # Specify the mainloop
        master.mainloop()
        
#Start the app
app = ControlsApplication()