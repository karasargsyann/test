#импорт нужных библиотек
from PyQt5.QtCore import Qt
from random import randint

from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout, QVBoxLayout, QPushButton,
    QGroupBox, QButtonGroup, QLabel, QWidget, QRadioButton
)
from random import shuffle
from random import randint

#создание класса
class Question():
    def __init__(self, question, sanguine, melancholic, phlegmatic, choleric):
        self.question = question
        self.sanguine = sanguine
        self.phlegmatic = phlegmatic
        self.choleric = choleric
        self.melancholic = melancholic

#создание списка вопросов
list_questions = []

#вопросы
list_questions.append(
    Question(
    '2. Ваши особенности в общении с людьми?', 
    'Я быстро нахожу контакт с любым человеком', 
    'Я всегда чувствую истинные мотивы человека при общении',
    'Я никогда не перебиваю собеседника и ценю его мнение', 
    'Я задаю настроение беседы')
)

list_questions.append(
    Question(
    '3. Какой вы на работе или на учёбе?', 
    'Любитель сложных задач и креативщик', 
    'Исполнительный трудяга', 
    'Стрессоустойчивый лидер любого проекта', 
    'Деятельный перфекционист')
)

list_questions.append(
    Question(
    '4. А теперь попробуйте посмотреть на себя со стороны. Какой из вариантов можно отнести к вам?', 
    'Частенько перескакиваю с темы на тему, иногда нетерпелив и могу перебить', 
    'Стою скомкано, а говорю негромко', 
    'Редко выражаю чувства, обычно сдержанный', 
    'Часто тараторю и жестикулирую')
)

list_questions.append(
    Question(
    '5. Ваши негативные черты, которые проявляются особенно ярко?',
    'Часто агрессивный, упрямый и сомневающийся', 
    'Ленивый, нерешительный, ведомый', 
    'Сварливый, вялый, порой пессимистичный', 
    'Непостоянный, нетерпеливый, вспыльчивый')
)

list_questions.append(
    Question(
    '6. Что вы обычно делаете на вечеринке?', 
    'Обычно я в гуще событий: знакомлюсь, общаюсь, веселюсь', 
    'Хожу с бокальчиком любимого напитка и пою знакомые песни', 
    'Кто сказал, что я вообще хожу на вечеринки?', 
    'Танцую как в последний раз')
)

list_questions.append(
    Question(
    '7. Сейчас у вашего друга непростой период в жизни. Что вы сделаете при встрече?', 
    'Найду подходящие слова и вселю в друга\n уверенность в завтрашнем дне. Надо быть позитивнее!',
    'Крепко обниму и выслушаю, помогу найти лучшее решение проблемы', 
    'Дам обдуманный и объективный совет', 
    'Поддержу всеми возможными способами, включая авантюры и приключения до\n ближайшего магазина с мороженым. А еще вытащу на вечеринку!')
)

list_questions.append(
    Question(
    '8. Что вам нравится в людях?', 
    'Жизнерадостность и любовь к своему делу', 
    'Способность видеть прекрасное и проницательность', 
    'Любознательность и тяга к новому', 
    'Отзывчивость и неравнодушие')
)

list_questions.append(
    Question(
    '9. Много ли нужно, чтобы вывести вас из себя? ', 
    'Я злюсь, только когда на это есть веская причина', 
    'Скорее всего, я заплачу и загрущу вместо того чтобы  злиться', 
    'Чтобы вывести меня на эмоции, необходимо приложить много усилий', 
    'Можно даже не стараться, меня может взбесить любая мелочь')
)

list_questions.append(
    Question(
    '10. Что Вы думаете о своей самооценке?', 
    'Она высокая, но не завышенная', 
    'Заниженная', 
    'Она в порядке', 
    'Не могу сказать точно')
)
#главное окно
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Тест на темперамент')
main_window.resize(200, 200)

main_window.sanguine_ball = 0
main_window.melancholic_ball = 0
main_window.phlegmatic_ball = 0
main_window.choleric_ball = 0
main_window.qur_qstn =- 1

#надпись на главном окне и кнопка
main_text = QLabel('Тест создан в развлекательных целях и не несет в себе ничего серьезного.')
btn_ok = QPushButton('Ок')

