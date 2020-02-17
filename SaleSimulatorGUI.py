__version__ = '0.1.4'

__author__ = 'Vadim Rodberg'

from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import webbrowser as wb
import re

TOTAL_QUESTIONS = 28
COUNT_QUESTION = 1
WRONG_ANSWER = 0
NAME = ''
CITY = ''
STREET = ''
POST = ''

TITLE_WINDOW = f'Обязательный алгоритм поведения продавца в торговом зале'
LARGE_FONT = ('TkDefaultFont', 20)
LARGE_TOTAL_FONT = ('TkDefaultFont', 50)
QUESTION_FONT = ('TkDefaultFont', 12)
WIDTH = 1000
HEIGHT = 600
PADX = 20
PADY = 20

BUTTON_WIDTH = 30
ENTRY_WIDTH = 30
WIDTH_MAIN_FRAMES = 460

BG_BUTTON_GREEN = '#3e8f28'
BG_BUTTON_GREEN_DARK = '#406138'
BG_BUTTON_PUSH_GRAY = 'gray'
FONT_COLOR_WHITE = 'white'
LINK_COLOR_BLUE = 'blue'
DISABLED_COLOR_GRAY = '#adadad'
NO_ACTIVE_TEXT_TIP = '#f0f0f0'
COLOR_RED = 'red'
COLOR_BLACK = 'black'
COLOR_WHITE = FONT_COLOR_WHITE
DEFAULT_FONT = 'TkDefaultFont'

address_city_list = ['выберите город',
                     'г.Москва',
                     'г.Санкт-Петербург',
                     'г.Казань',
                     'г.Тверь',
                     'г.Архангельск',
                     'г.Сочи',
                     'г.Киришы',
                     'г.Уфа']
address_street_moscow_list = ['выберите магазин',
                              'ул.Преображенская, д.43',
                              'ул.Сибирская, д.2, корп.2',
                              'ул.Генерала Конева, д.132',
                              'ул.Смоленская, д.53, лит.А',
                              'пр-т Луначарского, д.55',
                              'ул.Смоленская, д.64',
                              'ул.Якиманка, д.1',
                              'ул.Валовая, д.46, лит.С',
                              'ул.Вишнякова, д.11, лит.В']
address_street_spb_list = ['выберите магазин',
                           'ул.Майора Газова, д.14',
                           'ул.Арсенальная, д.23, корп.1',
                           'ул.Ленина, д.5, лит.Б',
                           'ул.Пушкина, д.95, лит.Б',
                           'ул. Зои Космодемьянской, д.7',
                           'ул.Баринская, д.47, корп.1',
                           'Обводный канал, д.19',
                           'пр-т Невский, д.157, корп.1']
address_street_kazan_list = ['выберите магазин',
                             'ул.Панкратова, д.99',
                             'ул.Челобитная, д.4, корп.3',
                             'ул.Худайбердина, д.7']
address_street_tver_list = ['выберите магазин',
                            'ул.Битникова>, д.55',
                            'ул.Авиационная, д.25, корп.1',
                            'пр-т Космонавтов, д.8',
                            'пр-т Невзорова, д.46, лит.А']
address_street_arhangelsk_list = ['выберите магазин',
                                  'Арбурная площадь, д.21',
                                  'ул.Гостелло, д.66, корп.1']
address_street_sochi_list = ['выберите магазин',
                             'ул.Спортивная, д.2',
                             'ул.Родчельская, д.1, корп.7',
                             'ул.Центральная, д.55',
                             'ул.Лейтенанта Моцарелло, д.69']
address_street_kirishi_list = ['выберите магазин',
                               'ул.Дашевая, д.13',
                               'ул.Пьянова, д.8, корп.1']
address_street_ufa_list = ['выберите магазин',
                           'ул.Высоковольтная, д.5',
                           'ул.Гвардеейская, д.17, лит.В',
                           'ул.Мелеузовская, д.6',
                           'ул.Парвомайская, д.35']
post_list = ['выберите должность',
             'младший продавец',
             'продавец',
             'старший продавец',
             'менеджер',
             'директор магазина']

LISTS_LABEL_FRAME = [
    'Принципы работы с покупателями',  # 1
    'Принципы работы с покупателями',  # 2
    'Установление контакта',  # 3
    'Установление контакта',  # 4
    'Установление контакта',  # 5
    'Установление контакта',  # 6
    'Установление контакта',  # 7
    'Установление контакта',  # 8
    'Выявление потребностей',  # 9
    'Выявление потребностей',  # 10
    'Выявление потребностей',  # 11
    'Выявление потребностей',  # 12
    'Выявление потребностей',  # 13
    'Выявление потребностей',  # 14
    'Работа с возражениями',  # 15
    'Работа с возражениями',  # 16
    'Наиболее частые возражения',  # 17
    'Наиболее частые возражения',  # 18
    'Наиболее частые возражения',  # 19
    'Наиболее частые возражения',  # 20
    'Наиболее частые возражения',  # 21
    'Наиболее частые возражения',  # 22
    'Наиболее частые возражения',  # 23
    'Завершение покупки',  # 24
    'Завершение покупки',  # 25
    'Завершение покупки',  # 26
    'Работа на кассе',  # 27
    'Работа на кассе',  # 28

]

