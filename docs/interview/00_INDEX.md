# 면접 준비 자료 — 전체 지도

이용학 · 응용통계학 박사 · 데이터 분석 및 AI 모델 개발

---

## 이 자료의 사용법

이 문서 세트는 **자신의 연구와 프로젝트를 기초 개념부터 설명하고 방어하기 위한 학습 자료**다. 이미 아는 내용을 정리한 요약본이 아니라, 모르는 것을 아는 상태로 만드는 것이 목적이다.

학술지 논문 13편 중 제1저자는 1편, 교신저자는 1편이고 나머지 11편은 공저다. 공저 논문은 내용을 충분히 알지 못하는 상태일 수 있는데, 면접에서는 이력서에 적힌 모든 논문이 질문 대상이 된다. 그래서 13편을 모두 같은 깊이로 해부했다. 각 논문 문서는 원문 PDF를 전문 읽고 작성했으며, 수치·데이터셋·실험 설정은 전부 원문에서 인용했다.

읽는 순서는 **기초개념 → 논문 → 프로젝트 → 질문 뱅크**다. 기초개념을 먼저 두는 이유는, 논문 문서의 3절(사전지식)이 기초개념 문서를 참조하는 구조이기 때문이다. 토대를 먼저 잡아야 논문 문서에서 같은 설명을 반복해 읽지 않아도 된다.

면접이 임박했다면 [05_cheatsheet.md](05_cheatsheet.md)만 읽어도 된다. 논문 13편 한 줄 요약, 프로젝트 30초 스크립트, 반드시 외울 숫자가 압축돼 있다.

---

## 파일 지도

| 경로 | 책임 |
|------|------|
| [00_INDEX.md](00_INDEX.md) | 이 문서. 전체 지도, 학습 순서, D-day 플랜 |
| [01_통계·머신러닝_기초.md](01_foundations/01_통계·머신러닝_기초.md) | 회귀·정규화·편향분산·트리앙상블·PLS-DA·평가지표 |
| [02_딥러닝·CNN_기초.md](01_foundations/02_딥러닝·CNN_기초.md) | 역전파·옵티마이저·BN·백본 계보·전이학습·경량화 |
| [03_비전_검출·분할·키포인트.md](01_foundations/03_비전_검출·분할·키포인트.md) | YOLO·IoU/NMS/mAP·세그멘테이션·준지도·HRNet |
| [04_3D·PointCloud·LiDAR.md](01_foundations/04_3D·PointCloud·LiDAR.md) | LiDAR 원리·깊이맵·카메라 파라미터·역투영·정합·B-Rep |
| [05_생성모델_GAN·Diffusion.md](01_foundations/05_생성모델_GAN·Diffusion.md) | GAN·pix2pix/CycleGAN·DDPM·조건부 생성·생성 평가지표 |
| [06_강화학습·시계열·기타.md](01_foundations/06_강화학습·시계열·기타.md) | MDP/DQN/Replay·시계열 기술지표·블록체인/SBT/IPFS·LLM 기초 |
| [P1_모바일LiDAR_3차원계측.md](02_projects/P1_모바일LiDAR_3차원계측.md) | 모바일 LiDAR 기반 3차원 계측 및 속성 추정 (2023.01–2026.06) |
| [P2_가스배관_센서탐지.md](02_projects/P2_가스배관_센서탐지.md) | 로봇 센서 데이터 기반 가스배관 변화구간 탐지 (2022.01–2023.01) |
| [P3_상품추천_멀티모달.md](02_projects/P3_상품추천_멀티모달.md) | 시각 이미지와 메타데이터 통합 상품 추천 (2021.01–2022.01) |
| [P4_영상기반_미세먼지추정.md](02_projects/P4_영상기반_미세먼지추정.md) | 영상 기반 미세먼지 농도 추정 (2020.01–2021.01) |
| [P5_국가RnD과제·특허.md](02_projects/P5_국가RnD과제·특허.md) | 국가 R&D 과제 8건 + 특허 2건 |
| [T01_상품추천_멀티모달.md](03_papers/T01_상품추천_멀티모달.md) | 논문 T01 (제1저자) |
| [T02_전후면의류_확산모델.md](03_papers/T02_전후면의류_확산모델.md) | 논문 T02 (교신저자) |
| [T03_모바일LiDAR_인체계측.md](03_papers/T03_모바일LiDAR_인체계측.md) | 논문 T03 |
| [T04_의류치수_포인트클라우드.md](03_papers/T04_의류치수_포인트클라우드.md) | 논문 T04 |
| [T05_딸기_크기무게추정.md](03_papers/T05_딸기_크기무게추정.md) | 논문 T05 |
| [T06_NeuroBRep_CAD복원.md](03_papers/T06_NeuroBRep_CAD복원.md) | 논문 T06 |
| [T07_멀티뷰앙상블_준지도분할.md](03_papers/T07_멀티뷰앙상블_준지도분할.md) | 논문 T07 |
| [T08_치과영상_GAN생성.md](03_papers/T08_치과영상_GAN생성.md) | 논문 T08 |
| [T09_미세먼지_디헤이징.md](03_papers/T09_미세먼지_디헤이징.md) | 논문 T09 |
| [T10_강화학습_이중리플레이.md](03_papers/T10_강화학습_이중리플레이.md) | 논문 T10 |
| [T11_헤드앤숄더_투자모델.md](03_papers/T11_헤드앤숄더_투자모델.md) | 논문 T11 |
| [T12_SBT_분산스토리지.md](03_papers/T12_SBT_분산스토리지.md) | 논문 T12 |
| [T13_SBT_복구메커니즘.md](03_papers/T13_SBT_복구메커니즘.md) | 논문 T13 |
| [01_기초개념_QA.md](04_qa/01_기초개념_QA.md) | 기초 개념 질문 80문항 이상 |
| [02_프로젝트_QA.md](04_qa/02_프로젝트_QA.md) | 프로젝트 질문 80문항 이상 |
| [03_논문_QA.md](04_qa/03_논문_QA.md) | 논문 질문 150문항 이상 |
| [04_기여도·공저자_QA.md](04_qa/04_기여도·공저자_QA.md) | 기여도 압박 질문 25문항 이상 |
| [05_인성·직무·커리어_QA.md](04_qa/05_인성·직무·커리어_QA.md) | 인성·직무 질문 40문항 이상 |
| [06_역질문_리스트.md](04_qa/06_역질문_리스트.md) | 면접 끝에 던질 역질문 20문항 이상 |
| [05_cheatsheet.md](05_cheatsheet.md) | 전날 1시간 압축본 |

