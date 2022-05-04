
import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
import control.matlab 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import control

E = tk.E
W = tk.W
N = tk.N
S = tk.S

num = np.convolve((1),(1))
den = np.convolve((2/30,17/30,1,0),(1))
print("Num:", list(num))
print('Den:', list(den))

numD = np.polymul((1/3,1),(1/2,1)) 
denD = np.polymul((1/50,1),(1/32,1)) 
print(list(numD))
print(list(denD))


class ControlsApplication(tk.Frame):
    def __init__(self):
        # Lay out the master grid
        master = tk.Tk()
        master.geometry("1000x750")
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Control Systems Design")
        tx_lbls = np.array(['Plant Numerator', 'Plant Denominator', 'Controller Numerator', 'Controller Denominator', 'Gain (K)','Wn/Zeta','Poles/Zeros', 'L(s)', 'TF', 'Stability'])
        btn_lbls = np.array(['Calculate', 'Root Locus' ,'Bode Plot', 'Nyquist Plot', 'Step-Response'])
        
        # Configure rows
        # Start Bode/Nyquist
        rownum = 8 # Design with 5 columns
        for r in range(rownum):
            self.master.rowconfigure(r, weight=1)  
        # Start Bode/Nyquist
        
        # Configure columns
        colnum = 5 # Design with 5 columns
        # Labels for input
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            tx=tk.Text(master,bg='firebrick',fg='black')
            tx.grid(row=0,column=c,sticky=W+E+N+S)
            tx.insert('1.0',tx_lbls[c])
            tx.configure(state="disabled")
        
        # Text boxes for input
        txIns=[]
        for c in range(5):
            self.master.columnconfigure(c, weight=1);
            tx=tk.Text(master)
            tx.grid(row=1,column=c,sticky=W+E+N+S);
            if c == 0:
                tx.insert('1.0','1.')#,'1,4,68')
            elif c == 1:
                tx.insert('1.0','0.0667, 0.5667, 1.0, 0.0')
            elif c == 2:
                tx.insert('1.0','0.1667, 0.8333 , 1.0  ')
            elif c == 3:
                tx.insert('1.0','0.000625, 0.051250000000000004, 1.0'  )
            else:
                tx.insert('1.0','10')
            txIns.append(tx)
               
        # Labels for output
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            tx=tk.Text(master,bg='azure4',fg='black')
            tx.grid(row=2,column=c,sticky=W+E)
            tx.insert('1.0',tx_lbls[c+colnum])
            tx.configure(state="disabled")

            
        # Text boxes for output
        txOuts=[]
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            tx=tk.Text(master)
            tx.grid(row=3,column=c,sticky=W+E+N+S)
            txOuts.append(tx)
            tx.insert('1.0','[calc]')
            
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            tx=tk.Text(master)
            tx.grid(row=4,column=c,sticky=W+E+N+S)
            txOuts.append(tx)
            tx.insert('1.0','[calc]')
        
        for c in range(1):
            self.fig = Figure(figsize=(8,12))
            fig_plot= self.fig.add_subplot(111)
            canvas = FigureCanvasTkAgg(self.fig, master)
            plot_widget = canvas.get_tk_widget()
            # Start Bode/Nyquist
            plot_widget.grid(row=5,column=c, rowspan=3,columnspan=4, sticky=E+W+S+W)
            # End Bode/Nyquist
            canvas.draw()
        
        # Start Bode/Nyquist
        self.master.columnconfigure(4, weight=1)
        tx=tk.Text(master, bg = 'blue')
        tx.grid(row=5,column=4,sticky=W+E+N+S)
        txOuts.append(tx)
        tx.insert('1.0','Bode Margins: ')
        tx=tk.Text(master, bg = 'blue')
        tx.grid(row=6,column=4,sticky=W+E+N+S)
        txOuts.append(tx)
        tx.insert('1.0','Nyquist: ')
        tx=tk.Text(master, bg = 'green')
        tx.grid(row=7,column=4,sticky=W+E+N+S)
        txOuts.append(tx)
        tx.insert('1.0', 'SS: ')
        # End Bode/Nyquist
                
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            if c == 0:
                btn = tk.Button(master, text=btn_lbls[c],\
                                command = lambda:Calculate(),fg="violet")
            elif c == 1:
                btn = tk.Button(master, text=btn_lbls[c],\
                                command = lambda:RootLocus(),fg="violet")
            elif c == 2:
                btn = tk.Button(master, text=btn_lbls[c],\
                                command = lambda:Bode(),fg="violet")
            elif c == 3:
                btn = tk.Button(master, text=btn_lbls[c],\
                                command = lambda:Nyquist(),fg="violet")
            else:
                btn = tk.Button(master, text=btn_lbls[c],\
                                command = lambda:StepResp(),fg="violet")
            # Start Bode/Nyquist
            btn.grid(row=8,column=c,sticky=E+W)
            # End Bode/Nyquist
        
        # Function for TF
        def GetTF():
            num = txIns[0].get("1.0", "end-1c")
            num=np.array(num.split(',')).astype(float)
            print(num)
            den = txIns[1].get("1.0", "end-1c")
            den=np.array(den.split(',')).astype(float)
            print(den)
            cnum = txIns[2].get("1.0", "end-1c")
            cnum=np.array(cnum.split(',')).astype(float)
            print(cnum)
            cden = txIns[3].get("1.0", "end-1c")
            cden=np.array(cden.split(',')).astype(float)
            print(cden)
            G= control.tf(num,den);Dc = control.tf(cnum,cden)
            tf = G*Dc
            return tf
        
        # Function to calculate poles/zeros/wn/z
        def Calculate():
            tf = GetTF()
            K = float(txIns[4].get("1.0", "end-1c"))
            tf_cl=control.minreal(K*tf/(1+K*tf),verbose=False)
            zeros = control.zero(tf)
            zeros = np.asarray(zeros)
            poles = control.pole(tf)
            poles = np.asarray(poles)
            cl_poles=control.pole(tf_cl)
            
            wn, zeta, cl_poles = np.around(control.damp(tf_cl),2)
            wn = np.real(wn);zeta=np.real(zeta)
            str1= 'wn: ' + str(wn) + ' zeta: ' + str(zeta) 
            str2= 'poles: ' + str(np.around(cl_poles,2)) + ' zeros: ' + str(zeros)
            txOuts[0].delete('1.0','end')
            txOuts[1].delete('1.0','end')
            txOuts[0].insert('1.0',str1)
            txOuts[1].insert('1.0',str2)
            txOuts[2].delete('1.0','end')
            txOuts[2].insert('1.0',str(tf))
            txOuts[3].delete('1.0','end')
            txOuts[3].insert('1.0',str(tf_cl))
            ss = control.tf2ss(control.tf(tf_cl))
            ss,T = control.canonical_form(ss)
            txOuts[3].configure(font=("Courier",10))
            print('Pole natural freq and damp:', str1)
            print('Poles:', str2)
            print("SS is: ", ss)
            
            
            #Calculate the error constants
            sys_k =control.tf((1),(1))
            sys_k = control.minreal(K*sys_k*tf,None,False)
            sys_v =control.tf((1,0),(1))
            sys_v = control.minreal(K*sys_v*tf,None,False)
            sys_a =control.tf((1,0,0),(1))
            sys_a = control.minreal(K*sys_a*tf,None,False)
           
            Kp = control.evalfr(1/(sys_k+1),0)
            Kv = control.evalfr(1/sys_v,0)
            Ka = control.evalfr(1/sys_a,0)
            sys_errs= 'Kp = ' + str(np.abs(Kp)) + ', Kv = ' + str(np.abs(Kv)) +\
                ', Ka = ' + str(np.abs(Ka))
            print('System Errors: ',sys_errs)
            txOuts[4].delete('1.0','end')
            txOuts[4].insert('1.0',str(sys_errs))
            
            # Calculate departures and arrivals
            n= len(poles); p_angs=np.zeros(n)
            m= len(zeros); z_angs=np.zeros(m)

            # Departure angles at poles
            for i in range(0,n):
                ang = np.concatenate((np.angle(poles[i]-zeros), \
                                      -np.angle(poles[i]-poles))) #concatenate
                ang = np.sum(ang)*180/np.pi -180 -360*(i) #sum
                ang = np.round(np.mod(ang,360),2)
                p_angs[i]=ang
            # Arrival angles at zeros
            for i in range(0,m):
                ang = np.concatenate((np.angle(zeros[i]-poles), \
                                      -np.angle(zeros[i]-zeros)))  #concatenate
                ang = np.sum(ang)*180/np.pi +180 +360*(i); #sum
                ang = np.round(np.mod(ang,360),2)
                z_angs[i] = ang
            print('pole deps: ', p_angs)
            print('zero arrivs: ',z_angs)

            # Calculate the n-m asymptotes 
            # Location
            asym_loc = (np.sum(poles)-np.sum(zeros))/(n-m) #sum
            asym_loc = np.round(np.real( asym_loc),2)
            # Angles of n-m branches
            asym_angs=np.zeros(n-m)
            print('asymptote alpha: ', asym_loc)
            for i in range(0,n-m):
                asym_angs[i] = (180 + 360*i)/(n-m)
            print('asymptote angles: ', asym_angs)

            # Calculate multiple roots
            num=np.squeeze(tf.num); den = np.squeeze(tf.den)
            num_df = 0
            if np.ndim(num) > 0:
                num_df = np.polyder(num);
            
            den_df = np.polyder(den);
            df = np.polyadd(np.convolve(num_df,den),\
                            -np.convolve(den_df,num)) #convolve
            mroots=np.roots(df)
            mroots=(mroots[~np.iscomplex(mroots)])
            mroots = np.unique(mroots)
            print('multiple roots:', np.round(mroots,2))
            
            txOuts[5].delete('1.0','end')
            txOuts[5].insert('1.0','departures: ' + str(p_angs))
            txOuts[6].delete('1.0','end')
            txOuts[6].insert('1.0','arrivals: ' + str(z_angs))
           
            txOuts[7].delete('1.0','end')
            txOuts[7].insert('1.0','alpha: ' + str(asym_loc))
            txOuts[8].delete('1.0','end')
            txOuts[8].insert('1.0','asymptote angles: ' + str(asym_angs))
           
            txOuts[9].delete('1.0','end')
            txOuts[9].insert('1.0','multiple roots: ' + str(mroots))
            
            #Calculate the Bode Margins and output to a textbox
            gm, pm, wm, wp = np.around(control.matlab.margin(K*tf),2)
            txOuts[10].delete('1.0','end')
            txOuts[10].insert('1.0','gain-margin: ' + str(gm) + ' phase-margin: ' + str(pm) + ' gain-w: ' + str(wm) + ' phase-w: ' + str(wp))

            #Evaluate Nyquist stability and output to a textbox
            NY_p=np.count_nonzero(np.real(control.pole(K*tf))>1e-6)
            NY_c = control.nyquist(K*tf, plot = False)
            NY_z = NY_p+NY_c
            txOuts[11].delete('1.0','end')
            txOuts[11].insert('1.0', 'Nyquist zeros: ' + str(NY_z))
            txOuts[12].delete('1.0','end')
            txOuts[12].insert('1.0', 'SS: ' + str(ss))
            
            
        # Function to create the rootlocus
        def RootLocus():  
            tf = GetTF()
            print(tf)
            plt.figure()
            control.rlocus(tf,grid=True,plotstr=[],print_gain=True)
            canvas.draw()
        
        # Function for Bode plot
        def Bode():
            tf = GetTF()
            K = float(txIns[4].get("1.0", "end-1c"))
            print(control.matlab.margin(K*tf))
            plt.figure()
            control.bode_plot(K*tf,dB=True)
            canvas.draw()
            
        # Function for Nyquist plot
        def Nyquist():
            tf = GetTF()
            K = float(txIns[4].get("1.0", "end-1c"))
            control.nyquist(K*tf,plot=True) 
            
        # Function to compute and display the step-response
        def StepResp():
            tf = GetTF()
            K = float(txIns[4].get("1.0", "end-1c"))
            tf=control.minreal(K*tf/(1+K*tf),verbose=False)
            print(tf)
            t = np.arange(0,100,.1)
            y0=control.step_response(tf,t)
            print(control.step_info(tf))
            fig_plot.clear()
            fig_plot.plot(t,y0[1])
            fig_plot.set_ylim([min(y0[1]),1.25*max(y0[1])])
            fig_plot.set_xlabel('time (s)')
            fig_plot.set_ylabel ('y(t)')
            fig_plot.grid('on')
            self.fig.tight_layout()
            canvas.draw();
            self.fig.savefig('hello.tif')
        
        # Specify the mainloop
        master.mainloop()
        master.after(100)
        


#Start the app
app = ControlsApplication() 