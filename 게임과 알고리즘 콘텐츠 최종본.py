print("게임을 시작합니다.")

print("(게임을 계속하려면 엔터를 눌러주세요.)")
a = input("")
if (a == "") :
    print("-------------")
    print("수뭉이 게임을 시작합니다.")
    print("귀여운 새내기 수뭉이는 오늘도 학교에 갑니다.")
    print("준비를 마친 수뭉이는 집에서 나와 버스를 타러 갑니다.")
    print("(게임을 계속하려면 엔터를 눌러주세요.)")
else :
    print("게임을 종료합니다.")         
b = input("")
if  (b == ""):
    print("버스기사님 : 수뭉아 안녕~ 좋은 아침!! 학교 가니?")
    print("수뭉이 : 안녕하세요. 기사님! 네. 학교 가요~~")
    print("버스기사님 : 그렇구나! 오늘은 특별히 나와 가위바위보를 해서 이겨야지만 버스에 탈 수 있단다. 가위바위보!!!!")
    print("수뭉이 : 네......!?!?!?")
    print('')
    print("[지옥의 가위바위보 게임]")
    print("한번 이기면 1점씩 얻고 한번 질 때마다 1점씩 잃는다.")
    print("3점을 얻어야 버스를 탑승 가능")
    print("(게임을 계속하려면 엔터를 눌러주세요.)")
else :
    print("게임을 종료합니다.")

w = input("")
if (w == ""):

    rock = '''

            ****
            ****
            
'''

    scissor = '''
        *        *
         *      *
           *   *
             *
 '''
 
    paper = '''
				*******
				*******
				*******
				*******
'''

import random
point=3
 
game_option = [rock, scissor, paper]
com_choice_a = random.randint(0,2)
com_choice_b = random.randint(0,2)
com_choice_c = random.randint(0,2)

 
while True:
        user_choice = int(input(" 0: 바위, 1: 가위, 2: 보 >>>	"))
 
        print("나의 선택 : ")
        print(game_option[user_choice])
 
        print("컴퓨터 선택 : ")
        print(game_option[com_choice_a])
 
        if com_choice_a == user_choice :
                print("비겼습니다.")
 
        elif user_choice - com_choice_a == -1 or (user_choice ==2 and com_choice_a ==0 ) :
                 point+=1
                 print("이겼습니다.")

        else:
                point+=-1
                print("졌습니다.")

        if point<1:
                print('버스기사님의 승리입니다. 수뭉이는 다음 버스를 타야 합니다!')
                play = False

        elif point>=6:
                 print('버스기사님과의 가위바위보 대결에서 승리하였습니다! 버스에 탑승합니다.')
                 break

        else:
                if point==2 or point==4 :
                        user_choice = int(input(" 0: 바위, 1: 가위, 2: 보 >>>	"))
 
                        print("나의 선택 : ")
                        print(game_option[user_choice])
 
                        print("컴퓨터 선택 : ")
                        print(game_option[com_choice_b])
 
                        if com_choice_b == user_choice :
                                print("비겼습니다.")
 
                        elif user_choice - com_choice_b == -1 or (user_choice ==2 and com_choice_b ==0 ) :
                                 point+=1
                                 print("이겼습니다.")

                        else:
                                point+=-1
                                print("졌습니다.")
                elif point==1 or point==5 :
                        user_choice = int(input(" 0: 바위, 1: 가위, 2: 보 >>>	"))
 
                        print("나의 선택 : ")
                        print(game_option[user_choice])
 
                        print("컴퓨터 선택 : ")
                        print(game_option[com_choice_c])
 
                        if com_choice_c == user_choice :
                                print("비겼습니다.")
 
                        elif user_choice - com_choice_c == -1 or (user_choice ==2 and com_choice_c ==0 ) :
                                 point+=1
                                 print("이겼습니다.")

                        else:
                                point+=-1
                                print("졌습니다.")
                
#민서게임 시작 

print("게임을 시작합니다.")
print("(게임을 계속하려면 엔터를 눌러주세요.)")

c = input("")
if (c == "") :
    print("수뭉이 : 휴...간신히 탔다....!!")
    print("(꼬르르르르륵)")
    print("(사람들이 모두 수뭉이를 쳐다본다.)")
    print("수뭉이 : 맞다! 오늘 아침을 안먹고 나왔잖아!?")
    print("수뭉이 : 지금 먹고 가야겠다!")
    print('')
    print("[아침밥 먹기 게임]")
    print("밥을 먹으면 1점씩 올라간다.")
    print("벽에 몸이 닿거나 자기 꼬리에 닿으면  탈락")
    print("5점을 얻게되면 게임 클리어!")
