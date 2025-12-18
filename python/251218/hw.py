# 과제)
# 할인 후 금액에 → 부가세(0.19) 까지 더한 최종 제품판매가 계산해라

VAT = 0.19  #부가세율

price_before = float(input("상품가격: "))   #제품가격 입력
dsct = int(input("discount %: "))   #할인율 입력

price_discounted = price_before * (1 - dsct / 100)   #할인된 가격 계산
price_final = price_discounted * (1 + VAT)  #부가세 포함 최종 가격 계산

print("최종 판매가: ", price_final)     #최종 판매가격 출력