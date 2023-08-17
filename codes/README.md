### TitanicFromDisaster

<details>
<summary>TitanicFromDisaster</summary>

#### DDA
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | --- |
| survival | Survival | 0 = No, 1 = Yes | 범주형, 확인 결과 데이터 타입이 결정됨. |
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형 |
| sex | Sex | |범주형, 범주형 데이터로 결과가 나옴|
| Age | Age in years | | --- |
| sibsp | # of siblings / spouses aboard the Titanic | | --- |
| parch | # of parents / children aboard the Titanic | | --- |
| ticket | Ticket number | | --- |
| fare | Passenger fare | | --- |
| cabin | Cabin number | | --- |
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton | --- |

</details>

### TypeOfContractChannel

<details>
<summary>TypeOfContractChannel</summary>

#### DDA
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | --- |
| type_of_contract | type_of_contract | '렌탈', '멤버십' | 범주형, 순서 관계가 없는 명목형 |
| type_of_contract2 | type_of_contract | 'Normal', 'Extension_Rental', 'TAS', 'Promotion', ... | 범주형 |
| channel | channel | |범주형, 순서 관계가 없는 명목형|
| datetime | datetime | | --- |
| payment_type | payment_type | 'CMS', '카드이체', '가상계좌', '지로', '무통장' | 범주형, 순서 관계가 없는 명목형 |
| product | 제품 종류 | 'K1', 'K3', 'K2', 'K4', 'K6', nan, 'K5' | 범주형, 순서 관계가 없는 명목형 |
| state | 현재상태 | '계약확정', '해약확정', '기간만료', '해약진행중' | 범주형, 순서 관계가 없는 명목형 |
| overdue | 연체여부 | '없음', '있음' | 범주형, 순서 관계가 없는 명목형 |
| bank | bank | '새마을금고', '현대카드', '우리은행', '농협은행', ... | 범주형, 순서 관계가 없는 명목형 |
| cancellation | 해약 여부? | '정상', '해약' | 범주형, 순서 관계가 없는 명목형 |

</details>