else :
    print("게임을 종료합니다.")

z = input("")
if (z == ""):
    #터틀 객체/시간/랜덤/스크린 소환
    from turtle import Turtle, Screen
    import time
    import random
    
# snake 함수의 0번째 인덱스 (머리)

def up() :
    # up키는 아래쪽(270)을 향하고 있지 않을 때만 실행 모든 방향 동일
    if snakes[0].heading() != 270:
        snakes[0].setheading(90)

def down() :
    if snakes[0].heading() != 90 :
        snakes[0].setheading(270)

def right() :
    if snakes[0].heading() != 180 :
        snakes[0].setheading(0)

def left() :
    if snakes[0].heading() != 0 :
        snakes[0].setheading(180)

# 스네이크 만들기 / 먹이를 먹을 때마다 snake 길이가 늘어나기 때문에 함수로 설정
# 바뀌는 위치를 매개변수 (pos) 로 설정

def create_snake(pos) :
    snake_body = Turtle()
    snake_body.shape("square")
    snake_body.color("orangered")
    snake_body.up()
    snake_body.goto(pos)
    snakes.append(snake_body)

# food 위치 랜덤 함수

def rand_pos() :
    rand_x = random.randint(-250,250)
    rand_y = random.randint(-250,250)
    # rand x, rand y의 값을 return 으로 가져
    return rand_x, rand_y 

# 점수 올려주는 함수

def score_update():
    # 전역부 함수 - global 키워드 
    global score
    #점수 1점씩 올려줌 
    score += 1
    #이전의 글 지워줌 
    score_pen.clear()
    score_pen.write(f"점수 : {score}", font = ("", 15, "bold"))

# 게임오버 알려주는 함수 
def game_over() :
    score_pen.goto(0,0)
    score_pen.write("Game Over", False, "center", ("", 30, "bold"))
    exitonclick()

# 게임윈 알려주는 함수
def game_clear() :
    score_pen.goto(0,0)
    score_pen.write("Game Clear", False, "center", ("", 30, "bold"))
    
#스크린 설정
screen = Screen()
screen.setup(600,600)
screen.bgcolor("khaki")
screen.title("Snake Tail Game")
screen.tracer(0)   #트레이서 기능을 끄면 스크린 업데이트 뜰 때만 업데이트 시켜서 이동의 부드러움 증가시킴 


# snake 객체 만들기
#세개의 snake 모양 3개 잡고 위치 잡기

start_pos = [(0,0),(-20,0),(-40,0)]
snakes = []  #이런 snake 바디를 저장해줄 리스트
score = 0 # 스코어 변수 초기값 0으로 설정 

for pos in start_pos :
    create_snake(pos)

#먹이
food = Turtle()
food.shape("circle")
food.color("snow")
food.up()
food.speed(0)
# food 위치 랜덤 <- 위에 함수 
food.goto(rand_pos())

#점수 표시
#점수를 만들기 위한 객체
score_pen = Turtle()
#점수 위에 위치 
score_pen.ht()
score_pen.up()
score_pen.goto(-270,250)
score_pen.write(f"점수 : {score}", font = ("", 15, "bold"))


#그래픽창에 포커스를 맞추기 위해
screen.listen()
# 키보드 사용해서 이동시키려면
screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")
screen.onkeypress(left,"Left")
screen.onkeypress(right,"Right")

# game_on 변수 설정
game_on = True
while game_on :
    screen.update()
# snake 속도 조절
    time.sleep(0.1)

# 꼬리에 해당하는 인덱스 = 전체 -1 (인덱스는 0부터 시작이니) /꼬리부터 -1씩 이동 / 0까지
    for i in range(len(snakes) -1, 0, -1):
# i번째보다 한칸 앞에 있는 위치로 이동
        snakes[i].goto(snakes[i-1].pos())

# 각 앞쪽에 있는 위치로 이동 ㅇ ㅇ ㅇ
# 게임의 속도 높이기 위하면 forward(여기) 조절
    snakes[0].forward(20)

# 뱀이 food 에 닿았는지 계산 
# food까지의 거리가 15보다 작으면 먹이 먹은걸로 간주 
    if snakes[0].distance(food) < 15 :
        score_update()
# food를 먹을 때마다 food 자리 변경 
        food.goto(rand_pos())
# 먹을 때마다 꼬리 길어짐 / () 안에 값이 매개변수 -> 늘어나는 꼬리의 위치를 적은 것
        create_snake(snakes[-1].pos())