#главный лайоут, выравнивание текста и кнопки по центру
layout_main = QVBoxLayout()
layout_main.addWidget(main_text, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_ok, alignment = Qt.AlignCenter)

#соединение
main_window.setLayout(layout_main)

#создание горизонтальных лайоутов
hor_line1 = QHBoxLayout()
hor_line2 = QHBoxLayout()
hor_line3 = QHBoxLayout()

#radio button group layouts
rbtn_vert1_layout = QVBoxLayout()
rbtn_vert2_layout = QVBoxLayout()
rbtn_hor_layout = QHBoxLayout()

#виджеты
question_label = QLabel('1. Какие качества можно отнести к вам?')
result = QLabel()

#Radio button groupbox
radio_btn_group = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('Харизматичный, подвижный, непостоянный')
rbtn_2 = QRadioButton('Чувствительный, мягкий, нерешительный')
rbtn_3 = QRadioButton('Спокойный, невозмутимый, целеустремлённый')
rbtn_4 = QRadioButton('Оптимистичный, эмоциональный, общительный')

#Radio button group for renewing rbtns statuses
radio_group = QButtonGroup()
radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)

answer_btn = QPushButton('Ответить')

answer_btn_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# Add radio buttons on layouts of group widget
rbtn_vert1_layout.addWidget(rbtn_1)
rbtn_vert1_layout.addWidget(rbtn_2)
rbtn_vert2_layout.addWidget(rbtn_3)
rbtn_vert2_layout.addWidget(rbtn_4)
rbtn_hor_layout.addLayout(rbtn_vert1_layout)
rbtn_hor_layout.addLayout(rbtn_vert2_layout)
# add layout to radio button widget
radio_btn_group.setLayout(rbtn_hor_layout)

# Add all widgets on main layout and set layout to main window
hor_line1.addWidget(question_label)
hor_line1.addWidget(result)
hor_line2.addWidget(radio_btn_group)
hor_line3.addWidget(answer_btn)

layout_main.addLayout(hor_line1)
layout_main.addLayout(hor_line2)
layout_main.addLayout(hor_line3)

def click_ok():
    if btn_ok.text() == 'Ок':
        question_label.show()
        radio_btn_group.show()
        # answer_btn.show
        main_text.hide()
        btn_ok.hide()
        answer_btn.show()

btn_ok.clicked.connect(click_ok)

question_label.hide()
radio_btn_group.hide()
result.hide()
answer_btn.hide()

def ask(q: Question):
    shuffle(answer_btn_list)
    question_label.setText(q.question)
    answer_btn_list[0].setText(q.sanguine)
    answer_btn_list[1].setText(q.melancholic)
    answer_btn_list[2].setText(q.phlegmatic)
    answer_btn_list[3].setText(q.choleric)
    show_question()

# result = QLabel('результат: сангвиник')
hor_line1.addWidget(result)

def next_question():
        #main_window.quest_counter += 1
        main_window.qur_qstn += 1
        
        if main_window.qur_qstn < len(list_questions):
            qstn = list_questions[main_window.qur_qstn]
            ask(qstn)
        else:
            
            result.setText(
                f"сангвиник: {main_window.sanguine_ball}, "
                f"меланхолик: {main_window.melancholic_ball}, "
                f"флегматик: {main_window.phlegmatic_ball}, "
                f"холерик: {main_window.choleric_ball}"
            )
            result.show()
            question_label.hide()
            radio_btn_group.hide()
            answer_btn.hide()

            

def show_question():
    result_counter()
    question_label.show()
    radio_btn_group.show()
    answer_btn.setText('Ответить')
    # Reset radio buttons statuses
    radio_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio_group.setExclusive(True)


main_window.quest_counter = 0
answer_btn.clicked.connect(next_question)

#показ
def result_counter():
    if answer_btn_list[0].isChecked():
        main_window.sanguine_ball += 1
    if answer_btn_list[1].isChecked():
        main_window.melancholic_ball += 1
    if answer_btn_list[2].isChecked():
        main_window.phlegmatic_ball += 1
    if answer_btn_list[3].isChecked():
        main_window.choleric_ball += 1

main_window.show()
app.exec()