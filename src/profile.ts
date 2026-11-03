// Official source could not be read (proxy HTTP 403). These are learning assumptions.
export const PROFILE = {
  name: '제과기능사',
  subjects: ['과자류 재료, 제조 및 위생관리'],
  questionCount: 60,
  durationMinutes: 60,
  passRatio: 0.6,
  rulesVerificationStatus: 'pending',
  officialSource: 'https://www.q-net.or.kr/crf005.do?id=crf00503&jmCd=7892',
  selectionPolicy: '전체 검수 문항 무작위; 공식 세부 영역별 배분 미확인',
} as const;
