import ctypes
import time
import tkinter as tk
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except AttributeError:
    pass

from equation_calculater import *
from color_blank import *

root = tk.Tk()
root.configure(bg=color_dark_blue)
root.title("CiseCount 计算器")
root.geometry("1440x810")

# 显示答案的地方
head_label = None
def create_head(head_text, color=color_black):
    global head_label
    if head_label:
        # 如果 Label 组件已经存在，更新其文本内容
        head_label.config(text=head_text)
    else:
        # 如果 Label 组件不存在，创建新的 Label 组件
        head_label = tk.Label(root, text=head_text, bg=color_orange, fg=color, font=('黑体', 20))
        head_label.place(relx=0.82, rely=0.3, relwidth=0.31, relheight=0.08, anchor="center")

def equation_calculate():
    equation = equation_text.get()
    variables = variable_frame.get()
    result = equation_calculater(equation, variables, fraction_enable=not realness_or_fraction)
    if "#" in str(result):
        result = result.replace("#", "")
        create_head(result, color=color_red)
    else:
        create_head(result)



# 点击计算按钮
def calculate_button():
    equation_calculate()
calculate_button = tk.Button(root, text="计算", bg=color_light_blue, command=calculate_button, font=("黑体", 20))
calculate_button.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.08, anchor="center")


equation_frame = tk.Frame(root, bg=color_grey)
equation_frame.place(relx=0.5, rely=0.14, relwidth=0.95, relheight=0.15, anchor="center")
# 在equation_frame中添加一个输入文本框
equation_text = tk.Entry(equation_frame, bg=color_white, fg=color_black, font=("Arial", 20))
equation_text.place(relx=0.5, rely=0.25, relwidth=0.95, relheight=0.4, anchor="center")
# 在equation_frame中添加一个变量的输入文本框，直接建立在equation_frame的逻辑关系下
variable_frame = tk.Entry(equation_frame, bg=color_white, fg=color_black, font=("Arial", 20))
variable_frame.place(relx=0.3, rely=0.75, relwidth=0.55, relheight=0.4, anchor="center")
# 提示文本
equation_inform = tk.Label(equation_frame, text="←变量   表达式↑ 计算模式→",
                           bg=color_grey, fg=color_black, font=("黑体", 16))
equation_inform.place(relx=0.73, rely=0.75, relwidth=0.29, relheight=0.4, anchor="center")
# 在equation_frame中添加一个按钮，用于切换计算模式
realness_or_fraction = False  # 初始状态为fraction有理数模式

def calculate_mode_button():
    global realness_or_fraction
    if realness_or_fraction:
        search_link_fuzzy_button.config(bg=color_light_pink, text="有理数")
        realness_or_fraction = False
    else:
        search_link_fuzzy_button.config(bg=color_light_blue, text="浮点数")
        realness_or_fraction = True

search_link_fuzzy_button = tk.Button(equation_frame, text="有理数", bg=color_light_pink,
                                     command=calculate_mode_button, font=("黑体", 16))
search_link_fuzzy_button.place(relx=0.93, rely=0.75, relwidth=0.09, relheight=0.4, anchor="center")


create_head("结果在这里")
root.mainloop()

# 一直循环，直到用户关闭窗口








