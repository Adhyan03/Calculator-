from tkinter import *

root = Tk()
def onClick(btnVal):
    exp = strvar.get()
    if btnVal=='=':
        exp=str(eval(exp))
    elif btnVal=='AC':
        exp = ''
    elif btnVal=='C':
        li = [i for i in exp]
        li.pop()
        exp = ''.join(li)
    else:
        exp = exp + btnVal
    strvar.set(exp)

strvar = StringVar()

Label(root,textvariable = strvar,width = 21,height = 3).grid(row=0,column = 0,columnspan = 5)

Button(root,text = 'C',command = lambda:onClick('C'),width = 21,height = 3,bg='#00afaf',fg='white').grid(row=1,columnspan = 3)
Button(root,text = 'AC',command = lambda:onClick('AC'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=1,column = 3)

Button(root,text = '1',command = lambda:onClick('1'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=2,column = 0)
Button(root,text = '2',command = lambda:onClick('2'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=2,column = 1)
Button(root,text = '3',command = lambda:onClick('3'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=2,column = 2)
Button(root,text = '*',command = lambda:onClick('*'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=2,column = 3)

Button(root,text = '4',command = lambda:onClick('4'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=3,column = 0)
Button(root,text = '5',command = lambda:onClick('5'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=3,column = 1)
Button(root,text = '6',command = lambda:onClick('6'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=3,column = 2)
Button(root,text = '/',command = lambda:onClick('/'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=3,column = 3)

Button(root,text = '7',command = lambda:onClick('7'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=4,column = 0)
Button(root,text = '8',command = lambda:onClick('8'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=4,column = 1)
Button(root,text = '9',command = lambda:onClick('9'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=4,column = 2)
Button(root,text = '+',command = lambda:onClick('+'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=4,column = 3)

Button(root,text = '0',command = lambda:onClick('0'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=5,column = 0)
Button(root,text = '.',command = lambda:onClick('.'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=5,column = 1)
Button(root,text = '=',command = lambda:onClick('='),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=5,column = 2)
Button(root,text = '-',command = lambda:onClick('-'),width = 6,height = 3,bg='#00afaf',fg='white').grid(row=5,column = 3)



root.mainloop()