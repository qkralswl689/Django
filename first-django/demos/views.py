import imp
import re
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def calculator(request):
    # return HttpResponse('계산기 기능 구현 시작2')

    # 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    # 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0
    return render(request, 'calculator.html', {'result': result})


def getRandomNumber():
    number = random.randint(1, 45)
    return number


def lotto(request):
    """
    num = int(request.GET.get('num'))
    count = 0
    lotto_num = []
    #result = random.sample(range(1, 46), 6)
    while True:
        if count > 6:
            break
        random_number = getRandomNumber()
        if random_number not in lotto_num:
            lotto_num.append(random_number)
            count = count + 1
    """

    return render(request, 'lotto.html')


def result(request):

    lotto_num = []
    answer = list()
    num = request.GET.get('num', 1)
    count = 0
    # 로또번호생성
    while True:
        if count > 6:
            break
        random_number = getRandomNumber()
        if random_number not in lotto_num:
            lotto_num.append(random_number)
            count = count + 1

    # 생성된 로또번호를 입력받은 수만큼 출력해줄 리스트에 넣는다
    for i in range(int(num)):
        answer.append(lotto_num)

    return render(request, 'result.html', {'result': answer, 'num': num})
