# coding: utf-8
from nlp import analyze_string
from taipy.gui import notify


def analyze_text_input(state):
    notify(state, "Info", f"The text is: {state.text}", True)
    temp = state.dataframe.copy()
    scores = analyze_string(state.text)
    temp.loc[len(temp)] = scores
    state.dataframe = temp
    state.text = ""

   
def analyze_file_input(state):
    # state.dataframe2 = dataframe2
    state.treatment = 0
    with open(state.path, "r", encoding="utf-8") as f:
        data = f.read()
        # split lines and eliminates duplicates
        file_list = list(dict.fromkeys(data.replace("\n", " ").split(".")[:-1]))

    for i in range(len(file_list)):
        text = file_list[i]
        state.treatment = int((i+1)*100/len(file_list))
        temp = state.dataframe2.copy()
        scores = analyze_string(text)
        temp.loc[len(temp)] = scores
        state.dataframe2 = temp

    state.path = None
