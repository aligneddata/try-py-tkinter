from tkinter import *
from tkinter import ttk

def on_search():
    pass

def create_listbox_to_frame(frame_panel, a_row, a_column, listbox_title, listbox_items):
    label = ttk.Label(frame_panel, text=listbox_title).grid(row=0, column=0)
    
    listbox1 = Listbox(frame_panel, selectmode='single')
    listbox1.grid(row=1, column=0, padx=2, pady=2)
    for item in listbox_items:
        listbox1.insert(END, item)

def create_choices_to_frame(frame_panel, students, years, terms):
    frm_choices1 = ttk.Frame(frame_panel, padding=5)
    create_listbox_to_frame(frm_choices1, 0, 0, "Student", students)
    frm_choices1.grid(row=0,column=0)

    frm_choices2 = ttk.Frame(frame_panel, padding=5)
    create_listbox_to_frame(frm_choices2, 0, 1, "Year", years)
    frm_choices2.grid(row=0,column=1)
        
    frm_choices3 = ttk.Frame(frame_panel, padding=5)
    create_listbox_to_frame(frm_choices3, 0, 1, "Year", terms)
    frm_choices3.grid(row=0,column=2)
    
def create_subject_scores_to_frame(frame_panel, score_list):
    frm = ttk.Frame(frame_panel, padding=1)
    frm.grid()
    row_id = 0
    for subject, score in score_list:
        subject_label = ttk.Label(frm, text=subject).grid(row=row_id, column=0)
        score_label = ttk.Label(frm, text=score).grid(row=row_id, column=1)
        row_id += 1

def get_count(score_list):
    return len(score_list)

def get_average(score_list):
    sum = 0
    for subject, score in score_list:
        sum += int(score)
    return 1. * sum / get_count(score_list)

def create_stats_to_frame(frame_panel, score_list):
    frm = ttk.Frame(frame_panel, padding=1)
    frm.grid()
    count_label = ttk.Label(frm, text="Total number of subjects: %d" % get_count(score_list)).grid(row=0, column=0)
    average_label = ttk.Label(frm, text="Average score: %.1f" % get_average(score_list)).grid(row=1, column=0)

def create_results_to_frame(frame_panel, data):
    frm_result1 = ttk.Frame(frame_panel, padding=5)
    create_subject_scores_to_frame(frm_result1, data)
    frm_result1.grid(row=1,column=0)

    frm_result2 = ttk.Frame(frame_panel, padding=5)
    create_stats_to_frame(frm_result2, data)
    frm_result2.grid(row=1,column=1)



#
# main
#
root = Tk()
root.title("Student Report Card")
frm = ttk.Frame(root, padding=5)
frm.grid()


students = ["John", "Rick", "Jane", "Lucy"]
years = ["2021", "2022", "2023"]
terms = ["Term 1", "Term 2", "Term 3", "Term 4"]
create_choices_to_frame(root, students, years, terms)

data = [["math", "98"], ["physics", "88"], ["english", "75"]]
create_results_to_frame(root, data)

ttk.Button(root, text="Quit", command=root.destroy).grid(row=10, column=0, columnspan=3)

root.mainloop()