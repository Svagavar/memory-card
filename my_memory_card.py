#создай приложение для запоминания информации
from PyQt5.Qt.Core import Qt
from PyQt5.QtWidgets import QApplication, Qwidget, QPushButton, QLabel, QVBoxLayout
class Question():
    ''' Содержит вопрос, 1 правильный и 3 не правильных '''
    def __init__(self, qustion, right_answer, wrong1, wrong2, wrong3):
     self.question = question
     self.right_answer = right_answer
     self.wrong1 = wron1
     self.wrong2 = wrong2
     self.wrong3 = wrong3
question_list = []
question_list.append(Question('Госудраственный язык Бразилии,','Португальский', 'Английский','Испанский', 'Бразильский' ))
question_list.append(Question('Какого цвета нет на флаге Росии?','Зеленый', 'Красный', 'Белый', 'синий' ))
question_list.append(Question('Национальная хижина якутов', 'Ураса','Юрта', 'Иглу', 'Хата' ))
app=QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,200 )
btn_OK = Qpush('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox('Варианты ответов')

btn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Прав ты или нет')

layout_res = QVBoxLayout
layout_res.addWidget(lb_result, alingment=(Qt.AlignLeft | Qt.AlignVTop))
layout_res.addWidget(lb_correct, alingment= Qt.AlignHcenter, strech = 2)
AnsGroupBox.set(layout/res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment(Qt.AlignHcenter | Qt/AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
'''layout_line2.addWidget9AnsGroupBox)
layout_line2.addwidget(AnsGroupBox)
RadioGroupBox.hide()'''
layout_line3.addStrecth(1)
layout-line3.addwidget(btn_OK,stretch=2)
layout_line3.addstrech(1)
layout_card=QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStrech(1)
layout_card.set.Spacing(5)
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.show()

app.exec()

def show_qustion():
  ''' показать понель ответов '''
  RadioGroupBox.show()
  AnsGroupBox.hide
  btn_OK.setText('Ответить')

def show_result():
  ''' показать панель ответов '''
  RadioGroupBox.hide()
  AnsGroupBox.show()
  btn_OK.setText('Следующий вопрос')

  RadioGroup.setExclusive(false)
  rbtn_1.setChecked(false)
  rbtn_2.setChecked(false)
  rbtn_3.setChecked(false)
  rbtn_4.setChecked(false)
  RadioGroup.setExclusive(false)

def test():
    ''' временная функция, котораафя позволяет нажатием на кнопку вызывать по очереди show_result() либо show_question() '''
    if 'ответить' == btn_OK.text():
        show_result()
    else:
        show_question
answers= [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(question, right_answer, wrong1, wrong2, wrong3):
    ''' функция записывает значения вопроса  и ответов в соответствующие виджеты, при этом варианты ответов  распределяются случайным образом '''
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_Question.setText(question)
    lb.correct.setText(right_answer)
    show.question()
def show_correct(res):
    ''' показать результат  - установим переданный текст в надпись ''результат'' и покажем нужную панель '''
   
    lb_Result.setText(res)
    show_result()
def check_answer():
 ''' показать результат  - установим переданный текст в надпись ''результат'' и покажем нужную панель '''
   
inanswers[0.is Checked]
btn_Ok.clicked.connect(check_answers)
window.setLayout(layout_card)
windows.show()
app.exec
def next_question():
    ''' задает следущий запрос из списка '''
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
        q = question_list(window.cur_question)
        ask(q)
def click_OK(): 
    ''' определяет надо ли сказать другой вопрос либо проверить на этот '''
    if btn_Ok.text() == 'Ответить':
        check_answer
    else:
        next_question()
def asc(q: Question):
    ''' функция  записывает значения вопроса и ответов в соответствующие при этом варианты ответов распределяются случайным образом'''
    suffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show-question()
def next_question():
    ''' задает случайный вопрос из списка '''
    window.total += 1
    print ('Статистика\n-вс-всего:', 'window total,' '\n-Правильных оветов: ', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q =  question_list[cur_question]
    ask(q)
window = Qwidget()
window.score = 0
window.total = 0
next_question()
window.resize(400,300)
window.show()
app.exec