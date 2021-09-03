import tkinter as tk


def cal():
    wrong = 0
    if height_input.get() == '':
        wrong += 1
    else:
        for i in height_input.get():
            if i == '.':
                continue
            if i < '0' or i > '9':
                wrong += 1

    if weight_input.get() == '':
        wrong += 1
    else:
        for i in weight_input.get():
            if i < '0' or i > '9':
                wrong += 1
    if wrong > 0:
        result_label = '請輸入數字'
        result.configure(text=result_label, bg='black', fg='white')
    else:
        hvalue = float(height_input.get())
        wvalue = float(weight_input.get())
        bmi_value = round(wvalue / (hvalue*hvalue), 2)
        result_label = '你的 BMI 指數為：{} {}'.format(bmi_value, get_bmi_status_description(bmi_value))
        result.configure(text=result_label, bg='white', fg='black')


def get_bmi_status_description(bmi_value):
    if bmi_value < 18.5:
        return '體重過輕囉，多吃點！'
    elif (bmi_value >= 18.5) and (bmi_value < 24):
        return '體重剛剛好，繼續保持！'
    elif bmi_value >= 24:
        return '體重有點過重囉，少吃多運動！'


# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
window.title('BMI calculator')
window.geometry('500x300')
window.config(bg='white')

label = tk.Label(window, text='BMI calculator', bg='white', font=('Times New Roman', 14), height=2)
label.pack()

heightFrame = tk.Frame(window)
heightFrame.config(bg='white')
heightFrame.pack()
tk.Label(heightFrame, bg='white').pack()
height = tk.Label(heightFrame, text='身高 (m): ', bg='white', font=('Times New Roman', 14))
height.pack(side=tk.LEFT)
height_input = tk.Entry(heightFrame)
height_input.pack()


weightFrame = tk.Frame(window)
weightFrame.config(bg='white')
weightFrame.pack()
tk.Label(weightFrame, bg='white').pack()
weight = tk.Label(weightFrame, text='體重 (kg): ', bg='white', font=('Times New Roman', 14))
weight.pack(side=tk.LEFT)
weight_input = tk.Entry(weightFrame)
weight_input.pack()

result = tk.Label(bg='white')
result.pack()

button = tk.Button(window, text='立即計算', command=cal)
button.pack()

# 運行主程式
window.mainloop()
