# 파일이름 : 스마트 뷰티 컨설턴트
# 작 성 자 : 박 서 연

import random
from datetime import datetime, timedelta, timezone
from itertools import combinations

# [1. 데이터베이스]
cosmetics_db = [
    {"이름": "어성초 80 진정 토너", "카테고리": "스킨", "타입": "지성", "고민": ["트러블", "진정"], "연령대": [10, 20], "성분": {"어성초": 80}, "가격": 18000, "별점": 4.8, "후기": ["여드름이 쏙 들어갔어요", "붉은기 진정에 최고예요"]},
    {"이름": "고보습 히알루론 토너", "카테고리": "스킨", "타입": "건성", "고민": ["수분", "건조"], "연령대": [20, 30, 40], "성분": {"히알루론산": 5}, "가격": 21000, "별점": 4.6, "후기": ["속건조 잡는데 최고"]},
    {"이름": "세라마이드 장벽 토너", "카테고리": "스킨", "타입": "복합성", "고민": ["장벽케어", "건조"], "연령대": [20, 30], "성분": {"세라마이드": 1}, "가격": 19000, "별점": 4.5, "후기": ["피부가 튼튼해지는 느낌"]},
    {"이름": "레티놀 탄력 앰플", "카테고리": "세럼", "타입": "복합성", "고민": ["탄력", "주름", "모공"], "연령대": [30, 40, 50], "성분": {"레티놀": 0.1}, "가격": 38000, "별점": 4.4, "후기": ["잔주름이 옅어져요"]},
    {"이름": "비타민C 맑음 세럼", "카테고리": "세럼", "타입": "건성", "고민": ["미백", "잡티"], "연령대": [20, 30], "성분": {"비타민C": 12}, "가격": 25000, "별점": 4.5, "후기": ["잡티가 연해졌어요"]},
    {"이름": "시카 릴리프 앰플", "카테고리": "세럼", "타입": "민감성", "고민": ["진정", "트러블"], "연령대": [10, 20, 30], "성분": {"병풀추출물": 50}, "가격": 28000, "별점": 4.9, "후기": ["붉은기 진정에 최고"]},
    {"이름": "펩타이드 리프팅 세럼", "카테고리": "세럼", "타입": "건성", "고민": ["주름", "탄력"], "연령대": [40, 50, 60], "성분": {"펩타이드": 5}, "가격": 45000, "별점": 4.8, "후기": ["피부가 팽팽해져요"]},
    {"이름": "세라마이드 집중 크림", "카테고리": "크림", "타입": "건성", "고민": ["장벽케어", "건조"], "연령대": [20, 30, 40, 50], "성분": {"세라마이드": 5}, "가격": 32000, "별점": 4.9, "후기": ["피부 장벽 탄탄해짐"]},
    {"이름": "수분 가득 젤크림", "카테고리": "크림", "타입": "지성", "고민": ["수분", "건조"], "연령대": [10, 20, 30], "성분": {"히알루론산": 2}, "가격": 24000, "별점": 4.7, "후기": ["산뜻한데 촉촉해요"]},
    {"이름": "아이 앤 페이스 주름크림", "카테고리": "크림", "타입": "복합성", "고민": ["주름", "탄력"], "연령대": [30, 40, 50, 60], "성분": {"콜라겐": 10}, "가격": 55000, "별점": 4.8, "후기": ["눈가 주름에 효과봄"]},
    {"이름": "판테놀 시카 밤", "카테고리": "크림", "타입": "민감성", "고민": ["진정", "장벽케어"], "연령대": [10, 20, 30], "성분": {"판테놀": 5}, "가격": 27000, "별점": 4.7, "후기": ["예민한 날 필수템"]},
    {"이름": "쌀겨 광채 토너", "카테고리": "스킨", "타입": "건성", "고민": ["미백", "피부결"], "연령대": [20, 30, 40], "성분": {"쌀추출물": 70}, "가격": 23000, "별점": 4.3, "후기": ["결이 매끈해져요"]},
    {"이름": "티트리 조절 토너", "카테고리": "스킨", "타입": "지성", "고민": ["트러블", "모공"], "연령대": [10, 20], "성분": {"티트리": 5}, "가격": 16000, "별점": 4.2, "후기": ["기름기 싹 잡아줌"]},
    {"이름": "무기자차 진정 선크림", "카테고리": "크림", "타입": "민감성", "고민": ["진정", "장벽케어"], "연령대": [10, 20, 30, 40, 50], "성분": {"징크": 10}, "가격": 19000, "별점": 4.5, "후기": ["자극 없이 순해요"]},
    {"이름": "블랙헤드 클리어 토너", "카테고리": "스킨", "타입": "지성", "고민": ["모공", "트러블"], "연령대": [10, 20, 30], "성분": {"BHA": 0.5}, "가격": 20000, "별점": 4.4, "후기": ["코가 깨끗해져요"]}
]

