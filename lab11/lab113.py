from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title('Tic Tac Toe')
click = True



def who_wins():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        return 'X'
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
        return 'O'


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def compMove():
    possibleMoves = buttons
    move = False

    if str(button5) in possibleMoves:
        move = str(button5)
        return move

    for i in possibleMoves:
        buttonsCopy = buttons.copy()
        for sign in ['O', 'X']:
            buttonsCopy[i]['text'] = sign
            if who_wins() == 'O':
                move = i
                buttonsCopy[i]['text'] = ''
                return move
            elif who_wins() == 'X':
                move = i
                buttonsCopy[i]['text'] = ''
                return move
            else:
                buttonsCopy[i]['text'] = ''

    cornersOpen = []
    for i in possibleMoves:
        if i in [str(button1), str(button3), str(button7), str(button9)]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [str(button2), str(button4), str(button6), str(button8)]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def checker(button):
    global click
    is_winner_exists = False

    if button['text'] == " " or button['text'] == '' and click == True:
        button['text'] = 'X'
        click = False
        del buttons[str(button)]
        if who_wins() == 'X':
            is_winner_exists = True
            tkinter.messagebox.showinfo('Winner X', 'You have just won the game')
        else:
            comp_btn_pressed = compMove()
            if comp_btn_pressed:
                buttons[comp_btn_pressed]['text'] = 'O'
                del buttons[str(comp_btn_pressed)]
                click = True
                if who_wins() == 'O':
                    is_winner_exists = True
                    tkinter.messagebox.showinfo('Winner O', 'You have just won the game')

    if len(buttons) == 0 and not is_winner_exists:
        tkinter.messagebox.showinfo('A draw!!!', 'Game is over.It\'s a draw!!!')


buttons = StringVar()

button1 = Button(tk, text=' ', font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(tk, text=' ', font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(tk, text=' ', font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(tk, text=' ', font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(tk, text=' ', font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(tk, text=' ', font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(tk, text=' ', font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(tk, text=' ', font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(tk, text=' ', font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)
buttons = {
    str(button1): button1,
    str(button2): button2,
    str(button3): button3,
    str(button4): button4,
    str(button5): button5,
    str(button6): button6,
    str(button7): button7,
    str(button8): button8,
    str(button9): button9,
}
tk.mainloop()