# snake 머리 [0] 이 벽면 감지
# x, y 좌표 값이 280보다 크거나 -280보다 작으면 벽면에 닿은걸로 간주
    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 \
       or snakes[0].ycor() > 280 or snakes[0].ycor() < -280 :
# game_on 이라는 변수를 False 로 바꿔
        game_on = False
        game_over()

# 꼬리의 길이는 snakes 라는 리스트에 담겨있음
# 머리를 기준으로 1번 인덱스부터 마지막 인덱스까지 닿았는지 확인하기 위해 슬라이
# 머리가 꼬리에 닿았는지 거리가 10 이하이면 닿은걸로 간주 
    for body in snakes[1:]:
        if snakes[0].distance(body) < 10 :
            game_over()
            
    if score >= 5 :
        game_clear()
        game_on = False

screen.exitonclick()

# 경채 게임 시작

print("(게임을 계속하려면 엔터를 눌러주세요.)")
d = input("")
if ( d == "" ):
    print("수뭉이 : 아유 배부르다~~~~~ 잘 먹었네. 그럼 힘내서 학교에 가볼까?")
    print("(괴기하고 이상한 소리가 어디선가 들려온다.)")
    print("(많은 과제로 인해 좀비로 변한 상명대 학생들이 학교를 누비며 다른 학생들을 공격하고 있다.)")
    print("수뭉이 : 헉.....언제 이 사람들을 다 피해서 강의실로 가지???.")
    print('')
    print("[좀비로 가득한 미로 탈출 게임]")
    print("방향키를 사용하여 스뭉이를 이동시켜라")
    print("스뭉이가 학교에 도착하면 게임 클리어!")
    print("좀비에 닿으면 게임 탈락")
    print("(게임을 계속하려면 엔터를 눌러주세요.")
else :
    print("게임을 종료합니다.")

from tkinter import *
from tkinter import messagebox
import time

window = Tk()
window.title("장애물 피해 언덕 오르기")

def player_move(event):
    global x,y
    if event.keysym == "Up" and maze[y-1][x] !=1 :
        canvas. move(player,0,-60)
        y -=1
    elif event.keysym == "Down" and maze[y+1][x] !=1 :
        canvas.move(player,0,60)
        y +=1
    elif event.keysym == "Left" and maze[y][x-1] !=1: 
        canvas.move(player,-60,0)
        x -=1
    elif event.keysym == "Right" and maze[y][x+1] !=1:
        canvas.move(player,60,0)
        x +=1

    if maze[y][x]==2:
        messagebox.showinfo("출석","GAME CLEAR")

    elif maze [y][x]==3:
        messagebox.showinfo("웹엑스 탈락","GAME OVER")

canvas=Canvas(window, width=720, height=720, bg="#FFF8E5")
canvas.pack()

maze = [
    [1,1,1,1,0,1,1,1,1,1,1,1],
    [0,0,0,1,0,1,1,1,0,2,0,1],
    [1,1,0,1,0,1,1,0,0,1,0,1],
    [1,0,0,0,0,0,1,0,1,1,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,1],
    [1,0,1,1,0,0,1,0,1,0,0,1],
    [1,0,1,1,0,1,1,0,1,1,0,1],
    [1,0,1,1,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,1,0,1,0,1,0,0],
    [1,1,0,1,0,1,0,1,0,3,0,1],
    [0,0,0,1,0,0,0,1,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,0,1,1],
]
for y in range(12):
    for x in range(12):
        if maze[y][x]==1:
            canvas.create_rectangle(x*60, y*60, (x+1)*60, (y+1)*60,
                                    fill="#C6D57E", outline="white")

x=1
y=1

img_end=PhotoImage(file="goal_img.png")
end=canvas.create_image(570,90,image=img_end)

play_img=PhotoImage(file="player_img.png")
player=canvas.create_image(90,90,image=play_img)

zombie_img=PhotoImage(file="zombie_img.png")
disturb=canvas.create_image(570,570,image=zombie_img)

canvas.bind_all("<KeyPress>", player_move)

window.mainloop()            

v = input("")
if (v == ""):
    print("수뭉이 : 휴우~~ 학교에 무사히 도착했다.!! 오늘따라 쉽지 않은 등굣길이였어....")
    print("교수님 : 자자 수업 시작하겠습니다...~~ 얼른 자리에 착석해주세요!!")
    print("<축하합니다. 게임에 모두 통과하였습니다.>")