---

## 논문 대응표

문서 번호 `T01`~`T13`은 **본인 기여가 큰 순서**로 매긴 것이다. 게재 연도순이 아니다.

| 문서 | 논문 제목 | 게재처·연도 | 저자 위치 |
|------|-----------|-------------|-----------|
| T01 | Integrated Analytic Methodology Using Visual Image and Meta-Data for Product Recommendation | Quant. Bio-Science 2022 | **제1저자** |
| T02 | A Two-Stage Diffusion Pipeline for Consistent Front-Back Clothing Generation | Quant. Bio-Science 2025 | **교신저자** |
| T03 | A Mobile LiDAR-Based Deep Learning Approach for Real-Time 3D Body Measurement | Applied Sciences 2025 | 공저 |
| T04 | Automatic Measurements of Garment Sizes Using Computer Vision Deep Learning Models and Point Cloud Data | Applied Sciences 2022 | 공저 |
| T05 | Automated Technology for Strawberry Size Measurement and Weight Prediction Using AI | IEEE Access 2024 | 공저 |
| T06 | Topology-Constrained NeuroB-Rep: Contact-Aware CAD Reconstruction From 3D Point Clouds | IEEE Access 2026 | 3/4저자 |
| T07 | A Multi-View Integrated Ensemble for the Background Discrimination of Semi-Supervised Semantic Segmentation | Applied Sciences 2023 | 공저 |
| T08 | Dental Image Data Generation for Instance Segmentation using Generative Adversarial Networks | Quant. Bio-Science 2023 | 공저 |
| T09 | Estimation of Particulate Levels Using Deep Dehazing Network and Temporal Prior | Journal of Sensors 2020 | 공저 |
| T10 | Reinforcement Learning Guided by Double Replay Memory | Journal of Sensors 2020 | 공저 |
| T11 | An Investment Model Based on a Head-And-Shoulder Pattern with Multiple Moving Average Technical Indicators for Future Markets | Quant. Bio-Science 2022 | 공저 |
| T12 | Implementation of SoulBound Token Using Economical and Efficient Decentralized File Storage Methods | 정보보호학회논문지 2024 | 공저 |
| T13 | SoulBound Token Recovery Mechanism and the Application of a Customer-Centric Guardian System | 정보보호학회논문지 2025 | 공저 |

원문 PDF는 저장소의 `papers/` 폴더에 있다. 각 논문 문서의 11절 Reference에서 직접 열 수 있다.

---

## 논문 · 프로젝트 · 기초개념 상호 참조표

한 주제를 파고들 때 함께 봐야 할 문서를 묶었다.

| 주제 | 논문 | 프로젝트 | 기초개념 |
|------|------|----------|----------|
| 3D 계측 (역투영·키포인트) | T03, T04, T05 | P1 | 03_비전, 04_3D |
| CAD 복원 · 포인트 클라우드 | T06 | — | 04_3D |
| 멀티모달 (이미지+텍스트) | T01 | P3 | 02_딥러닝, 06_LLM |
| 생성모델 | T02, T08 | — | 05_생성모델, 06_LLM |
| 분할 · 준지도 학습 | T07, T08 | — | 03_비전 |
| 대기환경 · 영상 분석 | T09 | P4 | 01_통계, 02_딥러닝 |
| 강화학습 | T10 | — | 06_강화학습 |
| 시계열 · 금융 | T11 | — | 01_통계, 06_시계열 |
| 블록체인 · 보안 | T12, T13 | — | 06_블록체인 |
| 센서 시계열 · 트리 모델 | — | P2 | 01_통계 |
| 국가 R&D · 특허 | — | P5 | — |

