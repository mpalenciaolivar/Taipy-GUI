# coding: utf-8
import numpy as np
import pandas as pd
from callbacks import analyze_file_input, analyze_text_input
from taipy.gui import Gui, notify

# Page 1
text = "Original text"

dataframe = pd.DataFrame({"Text": [""],
                          "Score Pos": [0.33],
                          "Score Neu": [0.33],
                          "Score Neg": [0.33],
                          "Overall":   [0]})

property_chart = {
    "type": "bar",
    "x": "Text",
    "y[1]": "Score Pos",
    "y[2]": "Score Neu",
    "y[3]": "Score Neg",
    "y[4]": "Overall",
    "color[1]": "green",
    "color[2]": "grey",
    "color[3]": "red",
    "type[4]": "line"
    }

page = """
# Getting started with Taipy GUI

<|layout|columns=1 1|
<|
My text: <|{text}|>

Enter a word:
<|{text}|input|>
<|Analyze|button|on_action=analyze_text_input|>
|>

<|Table|expandable|
<|{dataframe}|table|>
|>
|>


<|{dataframe}|chart|properties={property_chart}|>


<|layout|columns=1 1 1|
## Positive <|{np.mean(dataframe['Score Pos'])}|text|format=%.2f|raw|>

## Neutral <|{np.mean(dataframe['Score Neu'])}|text|format=%.2f|raw|>

## Negative <|{np.mean(dataframe['Score Neg'])}|text|format=%.2f|raw|>
|>
"""

# Page 2
dataframe2 = dataframe.copy()
path = ""
treatment = 0
page_file = """
<|{path}|file_selector|extensions=.txt|label=Upload .txt file|on_action=analyze_file_input|> <|{f"Downloading {treatment}%..."}|>

<|Table|expandable|
<|{dataframe2}|table|width=100%|>
|>

<|{dataframe2}|chart|properties={property_chart}|>
"""

# Assembling pages
pages = {"/": "<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
         "line": page,
         "text": page_file}


# Run
if __name__ == "__main__":
    Gui(pages=pages).run(title="Hello Taipy GUI", use_reloader=True)
