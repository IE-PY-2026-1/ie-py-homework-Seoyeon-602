# 파일이름 : 스마트 뷰티 컨설턴트
# 작 성 자 : 박 서 연

import random

consultation_count = 0
total_score_sum = 0.0
program_name = '스마트 뷰티 컨설턴트'
user_history = []
ingredients_tags = []

print(f'---{program_name}에 오신 것을 환영합니다!---')

for i in range(1000) :
    print('\n' + '='*35)
    print('(1) 제품 추천')
    print('(2) 오늘의 피부 운세')
    print('(3) 성분 궁합 체크')
    print('(4) 프로그램 종료')
    print('='*35)

    choice = input(f'원하는 메뉴 번호를 입력하세요: ')

    if choice == '1':
        user_name = input('성함을 입력해주세요: ')
        skin_type = input('피부 타입을 입력해주세요 (건성/복합성/지성): ')
        age = int(input('나이를 정수로 입력해 주세요 (예: 23): '))
        skin_score = float(input('현재 피부 점수를 실수로 입력해주세요: '))

        new_data = [user_name, skin_type, age]
        for data in new_data:
            user_history.append(data)

        consultation_count += 1
        total_score_sum += skin_score

        print(f'\n[{user_name}님 분석 결과]')
        if age >= 30:
            if skin_type == '건성' or skin_type == '복합성':
                print('추천: 보습력이 강한 [세라마이드 크림]')
            else:
                print('추천: 가벼운 안티에이징 [레티놀 에센스]')

        elif age >= 10 and age <30:
            print('추천: 수분 밸런스를 돕는 [히알루론산 앰플]')

        else:
            print('추천: 자극 없는 [기초 수분 라인]')
    
    elif choice == '2':
        ingredients = ['비타민C', '레티놀', '판테놀', '히알루론산', '세라마이드']
        fortunes = ['피부 결이 매끄러워지는 날!', '자외선을 조심하세요.', '충분한 수면이 정답!']

        selected_ing = random.choice(ingredients)
        lucky_ment = random.choice(fortunes)
        ingredients_tags.insert(0, selected_ing)

        luck_score = random.randint(1, 100)
        
        print(f'\n 오늘의 피부 운세 점수: {luck_score}점')
        print(f'오늘의 추천 성분: {selected_ing}')
        print(f'운세: {lucky_ment}')

    elif choice == '3':
        ing1 = input('비교할 첫 번째 성분: ')
        ing2 = input('비교할 두 번째 성분: ')

        if (ing1 == '레티놀' and ing2 == '비타민C') or (ing1 == '비타민C' and ing2 == '레티놀'):
            print('주의: 두 성분은 동시 사용 시 자극적일 수 있습니다.')
        elif not (ing1 == '레티놀') and ing2 == '히알루론산':
            print('추천: 수분 공급에 최적화 된 조합입니다.')
        else:
            print('무난한 조합입니다.')

    elif choice == '4':
        exit_ment = ['내일은 오늘보다 더 빛나는 피부가 될 거예요!', '오늘 관리는 내일의 꿀피부!', '잠은 피부의 보약입니다! 푹 자고 맑은 피부로 만나요.']
        print(f'\n{random.choice(exit_ment)}')
        print('이용해 주셔서 감사합니다!')

        print('\n--- 오늘 상담 데이터 요약 ---')
        if len(user_history) > 0:
            for i in range(0, len(user_history), 3):
                print(f'- 고객 정보: {user_history[i]}님 ({user_history[i+1]}), {user_history[i+2]}세')

        if consultation_count > 0:
            avg = int(total_score_sum / consultation_count)
            print(f'최종 평균 피부 컨디션: {avg}점')
        break

    else:
        print('잘못된 번호입니다. 다시 선택해주세요.')
        continue