---

## 권장 학습 순서

| 단계 | 내용 | 예상 소요 |
|------|------|-----------|
| 1 | `01_foundations/` 6종 정독 | 8~10시간 |
| 2 | `03_papers/` T01·T02 (제1저자·교신저자) | 3시간 |
| 3 | `03_papers/` T03~T05 (3D 계측 3부작) | 4시간 |
| 4 | `03_papers/` T06~T13 (나머지 8편) | 8시간 |
| 5 | `02_projects/` P1~P5 | 4시간 |
| 6 | `04_qa/` 6종 — 소리 내어 답해 보기 | 6시간 |
| 7 | [05_cheatsheet.md](05_cheatsheet.md) 반복 | 1시간 × N |

**5단계(프로젝트)를 논문 뒤에 두는 이유**: 프로젝트 문서는 논문에서 확인한 정량 결과를 인용한다. 논문을 먼저 읽어야 프로젝트 설명에 숫자를 넣을 수 있다.

---

## 남은 기간별 플랜

### D-14 이상 — 전체 정독

1~7단계를 순서대로. 기초개념에 시간을 아끼지 않는다. 논문의 방법론이 이해되지 않으면 대개 기초개념 쪽에 구멍이 있다.

### D-7 — 논문과 프로젝트 중심

기초개념은 각 문서의 `## 예상 질문` 절만 훑는다. 논문 13편의 0절(30초 요약)·4절(방법론)·7절(결과)을 집중해서 읽고, 프로젝트 5종은 3절(STAR)을 소리 내어 말해 본다.

### D-3 — 질문 뱅크 회전

`04_qa/` 6종을 처음부터 끝까지 소리 내어 답한다. 막히는 질문에 표시하고, 해당 원 문서로 돌아가 그 부분만 다시 읽는다. 특히 [04_기여도·공저자_QA.md](04_qa/04_기여도·공저자_QA.md)의 빈칸은 이 시점까지 반드시 채워 둔다.

### D-1 — 치트시트만

[05_cheatsheet.md](05_cheatsheet.md)를 세 번 읽는다. 새 내용을 넣지 않는다. `## 반드시 외울 숫자`와 `## 답하기 어려운 질문 Top 10`에 시간을 쓴다.

---

## 문서 규약

읽는 도중 마주칠 표기법이다.

### 질문 형식

모든 예상 질문은 아래 형식을 따른다.

```
#### Q001. 질문 내용 🟡

**의도:** 면접관이 이 질문으로 무엇을 확인하려는가

**답변:** 구어체 답변 스크립트 (30초~1분 분량)

**꼬리질문:** 이 답변 뒤에 이어질 가능성이 높은 질문
```

**난이도 표기**

| 기호 | 뜻 | 대응 |
|------|-----|------|
| 🟢 | 기초 | 못 답하면 곤란한 질문. 반사적으로 나와야 한다 |
| 🟡 | 실무 | 경험과 판단을 묻는 질문. 근거를 갖춰 답한다 |
| 🔴 | 압박 | 약점을 찌르는 질문. 방어 논리를 미리 준비한다 |

[06_역질문_리스트.md](04_qa/06_역질문_리스트.md)만 이 형식을 다르게 쓴다. 그쪽은 내가 면접관에게 던지는 질문이라, `**의도:**`가 "이 질문으로 무엇을 알아내려는가", `**답변:**`이 "돌아올 답을 어떻게 해석할 것인가"가 된다.

### 원문과 보충의 구분

논문 문서의 수치·데이터셋·실험 설정은 전부 원문 PDF에서 인용했다. 원문에 없는 값은 쓰지 않았다.

| 표기 | 뜻 |
|------|-----|
| `※ 배경 보충` | 원문에 없지만 이해를 돕기 위해 덧붙인 배경지식. 면접에서 "논문에 그렇게 써 있나요"라는 확인이 들어오면 논문 내용이 아니라고 답해야 하는 부분 |
| `원문에 명시되지 않음` | 원문에서 확인되지 않는 항목. 추측으로 채우지 않았다 |
| `(검색 필요)` | 참고문헌의 DOI/arXiv ID를 확신할 수 없어 식별자를 생략한 것. 제목으로 검색해 확인할 것 |
| `[ 직접 작성 ]` | 본인만 답할 수 있는 자리. 기억을 되살려 직접 채워야 한다 |

`[ 직접 작성 ]` 빈칸은 대부분 각 논문 문서의 9절(기여도 질문 대응)에 있다. **이 빈칸을 채우지 않으면 이 자료의 가장 중요한 부분이 비어 있는 셈이다.** 공저 논문 11편에 대해 "여기서 본인 기여는 무엇입니까"는 거의 반드시 나오는 질문이다.