LISTS_LABEL_QUESTION = [
    'Какими качествами должен обладать успешный\nпродавец?',  # 1
    'Как приветствовать покупателя?',  # 2
    'Для чего это нужно?',  # 3
    'Что нужно сделать, когда контакт установлен?',  # 4
    'Покупатель начал осматриваться в магазине.\nКакой вопрос необходимо задать?',  # 5
    'Если на вопрос "Вы у нас впервые?", ответ - ДА,\nЧто сделать?',  # 6
    'Если на вопрос "Вы у нас впервые?", ответ - НЕТ,\nЧто сделать?',  # 7
    'Что сделать если покупатель уверенно чувствует\nсебя в магазине?',  # 8
    'Какие вопросы запрещено использовать?',  # 9
    'Какие вопросы помогают выявлять\nпотребности покупателя?',  # 10
    'Покупатель выбирает ДЛЯ СЕБЯ.\nКак уточнить предпочтения?',  # 11
    'Покупатель выбирает В ПОДАРОК.\nКак уточнить предпочтения?',  # 12
    'Стало понятно, для кого покупатель выбирает алкоголь.\nКакие уточняющие вопросы можно задать?',  # 13
    'Что рекомендуется выявлять в последнюю очередь?',  # 14
    'Почему возникают возражения?',  # 15
    'Из каких пунктов состоит алгоритм\nработы с возражениями?',  # 16
    '"Хочу сравнить цены в другом магазине!"\nВаш ответ:',  # 17
    '"Хочу сравнить с другими магазинами (ассортимент)"\nВаш ответ:',  # 18
    '"Дайте скидку (пожалуйста)!"\nВаш ответ:',  # 19
    '"Мне надо подумать"\nВаш ответ:',  # 20
    '"Мне не нравится светлый цвет коньяка"\nВаш ответ:',  # 21
    '"Это вино не настоящее!(этикетка на русском языке)"\nВаш ответ:',  # 22
    '"У вас нет того, что я хочу/нужно"\nВаш ответ:',  # 23
    'Что важно по завершению покупки?',  # 24
    'Какие фразы запрещено использовать в работе\nс дополнительным товаром?',  # 25
    'На этом этапе нельзя задавать закрытые вопросы.\nНужно рекомендовать и предлагать. Как?',  # 26
    'Обязательные требования при работе за кассой.\nЧто необходимо сделать?',  # 27
    'Для чего нужна карта АМ?',  # 28
]

