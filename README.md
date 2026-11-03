# Craftsman-Confectionery-Making-CBT

제과기능사 필기 CBT — 비공식 학습용 React/TypeScript 정적 앱.

## 실행과 검사

Node 24.19.0, `npm ci`, `npm run dev`.
`npm test`로 모델 검사, `npm run build`로 타입 검사와 프로덕션 빌드.
`npx playwright install --with-deps chromium` 후 `npm run test:e2e`로 PC/모바일 검사.
시스템 Chromium을 사용하려면 `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/usr/bin/chromium`을 설정한다.
이 클라우드는 격리된 작업 환경이므로 현재 체크아웃을 사용하며 별도 worktree는 만들지 않는다.

## 구현

실전·랜덤, 두 모드의 Space 다음 이동, 절대 종료 시각과 자동 제출, 답안 변경,
결과·해설·시험 오답 재학습, 오답노트·북마크·통계, JSON/CSV 가져오기와 중복 제거,
근거 입력 후 로컬 검수 승인, 백업·초기화를 제공한다. 학습 기준 선택 메뉴는 없다.
작은 화면의 메뉴는 독립적으로 세로 스크롤된다.
기록은 `Craftsman-Confectionery-Making-CBT:v1` localStorage에 저장한다.
최근 응답 5,000건·시험 30회 보관. 백업 내보내기를 제공하며 백업 복원 UI는 없다.

## 시험 규칙 확인 상태

**공식 확인 미완료.** Q-Net 제과기능사 종목 정보 후보 URL:
https://www.q-net.or.kr/crf005.do?id=crf00503&jmCd=7892

2026-11-03 공식 자료 요청은 CONNECT HTTP 403 Forbidden으로 차단되었다.
자료 본문·현행 출제기준·문항 이용 조건을 읽지 못했다.
앱 설정은 학습용 가정으로 과자류 재료, 제조 및 위생관리 / 60문항 / 60분 /
객관식 4지선다 / 문항 동일 배점(정답수 ÷ 60 × 100) / 60점 이상 / 과락 없음이다.
미응답은 오답, 점수 표시 소수 첫째 자리 반올림과 합격 판정 원값을 구분한다.
공식 영역별 비율은 확인하지 않았으며 전체 검수 은행에서 무작위 추출한다.
설정의 확인 상태는 `src/profile.ts`와 문제은행 관리 화면에 기록했다.
공식 시험 재현·최신 공식 규칙 준수 완료를 주장하지 않는다.

## 실제 문제은행과 이용 조건

기본 JSON 등록: **60문항**, 내부 문장·보기 검토 완료 60, 검증 대기 0.
목표 1,000 대비 **940문항 부족 — 표준 수량 미충족**.
과목은 위 통합 과목 1개, 학습 단원은 재료 20 / 제조 20 / 위생 20.
원문 기출 0 / 복원 0 / 자체 제작 60 / 숫자 조건 변형 0 / 계산형 0.
서로 다른 개념 문항 60개이며 ID와 정규화 본문·보기 중복은 0이다.
의미 중복도 내부 문장 검토 범위에서 확인했으나 독립 전문가 검수는 아니다.

AI 일반 제과 지식으로 직접 작성한 입문 개념 문항이다.
외부 공식·교재와 정답 대조, 외부 전문가 검수, 현행 출제기준 전 범위 대조는 미실시다.
해설 및 오답 보기의 내부 논리 검토와 자동 스키마 검사는 외부 정답 보증이 아니다.
숫자 변형으로 목표 수를 채우지 않았다. 확보·검수하지 못한 940문항은 등록하지 않았다.
모든 연도·회차는 null이며 확인되지 않은 기출 이력은 부여하지 않았다.
문항별 저장소 URL은 작성 위치이며 외부 정답 증빙이 아니다.
민간 사이트 기출을 복사하지 않았다. 원문 기출의 재배포 조건도 미확인이다.
자체 제작 문항은 CC BY 4.0으로 제공하며 출처는 이 저장소와 문항 ID로 표시한다.
`python3 scripts/prepare.py`로 같은 ID·순서·내용을 재생성한다.
가져온 문항은 브라우저 로컬에만 저장되며 공용 은행에 자동 게시되지 않는다.

## 표준과 라이선스

최신 main `76b990b8720adfa85c22a0a8f699b17094aa357b`의 CBT 표준 v1.4.0
폴더 전체를 `.agents/skills/cbt-site-standard`에 복사했다.
기준 앱 `b9a682ccff1b460334b78d5bfad9375b7ec4fbb6`의 코드를 재사용했다.
원본 MIT 고지는 LICENSE에 보존했다. 전기 문항·원고는 재사용하지 않았다.
기존 저장소는 README만 있었고 AGENTS.md는 신규 생성했다.

## 배포 상태

main push → validate → Pages deploy, PR은 validate만 실행하는 workflow를 준비했다.
배포 사전 확인 첫 명령:
`gh api repos/YunSangYeong/Craftsman-Confectionery-Making-CBT --jq '{full_name,default_branch,permissions}'`

결과: `Get "https://api.github.com/repos/YunSangYeong/Craftsman-Confectionery-Making-CBT": Forbidden`.
첫 차단 정책에 따라 배포 중단. main push·workflow 실행·재실행·대체 배포 없음.
현재 Pages 설정·기존 게시 여부·CI 상태는 미확인이다.
코드는 배포 트리거가 없는 보존 브랜치로만 원격 반영을 시도한다.
예상 주소(배포 확인 주소가 아님):
https://YunSangYeong.github.io/Craftsman-Confectionery-Making-CBT/

사용자 최소 다음 동작: 클라우드 환경 설정의 인터넷 접근 허용 목록에서
`api.github.com` 허용 여부를 확인한다. 이 변경만으로 API 인증·배포 성공은 보장되지 않는다.
첫 차단 뒤 배포 마무리는 사용자에게 맡기며 자동 재시도하지 않는다.
현재 기능 검증 범위와 결과는 [검증 기록](docs/validation.md)에 기록한다.
