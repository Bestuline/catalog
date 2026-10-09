import json
d=json.load(open('data.json'))
payload=json.dumps(d,ensure_ascii=False,separators=(',',':'))

HTML = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow,noarchive">
<title>Bestuline Wholesale Catalog</title>
<style>
*{box-sizing:border-box}
body{--cols:6;--ratio:105%;--gap:8px;margin:0;font:13px/1.35 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;color:#111;background:#fff}
.wrap{max-width:1180px;margin:0 auto;padding:0 28px}
header{position:sticky;top:0;z-index:10;background:#fff;border-bottom:1px solid #ddd;padding:10px 0}
.brandrow{display:flex;align-items:center;gap:12px;flex-wrap:wrap;justify-content:center}
h1{font-size:16px;margin:0;letter-spacing:.03em}
input[type=search]{padding:6px 10px;border:1px solid #ccc;border-radius:4px;font-size:13px;width:180px}
select{padding:6px 8px;border:1px solid #ccc;border-radius:4px;font-size:12px}
button{padding:6px 14px;border:1px solid #111;background:#111;color:#fff;border-radius:4px;cursor:pointer;font-size:13px}
button.ghost{background:#fff;color:#111}
nav{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px;justify-content:center}
nav a{padding:5px 11px;border:1px solid #ccc;border-radius:3px;text-decoration:none;color:#333;font-size:12px}
nav a.on{background:#111;color:#fff;border-color:#111}
nav a.sale{color:#c00;border-color:#c00;font-weight:700}
nav a.new{color:#0a7;border-color:#0a7;font-weight:700}
nav a.new.on{background:#0a7;color:#fff;border-color:#0a7}
.cat h2.new{border-bottom-color:#0a7;color:#0a7}
.nbadge{position:absolute;top:0;right:0;background:#0a7;color:#fff;font-size:8.5px;font-weight:700;padding:1px 4px;z-index:2}
nav a.sale.on{background:#c00;color:#fff;border-color:#c00}
.cat h2.sale{border-bottom-color:#c00;color:#c00}
.cat h3{font-size:11.5px;margin:12px 0 6px;padding-bottom:3px;border-bottom:1px solid #bbb;letter-spacing:.05em;text-transform:uppercase;color:#444}
.off{position:absolute;top:0;left:0;background:#c00;color:#fff;font-size:9px;font-weight:700;padding:1px 4px;z-index:2}
nav a span{opacity:.6;font-size:11px}
.meta{font-size:11px;color:#666;margin-top:7px;text-align:center}
main{padding:16px 0 40px}
.cat{margin-bottom:26px}
.cat h2{font-size:14px;margin:0 0 8px;padding-bottom:5px;border-bottom:2px solid #111;text-transform:uppercase;letter-spacing:.06em}
.grid{display:grid;grid-template-columns:repeat(var(--cols),minmax(0,1fr));grid-auto-rows:1fr;gap:var(--gap)}
.card{min-width:0;border:1px solid #e5e5e5;padding:5px;text-align:center;text-decoration:none;color:inherit;display:flex;flex-direction:column;background:#fff}
.card:hover{border-color:#111}
.ph{position:relative;width:100%;padding-top:var(--ratio);overflow:hidden;background:#fff;margin-bottom:4px}
.ph img{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:contain;object-position:center;display:block}
.sty.multi{font-size:9.5px;letter-spacing:-.01em}
.sty{min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#c00;font-weight:700;font-size:11.5px}
.pk{min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#c00;font-size:10px}
.nm{font-size:10px;line-height:1.22;color:#1a3a6b;font-weight:600;margin-top:2px;height:24px;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.sz{font-size:9px;line-height:1.2;color:#777;margin-top:1px;height:11px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.empty{padding:40px;text-align:center;color:#888}
.live{font-size:11px;margin-top:4px;text-align:center;color:#b26a00}
.live.warn{color:#b26a00}
.live.err{color:#999}
.card.oos{opacity:.55}
.oostag{position:absolute;bottom:0;left:0;right:0;background:#555;color:#fff;font-size:9px;font-weight:700;padding:1px 0;z-index:2}
@media print{ .card.oos{opacity:1} .oostag{-webkit-print-color-adjust:exact;print-color-adjust:exact} }
@media screen and (max-width:900px){body{--cols:3}.wrap{padding:0 12px}}
@media print{
 @page{size:letter portrait;margin:0.4in}
 header{display:none}
 .wrap{max-width:none;padding:0}
 main{padding:0}
 .grid{grid-template-columns:repeat(var(--cols),minmax(0,1fr));gap:4px}
 .card{padding:4px;border:1px solid #ddd;break-inside:avoid;page-break-inside:avoid}
 .cat h2{break-after:avoid;page-break-after:avoid;margin-bottom:6px}
 .cat h3{break-after:avoid;page-break-after:avoid;margin:9px 0 5px}
 .off,.nbadge{-webkit-print-color-adjust:exact;print-color-adjust:exact}
 img{max-width:100%}
 a{text-decoration:none;color:inherit}
 body{font-size:10px}
}
</style></head><body>
<header><div class="wrap">
 <div class="brandrow">
  <h1>BESTULINE WHOLESALE CATALOG</h1>
  <input type="search" id="q" placeholder="Style # or keyword">
  <select id="sz" title="Photo size">
   <option value="6|130%">Photo: Large</option>
   <option value="6|105%" selected>Photo: Medium</option>
   <option value="7|100%">Photo: Small</option>
   <option value="8|95%">Photo: Tiny</option>
  </select>
  <select id="so" title="Sort">
   <option value="new">Sort: Newest</option>
   <option value="style">Sort: Style #</option>
   <option value="off">Sort: Discount %</option>
  </select>
  <button class="ghost" id="all">All categories</button>
  <button id="print">Print / PDF</button>
 </div>
 <nav id="nav"></nav>
 <div class="meta" id="meta"></div>
</div></header>
<main><div class="wrap" id="out"></div></main>
<script>
const DATA=__PAYLOAD__;
let cur=DATA.cats[0], q='';
const nav=document.getElementById('nav'), out=document.getElementById('out'), meta=document.getElementById('meta');

function sizes(s){ return s||''; }
function sortList(a){const s=document.getElementById('so').value;
 const c={new:(x,y)=>x.ord-y.ord,
  style:(x,y)=>String(x.s).localeCompare(String(y.s),undefined,{numeric:true}),
  off:(x,y)=>(y.off||0)-(x.off||0)}[s];
 return a.slice().sort(c);}
function card(p){
 return `<a class="card${p.oos?' oos':''}" target="_blank" href="https://bestuline.com/products/${p.h}">
   <div class="ph">${p.sale?`<span class="off">-${p.off}%</span>`:''}${p.new?`<span class="nbadge">NEW</span>`:''}${p.img?`<img loading="eager" src="${p.img}" alt="" onerror="this.style.display='none'">`:''}${p.oos?`<span class="oostag">OUT OF STOCK</span>`:''}</div>
   <div class="sty${p.s.indexOf('/')>0?' multi':''}">#${p.s}</div>
   <div class="pk">${p.pkl||''}</div>
   <div class="nm">${p.t.replace(/&/g,'&amp;').replace(/</g,'&lt;')}</div>
   <div class="sz">${sizes(p.sz)}</div></a>`;
}
function match(p){ if(p.gone) return false;
 if(!q) return true; return (p.s+' '+p.ft).toLowerCase().includes(q); }

function render(){
 const ns=DATA.prods.filter(p=>p.sale&&match(p)).length;
 const nn=DATA.prods.filter(p=>p.new&&match(p)).length;
 nav.innerHTML=`<a href="#" data-c="NEW" class="new ${cur==='NEW'?'on':''}">NEW <span>${nn}</span></a>`+
  `<a href="#" data-c="SALE" class="sale ${cur==='SALE'?'on':''}">SALE <span>${ns}</span></a>`+
  DATA.cats.map(c=>{
   const n=DATA.prods.filter(p=>p.ty===c&&match(p)).length;
   return `<a href="#" data-c="${c}" class="${cur===c?'on':''}">${c} <span>${n}</span></a>`}).join('');
 let total=0, parts=[];
 if(cur==='SALE'||cur==='NEW'){
   const isNew=cur==='NEW';
   const all=sortList(DATA.prods.filter(p=>(isNew?p.new:p.sale)&&match(p))); total=all.length;
   let inner='';
   for(const c of DATA.cats){
     const list=all.filter(p=>p.ty===c);
     if(!list.length) continue;
     inner+=`<h3>${c} (${list.length})</h3><div class="grid">`+list.map(card).join('')+`</div>`;
   }
   parts.push(`<section class="cat"><h2 class="${isNew?'new':'sale'}">${cur} (${total})</h2>${inner}</section>`);
 } else {
   const cats = cur==='*'?DATA.cats:[cur];
   for(const c of cats){
     const list=sortList(DATA.prods.filter(p=>p.ty===c&&match(p)));
     if(!list.length) continue; total+=list.length;
     parts.push(`<section class="cat"><h2>${c} (${list.length})</h2><div class="grid">`+
       list.map(card).join('')+`</div></section>`);
   }
 }
 out.innerHTML=parts.join('')||'<div class="empty">No matching items.</div>';
 meta.textContent=`${total} items shown  |  ${DATA.prods.length} published products  |  Data as of ${DATA.built||'-'}`;
}
nav.addEventListener('click',e=>{const a=e.target.closest('a'); if(!a)return; e.preventDefault(); cur=a.dataset.c; render();});
document.getElementById('all').onclick=()=>{cur='*';render();};

document.getElementById('q').addEventListener('input',e=>{q=e.target.value.trim().toLowerCase();render();});
document.getElementById('sz').addEventListener('change',()=>applySize());
document.getElementById('so').addEventListener('change',()=>render());
document.getElementById('print').onclick=async()=>{
  const b=document.getElementById('print'), imgs=[...document.images].filter(i=>!i.complete);
  if(imgs.length){ b.textContent='Loading images...';
    await Promise.all(imgs.map(i=>new Promise(r=>{i.onload=i.onerror=r;})));
    b.textContent='Print / PDF'; }
  window.print();
};
applySize();
render();

function applySize(){const[c,r]=document.getElementById('sz').value.split('|');
 document.body.style.setProperty('--cols',c); document.body.style.setProperty('--ratio',r);}
</script></body></html>"""

open('/mnt/user-data/outputs/bestuline-catalog.html','w',encoding='utf-8').write(HTML.replace('__PAYLOAD__',payload))
print('ok')
