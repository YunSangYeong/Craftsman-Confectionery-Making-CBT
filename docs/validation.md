# 검증 기록

2026-11-03, 작업 디렉터리 `/workspace/Craftsman-Confectionery-Making-CBT`.

- `npm ci`: 성공.
- `npm test`: 959개 통과(기존 모델 17 + 계산·구성 942). 1,000개 스키마·정규화 중복·출처 상태, 940개 독립 재계산과 정답 보기, 35/36개 합격 경계,
  추출·시간·응답 변경·만료·중복 제출·복습·JSON/CSV 중복·손상 복원 검사.
- `npm run build`: TypeScript와 Vite 빌드 성공.
- `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/usr/bin/chromium npx playwright test tests/e2e/app.spec.ts`:
  PC Chromium 9개 + Pixel 7 에뮬레이션 9개 = 18개 통과.
  실제 keydown/keyup Space, 버튼 포커스, 미응답·마지막 문제 보호,
  결과·오답·북마크·통계·가져오기·승인·초기화·새로고침·자동 제출·손상 원본 보존 확인.
- 메뉴 회귀: 390×480·740×360 각각 실제 mouse wheel 및 CDP touchStart/move/end 입력.
  PC/모바일 프로젝트 합계 8개 통과. 하단 백업·초기화 뷰포트 진입, 초기화 확인창 열기·취소,
  반대 입력으로 상단 대시보드 복귀·클릭 성공. scrollTop 직접 변경 없음.
- 브라우저 회귀 합계 26개 통과. 스크린샷으로 작은 화면 대시보드도 확인.

실기기, Safari, Firefox, 블로그 iframe 입력·스토리지 제한은 미검사.
공식 자료 및 정답 대조 미완료, 외부 전문가 검수 미실시.
프로덕션 빌드 성공과 GitHub CI·배포 성공은 별개이다.
배포 사전 GitHub API 요청 Forbidden으로 중단했으며 CI·배포는 실행하지 않았다.


1,000문항 확장 시 기존 60개의 전체 객체가 이전 커밋과 동일함을 비교했고,
연속 두 번 생성한 데이터 SHA256도 동일했다(`bank-audit.json`).
Vite는 큰 청크 경고를 출력한다. 빌드는 성공하며 JS 청크 약 1.745 MB,
gzip 약 149 kB다. 문항은 정적 JSON으로 앱 번들에 포함된다.
