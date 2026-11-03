"""20 explicitly labelled arithmetic families, 47 deterministic conditions each.
All percentages, densities and energy factors are supplied assumptions, not legal
limits, measured ingredient specifications or claims about official exam weights.
"""
from decimal import Decimal, ROUND_HALF_UP

D = lambda n: Decimal(str(n))
def fmt(n):
    return format(D(n).normalize(), 'f')

def numeric_questions():
    out = []
    for kind in range(1, 21):
        for i in range(47):
            # Distinct masses per condition, bounded to classroom/bakery-scale values.
            mass = 500 + i * 25
            pct = 10 + (i % 9) * 5
            if kind == 1:
                topic, unit, v = '제조·배합 백분율', 'g', [mass, pct]
                question = f'밀가루 {mass} g을 100%로 하는 배합에서 설탕의 베이커스 퍼센트가 {pct}%이다. 설탕은 몇 g인가?'
                result = D(mass) * D(pct) / 100
                formula = f'설탕 질량 = 밀가루 질량 × 설탕 비율/100 = {mass} × {pct}/100'
            elif kind == 2:
                topic, unit, v = '제조·배합 확대', 'g', [mass, 1000, 1250 + i * 50]
                a,b,c=v
                question=f'기준 배합은 밀가루 {b} g에 버터 {a} g이다. 모든 재료 비율을 유지하여 밀가루를 {c} g으로 바꿀 때 버터는 몇 g인가?'
                result=D(a)*D(c)/D(b)
                formula=f'확대 배율 = {c}/{b}, 버터 질량 = {a} × {c}/{b}'
            elif kind == 3:
                topic, unit, v = '제조·총 배합량', 'g', [mass, 60, 50, 40]
                a,b,c,d=v
                question=f'밀가루 {a} g을 100%로 하고 설탕 {b}%, 달걀 {c}%, 유지 {d}%만 넣는다. 손실이 없을 때 총 반죽 질량은 몇 g인가?'
                result=D(a)*(100+D(b)+D(c)+D(d))/100
                formula=f'총 비율 = 100+{b}+{c}+{d} = 250%, 총 질량 = {a} × 250/100'
            elif kind == 4:
                topic, unit, v = '제조·굽기 손실량', 'g', [mass, 8 + i % 13]
                a,b=v
                question=f'굽기 전 반죽 {a} g이 굽는 동안 초기 질량의 {b}%를 잃었다. 굽기 후 질량은 몇 g인가?'
                result=D(a)*(100-D(b))/100
                formula=f'남은 비율 = 100−{b}%, 굽기 후 질량 = {a} × (100−{b})/100'
            elif kind == 5:
                topic, unit, v = '제조·손실률', '%', [1000+i*40, 80+i*3]
                a,b=v
                question=f'굽기 전 질량이 {a} g이고 굽는 중 감소한 질량이 {b} g이다. 초기 질량 기준 굽기 손실률은 몇 %인가?'
                result=D(b)*100/D(a)
                formula=f'손실률 = 감소 질량/초기 질량 × 100 = {b}/{a} × 100'
            elif kind == 6:
                topic, unit, v = '제조·분할 개수', '개', [mass, 25+(i%6)*5]
                a,b=v
                question=f'반죽 {a} g을 한 개당 {b} g씩 분할한다. 손실은 없고 남은 반죽은 별도 보관할 때, 정량으로 만들 수 있는 최대 개수는?'
                result=D(a)//D(b)
                formula=f'정량 개수 = {a}/{b}의 정수 부분. 나머지로는 정량 한 개를 만들 수 없으므로 버림'
            elif kind == 7:
                topic, unit, v = '제조·개당 반죽량', 'g', [800+i*40, 16+i%5]
                a,b=v
                question=f'반죽 {a} g을 손실 없이 {b}개로 똑같이 나눈다. 한 개의 반죽 질량은 몇 g인가?'
                result=D(a)/D(b)
                formula=f'개당 질량 = 총 반죽 질량/개수 = {a}/{b}'
            elif kind == 8:
                topic, unit, v = '재료·시럽 농도', '%', [200+i*10, 300+i*5]
                a,b=v
                question=f'설탕 {a} g을 물 {b} g에 완전히 녹였다. 증발이 없을 때 용액 전체 질량에 대한 설탕의 질량 백분율은 몇 %인가?'
                result=D(a)*100/(D(a)+D(b))
                formula=f'전체 용액 질량 = {a}+{b} g, 설탕 질량 백분율 = {a}/({a}+{b}) × 100'
            elif kind == 9:
                topic, unit, v = '재료·시럽 희석', 'g', [mass, 60, 30]
                a,b,c=v
                question=f'설탕 {b} 질량%인 시럽 {a} g에 물만 넣어 {c} 질량%로 만든다. 증발이나 손실이 없을 때 추가할 물은 몇 g인가?'
                result=D(a)*D(b)/D(c)-D(a)
                formula=f'설탕 질량 보존: 최종 질량 = {a} × {b}/{c}, 추가 물 = 최종 질량−{a}'
            elif kind == 10:
                topic, unit, v = '재료·지방 함량 혼합', '%', [200+i*10, 100+i*5, 35, 4]
                a,b,c,d=v
                question=f'지방 {c} 질량%의 크림 {a} g과 지방 {d} 질량%의 우유 {b} g을 섞는다. 손실 없이 균일하게 섞었을 때 혼합물의 지방 질량%는?'
                result=(D(a)*D(c)+D(b)*D(d))/(D(a)+D(b))
                formula=f'지방 질량 = ({a} × {c}+{b} × {d})/100 g, 혼합 지방% = ({a} × {c}+{b} × {d})/({a}+{b})'
            elif kind == 11:
                topic, unit, v = '재료·단백질 함량 혼합', '%', [300+i*10, 200+i*5, 8, 12]
                a,b,c,d=v
                question=f'단백질 {c} 질량%인 밀가루 {a} g과 {d} 질량%인 밀가루 {b} g을 섞는다. 손실이 없을 때 혼합 가루의 단백질 질량%는?'
                result=(D(a)*D(c)+D(b)*D(d))/(D(a)+D(b))
                formula=f'단백질 총량을 전체 가루 질량으로 나눈다. 단백질% = ({a} × {c}+{b} × {d})/({a}+{b})'
            elif kind == 12:
                topic, unit, v = '재료·원료 수분량', 'g', [mass, 20+i%16]
                a,b=v
                question=f'원료 {a} g의 수분 함량을 {b} 질량%로 가정한다. 이 원료에 들어 있는 물의 질량은 몇 g인가?'
                result=D(a)*D(b)/100
                formula=f'물 질량 = 원료 질량 × 수분 비율/100 = {a} × {b}/100'
            elif kind == 13:
                topic, unit, v = '재료·고형분량', 'g', [mass, 70+i%11]
                a,b=v
                question=f'달걀 혼합물 {a} g의 수분을 {b} 질량%로 가정한다. 물 이외의 고형분 질량은 몇 g인가?'
                result=D(a)*(100-D(b))/100
                formula=f'고형분 비율 = 100−수분%, 고형분 질량 = {a} × (100−{b})/100'
            elif kind == 14:
                topic, unit, v = '재료·주어진 계수의 열량', 'kcal', [30+i, 4+i%7, 5+i%8]
                a,b,c=v
                question=f'제품 1개에 탄수화물 {a} g, 단백질 {b} g, 지방 {c} g만 있다. 각각 4, 4, 9 kcal/g으로 계산할 때 총 열량은 몇 kcal인가?'
                result=D(a)*4+D(b)*4+D(c)*9
                formula=f'열량 = 탄수화물×4 + 단백질×4 + 지방×9 = {a}×4+{b}×4+{c}×9'
            elif kind == 15:
                topic, unit, v = '제조·원료 사용 원가', '원', [2000+i*100, 150+i*5]
                a,b=v
                question=f'원료 1 kg의 가격이 {a}원이다. 포장·인건비를 제외하고 원료 {b} g의 사용 원가만 구하면 몇 원인가?'
                result=D(a)*D(b)/1000
                formula=f'1 kg = 1,000 g, 사용 원가 = kg당 가격 × 사용 g/1,000 = {a} × {b}/1,000'
            elif kind == 16:
                topic, unit, v = '제조·개당 재료 원가', '원', [10000+i*250, 20+i%11]
                a,b=v
                question=f'재료 원가 합계 {a}원으로 판매 가능한 과자 {b}개를 만들었다. 다른 비용을 제외한 개당 평균 재료 원가는 몇 원인가?'
                result=D(a)/D(b)
                formula=f'개당 평균 재료 원가 = 총 재료 원가/완제품 개수 = {a}/{b}'
            elif kind == 17:
                topic, unit, v = '위생·이력 재고 계산', 'g', [3000+i*50, 500+i*10, 200+i*5]
                a,b,c=v
                question=f'원료 재고 {a} g에서 오전 {b} g, 오후 {c} g을 사용했다. 입고·폐기·계량 손실이 없을 때 장부상 남은 재고는 몇 g인가?'
                result=D(a)-D(b)-D(c)
                formula=f'남은 재고 = 시작 재고−오전 사용량−오후 사용량 = {a}−{b}−{c}'
            elif kind == 18:
                topic, unit, v = '제조·팬 면적 배합 조정', 'g', [mass, 20, 22+i%9]
                a,b,c=v
                question=f'지름 {b} cm인 원형 팬에 반죽 {a} g을 쓴다. 같은 두께로 지름 {c} cm인 원형 팬을 채울 때 필요한 반죽은 몇 g인가? 밀도와 굽기 전 두께는 같다.'
                result=D(a)*D(c)**2/D(b)**2
                formula=f'두께와 밀도가 같으면 질량은 면적에 비례한다. 원 면적의 공통 상수는 약분되어 필요량 = {a} × {c}²/{b}²'
            elif kind == 19:
                topic, unit, v = '제조·반죽 비중', '', [60+i, 100]
                a,b=v
                question=f'용기 무게를 뺀 같은 부피의 반죽 질량은 {a} g, 물 질량은 {b} g이다. 물을 기준으로 한 반죽 비중은?'
                result=D(a)/D(b)
                formula=f'같은 부피의 질량비 = 반죽 질량/물 질량 = {a}/{b}. 비중은 무차원 값'
            else:
                topic, unit, v = '제조·생산 회차 올림', '회', [200+i*7, 24+i%9]
                a,b=v
                question=f'한 회에 최대 {b}개를 구울 수 있는 오븐으로 과자 {a}개를 굽는다. 마지막 회는 일부만 채워도 될 때 필요한 최소 굽기 회차는?'
                result=(D(a)/D(b)).to_integral_value(rounding='ROUND_CEILING')
                formula=f'필요 회차 = {a}/{b}를 올림. 남은 제품이 있으면 추가 한 회가 필요함'
            precision=0 if kind in (6,20) else 2
            result=result.quantize(D(1).scaleb(-precision),rounding=ROUND_HALF_UP)
            # Distinct numeric distractors in the same unit, not equivalent strings.
            step=max(D(1) if precision==0 else D('.01'),abs(result)*D('0.08')).quantize(D(1) if precision==0 else D('.01'),rounding=ROUND_HALF_UP)
            offsets=((1,2,3),(-1,1,2),(-2,-1,1),(-3,-2,-1))[i%4]
            vals=[result,*[result+step*k for k in offsets]]
            shift=(kind+i)%4
            vals=vals[shift:]+vals[:shift]
            choices=[f'{fmt(n)}{(" "+unit) if unit else ""}' for n in vals]
            answer=vals.index(result)+1
            rounding='整数 개수 조건을 적용한다.' if precision==0 else '최종 결과는 소수 셋째 자리에서 반올림해 소수 둘째 자리까지 구한다.'
            question+=' '+rounding.replace('整数','정수')
            explanation=f'{formula}. 따라서 정답은 {fmt(result)} {unit}이다. '+rounding.replace('整数','정수')+' 제시한 함량과 손실 조건은 이 문제의 계산 가정이며 실제 원료 규격이나 법정 기준이 아니다.'
            out.append(dict(id=f'CONF-N{kind:02}-{i+1:03}',subject='과자류 재료, 제조 및 위생관리',topic=topic,question=question,choices=choices,answer=answer,explanation=explanation,difficulty='중',year=None,session=None,type='original',sourceUrl='https://github.com/YunSangYeong/Craftsman-Confectionery-Making-CBT/blob/feat/confectionery-cbt/scripts/numeric_questions.py',verificationStatus='reviewed',reviewNote='자체 제작 계산 조건 변형. 내부 유형별 문장·공식 검토 및 Python Decimal 생성/별도 TypeScript 공식 검증. 외부 전문가 검수·공식 출제기준 대조 미실시. 출처 URL은 작성 위치이며 외부 정답 증빙이 아님.',version='main',rights='자체 제작 학습 문항, CC BY 4.0. 외부 기출 원문 미사용.',family=f'CONF-N{kind:02}',calculation=dict(kind=f'confectionery{kind:02}',values=v,result=float(result),unit=unit,precision=precision)))
    assert len(out)==940
    return out