# 데이터 초기화
for p in cosmetics_db:
    if "별점" in p and "별점목록" not in p:
        p["별점목록"] = [p.pop("별점")]

# [2. 유틸리티 함수]
def calculate_average_rating(rating_list):
    if not rating_list: return 0.0
    return round(sum(rating_list) / len(rating_list), 1)

def get_kst_now():
    return datetime.now(timezone.utc) + timedelta(hours=9)

def show_detailed_reviews(product_list):
    if not product_list: return
    try:
        choice = input("\n🔍 상세 후기를 보려면 제품 번호를 입력하세요 (없으면 0): ")
        if choice == '0' or not choice: return
        idx = int(choice) - 1
        if 0 <= idx < len(product_list):
            target = product_list[idx]
            avg = calculate_average_rating(target['별점목록'])
            print(f"\n✨ [{target['이름']}] 전체 후기 목록 (⭐ {avg}) ✨")
            for i, rev in enumerate(target['후기'], 1): print(f"  {i}. {rev}")
        else: print("잘못된 번호입니다.")
    except ValueError: print("숫자만 입력 가능합니다.")

# [3. 주요 기능 함수]
def show_welcome_screen():
    kst = get_kst_now()
    print("\n" + "="*55)
    print("✨ 스마트 뷰티 컨설턴트 ✨")
    print(f"⏰ 현재 시간: {kst.strftime('%Y-%m-%d %H:%M:%S')} (KST)")
    print("="*55)
    greet = "🌅 아침" if kst.hour < 12 else "☀️ 오후" if kst.hour < 18 else "🌙 저녁"
    fortunes = ["피부 장벽 튼튼!", "수분 충전 필요!", "비타민 같은 하루!", "결이 고운 날!", "물 많이 마시기!"]
    lucky_ingre = ["히알루론산", "세라마이드", "비타민C", "티트리", "판테놀", "시카", "레티놀"]
    print(f"{greet} 인사: 오늘 당신의 피부 운세는 '{random.choice(fortunes)}'")
    print(f"🌟 오늘의 럭키 성분: [{random.choice(lucky_ingre)}]")
    print("="*55)

