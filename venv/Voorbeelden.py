import tkinter
from tkinter.ttk import Combobox
# lijst = [["auto", 4, "onzin"],["fiets", 2, "onzin"],["driewieler", 3,"onzin"]]
# #print (lijst)
#
# for i in range(len(lijst)):
#
#     print((lijst[i][0])+" "+str((lijst[i][1])))
#
# # print("auto" + str(4))



# ref = "CHHCQWYHSJ"
# seq = "HHCCWSFHSJSEYTRIK"
#
# score = 0
#
# if len(ref) != len(seq):
#     verschil = len(ref) - len(seq)
#     # print (verschil)
#     if verschil <0:
#         score += verschil
#     else:
#         score -= verschil
#
# # print(ref[0])
#
# if len(ref)<len(seq):
#     for i in range (len(ref)):
#         if ref[i] == seq[i]:
#             score +=1
#         else:
#             score -=1
# else:
#     for i in range (len(seq)):
#         if ref[i] == seq[i]:
#             score +=1
#         else:
#             score -=1
#
# print(score)


#
# lijst = [["niks", "3"],["7","adsofjad"],["20","0"]]
# #
# # print(lijst)
# #
# # score = 0
# #
# #
# # for i in range(len(lijst)):
# #     # print(int(lijst[i][0]) + int(lijst[i][1]))
# #     try:
# #         score += (int(lijst[i][0]))
# #     except ValueError:
# #         print("Andere fout")
# #     try:
# #         score += (int(lijst[i][1]))
# #     except ValueError:
# #         print("Fout")
# # print(score)

lijst = ["lijst aa1","lijst aa2"]

class Gui:

    def __init__(self, lijst):
        # maakt een window en geeft een titel
        self.lijst = lijst

        self.main_window = tkinter.Tk()
        self.main_window.title("Uitleg")

        # maakt Frames ( gedeeltes in de main_window).
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #label toevoegen

        self.label = tkinter.Label(self.bottom_frame,
                                   text ="hoi Christel")

        self.label.pack()

        self.label1 = tkinter.Label(self.bottom_frame,
                                   text ="hoi Christel")

        self.label1.pack()

        self.label2 = tkinter.Label(self.bottom_frame,
                                   text ="hoi Christel")

        self.label2.pack()

        #lijst in gui

        self.drop = Combobox(self.bottom_frame,
                             values = self.lijst)

        self.drop.set("Select")

        self.drop.pack()

        # knop die functie doe iets aanroept
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.doe_iets)

        self.ok_button.pack()

        # pack Frames (zichtbaar maken frames in main window)
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        #zorg dat Gui 'aan' gaat
        tkinter.mainloop()

    def doe_iets(self):
        entry = self.drop.get()
        print(entry)

my_gui = Gui(lijst)