# 면접 준비 자료 설계 (Interview Prep Docs)

작성일: 2026-08-19
작성자: 이용학 (feint225@gmail.com)

## 1. 목적

이력서·경력기술서·자기소개서(`asan_hospital/`)와 학술지 논문 13편(`papers/`)을
바탕으로, 면접에서 자신의 연구·프로젝트를 기초 개념부터 설명하고 방어할 수
있게 하는 학습용 문서 세트를 만든다.

특정 기관 전용이 아니라 **연구직·실무직 양쪽에 쓰이는 범용 자료**로 만든다.
`asan_hospital/`은 경력 사실의 출처로만 쓰고, 문서 안에 기관명은 넣지 않는다.

### 전제

작성자는 13편 중 제1저자 1편, 교신저자 1편이고 나머지는 공저다. 공저 논문의
내용을 충분히 알지 못하는 상태이므로, 문서는 **모르는 것을 아는 상태로 만드는
것**이 목표다. 이미 아는 내용을 정리하는 요약본이 아니다.

## 2. 범위

### 대상 자료

프로젝트 4건 + 국가 R&D 과제 8건 + 특허 2건 (경력기술서 기준)

| ID | 프로젝트 | 기간 |
|----|----------|------|
| P1 | 모바일 LiDAR 기반 3차원 계측 및 속성 추정 프레임워크 | 2023.01–2026.06 |
| P2 | 로봇 센서 데이터 기반 가스배관 변화구간 및 길이 탐지 | 2022.01–2023.01 |
| P3 | 시각 이미지와 메타데이터를 통합한 상품 추천 방법론 | 2021.01–2022.01 |
| P4 | 영상 기반 미세먼지 농도 추정 솔루션 | 2020.01–2021.01 |
| P5 | 국가 R&D 과제 8건 + 특허 2건 (묶음 문서) | 2019–2025 |

논문 13편 (모두 동일 깊이로 작성)

| ID | 제목 | 게재처 | 연도 | 저자 위치 |
|----|------|--------|------|-----------|
| T1 | A Mobile LiDAR-Based Deep Learning Approach for Real-Time 3D Body Measurement | Applied Sciences | 2025 | 공저 |
| T2 | Automatic Measurements of Garment Sizes Using CV DL Models and Point Cloud Data | Applied Sciences | 2022 | 공저 |
| T3 | Automated Technology for Strawberry Size Measurement and Weight Prediction Using AI | IEEE Access | 2024 | 공저 |
| T4 | Topology-Constrained NeuroB-Rep: Contact-Aware CAD Reconstruction From 3D Point Clouds | IEEE Access | 2026 | 공저 |
| T5 | A Two-Stage Diffusion Pipeline for Consistent Front-Back Clothing Generation | Quant. Bio-Science | 2025 | **교신저자** |
| T6 | Dental Image Data Generation for Instance Segmentation using GAN | Quant. Bio-Science | 2023 | 공저 |
| T7 | A Multi-View Integrated Ensemble for the Background Discrimination of Semi-Supervised Semantic Segmentation | Applied Sciences | 2023 | 공저 |
| T8 | Integrated Analytic Methodology Using Visual Image and Meta-Data for Product Recommendation | Quant. Bio-Science | 2022 | **제1저자** |
| T9 | Estimation of Particulate Levels Using Deep Dehazing Network and Temporal Prior | Journal of Sensors | 2020 | 공저 |
| T10 | Reinforcement Learning Guided by Double Replay Memory | Journal of Sensors | 2020 | 공저 |
| T11 | An Investment Model Based on a Head-And-Shoulder Pattern with Multiple MA Technical Indicators | Quant. Bio-Science | 2022 | 공저 |
| T12 | Implementation of SoulBound Token Using Economical and Efficient Decentralized File Storage Methods | 정보보호학회논문지 | 2024 | 공저 |
| T13 | SoulBound Token Recovery Mechanism and the Application of a Customer-Centric Guardian System | 정보보호학회논문지 | 2025 | 공저 |

원문 총량은 약 113,000단어(161페이지)로, 전문 완독이 가능한 규모다.

