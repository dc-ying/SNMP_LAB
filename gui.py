#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

def snmpWalk(host, oid):
    result = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read()
    return result

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('817x409')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Text1Var = StringVar(value='(Please enter an OID)')
        self.Text1 = Entry(self.top, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.049, rely=0.07, relwidth=0.256, relheight=0.12)

        self.style.configure('Label1.TLabel',anchor='w', font=('宋体',9))
        self.Label1 = Label(self.top, text='输入：', style='Label1.TLabel')
        self.Label1.place(relx=0.049, rely=0.02, relwidth=0.06, relheight=0.04)

        self.style.configure('Command1.TButton',font=('宋体',9))
        self.Command1 = Button(self.top, text='确认', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.049, rely=0.215, relwidth=0.07, relheight=0.061)

        self.style.configure('Command3.TButton',font=('宋体',9))
        self.Command3 = Button(self.top, text='查看信息', command=self.Command3_Cmd, style='Command1.TButton')
        self.Command3.place(relx=0.2, rely=0.215, relwidth=0.12, relheight=0.061)

###
        self.Text2Font = Font(font=('宋体',9))
        self.Text2 = Text(self.top, font=self.Text2Font)
        self.Text2.place(relx=0.421, rely=0.06, relwidth=0.177, relheight=0.08)

        self.Text3Font = Font(font=('宋体',9))
        self.Text3 = Text(self.top, font=self.Text2Font)
        self.Text3.place(relx=0.421, rely=0.23, relwidth=0.177, relheight=0.16)
        
        self.Text4Font = Font(font=('宋体',9))
        self.Text4 = Text(self.top, font=self.Text2Font)
        self.Text4.place(relx=0.421, rely=0.45, relwidth=0.177, relheight=0.08)

        self.Text5Font = Font(font=('宋体',9))
        self.Text5 = Text(self.top, font=self.Text2Font)
        self.Text5.place(relx=0.421, rely=0.59, relwidth=0.177, relheight=0.10)

        self.Text6Font = Font(font=('宋体',9))
        self.Text6 = Text(self.top, font=self.Text2Font)
        self.Text6.place(relx=0.049, rely=0.45, relwidth=0.35, relheight=0.3)


        self.style.configure('Command2.TButton',font=('宋体',9))
        self.Command2 = Button(self.top, text='确认', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.049, rely=0.8, relwidth=0.089, relheight=0.061)

        self.style.configure('Label2.TLabel',anchor='w', font=('宋体',9))
        self.Label2 = Label(self.top, text='CPU 阈值:', style='Label2.TLabel')
        self.Label2.place(relx=0.049, rely=0.372, relwidth=0.12, relheight=0.061)

        self.style.configure('Label3.TLabel',anchor='w', font=('宋体',9))
        self.Label3 = Label(self.top, text='CPU', style='Label3.TLabel')
        self.Label3.place(relx=0.421, rely=0.02, relwidth=0.12, relheight=0.04)

        self.style.configure('Label4.TLabel',anchor='w', font=('宋体',9))
        self.Label4 = Label(self.top, text='内存', style='Label4.TLabel')
        self.Label4.place(relx=0.421, rely=0.18, relwidth=0.12, relheight=0.04)

        self.style.configure('Label5.TLabel',anchor='w', font=('宋体',9))
        self.Label5 = Label(self.top, text='硬盘空间', style='Label5.TLabel')
        self.Label5.place(relx=0.421, rely=0.40, relwidth=0.12, relheight=0.04)

        self.style.configure('Label4.TLabel',anchor='w', font=('宋体',9))
        self.Label6 = Label(self.top, text='流量值', style='Label6.TLabel')
        self.Label6.place(relx=0.421, rely=0.54, relwidth=0.12, relheight=0.04)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        self.Text6.delete("0.0",END)
        oid_result = snmpWalk(host,self.Text1Var.get())
        self.Text6.insert("1.0",str(oid_result))

    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command3_Cmd(self, event=None):
        #TODO, Please finish the function here!
        # CPU信息
        """
        self.Text2.delete('0.0',END)
        cpu_result = snmpWalk(host,'1.3.6.1.2.1.25.3.3.1.2')
        pro_num=len(cpu_result)
        tmp=1
        diskstr=''
        pro=0
        while tmp<=pro_num:
            pro=pro+int(snmpWalk(host, 'HOST-RESOURCES-MIB::hrProcessorLoad.'+str(tmp+5))[0].split(' ')[3])
            tmp+=1
        pro=round(float(pro/pro_num),2)
        self.Text2.insert('1.0',"CPU使用率："+str(pro)+'%\n')
        """
        self.Text2.delete('0.0',END)
        cpu_result = snmpWalk(host, '1.3.6.1.4.1.2021.11.9.0').split(' ')[-1][:-1]
        self.Text2.insert('1.0',"用户CPU使用率："+str(cpu_result)+'%\n')
        # 内存
        self.Text3.delete('0.0',END)
        """
        mem_total = snmpWalk(host, 'HOST-RESOURCES-MIB::hrMemorySize.0')[0].split(' ')[3]
        mem_sto_used = snmpWalk(host, 'HOST-RESOURCES-MIB::hrStorageUsed.7')[0].split(' ')[3]
        mem_sto_unit = snmpWalk(host, 'HOST-RESOURCES-MIB::hrStorageAllocationUnits.7')[0].split(' ')[3]
        mem_used=str(round(float(mem_sto_used)*float(mem_sto_unit)/1024/1024/1024,2))
        mem_used_total=float(mem_total)     
        mem_used_rate=str(round(float(mem_sto_used)*float(mem_sto_unit)/1024/mem_used_total*100,2))+'%'
        """
        mem_total = snmpWalk(host, '.1.3.6.1.2.1.25.2.2.0').split(' ')[-2]
        mem_used  = snmpWalk(host, '.1.3.6.1.4.1.2021.4.6.0').split(' ')[-2]
        mem_used_rate = 100*float(mem_used)/float(mem_total)
        self.Text3.insert('1.0',"总内存 : "+str(round(float(mem_total)/1024/1024,2))+" GB\n"+"内存使用："+mem_used+"GB\n"+"内存使用率："+str(round(mem_used_rate,2))+"%\n")
        
        # 流量信息
        device_mib = snmpWalk(host, 'RFC1213-MIB::ifDescr').split("\n")
        device_list = []
        for item in device_mib[:-1]:
            device_list.append(item.split(':')[3].strip())
        # 流入流量
        data_mib = snmpWalk(host, 'IF-MIB::ifInOctets').split("\n")
        data = []
        for item in data_mib[:-1]:
            byte = float(item.split(':')[3].strip())
            data.append(str(round(byte / 1024, 2)))
        inside = data
        # 流出流量
        data_mib = snmpWalk(host, 'IF-MIB::ifOutOctets').split("\n")
        data = []
        for item in data_mib[:-1]:
            byte = float(item.split(':')[3].strip())
            data.append(str(round(byte / 1024, 2)))
        outside = data
        rxsum=0.0
        txsum=0.0
        for i, item in enumerate(device_list):
            rxsum+=float(inside[i])
            txsum+=float(outside[i])
        rxsum=round(rxsum/1024,2)
        txsum=round(txsum/1024,2)
        self.Text5.delete('0.0',END)
        self.Text5.insert('1.0',"发送流量："+str(txsum)+'MB'+'\n'+"接收流量："+str(rxsum)+'MB'+'\n')

        #硬盘
        self.Text4.delete('0.0',END)
        disk_total = snmpWalk(host, 'HOST-RESOURCES-MIB::hrStorageIndex').split("\n")
        disk_num=len(disk_total)-2
        tmp=1
        diskstr=''
        while tmp<=disk_num:
            unit=snmpWalk(host, 'HOST-RESOURCES-MIB::hrStorageAllocationUnits.'+str(tmp)).split("\n")[0].split(' ')[3]
            stor=snmpWalk(host, 'HOST-RESOURCES-MIB::hrStorageSize.'+str(tmp)).split("\n")[0].split(' ')[3]
            storge=round(float(unit)*float(stor)/1024/1024/1024,4)
            diskstr=diskstr+snmpWalk(host, 'HOST-RESOURCES-MIB::hrStorageDescr.'+str(tmp)).split("\n")[0].split(' ')[3]+' '+str(storge)+'GB'+'\n'
            tmp+=1
        self.Text4.insert('1.0',"硬盘数："+str(disk_num)+'\n'+diskstr)




        



if __name__ == "__main__":
    host="127.0.0.1"
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
