#My Magic 8 Ball

import random

a1="자, 해보세요."
a2="알겠어요. 고마워요."
a3="애초에 기대를 하니까 배신을 당하는 거예요."
a4="잘 들어보세요."
a5="무슨 말씀을 하시는 건지 모르겠어요."
a6="그래도 그건 아닌 것 같아요."
a7="제 생각엔 당신이 옳은 일을 하신 것 같네요. 잘하셨어요."
a8="그렇게 말씀하시면 안 되죠."

print("My Magic 8 Ball에 오신 것을 환영합니다.")

question=input("조언을 구하려면 질문을 입력하고 엔터 키를 누르세요.")

choice=random.randint(1,8)
if choice==1:
    answer=a1
elif choice==2:
    answer=a2
elif choice==3:
    answer=a3
elif choice==4:
elif choice==a5:
    answer=a5
elif choice==6:
    answer=a6
elif choice==7:
    answer=a7
elif choice==8:
    answer=a8

print(answer)

input("\n\n마치려면 엔터 키를 누르세요.")
