import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg      
#c1 = '#cf630c' #dark orange
#c2 = '#80f0e7' #turqoise
# pyinstaller two_color_gradient.py --onefile -w

def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

layout = [[sg.Text('Enter hex codes :')],      
          [sg.Input('#b73d06', key='-IN1-',size =(10,1))],
          [sg.Input('#80f0e7',key='-IN2-',size =(10,1))],          
          [sg.Button('Plot')]]      

window = sg.Window('Plot two color gradient', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    if event == 'Plot':
        c1 = values['-IN1-']
        c2 = values['-IN2-']
        fig, ax = plt.subplots(figsize=(8, 5))
        a = [] #gradients list
        n=30
        for x in range(n+1):
            a += [colorFader(c1,c2,x/n)]
            ax.axvline(x, color=colorFader(c1,c2,x/n), linewidth=4)
        plt.show()
    
    if event == sg.WIN_CLOSED:
        break      

window.close()