LISTS_LABEL_NAMES_BUTTON = [
    ['Настойчивость',
     'Доброжелательность',
     'Внимание к портебностям покупателя',
     '"Спотривная" агрессия',
     'Открытость',
     'Умение "впарить"',
     'Фамильярность'],  # 1
    ['Добрый день',
     'Привет! Как дела?',
     'Здрасьте!',
     'Молча кивнуть(поздороваться)',
     'Доброе утро',
     'Добрый вечер',
     'Здравствуйте! Рады вас видеть'],  # 2
    ['Просто так надо/манеджер сказал',
     'В учебниках по маркетингу написано',
     'Чтобы возникло доверие',  #
     'Для того, чтобы "развести" покупателя',
     'Для повышения лояльности покупателя',  #
     'Для повышения уровня собственной коммуникации',
     'Для выявления потребностей'],  # 3
    ['Рассказать о "супер акциях"',
     'Спросиить про погоду',
     'Попросить написать положительный отзыв соцсетях',
     'Дать покупателю осмотреться (1-3 мин)',  #
     'Предложить новинки/эксклюзив',
     'Попросить уйти',
     'Не обращать на него внимания'],  # 4
    ['Вы у нас впервые?',  #
     'Как вы себя чувствуете?',
     'Сколько времени?',
     'Что-то купить хотите?',
     'Подсказать?/Вам помочь?',
     'Чё смотришь? Покупай и уходи!',
     'Какой алкоголь предпочитаете?'],  # 5
    ['Ознакомить покупателя с ассортиментом магазина',  #
     'Отвести к самой продаваемой витрине',
     'Обратить внимание на крепкие напитки',  #
     'Ответить: "Рады видеть вас снова"',
     'Обратить внимание на вина',  #
     'Спросить: "Какой напиток выбираете?"',  #
     'Вам подешевле или подороже?'],  # 6
    ['Ответить: "Вам как обычно?"',
     'Обратить внимание на новинки в ассортименте',  #
     'Обратить внимание на новые акции',  #
     'Предложить сесть',
     'Взять номер телефона',
     'Предложить самый дорогой алкоголь',
     'Спросить: "Какой напиток выбираете?"'],  # 7
    ['Отвести в отдел с коньяками',
     'Ждать когда он попросит помощи',
     'Поздороваться',
     'Предложить самое дешевое красное вино',
     'Спросить: "Вам по-дороже или по-дешевле?"',
     'Поинтересоваться о чем он думает',
     'Начать выявлять потребности'],  # 8
    ['Могу я вам помочь? (Как я мог бы вам помочь?)',
     'Что вас интересует?',
     'Что вы ищете?',
     'Могу я ответить на ваши вопросы?',
     'Водку ищите?',
     'Вы зарплату получили?',
     'Вам похмелиться?'],  # 9
    ['Красное или белое вино?',
     'Какой напиток вы выбираете?',  #
     'Вы закусываете?',
     'Для себя или в подарок?',  #
     'Вы в одиночку будете пить?',
     'Хотите купить дешевый коньяк?',
     'На работу завтра рано вставать?'],  # 10
    ['Что любите?',  #
     'Вы закусываете?',
     'Есть ли предпочтения по сортам винограда, по странам?',  #
     'Что уже пробовали?',  #
     'Будет ли гастрономическое сопровождение? Какое?',  #
     'Хотите купить дешевый коньяк?',
     'Вам виски подороже?'],  # 11
    ['Какие предпочтения у человека?',  #
     'Как видите сами этот подарок?',  #
     'Он часто употребляет алкоголь?',
     'Что для Вас важно в подарке?',  #
     'Можете взять по-дешевле вот это вино',
     'Какой бюджет покупки?',  #
     'Ваш друг/подруга водку пьет?'],  # 12
    ['Какой сорт винограда предпочитаете?',  #
     'Может быть купите подороже?',
     'Для чего Вам алкоголь?..',
     'Для Вас важна страна производителя?',  #
     'Хотите скидку?',
     'Вас инетересуют наши акции?',
     'Вам важна выдержка алкоголя?'],  # # 13
    ['Адрес покупателя',
     'Приходил ли он ранее к нам',
     'Какой алкоголь нравится больше',
     'Лечится ли он от алкоголизма',
     'Знает ли он об акциях магазина',
     'Какая сумма покупки для него комфортна',  #
     'Бывает ли он у конкурентов'],  # 14
    ['Покупатель волнуется',
     'У продавца неприятно пахнет изо рта',
     'Покупатель смотрит влево',
     'Из-за недостаточной информированности покупателя',  #
     'Продавец хамит',
     'Из-за отсутствия денег',
     'По личной инициативе покупателя'],  # 15
    ['Дать клиенту возможность возразить',  #
     'Возвратная реплика',  #
     'Задать уточняющий вопрос',  #
     'Убедить клиента в том, что он не прав',
     'Привести аргументы на языке пользы',  #
     'Подробнее рассказать об акциях',
     'Предложить дальнейшие действия'],  # # 16
    ['Это неправильно. У нас самые низкие цены',
     'Я вас понимаю, важно купить по хорошей цене',  #
     'У конкурентов хуже',
     'У нас гибкая система скидок(дисконтную карта)',  #
     'Если уйдете потом уже не купить со скидкой',
     'Какая цена была бы для вас комфортна?',  #
     'Зачем Вам это нужно?'],  # 17
    ['Вам не нравится наш ассортимент?',
     'Что именно будете сравнивать?',  #
     'Сравнивать нет смысла, у нас лучше',
     'В нашем магазине представлен широкий ассортимент',  #
     'Не тратьте свое время на другие магазины',
     'Какие напитки вы предпочитаете?',
     'Да, понимаю, важно сделать оптимальный выбор'],  # # 18
    ['Мы можем с вами это обсудить',  #
     'Мы не даём скидок, извините',
     'У нас действительно гибкая система скидок',  #
     'У вас есть наша дисконтная карта?',  #
     'Предлагаю оформить карту прямо сейчас, пройдем к кассе',  #
     'Хорошо, какую скидку хотите?',
     'У нас скидки только на водку'],  # 19
    ['Пока думаете товар будет распродан',
     'У нас есть подходящая для Вас акция...',
     'Подумайте над покупкой вот этого коньяка по скидке',
     'Хорошо, думайте. Если что, я возле кассы',
     'Да, важно выбрать то, что вам нужно, то, в чем вы уверены',  #
     'Что именно заставляет вас сомневаться?',  #
     'Что Вас смущает?'],  # # 20
    ['Это естественный цвет, не переживайте',
     'Действительно, коньяк бывает разных оттенков',  #
     'На самом деле цвет этого коньяка натуральный, карамель в него не добавляли',  #
     'Почему вас смущает цвет?',  #
     'Предлагаю выбрать объем и посмотреть его поближе',  #
     'У всех коньяков примерно одинаковый цвет',
     'Его стоит попробовать, предлагаю убедиться в этом'],  # # 21
    ['Я вас понимаю, проблема подлинности алкоголя очень важна',  #
     'Почему вы так думаете?/В чем ваши сомнения?',  #
     'Как только Вы попробуете это вино, Вы поймёте, что заблуждались',
     'Это вино настоящее, гарантирую',
     'Вы просто не разбираетесь в винах, оно подлинное',
     'Предлагаю посмотреть сертификаты качества (система ЕГАИС)',  #
     'Этикетки на русском языке - подтверждение качества напитка'],  # # 22
    ['Да, при таком широком выборе сразу и не сориентироваться/не увидеть',  #
     'Думаю, Вы хотите/Вам нужно воспользоваться нашим спецпредложением',
     'Вино(крепкие напитки) представлено в другом зале',  #
     'Давайте, я помогу Вам понять чего вы хотите?',
     'А что именно вы выбираете?',  #
     'Я уверен, что вы хотите вот эту водку по скидке',
     'Предлагаю пройти и выбрать'],  # # 23
    ['Определиться с выбором (иногда, покупатель ждет рекомендации от вас)',  #
     'Говорить с покупателем на самые разные темы',
     'Напомните, чтобы он не забыл и себя "порадовать"(если покупает в подарок)',  #
     'Открыть дверь на выход',
     'В процессе продажи вы можете предлагать дополнительные товары',  #
     '"К Вашему вину прекрасно подойдет этот сыр"',  #
     'Взять номер телефона'],  # 24
    ['Вот та колбаса - то, что Вам нужно',  #
     'Возьмите сухарики',  #
     'Что то еще?',  #
     'Просто перечислять ассортимент гастрономии',  #
     'Сыр посмотрите?',  #
     'Может быть сыр..?',  #
     'Взять номер телефона'],  # # 25
    ['Вы довольны выбором?',
     'Может быть еще что-то купите?',
     'Приходите к нам как можно чаще...',
     'Я рекомендую...',  #
     'Я надеюсь, что Вам понравился сервис...',
     'Обратите внимание...',  #
     'С вашим вином будет хорошо сочетаться...'],  # # 26
    ['Поприветствовать',  #
     'Уточнить возраст: "Пожалуйста, покажите Ваш паспорт"',  #
     'Не продавать алкоголь покупателю, если ему менее 18 лет',  #
     'Не продавать покупателю табачные изделия, если ему менее 18 лет',  #
     'Уточнить у покупателя о наличии дисконтной карты',  #
     'Если карты нет, предложить ее приобрести, рассказать о преимуществах',  #
     'Убедиться, что покупатель придет в магазин вновь'],  # 27
    ['Для того, чтобы расчитываться ей',
     'Специальные цены для участников Программы лояльности – до 30%',  #
     'Для быстрого доступа к личному кабинету',
     'Скидки, которые иногда суммируются и быстро растут',  #
     'Скидка на день рождения, свадьбу',  #
     'Специальные мероприятия и дегустации',  #
     'Скидки у партнеров']  # # 28
]

