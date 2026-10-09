# Bestuline Wholesale Catalog

도매 제품 849개를 한 화면에 보는 카달로그. 내부용(세일즈·생산).

## 파일

| 파일 | 역할 | GitHub Pages |
|---|---|---|
| `index.html` | 카달로그 본체. 이것만 있으면 사이트가 돌아감 | **사용** |
| `robots.txt` | 검색엔진 노출 차단 | **사용** |
| `data.json` | 제품 데이터 (849개). 다음 갱신의 입력값 | 보관용 |
| `build.py` | CSV → data.json | 보관용 |
| `make_html-public.py` | data.json → 공개용 index.html (가격·토큰 없음) | 보관용 |
| `make_html-prices.py` | data.json → 손님용 가격 파일 | 보관용 |

`data.json`, `build.py`, `make_html.py` 는 사이트가 읽지 않습니다.
**제 작업 공간은 리셋되므로 저장소에 보관해 두어야 다음에 갱신할 수 있습니다.**

## 두 가지 버전

| 파일 | 가격 | Shopify 토큰 | 용도 |
|---|---|---|---|
| `index.html` | **없음** | **없음** | GitHub Pages. 공개 |
| `Bestuline-Wholesale-Catalog.html` | **있음** | 있음 | 지정한 손님에게 파일로 |

가격 버전은 저장소에 올리지 마세요.
갱신할 때 두 파일 다 새로 만들어야 합니다 (같은 data.json 에서).

### 왜 공개본에서 토큰까지 뺐나
Faire 는 "Faire 가격이 다른 채널(본인 도매 사이트 포함)보다 같거나 낮아야 한다"고 요구합니다.
bestuline.com 가격이 Faire 보다 낮으므로, 공개 파일에서 가격이 조회되면 안 됩니다.
토큰이 남아 있으면 소스를 열어 Shopify Storefront API 로 가격을 받아올 수 있었습니다.

토큰을 빼면서 공개본은 아래 실시간 기능을 잃었습니다:
- 단종/draft 제품 자동 제거
- 품절 OUT OF STOCK 표시
- 세일 배지 최신화

손님용 가격 파일에는 토큰이 남아 있어 위 기능이 계속 작동합니다.
(그 파일은 어차피 가격이 적혀 있어 토큰이 추가 노출을 만들지 않음)

주의: 파일 안의 Shopify Storefront API 토큰으로는 기술적으로 가격 조회가 가능합니다.
완전히 막으려면 토큰을 빼야 하고, 그러면 아래 실시간 기능을 전부 잃습니다.

## CSV가 필요한 것 (공개본은 전부 해당)

- 신제품 추가
- 단종 제품 제거
- 품절 반영
- 제목 / 프리팩 / 사이즈 / 세일 변경

손님용 가격 파일만 단종·품절·세일을 열 때마다 자동 확인합니다.

## 갱신 방법

### 1) 신제품 추가 (권장, 2분)
Shopify 제품 목록 → 최신순 확인 → 내보내기 → **Current page** (50개) → CSV

```
python3 build.py 새파일.csv --merge
python3 make_html-public.py     # 공개용 index.html
python3 make_html-prices.py     # 손님용 가격 파일
```

`--merge` 는 파일에 들어있는 제품만 갱신/추가하고 나머지는 그대로 둡니다.
신제품은 맨 앞에, draft 로 바뀐 제품은 목록에서 빠집니다.

### 2) 전체 재빌드 (분기 1회)
Shopify → 내보내기 → **All products** → CSV

```
python3 build.py 전체파일.csv
python3 make_html-public.py
python3 make_html-prices.py
```

주의: `--merge` 없이 돌리면 그 CSV가 전부가 됩니다.
인자 없이 `python3 build.py` 만 치면 스크립트 안에 적힌 옛날 경로를 읽으므로 쓰지 마세요.

### 3) 배포
생성된 `index.html` 을 이 저장소에 덮어쓰기 → 1~2분 후 반영

## 특수 표시

- 양말 번들: `8 Bundles · 24 Pairs - Prepack` (본문 설명에서 읽음)
- 행거 포장: `6 Hangers · 12 Pcs - Prepack`
- 그 외: `12pcs - Prepack`
- 합본 리스팅: 제목에 번호가 없으면 SKU 앞자리에서 가져옴 (`#80164/80165/80166`)

## 포함 기준

Status = active 인 제품만. draft 는 제외.
