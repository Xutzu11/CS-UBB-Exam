# App made by Alex Ignat
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.font as font

# Create answers
nr = {('2023', 'Iulie', 'Informatica'): 24,
      ('2023', 'Septembrie', 'Informatica'): 24,
      ('2023', 'Concurs', 'Informatica'): 24,
      ('2022', 'Iulie', 'Informatica'): 30,
      ('2022', 'Septembrie', 'Informatica'): 30,
      ('2022', 'Concurs', 'Informatica'): 30,
      ('2021', 'Iulie', 'Informatica'): 30,
      ('2021', 'Septembrie', 'Informatica'): 30,
      ('2021', 'Concurs', 'Informatica'): 30,
      ('2023', 'Iulie', 'Matematica'): 24,
      ('2023', 'Septembrie', 'Matematica'): 24,
      ('2023', 'Concurs', 'Matematica'): 24,
      ('2022', 'Iulie', 'Matematica'): 30,
      ('2022', 'Septembrie', 'Matematica'): 30,
      ('2022', 'Concurs', 'Matematica'): 30,
      ('2021', 'Iulie', 'Matematica'): 30,
      ('2021', 'Septembrie', 'Matematica'): 30,
      ('2021', 'Concurs', 'Matematica'): 30,
      }
ans = {('2023', 'Iulie', 'Informatica'):
           ["AB", "C", "B", "AC", "B", "ABD", "B", "C", "ABC", "A", "AD", "D", "C", "ABC", "AB",
            "A", "B", "AC", "BC", "A", "A", "BD", "CD", "C"],
       ('2023', 'Septembrie', 'Informatica'):
           ["B", "AD", "D", "C", "BCD", "C", "A", "B", "AB", "BD", "A", "AD", "AB", "ABC", "ABC",
            "C", "AC", "BCD", "B", "ACD", "C", "BC", "A", "CD"],
       ('2023', 'Concurs', 'Informatica'):
           ["A", "A", "AD", "ABC", "ABC", "C", "AC", "A", "B", "CD", "BD", "D", "AB", "AC", "BD",
            "AD", "AC", "AC", "BCD", "BD", "AC", "AD", "BC", "BD"],
       ('2022', 'Iulie', 'Informatica'):
           ["B", "A", "BC", "D", "CD", "A", "BD", "B", "BC", "B", "C", "D", "C", "B", "A",
            "D", "B", "B", "C", "BCD", "C", "ABC", "B", "ACD", "ACD", "AC", "ABD", "A", "CD", "CD"],
       ('2022', 'Septembrie', 'Informatica'):
           ["AB", "AB", "AB", "C", "B", "AD", "C", "D", "D", "A", "A", "B", "AC", "ACD", "D",
            "C", "BD", "B", "ABD", "BD", "BC", "D", "C", "BC", "D", "ACD", "AD", "ABC", "AB", "AB"],
       ('2022', 'Concurs', 'Informatica'):
           ["C", "ABD", "AD", "C", "B", "D", "ABD", "C", "B", "C", "C", "ACD", "C", "B", "BD",
            "B", "CD", "AC", "BD", "B", "D", "AC", "AD", "A", "A", "B", "D", "C", "BC", "AD"],
       ('2021', 'Septembrie', 'Informatica'):
           ["C", "B", "A", "BD", "B", "D", "ABC", "B", "D", "C", "AC", "A", "AB", "ACD", "AB",
            "A", "BD", "BD", "C", "CD", "A", "BD", "BC", "C", "BC", "AD", "A", "BC", "BC", "A"],
       ('2021', 'Iulie', 'Informatica'):
           ["AC", "B", "C", "D", "D", "BC", "A", "BC", "ABD", "BC", "CD", "C", "D", "ABCD", "B",
            "B", "CD", "ACD", "ABCD", "AC", "BD", "C", "BD", "D", "BD", "A", "B", "D", "BC", "BC"],
       ('2021', 'Concurs', 'Informatica'):
           ["AB", "B", "A", "C", "B", "C", "D", "B", "ABC", "D", "BCD", "D", "B", "D", "AC",
            "C", "B", "A", "B", "AC", "BD", "B", "C", "BD", "ABD", "AD", "BD", "B", "C", "B"],
       ('2023', 'Iulie', 'Matematica'):
           ["C", "B", "C", "AB", "A", "B", "AD", "AC", "C", "D", "C", "AC", "D", "B", "AD",
            "ABC", "B", "A", "AC", "AD", "D", "C", "AB", "D"],
       ('2023', 'Septembrie', 'Matematica'):
           ["B", "C", "B", "D", "ABD", "B", "AD", "A", "B", "C", "D", "AB", "ACD", "ACD", "BD",
            "BC", "A", "B", "A", "ACD", "B", "AC", "D", "BCD"],
       ('2023', 'Concurs', 'Matematica'):
           ["B", "D", 'C', "AD", "D", "BD", "AC", "C", "AD", "ABD", "BD", "AC", "D", "ACD", "AB",
            "B", "AD", "B", "ACD", "D", "AB", "D", "C", "BC"],
       ('2022', 'Iulie', 'Matematica'):
           ["C", "D", "AB", "ACD", "A", "AB", "C", "C", "AB", "C", "C", "B", "AB", "BC", "B",
            "D", "AC", "B", "BCD", "D", "C", "C", "AD", "AD", "AB", "B", "AC", "B", "BD", "BD"],
       ('2022', 'Septembrie', 'Matematica'):
           ["D", "B", "A", "B", "AB", "AB", "C", "C", "D", "C", "B", "A", "AC", "C", "AB",
            "ABD", "AD", "C", "BD", "D", "C", "A", "AC", "AB", "D", "BC", "B", "ABD", "AB", "ACD"],
       ('2022', 'Concurs', 'Matematica'):
           ["BC", "B", "C", "B", "B", "C", "D", "C", "B", "B", "C", "A", "BC", "B", "B",
            "CD", "BD", "A", "BD", "C", "AB", "D", "D", "C", "AB", "BD", "BCD", "A", "AB", "AC"],
       ('2021', 'Iulie', 'Matematica'):
           ["C", "ABC", "CD", "AB", "B", "B", "BD", "BCD", "ACD", "C", "BC", "C", "A", "D", "C",
            "D", "AD", "BCD", "C", "C", "ACD", "BC", "ACD", "BD", "B", "C", "AC", "D", "B", "ABD"],
       ('2021', 'Septembrie', 'Matematica'):
           ["B", "BCD", "C", "A", "AC", "B", "BC", "C", "D", "C", "BD", "BC", "AD", "B", "D",
            "B", "C", "A", "A", "C", "BD", "AC", "B", "BCD", "B", "C", "BD", "ACD", "ABC", "BC"],
       ('2021', 'Concurs', 'Matematica'):
           ["BD", "AD", "B", "AB", "BC", "BD", "B", "C", "ABC", "C", "C", "BC", "BCD", "ABD", "BD",
            "AB", "CD", "AC", "ABC", "C", "A", "ABC", "B", "D", "B", "BD", "D", "BC", "AC", "AD"],
       }

