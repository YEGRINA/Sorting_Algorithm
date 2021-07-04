import tkinter
from tkinter import *
from tkinter import ttk, filedialog
from colors import *
from selectionSort import selection_sort, selection_explanation
from insertionSort import insertion_sort, insertion_explanation
from bubbleSort import bubble_sort, bubble_explanation
from mergeSort import merge_sort, merge_explanation
from quickSort import quick_sort, quick_explanation

# 캔버스 크기
canvas_width = 970
canvas_height = 580

# 윈도우
window = Tk()
window.title('Sorting Visualization')
window.geometry('1000x700')
window.config(bg=WHITE)
window.resizable(False, False)

algorithm_name = StringVar()
algo_list = ['Selection Sort', 'Insertion Sort', 'Bubble Sort',
             'Merge Sort', 'Quick Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']


def drawData(data, colorArray):
    canvas.delete("all")
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * (canvas_height - 10)
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

# 파일에서 데이터 받아옴
def open_file():
    global data
    data = []

    # 파일 불러오기
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(parent=root, initialdir="/", title='Please select a text file')

    if file_path:  # 경로 선택했을 시
        input_file = open(file_path, 'r')
        # 데이터 추출
        line = input_file.readline()
        list = line.split(',')
        for i in list:
           data.append(int(i.strip()))

        input_file.close()
        drawData(data, [BLUE for x in range(len(data))])

# 데이터를 .txt 파일로 저장
def save_file():
    global data

    root = tkinter.Tk()
    root.withdraw()
    dir_path = filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')

    if dir_path:  # 경로 선택했을 시
        output_file = open(dir_path+'/output.txt', 'w')
        for i in data:
            output_file.write(str(i)+'\n')
        output_file.close()

# 정렬 속도
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.005

# 정렬
def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, drawData, timeTick)


# UI
UI_frame = Frame(window, width=1000, height=700, bg=WHITE)
UI_frame.grid(row=0, column=0)

# 정렬 알고리즘 선택
l1 = Label(UI_frame, text='Algorithm: ', bg=WHITE)
l1.grid(row=0, column=0)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list, state='readonly')
algo_menu.grid(row=0, column=1, columnspan=2, pady=5)
algo_menu.current(0)

# 정렬 속도 선택
l2 = Label(UI_frame, text='Speed: ', bg=WHITE)
l2.grid(row=1, column=0)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list, state='readonly')
speed_menu.grid(row=1, column=1, columnspan=2, pady=5)
speed_menu.current(0)

# 설명 라벨
l3 = Label(UI_frame, text='* Explanation *', bg=WHITE, justify='left')
l3.grid(row=0, column=5, rowspan=2)


def show_explanation():
    global l3
    l3.grid_forget()
    if algo_menu.get() == 'Selection Sort':
        l3 = Label(UI_frame, text=selection_explanation(), bg=WHITE, justify='left')
    elif algo_menu.get() == 'Insertion Sort':
        l3 = Label(UI_frame, text=insertion_explanation(), bg=WHITE, justify='left')
    elif algo_menu.get() == 'Bubble Sort':
        l3 = Label(UI_frame, text=bubble_explanation(), bg=WHITE, justify='left')
    elif algo_menu.get() == 'Merge Sort':
        l3 = Label(UI_frame, text=merge_explanation(), bg=WHITE, justify='left')
    elif algo_menu.get() == 'Quick Sort':
        l3 = Label(UI_frame, text=quick_explanation(), bg=WHITE, justify='left')
    l3.grid(row=0, column=5, rowspan=3)


def hide_explanation():
    global l3
    l3.grid_forget()


# 정렬 버튼
b1 = Button(UI_frame, text='Sort', command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=0, pady=10)

# 파일 열기 버튼
b2 = Button(UI_frame, text='Open file', command=open_file, bg=LIGHT_GRAY)
b2.grid(row=2, column=1, pady=10)

# 파일 저장 버튼
b3 = Button(UI_frame, text='Save file', command=save_file, bg=LIGHT_GRAY)
b3.grid(row=2, column=2, pady=10)

# 설명을 보여주는 버튼
b4 = Button(UI_frame, text='show explanation', command=show_explanation, bg=LIGHT_GRAY)
b4.grid(row=2, column=3, pady=10)

# 설명을 숨겨주는 버튼
b5 = Button(UI_frame, text='hide explanation', command=hide_explanation, bg=LIGHT_GRAY)
b5.grid(row=2, column=4, pady=10)

# 캔버스
canvas = Canvas(window, width=canvas_width, height=canvas_height, bg=WHITE)
canvas.grid(row=3, column=0, padx=12)

window.mainloop()