LISTS_TIPS = [
    'ВОПРОС 1.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 2.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 3.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 4.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 5.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 6.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 7.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 8.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 9.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 10.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 11.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 12.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 13.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 14.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 15.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 16.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 17.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 18.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 19.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 20.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 21.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 22.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 23.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 24.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 25.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 26.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 27.\nТекст по теме вопроса. Не более 5000 символов',
    'ВОПРОС 28.\nТекст по теме вопроса. Не более 5000 символов',

]


class MotivityTest(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        W_SCREEN = Tk.winfo_screenwidth(self)
        H_SCREEN = Tk.winfo_screenheight(self)
        GEOMETRY = f'{WIDTH}x{HEIGHT}+{W_SCREEN // 2 - WIDTH // 2}+{H_SCREEN // 2 - HEIGHT // 2}'

        Tk.iconbitmap(self, default=r'D:\top_secret\YandexDisk\saleSimulatorGUI\icon\icon1.ico')
        Tk.geometry(self, GEOMETRY)
        Tk.title(self, TITLE_WINDOW)
        Tk.resizable(self, False, False)

        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, InformationOfUser,
                  Question01,
                  Question02,
                  Question03,
                  Question04,
                  Question05,
                  Question06,
                  Question07,
                  Question08,
                  Question09,
                  Question10,
                  Question11,
                  Question12,
                  Question13,
                  Question14,
                  Question15,
                  Question16,
                  Question17,
                  Question18,
                  Question19,
                  Question20,
                  Question21,
                  Question22,
                  Question23,
                  Question24,
                  Question25,
                  Question26,
                  Question27,
                  Question28,
                  Congratulation, StatisticPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.init_style()
        self.init_widgets()

    def init_style(self):
        style_link = ttk.Style()
        style_link.configure('Link.TLabel', foreground=LINK_COLOR_BLUE)

        style_button = ttk.Style()
        style_button.configure('GreenWhiteButton.TLabel', foreground=FONT_COLOR_WHITE, background=BG_BUTTON_GREEN,
                               anchor=CENTER, width=BUTTON_WIDTH, padding=6)
        style_button.map('GreenWhiteButton.TLabel',
                         foreground=[('pressed', FONT_COLOR_WHITE), ('active', FONT_COLOR_WHITE)],
                         background=[('pressed', '!disabled', BG_BUTTON_PUSH_GRAY),
                                     ('active', BG_BUTTON_GREEN_DARK)])

    def init_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(padx=PADX, pady=PADY, expand=True)

        self.label_welcome = ttk.Label(frame, text='Здравствуйте!', font=LARGE_FONT)
        self.label_welcome.pack(pady=PADY)

        self.label_welcome_2 = ttk.Label(frame, text='Рады видеть Вас на обучающем портале Motivity.')
        self.label_welcome_2.pack()

        self.label_welcome_3 = ttk.Label(frame, text='https://ambusiness.ru/', cursor='hand2', style='Link.TLabel')
        self.label_welcome_3.pack(pady=PADY)
        self.label_welcome_3.bind('<Button-1>', lambda event: callback('https://ambusiness.ru/'))

        self.label_welcome_4 = ttk.Label(frame, text='Эта программа предназначена для проверки '
                                                     'знаний эффективных продаж.\n'
                                                     'Вам предлагается ответить на тестовые вопросы, '
                                                     'которые помогут понять какие навыки '
                                                     'нуждаются в улучшении.\n'
                                                     'По итогам формируется статистика ответов. '
                                                     '\n\nУдачного прохождения и хороших продаж!', justify=CENTER)
        self.label_welcome_4.pack()

        self.button = ttk.Button(frame, text='Продолжить', style='GreenWhiteButton.TLabel',
                                 command=lambda: self.controller.show_frame(InformationOfUser))
        self.button.pack(pady=PADY)

        def callback(url):
            wb.open_new_tab(url)


class InformationOfUser(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.init_style()
        self.init_widgets()

    def init_style(self):
        style_link = ttk.Style()
        style_link.configure('Link.TLabel', foreground=LINK_COLOR_BLUE)

        style_button = ttk.Style()
        style_button.configure('GreenWhiteButton.TLabel', foreground=FONT_COLOR_WHITE, background=BG_BUTTON_GREEN,
                               anchor=CENTER, width=BUTTON_WIDTH, padding=6)
        style_button.map('GreenWhiteButton.TLabel',
                         foreground=[('pressed', FONT_COLOR_WHITE), ('active', FONT_COLOR_WHITE)],
                         background=[('pressed', '!disabled', BG_BUTTON_PUSH_GRAY),
                                     ('active', BG_BUTTON_GREEN_DARK)])
        option_menu = ttk.Style()
        option_menu.configure('OM.TLabel', foreground=BG_BUTTON_PUSH_GRAY)

        disabled_button = ttk.Style()
        disabled_button.configure('DisabledButton.TLabel', foreground=FONT_COLOR_WHITE,
                                  background=DISABLED_COLOR_GRAY,
                                  anchor=CENTER, width=BUTTON_WIDTH, padding=6)

    def init_widgets(self):
        frame_0 = ttk.Frame(self)
        frame_0.pack(pady=PADY, expand=True)

        frame_1 = ttk.Frame(frame_0)
        frame_1.pack(pady=PADY, expand=True)
        label_user_name = ttk.Label(frame_1, text='Ваше имя и фамилия:')
        label_user_name.pack(pady=PADY / 2)
        self.label_entry_user_name = ttk.Entry(frame_1, width=ENTRY_WIDTH)
        self.label_entry_user_name.pack()

        frame_2 = ttk.Frame(frame_0)
        frame_2.pack(pady=PADY)
        label_user_name = ttk.Label(frame_2, text='Адрес магазина (в котором Вы работаете)\nи должность:',
                                    justify=CENTER)
        label_user_name.pack(pady=PADY / 2)

        self.change_city = StringVar(frame_2)
        self.change_city.set(address_city_list[0])
        self.change_city.trace('w', lambda *args: self.check_address)
        change_city_option_menu = ttk.OptionMenu(frame_2, self.change_city, *address_city_list, command=self.check_address)
        change_city_option_menu.pack()

        self.change_street = StringVar(frame_2)
        self.change_street.set(address_street_moscow_list[0])
        self.change_street.trace('w', lambda *args: self.check_address)
        self.change_street_option_menu = ttk.OptionMenu(frame_2, self.change_street, *address_street_spb_list,
                                                        command=self.check_address)
        self.change_street_option_menu.configure(state=DISABLED)
        self.change_street_option_menu.pack(pady=PADY / 2)

        self.change_post = StringVar(frame_2)
        self.change_post.set(address_street_moscow_list[0])
        change_change_post_option_menu = ttk.OptionMenu(frame_2, self.change_post, *post_list)
        change_change_post_option_menu.pack()

        button = ttk.Button(frame_2, text='Готово', style='GreenWhiteButton.TLabel',
                            command=lambda: self.buttonInformation())
        button.pack(pady=PADY)

    def buttonInformation(self):
        regex = re.compile('[@_!#$\'"%^&\-*+()<>?/|}{~:;=\]\[.,`]')
        if self.label_entry_user_name.get() == '' or not len(self.label_entry_user_name.get().split()) == 2:
            mb.showinfo('Внимание!', 'Необходимо ввести свои имя и фамилию,\nнапример: Иван Иванов')
        elif len(self.label_entry_user_name.get()) > 30:
            mb.showinfo('Внимание!', 'Ввод не должен превышать 30 символов.')
        elif len(self.label_entry_user_name.get()) <= 5:
            mb.showinfo('Внимание!', 'Ввод не должнен быть менее 5 символов.')
        elif re.findall(r'\d', self.label_entry_user_name.get()) or (regex.search(self.label_entry_user_name.get())):
            mb.showinfo('Внимание!', 'Имя может состоять только из букв.\nВведите корректно.')
        elif self.change_city.get() == address_city_list[0]:
            mb.showinfo('Внимание!', 'Необходимо выбрать город.')
        elif self.change_street.get() == address_street_moscow_list[0]:
            mb.showinfo('Внимание!', 'Необходимо выбрать магазин.')
        elif self.change_post.get() == post_list[0]:
            mb.showinfo('Внимание!', 'Необходимо выбрать вашу должность.')
        else:
            global NAME, CITY, STREET, POST
            NAME += self.label_entry_user_name.get().title()
            CITY += self.change_city.get()
            STREET += self.change_street.get()
            POST += self.change_post.get()
            self.controller.show_frame(Question01)

    def generate_new_option_menu(self, list_streets):
        self.change_street_option_menu.configure(state=NORMAL)
        self.change_street.set(list_streets[0])
        menu = self.change_street_option_menu['menu']
        menu.delete(0, END)
        for e in list_streets:
            menu.add_command(label=e,
                             command=lambda value=e: self.change_street.set(value))

    def check_address(self, *args):
        if self.change_city.get() == address_city_list[1]:
            self.generate_new_option_menu(address_street_moscow_list)
        elif self.change_city.get() == address_city_list[2]:
            self.generate_new_option_menu(address_street_spb_list)
        elif self.change_city.get() == address_city_list[3]:
            self.generate_new_option_menu(address_street_kazan_list)
        elif self.change_city.get() == address_city_list[4]:
            self.generate_new_option_menu(address_street_tver_list)
        elif self.change_city.get() == address_city_list[5]:
            self.generate_new_option_menu(address_street_arhangelsk_list)
        elif self.change_city.get() == address_city_list[6]:
            self.generate_new_option_menu(address_street_sochi_list)
        elif self.change_city.get() == address_city_list[7]:
            self.generate_new_option_menu(address_street_kirishi_list)
        elif self.change_city.get() == address_city_list[8]:
            self.generate_new_option_menu(address_street_ufa_list)


class Question01(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.c_list = []
        self.buttons_list = []
        self.init_style()
        self.init_widget()

    def init_style(self):
        style_button = ttk.Style()

        style_button.configure('GreenWhiteButton.TLabel', foreground=FONT_COLOR_WHITE, background=BG_BUTTON_GREEN,
                               anchor=CENTER, width=BUTTON_WIDTH - 8, padding=6)
        style_button.map('GreenWhiteButton.TLabel',
                         foreground=[('pressed', FONT_COLOR_WHITE), ('active', FONT_COLOR_WHITE)],
                         background=[('pressed', '!disabled', BG_BUTTON_PUSH_GRAY),
                                     ('active', BG_BUTTON_GREEN_DARK)])

        disabled_button = ttk.Style()
        disabled_button.configure('DisabledButton.TLabel', foreground=FONT_COLOR_WHITE,
                                  background=DISABLED_COLOR_GRAY,
                                  anchor=CENTER, width=BUTTON_WIDTH - 8, padding=6)
        style_status = ttk.Style()
        style_status.configure('SStatus.TLabel', foreground=DISABLED_COLOR_GRAY, relief=GROOVE, anchor=CENTER,
                               padding=6)

        style_font_question = ttk.Style()
        style_font_question.configure('SFQuestion.TLabel', font=QUESTION_FONT)

    def init_widget(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(side=TOP, padx=5, pady=5)

        self.label_name_frame = ttk.Labelframe(main_frame, text=LISTS_LABEL_FRAME[COUNT_QUESTION - 1],
                                               width=WIDTH_MAIN_FRAMES,
                                               height=560)
        self.label_name_frame.grid(row=0, column=0, columnspan=3, rowspan=10, sticky=W + E, padx=PADX - 15)
        self.label_question = ttk.Label(main_frame, text=LISTS_LABEL_QUESTION[COUNT_QUESTION - 1],
                                        style='SFQuestion.TLabel')
        self.label_question.grid(row=0, column=0, columnspan=3, rowspan=2, sticky=W, padx=PADX, pady=PADY / 2)
        self.buttons_names_list = LISTS_LABEL_NAMES_BUTTON[COUNT_QUESTION - 1]
        self.frame_container = ttk.Frame(main_frame)
        self.frame_container.grid(row=1, column=0, columnspan=3, sticky=W, padx=PADX, pady=PADY, rowspan=9)

        count = 0
        for checkbutton_text in self.buttons_names_list:
            c = ttk.Checkbutton(self.frame_container, text=checkbutton_text)
            c.state(['!alternate'])
            c.grid(row=count, column=0, sticky=W, columnspan=3, pady=PADY - 5)
            self.c_list.append(c)
            count += 1

        def clear_fun(ch_list):
            for i in ch_list:
                i.state(['!selected'])

        buttons_name_list = ['Ответить',
                             'Далее',
                             'Сброс']
        buttons_state_list = [NORMAL,
                              DISABLED,
                              NORMAL]
        buttons_style_list = ['GreenWhiteButton.TLabel',
                              'DisabledButton.TLabel',
                              'GreenWhiteButton.TLabel']
        button_command_list = [lambda: self.answer_fun(),
                               lambda: self.next_page_count(),
                               lambda: clear_fun(self.c_list)]

        count = 0
        for button in buttons_name_list:
            b = ttk.Button(self.frame_container,
                           text=button,
                           style=buttons_style_list[count],
                           state=buttons_state_list[count],
                           command=button_command_list[count])
            b.grid(row=7, column=count, sticky=W + E, rowspan=2, padx=1, pady=PADY)
            self.buttons_list.append(b)
            count += 1

        self.status_list = ['Отметьте правильные ответы и нажмите "Ответить"',
                            'Правильно! Прочитайте памятку на эту тему и нажмите "Далее"',
                            'Неверный ответ! Прочитайте памятку и попробуйте еще раз.']
        self.label_status = ttk.Label(self.frame_container, text=self.status_list[0], style='SStatus.TLabel')
        self.label_status.grid(row=9, column=0, columnspan=3, sticky=W + E + S + N)

        frame_tip = ttk.Frame(main_frame)
        frame_tip.grid(row=0, column=4, columnspan=3, sticky=W, padx=PADX, pady=PADY, rowspan=9)

        frame_2 = ttk.Labelframe(main_frame, text='Памятка', width=WIDTH_MAIN_FRAMES, height=560)
        frame_2.grid(row=0, column=4, columnspan=3, rowspan=9, sticky=E + W, padx=PADX - 15)

        self.tip = LISTS_TIPS[COUNT_QUESTION - 1]

        self.text_tip = Text(main_frame, height=30, width=69, relief=FLAT, font=DEFAULT_FONT, bg=NO_ACTIVE_TEXT_TIP,
                             wrap=WORD)
        self.text_tip.grid(row=0, column=4, columnspan=3, rowspan=8, padx=PADX, pady=PADY, sticky=W + N + S)
        text_tip_scrollbar = ttk.Scrollbar(main_frame, command=self.text_tip.yview)
        text_tip_scrollbar.grid(row=0, column=6, rowspan=8, columnspan=2, sticky=N + S + E, pady=10, padx=7)
        self.text_tip['yscrollcommand'] = text_tip_scrollbar.set

        self.checkbutton_tip = ttk.Checkbutton(main_frame, text='Я прочитал(а)')
        self.checkbutton_tip.state(['!alternate', DISABLED])
        self.checkbutton_tip.grid(row=8, column=4, sticky=W, padx=PADX, rowspan=2)

        self.go_to_motivity = ttk.Button(main_frame, text='Подробнее', state=DISABLED, style='DisabledButton.TLabel',
                                         command=lambda: wb.open_new_tab(
                                             'https://ambusiness.ru/study/plan/material/13'))
        self.go_to_motivity.grid(row=8, column=6, sticky=E, padx=PADX, rowspan=2)

        label_bottom = ttk.Frame(self)
        label_bottom.pack(side=TOP, fill=BOTH)

        self.label_info_user = ttk.Label(label_bottom, text='')
        self.label_info_user.pack(side=LEFT, anchor=W, padx=PADX + 3)
        self.label_info_user.after(100, self.refresh_label)

        label_author = ttk.Label(label_bottom, text=f'Author: {__author__}  |  v.{__version__}',
                                 foreground=DISABLED_COLOR_GRAY)
        label_author.pack(side=RIGHT, anchor=E, padx=PADX + 3)

    def refresh_label(self):
        INFO_USER = f'{NAME}  | {POST}  |  {CITY}, {STREET}  |  Вопрос: {COUNT_QUESTION}/{TOTAL_QUESTIONS}'
        self.label_info_user.configure(text=INFO_USER)
        self.label_info_user.after(100, self.refresh_label)

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def if_yes(self):
        for ct in self.c_list:
            ct.state(['!alternate', DISABLED])

        self.buttons_list[0].configure(state=DISABLED, style='DisabledButton.TLabel')
        self.buttons_list[2].configure(state=DISABLED, style='DisabledButton.TLabel')

        self.label_status.configure(text=self.status_list[1], foreground=FONT_COLOR_WHITE,
                                    background=BG_BUTTON_GREEN,
                                    relief=FLAT)

        self.text_tip.configure(state=NORMAL)
        self.text_tip.delete('1.0', END)
        self.text_tip.insert(END, self.tip)
        self.text_tip.configure(state=DISABLED)
        self.checkbutton_tip.configure(state=NORMAL,
                                       command=lambda: close_check_button_tip())
        self.checkbutton_tip.state(['!alternate'])
        self.checkbutton_tip.state(['!selected'])
        self.go_to_motivity.configure(state=NORMAL, style='GreenWhiteButton.TLabel')

        def close_check_button_tip():
            self.buttons_list[1].configure(state=NORMAL, style='GreenWhiteButton.TLabel')
            self.checkbutton_tip.configure(state=DISABLED)

    def if_not(self):
        global WRONG_ANSWER
        WRONG_ANSWER += 1

        for ch in self.c_list:
            ch.state(['!alternate', DISABLED])

        self.label_status.configure(text=self.status_list[2], foreground=FONT_COLOR_WHITE, background=COLOR_RED,
                                    relief=FLAT)

        self.text_tip.configure(state=NORMAL)
        self.text_tip.delete('1.0', END)
        self.text_tip.insert(END, self.tip)
        self.text_tip.configure(state=DISABLED)

        for bl in self.buttons_list:
            bl.configure(state=DISABLED, style='DisabledButton.TLabel')

        self.checkbutton_tip.configure(state=NORMAL, command=lambda: enabled_buttons())
        self.checkbutton_tip.state(['!alternate'])
        self.checkbutton_tip.state(['!selected'])

        self.go_to_motivity.configure(state=NORMAL, style='GreenWhiteButton.TLabel')

        def enabled_buttons():
            for chl in self.c_list:
                chl.configure(state=NORMAL)
                chl.state(['!alternate'])
                chl.state(['!selected'])

            self.buttons_list[0].configure(state=NORMAL, style='GreenWhiteButton.TLabel')
            self.buttons_list[2].configure(state=NORMAL, style='GreenWhiteButton.TLabel')

            self.checkbutton_tip.configure(state=DISABLED)
            self.checkbutton_tip.state(['!alternate'])

            self.label_status.configure(text=self.status_list[0], foreground=DISABLED_COLOR_GRAY,
                                        background=NO_ACTIVE_TEXT_TIP,
                                        relief=GROOVE)

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question02)


class Question02(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[1])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[1])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[1]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[1]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question03)


class Question03(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[2])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[2])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[2]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[2]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question04)