# Function to set the window size
def set_window_size(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


# Create main components
root = Tk()
set_window_size(root)
frm = ttk.Frame(root, padding=10)
frm.grid()
for name in ["TkDefaultFont", "TkMenuFont", "TkTextFont", "TkHeadingFont"]:
    font.nametofont(name).configure(size=18, family='Helvetica')
submit_button = ttk.Button(frm)
barem_button = ttk.Button(frm)
help_button = ttk.Button(frm)
labels, alternate_labels, exercises, buttons_lists = [], [], [], []


# Open help
def show_help():
    help_window = tkinter.Toplevel(root)
    help_window.title("Ajutor")
    # help_window.iconbitmap("cs-logo.ico")
    font = ('Helvetica', 13)
    # Create a Text widget
    text_widget = tkinter.Text(help_window, wrap="word", font=font)
    text_widget.pack(expand=True, fill="both", padx=10, pady=10)

    # Insert larger text into the Text widget
    larger_text = ("Utilizarea aplicației:\n"
                   "    • Selectați subiectul pe care vreți să îl rezolvați (anul, sesiunea, materia)\n"
                   "    • Bifați răspunsurile pentru fiecare întrebare în parte\n"
                   "    • Apăsați butonul Rezultat pentru a afla nota obținută\n\n"
                   "Baremele sunt conform cu cele oficiale ale facultății.\n"
                   "Metoda de punctare:\n"
                   "    1. Fiecare întrebare are cel puțin 1 răspuns corect si cel puțin 1 răspuns incorect.\n"
                   "    2. Fiecare întrebare are asociat un punctaj „p” care este primit de către candidat daca bifează toate răspunsurile corecte si numai pe acelea.\n"
                   "    3. Dacă o întrebare are asociat un punctaj „p” si are un număr de „t” răspunsuri corecte si un număr de „f” răspunsuri incorecte, atunci:\n"
                   "        a. Dacă unul dintre cele „t” răspunsuri corecte este bifat, atunci candidatul primește „p/t” puncte.\n"
                   "        b. Dacă unul dintre cele „f” răspunsuri incorecte este bifat, atunci candidatul primește „(-0.66)*p/t” puncte (adică este penalizat).\n"
                   "        c. Punctajul pentru această întrebare este minim „0” (daca rezultatul evaluării tuturor bifărilor făcute de către candidat este negativ atunci rezultatul se înlocuiește cu „0”) si maxim „p”.\n"
                   "        d. Dacă toate raspunsurile sunt bifate, atunci candidatul primește nota „0”.\n"
                   "Excepție de la această regulă face sesiunea din Iulie 2021 - Informatică, care permite selectarea tuturor răspunsurilor, unele întrebări neavând răspunsuri greșite.\n\n"
                   "Pentru subiectele cu 30 de întrebări, punctajul „p” pentru fiecare întrebare este de 3p.\n"
                   "Pentru subiectele cu 24 de întrebări, punctajul „p” pentru fiecare întrebare este de 3.75p.\n"
                   "Se acordă 10p din oficiu.\n"
                   "Punctajul final se împarte la 10 pentru a obține media finală.\n\n"
                   "Mult succes tuturor!")
    text_widget.insert("1.0", larger_text)
    text_widget.config(state="disabled")

# Open solutions
def open_solutions():
    new_window = tkinter.Toplevel(root)
    new_window.title("Barem de rezolvare")
    # new_window.iconbitmap("cs-logo.ico")
    custom_font = ("Helvetica", 12)
    small_frm = ttk.Frame(new_window, padding=10)
    small_frm.grid()
    scroll_sol = ttk.Scrollbar(small_frm, orient=VERTICAL)
    scroll_sol.grid(column=1, row=0, sticky='N, S')
    canvas_sol = Canvas(small_frm, yscrollcommand=scroll_sol.set)
    canvas_sol.grid(column=0, row=0, sticky='N, E, S, W')
    small_inner_frame = ttk.Frame(canvas_sol)
    scroll_sol.config(command=canvas_sol.yview)
    canvas_sol.create_window((0, 0), window=small_inner_frame, anchor='nw')
    canvas_sol.config(scrollregion=canvas_sol.bbox("all"))
    small_inner_frame.bind("<Configure>", lambda event: canvas_sol.config(scrollregion=canvas_sol.bbox("all")))
    nr_rasp = nr[(year_var.get(), session_var.get(), subject_var.get())]
    answers = ans[(year_var.get(), session_var.get(), subject_var.get())]
    if (year_var.get(), session_var.get(), subject_var.get()) == ('2022', 'Concurs', 'Informatica'):
        special = 1
    else:
        special = 0
    for i in range(nr_rasp):
        label = ttk.Label(small_inner_frame, font=custom_font)
        if not special:
            label.config(text=labels[i].cget("text") + " " + answers[i])
        else:
            label.config(text=alternate_labels[i].cget("text") + " " + answers[i])
        label.grid(column=0, row=i)



# Handle exam selection
def exam_selection(event):
    if year_var.get() == '':
        return
    if session_var.get() == '':
        return
    if subject_var.get() == '':
        return
    submit_button.config(state="enabled")
    barem_button.config(state="enabled")
    for widget in inner_frame.winfo_children():
        widget.grid_forget()
    nr_rasp = nr[(year_var.get(), session_var.get(), subject_var.get())]
    if (year_var.get(), session_var.get(), subject_var.get()) == ('2022', 'Concurs', 'Informatica'):
        special = 1
    else:
        special = 0
    for i in range(nr_rasp):
        if not special:
            labels[i].grid(column=0, row=i, padx=6)
        else:
            alternate_labels[i].grid(column=0, row=i, padx=6)
        c = 1
        for button in buttons_lists[i]:
            button.grid(column=c, row=i, padx=6)
            c += 1


# Create a dropdown for year, session, subject
year_var = StringVar()
year = ttk.Combobox(frm, textvariable=year_var, state="readonly", width=4)
year['values'] = ('2023', '2022', '2021')
year.grid(column=0, row=0)
year.bind("<<ComboboxSelected>>", exam_selection)

session_var = StringVar()
session = ttk.Combobox(frm, textvariable=session_var, state="readonly", width=10)
session['values'] = ('Iulie', 'Septembrie', 'Concurs')
session.grid(column=1, row=0, columnspan=4)
session.bind("<<ComboboxSelected>>", exam_selection)

subject_var = StringVar()
subject = ttk.Combobox(frm, textvariable=subject_var, state="readonly", width=10)
subject['values'] = ('Matematica', 'Informatica')
subject.grid(column=5, row=0)
subject.bind("<<ComboboxSelected>>", exam_selection)

# Create a place for the exercises
scrollbar = ttk.Scrollbar(frm, orient=VERTICAL)
scrollbar.grid(column=6, row=1, rowspan=2, sticky='N, S')
canvas = Canvas(frm, yscrollcommand=scrollbar.set)
canvas.grid(column=0, row=1, rowspan=2, columnspan=6, sticky='N, E, S, W')
scrollbar.config(command=canvas.yview)
inner_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor='nw')
canvas.config(scrollregion=canvas.bbox("all"))
inner_frame.bind("<Configure>", lambda event: canvas.config(scrollregion=canvas.bbox("all")))

