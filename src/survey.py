import pandas as pd
import PySimpleGUI as sg
import matplotlib.pyplot as plt
df = pd.read_excel('../data/data.xlsx')

sg.theme_global("Dark")
layout = [[sg.Text("Please fil up the details: ")],
          [sg.Text("Name", size=(10, 2)), sg.InputText(key="Name")],
          [sg.Text("Age", size=(10, 2)), sg.InputText(key="Age")],
          [sg.Text("Education", size=(10, 2)), sg.InputText(key="Education")],
          [sg.Text("Address", size=(10, 2)), sg.InputText(key="Address")],
          [sg.Text("Favourite programming language", size=(10, 4)), sg.InputText(key="Favourite programming language")],
          [sg.Button("Submit"), sg.Button("Exit"), sg.Button("Clear"), sg.Button("Show previous chart")]
          ]
window = sg.Window("Survey application", layout)


# clearing the field
def clearForm():
    for keys in values:
        window[keys]('')


# showing the previous chart
def showChart():
    # df = pd.read_excel('../data/data.xlsx')
    # print(df['Known programming languages'])
    df['Favourite programming language'].value_counts().plot(kind='bar', figsize=(10, 7))
    plt.title("Survey")
    plt.xlabel("Programming languages")
    plt.ylabel("Uses")
    plt.legend()
    plt.show()


flag = 0
# try:
while True:
    event, values = window.read()
    print(values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Show previous chart":
        showChart()
    if event == "Clear":
        clearForm()
    if event == "Submit":
        for key in values:  # checking if fields are empty or not
            print(values[key])
            if values[key] == '':
                flag = 1
        if flag == 1:
            sg.Popup("Fields can't be empty!")
            break
        df = df.append(values, ignore_index=True)
        df.to_excel('../data/data.xlsx', index=False)
        sg.Popup("Data Saved")
        clearForm()

window.close()
# except:
#     print("Some error has occurred!")
