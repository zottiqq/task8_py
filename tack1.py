import random

questions = [
'ты кто?',
'сколько тебе лет?',
'как тебя зовут?',
'какой у тебя зз?',
'какая у тебя любимая компьютерная игра?',
'какая у тебя любимая песня?',
'как зовут твою маму?',
'как зовут твою бабушку?',
'как зовут твоего папу?',
'как зовут твоего деда?'
]

answer_fun = [
'лошок',
'5',
'васян',
'дракон',
'танки',
'руки вверх',
'бидонисиана',
'бига лав соса',
'хабиб',
'конор макшнакнекс',
]

answer_norm = [
'компьютер',
'???',
'pc',
'неизвестно',
'аватария',
'звуки вселенной',
'???',
'???',
'???',
'???',
]

answer_me = []
answer_pc = []
num_goal = 0

def game():
    global num_goal
    for i in range(10):
        num_goal = num_goal + 1

        if num_goal%2 == 0:
            print()
            print('Ход', i+1)
            print('Компьютер бросает мяч:')
            ran = random.random()
            if ran < 0.7:
                print('Бросок, вы поймали мяч.')
                print('Вопрос:', questions[i])
                answer_me.append(input())
            else:
                print('Бросок, вы не поймали мяч.')
                print('Вопрос:', questions[i])
                answer_me.append(answer_fun[i])

        elif num_goal%2 != 0:
            print()
            print('Ход', i+1)
            print('Вы бросаете мяч:')
            ran = random.random()
            if ran < 0.7:
                print('Компьютер поймал мяч.')
                print('Вопрос:', questions[i])
                answer_pc.append(answer_norm[i])
            else:
                print('Компьютер не поймал мяч.')
                print('Вопрос:', questions[i])
                answer_pc.append(input())
game()
print()
result_pc = list(answer_pc)
result_me = list(answer_me)
print('Жил был на свете', result_pc[0] + '. Ему было', result_me[0], 'лет. Его звали', result_pc[1] + '. Его знак зодиака был', result_me[1] + '. Его любимая игра была', result_pc[2] + '. Его любимая песня была', result_me[2] + '. Его маму звали', result_pc[3] + '. Его бабушку звали', result_me[3] + '. Его папу звали', result_pc[4] + '. Его деда звали', result_me[4])

game()
print()
result_pc = list(answer_pc)
result_me = list(answer_me)
print('Жил был на свете', result_pc[0] + '. Ему было', result_me[0], 'лет. Его звали', result_pc[1] + '. Его знак зодиака был', result_me[1] + '. Его любимая игра была', result_pc[2] + '. Его любимая песня была', result_me[2] + '. Его маму звали', result_pc[3] + '. Его бабушку звали', result_me[3] + '. Его папу звали', result_pc[4] + '. Его деда звали', result_me[4])