# Create exercise labels
for i in range(1, 31):
    label = ttk.Label(inner_frame, text=str(i) + ".")
    labels.append(label)

alternate_labels_texts = ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.",
                          "11.", "12.", "13.", "14.", "15.", "16.", "17.", "18.", "19.", "20a.",
                          "20b.", "21.", "22.", "23.", "24.", "25a.", "25b.", "26.", "27a.", "27b."]
for p in alternate_labels_texts:
    label = ttk.Label(inner_frame, text=p)
    alternate_labels.append(label)

# Create check buttons
check_buttons_types = ['A', 'B', 'C', 'D']
for i in range(1, 31):
    c = 1
    check_var = []
    buttons_list = []
    for o in check_buttons_types:
        var = BooleanVar(value=False)
        check_var.append(var)
        check_button = ttk.Checkbutton(inner_frame, text=o, variable=var)
        buttons_list.append(check_button)
        c += 1
    buttons_lists.append(buttons_list)
    exercises.append(check_var)


result = StringVar()
entry = ttk.Entry(frm, state="readonly", width=8, textvariable=result)  # Make the Entry read-only
entry.grid(column=1, row=3, padx=(0, 10), columnspan=2)


def calculate_result():
    variants = ['A', 'B', 'C', 'D']
    nr_rasp = nr[(year_var.get(), session_var.get(), subject_var.get())]
    rasp = ans[(year_var.get(), session_var.get(), subject_var.get())]
    pct = 0.0
    allow_all = 0
    if year_var.get() == '2021' and session_var.get() == 'Iulie':
        allow_all = 1
    expct = 90 / nr_rasp
    for i in range(nr_rasp):
        expected_correct = len(rasp[i])
        actual_correct, actual_wrong = 0, 0
        c = 0
        for o in exercises[i]:
            if o.get():
                if variants[c] in rasp[i]:
                    actual_correct += 1
                else:
                    actual_wrong += 1
            c += 1
        if actual_wrong + actual_correct == 4 and allow_all == 0:
            pct += 0.0
        else:
            pct += max(0.0, actual_correct * expct / expected_correct - actual_wrong * 0.66 * expct / expected_correct)
    result.set(str(round(pct / 10 + 1, 2)))


submit_button.config(text="Rezultat", command=calculate_result, state="disabled")
barem_button.config(text="Barem", command=open_solutions, state="disabled")
help_button.config(text="?", command=show_help, width=2)

submit_button.grid(column=0, row=3)
barem_button.grid(column=3, row=3)
help_button.grid(column=6, row=3)


# Start the GUI event loop
root.title("Admitere UBB - by Alex Ignat")
# root.iconbitmap("cs-logo.ico")
root.mainloop()

# have fun!