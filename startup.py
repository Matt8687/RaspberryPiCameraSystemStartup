import tkinter as tk
import subprocess
import time

root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
root.title("Startup-Hello")
font = ("Comic Sans MS", 12, "bold")
font1 = ("Arial", 15, "bold")

button_names = ["Greetings", "Raspberry Pi", "Arducam Cameras", "Ubiquiti", "PowerBoard", "Linux Stuff", "Troubles?"]
buttons = []
button_width = 0;
for i in range(len(button_names)):
    num = len(button_names[i])
    if(num>button_width):
        button_width = num
main_terminal = tk.Canvas(frame1, width = 100, height = 50, bg = "black")


greeting = tk.Label(main_terminal, 
    fg = "green",
    bg = "black",
    width = 100,
    height = 50,
    justify=tk.LEFT,
    anchor='nw',
    padx=10,
    pady=10
    )
greeting.configure(font=font)

hithere = tk.Button(frame2, text="Hello", command=lambda: sayhi(root, greeting, hithere), width=button_width, font=font1)
hithere.pack(side=tk.LEFT)
 
def main():
    frame1.pack(padx=10, pady=10, side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
    frame2.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        
    root.mainloop()

def systemdCheck():
    text = ''
    text += ">'systemctl status BOREALIS_CAM' :\n"+subprocess.getoutput("systemctl status BOREALIS_CAM")+"\n\n"
    text += ">'systemctl status BOREALIS_CAM_SAVE' :\n"+subprocess.getoutput("systemctl status BOREALIS_CAM_SAVE")+"\n\n"
    return str(text)

def systemInfo():
    text = ''
    text += ">'cat /etc/lsb-release' :\n"+subprocess.getoutput("cat /etc/lsb-release")+"\n\n"
    return str(text)

def outputA(root, text, label):
    delta = 17
    delay = 0
    total_delay = (delta*len(text))
    for i in range(len(text) + 1):
        s = text[:i]
        update_text = lambda s=s: label.configure(text=s)
        root.after(delay, update_text)
        delay += delta
    return total_delay

def outputB(text, label):
    label.configure(text=text)

def sayhi(root, label, button):
    button.destroy();
    button = tk.Button(frame2, text="Yes.", command=lambda: info(root, label, button, "Startup"), width=button_width, font=font1)
    label.pack(side=tk.TOP, anchor='w')
    delay = outputA(root, systemdCheck()+"\n>Guten Tag User, Ready to get started?", label)
    delay = int(delay)
    print(delay)
    update_button = lambda : button.pack(side=tk.LEFT)
    root.after(delay, update_button)
    main_terminal.pack(padx=10, pady=10, side=tk.RIGHT)

def info(root, label, button, text):
    button.destroy()
    tk.Label(frame2, text = "Info:", font = font1, bg='black', fg='white', width=button_width).pack(side=tk.TOP)
    i = 0
    for i in range(len(button_names)):
        buttons.append(tk.Button(frame2, text = button_names[i], command=lambda s=i: getInfo(s, greeting), width=button_width, font = font1))
        buttons[i].pack(side=tk.TOP)
    i+=1
    buttons.append(tk.Button(frame2, text = "Systemd Status", command = lambda: outputB(systemdCheck(), label), width=button_width, font = font1))
    buttons[i].pack(side=tk.BOTTOM)
    
    i+=1
    buttons.append(tk.Button(frame2, text = "System Info", command = lambda: outputB(systemInfo(), label), width=button_width, font = font1))
    buttons[i].pack(side=tk.BOTTOM)
    
    tk.Label(frame2, text = "System:", font = font1, bg='black', fg='white', width=button_width).pack(side=tk.BOTTOM)
    getInfo(0, label)
    
def getInfo(num, label):
    #print(num)
    file = open("texts/"+button_names[num]+'.txt')
    text = file.read()
    label.configure(text = text)
    

main()
