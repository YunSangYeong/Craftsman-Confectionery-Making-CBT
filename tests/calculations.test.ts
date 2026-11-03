import { describe, expect, it } from 'vitest';
import { BASE_BANK, fingerprint, createExam } from '../src/model';
// Independent JS number equations vs Python Decimal generator. Rounding is tested
// after solving, including division remainders, mass conservation and unit scaling.
const solve: Record<string,(v:number[])=>number> = {
 confectionery01: ([flour,ratio])=>flour/(100/ratio),
 confectionery02: ([ingredient,oldFlour,newFlour])=>ingredient/oldFlour*newFlour,
 confectionery03: ([flour,sugar,egg,fat])=>flour+flour*sugar/100+flour*egg/100+flour*fat/100,
 confectionery04: ([before,loss])=>before-before*loss/100,
 confectionery05: ([before,delta])=>delta/before*100,
 confectionery06: ([total,each])=>Math.floor(total/each),
 confectionery07: ([total,count])=>total/count,
 confectionery08: ([sugar,water])=>sugar/(water+sugar)*100,
 confectionery09: ([initial,from,to])=>initial*(from-to)/to,
 confectionery10: ([cream,milk,cf,mf])=>(cream*cf/100+milk*mf/100)/(cream+milk)*100,
 confectionery11: ([a,b,pa,pb])=>(a*pa/100+b*pb/100)/(a+b)*100,
 confectionery12: ([mass,water])=>mass/(100/water),
 confectionery13: ([mass,water])=>mass-mass*water/100,
 confectionery14: ([carbs,protein,fat])=>(carbs+protein)*4+fat*9,
 confectionery15: ([price,grams])=>price/1000*grams,
 confectionery16: ([price,count])=>price/count,
 confectionery17: ([stock,am,pm])=>stock-(am+pm),
 confectionery18: ([mass,oldD,newD])=>mass*((Math.PI*(newD/2)**2)/(Math.PI*(oldD/2)**2)),
 confectionery19: ([batter,water])=>batter/water,
 confectionery20: ([needed,capacity])=>Math.ceil(needed/capacity),
};
const numeric=BASE_BANK.filter(q=>q.calculation);
function rounded(n:number,p:number) {
 const scale=10**p;
 return Math.round((n+Number.EPSILON*Math.max(1,Math.abs(n)))*scale)/scale;
}
describe('제과 계산 변형 독립 검증',()=>{
 it('20개 유형 × 서로 다른 47개 조건이며 60개 기존 ID와 내용을 유지한다',()=>{
  expect(numeric).toHaveLength(940);
  expect(new Set(numeric.map(q=>q.family)).size).toBe(20);
  for(const family of new Set(numeric.map(q=>q.family))) {
   const group=numeric.filter(q=>q.family===family);
   expect(group).toHaveLength(47);
   expect(new Set(group.map(q=>JSON.stringify(q.calculation!.values))).size).toBe(47);
  }
  expect(BASE_BANK.slice(0,60).map(q=>q.id)).toEqual(Array.from({length:60},(_,i)=>`CONF-${String(i+1).padStart(3,'0')}`));
  expect(new Set(BASE_BANK.map(fingerprint)).size).toBe(1000);
 });
 for(const q of numeric) it(`${q.id} ${q.topic}`,()=>{
  const c=q.calculation!;
  const value=rounded(solve[c.kind](c.values),c.precision!);
  expect(c.result).toBeCloseTo(value,8);
  const options=q.choices.map(s=>Number(s.split(' ')[0]));
  expect(options[q.answer-1]).toBeCloseTo(value,8);
  expect(options.filter(n=>Math.abs(n-value)<1e-8)).toHaveLength(1);
  expect(new Set(options).size).toBe(4);
  expect(options.every(n=>n>=0&&Number.isFinite(n))).toBe(true);
  expect(q.explanation).toContain(String(c.result));
  expect(q.explanation).toContain('조건');
  expect(q.question).toContain(c.precision===0?'정수':'반올림');
  expect(q.year).toBeNull(); expect(q.session).toBeNull();
 });
 it('실전 추출은 숫자 변형 family를 중복 선택하지 않는다',()=>{
  for(let i=0;i<30;i++) {
   const exam=createExam(BASE_BANK,'main');
   const families=exam.questions.filter(q=>q.family).map(q=>q.family);
   expect(new Set(families).size).toBe(families.length);
   expect(exam.questions).toHaveLength(60);
  }
 });
});