def search_products():
    print("\n[1. 맞춤 제품 추천]")
    age_in = input("연령대(예: 25) 혹은 엔터: ")
    all_con = sorted(list(set(c for p in cosmetics_db for c in p['고민'])))
    print("\n피부 고민 선택:")
    for i, con in enumerate(all_con, 1): print(f"{i}.{con}", end="  ")
    u_con = input("\n\n번호 입력(쉼표 구분) 혹은 엔터: ")
    selected = [all_con[int(c)-1] for c in u_con.split(",") if c.strip().isdigit() and 0 < int(c) <= len(all_con)]
    
    results = cosmetics_db
    if age_in: results = [p for p in results if (int(age_in)//10)*10 in p['연령대']]
    if selected: results = [p for p in results if any(c in p['고민'] for c in selected)]
    
    print("\n" + "="*55)
    if not results: print("일치하는 제품이 없습니다.")
    else:
        for i, p in enumerate(results, 1):
            avg = calculate_average_rating(p.get("별점목록", []))
            print(f"{i}. [{p['카테고리']}] {p['이름']} | {p['가격']}원 | ⭐ {avg}")
            print(f"   💬 최신 후기: {p['후기'][-1] if p['후기'] else '없음'}")
        show_detailed_reviews(results)

def create_routine():
    print("\n[2. 나만의 스마트 루틴 생성]")
    u_type = input("피부 타입(건성/지성/복합성/민감성): ")
    u_budget = input("최대 예산(원): ")
    if not u_budget.isdigit(): return
    
    res = []
    skins = [p for p in cosmetics_db if p['카테고리']=="스킨" and p['타입']==u_type]
    serums = [p for p in cosmetics_db if p['카테고리']=="세럼" and p['타입']==u_type]
    creams = [p for p in cosmetics_db if p['카테고리']=="크림" and p['타입']==u_type]
    
    for s in skins:
        for se in serums:
            for c in creams:
                total = s['가격'] + se['가격'] + c['가격']
                if total <= int(u_budget):
                    score = (calculate_average_rating(s['별점목록']) + calculate_average_rating(se['별점목록']) + calculate_average_rating(c['별점목록'])) / 3
                    res.append({"items": [s, se, c], "total": total, "rating": score})
    
    if res:
        best = max(res, key=lambda x: x['rating'])
        print(f"\n✅ 추천 루틴 (총 {best['total']}원):")
        for i, item in enumerate(best['items'], 1): print(f"{i}. {item['이름']} ({item['가격']}원)")
        show_detailed_reviews(best['items'])
    else: print("예산 내 루틴이 없습니다.")

def check_chemistry():
    print("\n[3. 성분 궁합 체크 (q: 나가기)]")
    ing_raw = input("분석할 성분들(쉼표 구분, 예: 비타민C, 레티놀): ")
    if ing_raw.lower() == 'q': return
    ing_input = [i.strip() for i in ing_raw.replace(" ", "").split(",") if i.strip()]
    synergy = {
        ("비타민C", "레티놀"): "⚠️ 자극 주의! 아침(비타민), 저녁(레티놀)으로 나누어 쓰세요.",
        ("비타민C", "AHA"): "⚠️ 각질 제거 중복! 피부막이 얇아질 수 있어요.",
        ("비타민C", "비타민E"): "✨ 항산화 시너지! 비타민 E가 비타민 C의 흡수를 돕습니다.",
        ("히알루론산", "판테놀"): "✨ 보습 폭탄! 수분을 가두는 환상의 짝꿍입니다.",
        ("레티놀", "펩타이드"): "✨ 탄력 끝판왕! 탄력을 채워주는 찰떡궁합입니다."
    }
    matched = False
    for (s1, s2), msg in synergy.items():
        if s1 in ing_input and s2 in ing_input:
            print(f"▶ {s1} & {s2}: {msg}"); matched = True
    if not matched: print("✅ 특이사항이 있는 조합은 발견되지 않았습니다.")

def coupon_calculator():
    print("\n" + "="*50)
    print("💰 [최저가 조합 시뮬레이터]")
    print("="*50)
    
    # 1. 상품 가격 입력
    items = []
    i = 1
    while True:
        price = input(f"상품{i}의 가격을 입력하시오.(없으면 엔터): ").strip()
        if not price: break
        if price.isdigit():
            items.append({"name": f"상품{i}", "price": int(price)})
            i += 1
    
    if not items: return

    # 2. 쿠폰 정보 입력
    coupons = []
    while True:
        print(f"\n--- {len(coupons)+1}번째 쿠폰 설정 ---")
        is_overlap = input("중복 사용 가능한 쿠폰 입니까? (Y/N): ").upper() == 'Y'
        min_buy = int(input("쿠폰의 최소 구매 금액은 얼마입니까?: ") or 0)
        unit = input("쿠폰이 % 단위인가요? 금액 단위인가요? (%/금액): ").strip()
        val = float(input("쿠폰의 할인율(%) 또는 할인 금액을 입력해주세요: ") or 0)
        limit = int(input("쿠폰의 할인 가능한 금액 한도는 얼마입니까? (없으면 0): ") or 0)
        
        coupons.append({
            "is_overlap": is_overlap,
            "min_buy": min_buy,
            "unit": unit,
            "val": val,
            "limit": limit,
            "used": False
        })
        if input("\n추가 쿠폰이 있나요? (Y/N): ").upper() != 'Y': break

    # 3. 최적 조합 계산 (Greedy + Combination)
    remaining_items = items[:]
    results = []
    
    # 할인 효율이 좋은 쿠폰 순으로 정렬 (금액 단위는 그대로, %는 대략적인 가치로 계산)
    coupons.sort(key=lambda x: x['val'], reverse=True)

    while remaining_items and any(not c['used'] for c in coupons):
        best_combo = None
        best_coupon = None
        best_discount = -1

        for coupon in [c for c in coupons if not c['used']]:
            # 가능한 모든 상품 조합 시도
            for r in range(1, len(remaining_items) + 1):
                for combo in combinations(remaining_items, r):
                    current_sum = sum(it['price'] for it in combo)
                    
                    if current_sum >= coupon['min_buy']:
                        # 할인액 계산
                        if coupon['unit'] == '%':
                            discount = int(current_sum * (coupon['val'] / 100))
                            if coupon['limit'] > 0:
                                discount = min(discount, coupon['limit'])
                        else:
                            discount = int(coupon['val'])
                        
                        # 가장 할인이 큰 조합 선택
                        if discount > best_discount:
                            best_discount = discount
                            best_combo = combo
                            best_coupon = coupon
        
        if best_combo:
            results.append({
                "items": best_combo,
                "orig_sum": sum(it['price'] for it in best_combo),
                "discount": best_discount
            })
            best_coupon['used'] = True
            for it in best_combo:
                remaining_items.remove(it)
        else:
            break

    # 4. 결과 출력
    print("\n" + "🏆 최적의 구매 방법 🏆")
    total_orig = sum(it['price'] for it in items)
    total_disc = 0

    for res in results:
        names = " + ".join([it['name'] for it in res['items']])
        final_price = res['orig_sum'] - res['discount']
        print(f"{names} = {final_price}원 (원래 {res['orig_sum']}원, -{res['discount']}원 할인됨)")
        total_disc += res['discount']

    if remaining_items:
        names = " + ".join([it['name'] for it in remaining_items])
        rem_sum = sum(it['price'] for it in remaining_items)
        print(f"{names} = {rem_sum}원 (쿠폰 적용 불가)")

    print("-" * 50)
    print(f"할인 됐을 때 총 상품 가격: {total_orig - total_disc}원")
    print(f"기존 금액에서 총 {total_disc}원 할인되었습니다.")
    print("\n현명한 소비되세요! ✨")

def manage_data():
    print("\n[6. 후기 관리 및 신규 제품 등록]")
    search_name = input("후기를 작성할 제품명을 입력하세요: ").strip()
    if not search_name: return

    # 1. 검색 로직 (수정: matches 결과를 바탕으로 target_product를 실제로 할당함)
    matches = [p for p in cosmetics_db if search_name.replace(" ", "") in p['이름'].replace(" ", "")]
    target_product = None
    
    if matches:
        if len(matches) == 1:
            ans = input(f"👉 '{matches[0]['이름']}' 제품이 맞습니까? (Y/N): ").upper()
            if ans == 'Y': target_product = matches[0]
        else:
            print(f"\n유사한 제품이 {len(matches)}개 검색되었습니다:")
            for i, m in enumerate(matches, 1): print(f"{i}. {m['이름']}")
            idx = input("번호 선택 (취소: 엔터): ")
            if idx.isdigit() and 1 <= int(idx) <= len(matches):
                target_product = matches[int(idx)-1]

    # 2. 제품이 없는 경우 신규 등록 프로세스
    if not target_product:
        print(f"\n❌ '{search_name}'은(는) 등록되어 있지 않습니다.")
        if input("💡 신규 추가하시겠습니까? (예/아니오): ") in ['예', 'y', 'Y']:
            # [수정] 신규 등록에 필요한 변수들을 입력받도록 로직 추가 (기존 코드에서 빠진 부분)
            new_name = input("1. 제품 이름: ").strip() or search_name
            new_cat = input("2. 카테고리 (스킨/세럼/크림): ").strip()
            new_type = input("3. 피부 타입: ").strip()
            new_issue = input("4. 고민 (쉼표 구분): ").split(",")
            new_ages = [int(a.strip()) for a in input("5. 연령대 (쉼표 구분): ").split(",") if a.strip().isdigit()]
            new_ingre = {input("6. 주성분 이름: "): 0.0} # 성분 입력 간소화
            new_price = int(input("7. 가격(숫자): ") or 0)
            
            try:
                first_rating = float(input("10. 제품 별점을 입력해주세요 (1.0 ~ 5.0): "))
            except: first_rating = 5.0
            
            first_review = input(f"11. [{new_name}] 첫 후기를 작성해주세요: ").strip()
            
            new_product = {
                "이름": new_name, "카테고리": new_cat, "타입": new_type,
                "고민": new_issue, "연령대": new_ages, "성분": new_ingre, "가격": new_price,
                "별점목록": [first_rating],
                "후기": [first_review] if first_review else []
            }
            cosmetics_db.append(new_product)
            print(f"✅ '{new_name}' 제품과 첫 별점이 등록되었습니다!")
            return
        else:
            return # '아니오' 선택 시 메뉴로 복귀

    # 3. 기존 제품인 경우 후기와 별점 추가
    if target_product:
        try:
            new_rating = float(input(f"[{target_product['이름']}] 제품 별점 (1.0 ~ 5.0): "))
            if not (1.0 <= new_rating <= 5.0): raise ValueError
        except:
            print("❌ 올바른 별점을 입력해주세요. 저장되지 않았습니다.")
            return

        new_review = input("제품 후기를 작성하세요: ").strip()
        
        if "별점목록" not in target_product:
            target_product["별점목록"] = [target_product.get("별점", 5.0)]
        
        target_product["별점목록"].append(new_rating)
        if new_review:
            target_product["후기"].append(new_review)
            
        avg = calculate_average_rating(target_product["별점목록"])
        print(f"✅ 후기가 등록되었습니다! (현재 평균 별점: ⭐ {avg})")

# [5. 메인 실행 루프]
def main():
    show_welcome_screen()
    while True:
        print("\n" + "—"*20 + " MAIN MENU " + "—"*20)
        print("(1) 맞춤 제품 추천  (2) 스킨케어 루틴 생성")
        print("(3) 성분 궁합 알아보기 (4) 오늘의 운세 다시보기")
        print("(5) 최저가 계산기 (6) 후기/제품 관리  (Q) 종료")
        
        menu = input("메뉴 선택: ").upper()
        if menu == '1': search_products()
        elif menu == '2': create_routine()
        elif menu == '3': check_chemistry()
        elif menu == '4': show_welcome_screen()
        elif menu == '5': coupon_calculator()
        elif menu == '6': manage_data()
        elif menu == 'Q': break
        
        if input("\n메뉴로 돌아갈까요? (엔터: 예 / Q: 종료): ").upper() == 'Q': break
    print("\n오늘보다 내일 더 예쁜 피부 되세요! 👋")

if __name__ == "__main__":
    main()
