import { test, expect } from '@playwright/test';
for (const size of [{width:390,height:480},{width:740,height:360}]) {
 for (const input of ['wheel','touch'] as const) {
  test(`메뉴 ${size.width}x${size.height} ${input} 아래·위 실제 입력`, async ({page,context}) => {
   await page.setViewportSize(size);
   await page.goto('');
   await page.getByRole('button',{name:'메뉴 열기'}).click();
   await page.waitForTimeout(400);
   const sidebar=page.locator('.sidebar');
   const box=(await sidebar.boundingBox())!;
   const x=box.x+box.width/2, y=Math.min(size.height-60,300);
   const cdp=await context.newCDPSession(page);
   async function scroll(down:boolean) {
    if(input==='wheel') {await page.mouse.move(x,y);await page.mouse.wheel(0,down?600:-600);}
    else {
     const start=down?size.height-80:100, end=down?80:size.height-80;
     await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x,y:start}]});
     for(let i=1;i<=12;i++) {
      await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x,y:start+(end-start)*i/12}]});
      await page.waitForTimeout(20);
     }
     await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
    }
    await page.waitForTimeout(250);
   }
   for(let i=0;i<5;i++) await scroll(true);
   expect(await sidebar.evaluate(e=>e.scrollTop)).toBeGreaterThan(0);
   await expect(page.getByRole('button',{name:'데이터 초기화',exact:true})).toBeInViewport();
   await expect(page.getByRole('button',{name:'학습 기록 백업',exact:true})).toBeInViewport();
   await page.getByRole('button',{name:'데이터 초기화',exact:true}).click();
   await expect(page.getByRole('dialog')).toBeVisible();
   await page.getByRole('button',{name:'돌아가기',exact:true}).click();
   for(let i=0;i<5;i++) await scroll(false);
   await expect(page.getByRole('navigation').getByRole('button',{name:'학습 대시보드',exact:true})).toBeInViewport();
   await page.getByRole('navigation').getByRole('button',{name:'학습 대시보드',exact:true}).click();
   await expect(page.getByRole('heading',{name:'제과기능사 필기 CBT',exact:true})).toBeVisible();
   await expect(page.locator('.criteria-note')).toHaveCount(0);
   await page.screenshot({path:`test-results/menu-${size.width}-${input}.png`});
  });
 }
}