### 범위 밖

- 이력서·경력기술서·자기소개서 자체의 수정
- 기존 포트폴리오 HTML(`index.html`, `blind/`, `samsung/`) 변경
- 특정 기관 맞춤 지원동기 작성

## 3. 접근 방식

**원문 완독 기반 정밀 해부**를 택한다. 13편 PDF를 전문 읽고, 실제 수식·데이터셋·
실험 설정·수치 결과를 그대로 반영해 각 논문 문서를 쓴다.

대안이었던 "초록·방법론만 읽기"는 실험 세팅이나 baseline 비교를 파고드는 질문에
대응할 수 없고, "개념 중심 요약"은 논문을 하나하나 파헤치려는 목적과 맞지 않는다.
공저 논문은 원문 근거 없이 쓰면 문서 자체가 틀릴 수 있어, 원문 완독이 정확성의
전제 조건이다.

## 4. 문서 구조

```
docs/interview/
├─ 00_INDEX.md                     전체 지도 · 학습 순서 · D-day별 플랜
├─ 01_foundations/
│  ├─ 01_통계·머신러닝_기초.md
│  ├─ 02_딥러닝·CNN_기초.md
│  ├─ 03_비전_검출·분할·키포인트.md
│  ├─ 04_3D·PointCloud·LiDAR.md
│  ├─ 05_생성모델_GAN·Diffusion.md
│  └─ 06_강화학습·시계열·기타.md
├─ 02_projects/
│  ├─ P1_모바일LiDAR_3차원계측.md
│  ├─ P2_가스배관_센서탐지.md
│  ├─ P3_상품추천_멀티모달.md
│  ├─ P4_영상기반_미세먼지추정.md
│  └─ P5_국가RnD과제·특허.md
├─ 03_papers/                      T1_*.md ~ T13_*.md
├─ 04_qa/
│  ├─ 01_기초개념_QA.md
│  ├─ 02_프로젝트_QA.md
│  ├─ 03_논문_QA.md
│  ├─ 04_기여도·공저자_QA.md
│  ├─ 05_인성·직무·커리어_QA.md
│  └─ 06_역질문_리스트.md
└─ 05_cheatsheet.md
```

각 파일은 독립적으로 읽을 수 있어야 한다. 다른 파일의 내용을 전제로 하는 경우
상대 경로 링크로 해당 절을 가리키고, 링크를 따라가지 않아도 문맥이 통할 만큼의
한 줄 요약을 함께 둔다.

### 파일별 역할

**00_INDEX.md** — 문서 전체 지도, 권장 학습 순서, 남은 기간별(D-14 / D-7 / D-3 /
D-1) 학습 플랜, 논문↔프로젝트↔기초개념 상호 참조표.