class Question04(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[3])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[3])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[3]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[3]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question05)


class Question05(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[4])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[4])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[4]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[4]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question06)


class Question06(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[5])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[5])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[5]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[5]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question07)


class Question07(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[6])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[6])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[6]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[6]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question08)


class Question08(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[7])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[7])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[7]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[7]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question09)


class Question09(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[8])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[8])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[8]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[8]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question10)


class Question10(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[9])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[9])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[9]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[9]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question11)


class Question11(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[10])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[10])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[10]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[10]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question12)


class Question12(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[11])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[11])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[11]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[11]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question13)


class Question13(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[12])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[12])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[12]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[12]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question14)


class Question14(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[13])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[13])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[13]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[13]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question15)


class Question15(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[14])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[14])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[14]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[14]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question16)


class Question16(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[15])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[15])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[15]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[15]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        COUNT_QUESTION += 1
        self.controller.show_frame(Question17)


class Question17(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[16])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[16])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[16]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[16]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Question18)


class Question18(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[17])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[17])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[17]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[17]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Question19)


class Question19(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[18])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[18])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[18]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[18]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Question20)


class Question20(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[19])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[19])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[19]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[19]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Question21)


class Question21(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[20])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[20])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[20]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[20]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Question22)


class Question22(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[21])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[21])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[21]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[21]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Question23)


