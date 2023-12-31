
## 🐾 분석 정보 및 분석 내용 설명
<details>
<summary>NSC2_BND_DDA</summary>

[NSC2_BND_DDA](./NSC2_BND_DDA.ipynb)

#### DDA
| 컬럼명 | 컬럼 설명 | 컬럼값 설명 |분석가 설명|
|-----|-----|-----|-----|
| RN_INDI | 개인고유번호 | 7자리의 개인 고유번호, 연계코드 | 범주형의 명목형 |
| BTH_YYYY | 출생년도 (1921LE ~ 2015) | 대상자의 출생년도, 기준년도에서 출생년도를 뺀 값으로 산출됨 |날짜형(순서형), 범주형(연속형)|
| DTH_YYYYMM | 사망연월 | 사망자의 사망연월, 년월로 표기됨 |날짜형(순서형), 범주형(연속형)|
| COD1 | 사망원인1 | 한국표준질병‧사인분류(KCD) 코드 사용, 사망 원인을 상위 1차 분류로 기재된 코드 |범주형|
| COD2 | 사망원인2 | 한국표준질병‧사인분류(KCD) 코드 사용, 사망 원인을 상위 2차 분류(상세 원인)로 기재된 코드 |범주형, 이차 사망원인|

### * 분석 기준 : 연도별 주요 사망 원인 분석 (X : 사망연도, Y : COD1)

</details>

<details>
<summary>RecurrenceOfSurgery_DDA</summary>

[RecurrenceOfSurgery_DDA](./RecurrenceOfSurgery_DDA.ipynb)

#### DDA
| 컬럼명 | 컬럼 설명 | 컬럼값 설명 |분석가 설명|
|-----|-----|-----|-----|
| RN_INDI | 개인고유번호 | 7자리의 개인 고유번호, 연계코드 | 범주형의 명목형 |
| BTH_YYYY | 출생년도 (1921LE ~ 2015) | 대상자의 출생년도, 기준년도에서 출생년도를 뺀 값으로 산출됨 |날짜형(순서형), 범주형(연속형)|
| DTH_YYYYMM | 사망연월 | 사망자의 사망연월, 년월로 표기됨 |날짜형(순서형), 범주형(연속형)|
| COD1 | 사망원인1 | 한국표준질병‧사인분류(KCD) 코드 사용, 사망 원인을 상위 1차 분류로 기재된 코드 |범주형|
| COD2 | 사망원인2 | 한국표준질병‧사인분류(KCD) 코드 사용, 사망 원인을 상위 2차 분류(상세 원인)로 기재된 코드 |범주형, 이차 사망원인|

### * 분석 기준 : 연도별 주요 사망 원인 분석 (X : 사망연도, Y : COD1)

</details>