**01_foundations/** — 논문과 프로젝트를 읽기 위한 토대. 각 개념은
`개념 → 직관(비유) → 핵심 수식 → 내 어느 논문·프로젝트에 쓰였나 → 면접 단골질문
→ Reference` 순으로 쓴다. 수학 깊이는 **직관 우선 + 핵심 수식만**으로 하고,
면접에서 나올 수 있는 식(IoU, 손실함수, Bellman 방정식, DDPM 노이즈 스케줄 등)만
기호 하나씩 풀어 설명한다. 유도 과정은 넣지 않는다.

파일별 담을 개념:

- 01: 회귀, 정규화(L1/L2), 편향-분산, 교차검증, 트리·랜덤포레스트·부스팅(LightGBM),
  PLS-DA, 다변량 분석, 분류·회귀 평가지표, 클래스 불균형
- 02: 퍼셉트론~역전파, 활성함수, 옵티마이저, 배치정규화, 과적합 대응, 백본 계보
  (VGG/ResNet/EfficientNet/MobileNetV3), 전이학습, 경량화·온디바이스 추론
- 03: 객체 검출(YOLO 계열), IoU/NMS/mAP, Semantic vs Instance vs Panoptic
  Segmentation, U-Net/DeepLab, 준지도 학습, 키포인트·포즈 추정(HRNet), 히트맵 회귀
- 04: LiDAR·ToF 원리, 깊이맵, 카메라 내부·외부 파라미터, 2D↔3D 역투영, 포인트
  클라우드 자료구조, 정합(ICP)·다운샘플링·노이즈 제거, 메시·B-Rep·CAD 기초
- 05: GAN 원리와 학습 불안정성, pix2pix/CycleGAN, 확산모델(DDPM) 개념과 수식,
  조건부 생성(ControlNet/LoRA), 생성 품질 평가지표(FID/LPIPS 등)
- 06: MDP·Q-learning·DQN·Experience Replay(PER 포함), 시계열 기초와 기술적 지표
  (이동평균, 헤드앤숄더 패턴), 블록체인·NFT·SoulBound Token·IPFS/분산 스토리지,
  LLM 기초(트랜스포머·프롬프팅·Chain-of-Thought·instruction tuning)

  LLM 절을 넣는 이유: 교신저자 논문 T5가 Llama3-Instruct에 CoT와 instruction
  tuning을 결합해 텍스트를 생성한 뒤 확산모델에 넘기는 구조다. 경력기술서의 보유
  기술에는 LLM 항목이 없으므로, 교신저자 논문을 근거로 한 LLM 질문에 대비가
  필요하다.

**02_projects/** — 프로젝트 문서. 논문 템플릿의 3~7번을 STAR(상황–과제–행동–결과)
로 바꾸고 다음을 추가한다: 왜 그 기술을 골랐나 / 검토했던 대안 / 실패한 시도와
원인 / 다시 한다면 무엇을 바꾸겠나 / 이 경험에서 일반화할 수 있는 것.

**03_papers/** — 논문 13편, 아래 템플릿을 공통 적용.

**04_qa/** — 질문 뱅크. 논문별 질문은 각 논문 파일에도 싣고 여기에 통합 재수록해
주제 횡단 검색이 되게 한다.

**05_cheatsheet.md** — 면접 전날 1시간 안에 훑는 압축본. 논문 13편 한 줄 요약,
프로젝트 4건 STAR 30초 스크립트, 자주 틀리는 개념 정의, 숫자(성능·데이터 규모)
암기표.

## 5. 논문 문서 템플릿

13편 모두 아래 11개 절을 같은 순서로 갖는다.

```
0.  30초 요약        면접에서 이 논문을 한 문단으로 말하는 구어체 스크립트
1.  서지정보         저널·연도·저자 순서·본인 위치·저널 성격
2.  왜 이 연구를 했나  기존 방법의 한계, 이 논문이 메운 빈칸
3.  사전지식 (A to Z)  이 논문을 읽기 위해 알아야 할 개념을 바닥부터
                     (01_foundations 해당 절로 상호 링크)
4.  방법론 단계별 해부  파이프라인을 단계로 쪼개 각 단계의 입력·출력·이유
5.  핵심 수식        논문에 실제 등장하는 식만, 기호 하나씩 풀이
6.  실험 세팅        데이터셋 규모·수집 방법, 하드웨어, 하이퍼파라미터, 평가지표
7.  결과 읽기        주요 표·그림의 숫자와 그 숫자가 의미하는 것
8.  한계와 반박 대응   리뷰어·면접관이 찌를 지점과 방어 논리
9.  기여도 질문 대응   본인 역할 정리 프레임 + 직접 채울 빈칸
10. 예상 질문 10~15   답변 스크립트 포함
11. Reference        원전 논문(DOI/arXiv) + 입문 학습자료
```

### 9절(기여도)의 처리

공저 논문은 "여기서 본인 기여는 무엇입니까"가 거의 반드시 나온다. 각 논문 문서에
다음 프레임을 제공하고, 실제 기여 내용은 작성자가 채울 빈칸으로 남긴다.

```
- 내가 직접 한 것:        [ 직접 작성 ]
- 옆에서 지켜본 것:       [ 직접 작성 ]
- 논문 작성 후 이해한 것:  [ 직접 작성 ]
- 이 논문에서 배운 것:     [ 직접 작성 ]
```

답변 전략은 과장 없이 솔직하게 말하되 자신이 실제로 아는 부분을 분명히 드러내는
방향으로 쓴다. 기여를 부풀리는 문구는 넣지 않는다.

## 6. 질문 뱅크 설계

목표 총량 **320문항 이상**.

| 파일 | 내용 | 목표 문항 |
|------|------|-----------|
| 01_기초개념 | "CNN이 뭔가요" 수준부터 "왜 BN이 학습을 안정시키나"까지 | 80 |
| 02_프로젝트 | 프로젝트 4건 × 기술선택·실패·트레이드오프·재현성 | 80 |
| 03_논문 | 13편 × 10~15문항 통합 | 150 |
| 04_기여도·공저자 | 공저 11편에 대한 압박 질문 | 25 |
| 05_인성·직무 | 이직 사유, 재직 기간, 도메인 전환, 협업·갈등, 5년 후 | 40 |
| 06_역질문 | 연구직·실무직 각각의 마지막 질문 | 20 |

각 질문에 붙는 항목:

1. **면접관의 진짜 의도** — 이 질문으로 무엇을 확인하려는가
2. **답변 스크립트** — 구어체, 30초~1분 분량
3. **꼬리질문** — 이 답변 뒤에 이어질 가능성이 높은 질문

난이도 표기: 🟢 기초 / 🟡 실무 / 🔴 압박

## 7. Reference 정책

- **원전**: 저자·연도·학회/저널과 함께 arXiv ID 또는 DOI를 적는다. 확신이 없는
  식별자는 적지 않고, 제목만 쓴 뒤 `(검색 필요)`로 표기한다. 존재하지 않는 링크를
  만들어 넣지 않는다.
- **학습자료**: 한국어 자료를 우선 제시하고, 없으면 영문 강의·문서(CS231n,
  Distill.pub, Lil'Log 등)를 쓴다.
- **본인 논문**: `papers/` 안의 실제 PDF 파일명으로 상대 경로 링크를 건다.

## 8. 정확성 원칙

논문 문서의 수치·데이터셋·실험 세팅은 전부 원문에서 인용한다. 원문에 없는 값은
쓰지 않는다. 배경지식으로 보충한 설명은 `※ 배경 보충`으로 표시해 원문 내용과
구분한다. 면접장에서 문서의 잘못된 숫자를 말하는 사고를 막기 위해서다.

원문에서 확인하지 못한 항목(예: PDF에 하이퍼파라미터가 없는 경우)은 비워 두지
말고 `원문에 명시되지 않음`이라고 적는다.

## 9. 작성 순서

| 단계 | 산출물 | 확인 시점 |
|------|--------|-----------|
| 1 | `docs/interview/` 골격 + 00_INDEX + 전 파일 스켈레톤 | 단계 종료 시 |
| 2 | 01_foundations 6종 | 단계 종료 시 |
| 3 | 03_papers 13편 (PDF 완독 후 작성) | 3~4편 단위 |
| 4 | 02_projects 5종 | 단계 종료 시 |
| 5 | 04_qa 6종 + 05_cheatsheet | 단계 종료 시 |

논문 작성 순서는 본인 기여가 큰 순서를 따른다: T8(제1저자) → T5(교신저자) →
T1 → T2 → T3 → T4 → T7 → T6 → T9 → T10 → T11 → T12 → T13.

기초개념을 논문보다 먼저 쓰는 이유는, 논문 문서의 3절이 기초개념 문서를 참조하는
구조이기 때문이다. 토대가 먼저 있어야 중복 설명을 피할 수 있다.

## 10. 완료 조건

- `docs/interview/` 아래 32개 파일(INDEX 1 + 기초 6 + 프로젝트 5 + 논문 13 + QA 6 + 치트시트 1)이 모두 존재하고 빈 절이 없다
- 논문 13편 문서에 원문 기반 수치가 들어가 있고, 확인 불가 항목이 명시돼 있다
- 질문 뱅크 총합이 320문항 이상이다
- 문서 간 상대 경로 링크가 모두 유효하다
- Reference에 지어낸 DOI/arXiv ID가 없다