class Question23(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[22])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[22])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[22]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[22]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['!selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Question24)


class Question24(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[23])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[23])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[23]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[23]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['!selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Question25)


class Question25(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[24])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[24])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[24]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[24]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Question26)


class Question26(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[25])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[25])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[25]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[25]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['!selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['!selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Question27)


class Question27(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[26])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[26])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[26]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[26]

    def answer_fun(self):
        if self.c_list[0].instate(['selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['!selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Question28)


class Question28(Question01):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_widgets()

    def init_widgets(self):
        self.label_name_frame.configure(text=LISTS_LABEL_FRAME[27])
        self.label_question.configure(text=LISTS_LABEL_QUESTION[27])
        self.buttons_names_list[0:7] = LISTS_LABEL_NAMES_BUTTON[27]

        count_new_name = 0
        for new_name in self.c_list:
            new_name.configure(text=self.buttons_names_list[count_new_name])
            new_name.state(['!alternate'])
            count_new_name += 1

        self.tip = LISTS_TIPS[27]

    def answer_fun(self):
        if self.c_list[0].instate(['!selected']) and \
                self.c_list[1].instate(['selected']) and \
                self.c_list[2].instate(['!selected']) and \
                self.c_list[3].instate(['selected']) and \
                self.c_list[4].instate(['selected']) and \
                self.c_list[5].instate(['selected']) and \
                self.c_list[6].instate(['selected']):
            self.if_yes()
        else:
            self.if_not()

    def next_page_count(self):
        global COUNT_QUESTION
        self.controller.show_frame(Congratulation)


class Congratulation(StartPage):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.label_welcome.configure(text="Поздравляем!")
        self.label_welcome_2.configure(text="Вы прошли тестирование.\nНапоминаем, что все материалы Вы можете прочитать на нашем сайте:", justify=CENTER)
        self.label_welcome_4.configure(text="Мы сформировали небольшую статистику по вашим ответам.\nЧтобы её увидеть нажмите \"Узнать результат\"")
        self.button.configure(text="Узнать результат", command=lambda: self.controller.show_frame(StatisticPage))


class StatisticPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.init_style()
        self.init_widgets()

    def init_style(self):
        style_button = ttk.Style()
        style_button.configure('GreenWhiteButton.TLabel', foreground=FONT_COLOR_WHITE, background=BG_BUTTON_GREEN,
                               anchor=CENTER, width=BUTTON_WIDTH - 8, padding=6)
        style_button.map('GreenWhiteButton.TLabel',
                         foreground=[('pressed', FONT_COLOR_WHITE), ('active', FONT_COLOR_WHITE)],
                         background=[('pressed', '!disabled', BG_BUTTON_PUSH_GRAY),
                                     ('active', BG_BUTTON_GREEN_DARK)])

        style_font_total = ttk.Style()
        style_font_total.configure('SFTotal.TLabel', font=LARGE_FONT, foreground='#444343')

    def init_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(padx=PADX, pady=PADY, expand=True)

        frame_left = ttk.Frame(frame)
        frame_left.pack(side=LEFT, padx=PADX * 3)

        def refresh_label_name():
            name = f'Имя:\n{NAME}'
            label_name.configure(text=name)
            label_name.after(100, refresh_label_name)

        label_name = ttk.Label(frame_left, text='')
        label_name.grid(row=0, column=0, padx=PADX, pady=PADY // 2, sticky=W)
        label_name.after(100, refresh_label_name)

        def refresh_label_address():
            address = f'Адрес магазина:\n{CITY} {STREET}'
            label_address.configure(text=address)
            label_address.after(100, refresh_label_address)

        label_address = ttk.Label(frame_left, text='')
        label_address.grid(row=1, column=0, padx=PADX, pady=PADY // 2, sticky=W)
        label_address.after(100, refresh_label_address)

        def refresh_label_post():
            post = f'Должность:\n{POST}'
            label_post.configure(text=post)
            label_post.after(100, refresh_label_post)

        label_post = ttk.Label(frame_left, text='')
        label_post.grid(row=2, column=0, padx=PADX, pady=PADY // 2, sticky=W)
        label_address.after(100, refresh_label_post)

        frame_right = ttk.Labelframe(frame)
        frame_right.pack(side=LEFT, padx=PADX * 3)

        label_total = ttk.Label(frame_right, text='Итог:', style='SFTotal.TLabel')
        label_total.grid(row=0, column=0, padx=PADX, pady=PADY // 2, sticky=W)

        label_all_question = ttk.Label(frame_right, text='Всего вопросов:')
        label_all_question.grid(row=1, column=0, padx=PADX, pady=PADY // 2, sticky=W)
        label_all_question_1 = ttk.Label(frame_right, text=TOTAL_QUESTIONS)
        label_all_question_1.grid(row=1, column=1, padx=PADX, pady=PADY // 2, sticky=E)

        label_correct_answer = ttk.Label(frame_right, text='Правильных ответов:')
        label_correct_answer.grid(row=2, column=0, padx=PADX, pady=PADY // 2, sticky=W)

        def refresh_label_correct_answer():
            correct_answer = f'{COUNT_QUESTION}'
            label_correct_answer_1.configure(text=correct_answer)
            label_correct_answer_1.after(100, refresh_label_correct_answer)

        label_correct_answer_1 = ttk.Label(frame_right, text='')
        label_correct_answer_1.grid(row=2, column=1, padx=PADX, pady=PADY // 2, sticky=E)
        label_correct_answer_1.after(100, refresh_label_correct_answer)

        label_incorrect_answer = ttk.Label(frame_right, text='Неудачных попыток:')
        label_incorrect_answer.grid(row=3, column=0, padx=PADX, pady=PADY // 2, sticky=W)

        def refresh_label_wrong_answer():
            incorrect_answer = f'{WRONG_ANSWER}'
            label_incorrect_answer_1.configure(text=incorrect_answer)
            label_incorrect_answer_1.after(100, refresh_label_wrong_answer)

        label_incorrect_answer_1 = ttk.Label(frame_right, text='')
        label_incorrect_answer_1.grid(row=3, column=1, padx=PADX, pady=PADY // 2, sticky=E)
        label_incorrect_answer_1.after(100, refresh_label_wrong_answer)

        label_conclusion = ttk.Frame(frame_right)
        label_conclusion.grid(row=4, column=0, columnspan=2, padx=PADX, pady=PADY // 2, ipady=4)

        label_professional = ttk.Label(label_conclusion, text='Вы владеете мастерством продаж на:')
        label_professional.grid(row=0, column=0, ipady=5, sticky=W)

        def answer_professional():
            summary = (WRONG_ANSWER * 100) / TOTAL_QUESTIONS
            summary = 100 - summary
            if summary <= 0:
                summary = 0
            label_professional_1.configure(text=f'{round(summary, 1)}%')

        label_professional_1 = ttk.Label(label_conclusion, text='')
        label_professional_1.grid(row=0, column=1, sticky=E)

        button_professional = ttk.Button(label_conclusion, text='Узнать', style='GreenWhiteButton.TLabel',
                                         command=answer_professional)
        button_professional.grid(row=1, column=0, sticky=W, )


if __name__ == '__main__':
    app = MotivityTest()
    app.mainloop()
