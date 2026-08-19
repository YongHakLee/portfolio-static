# 면접 준비 자료 (Interview Prep Docs) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 이용학의 논문 13편·프로젝트 4건·국가 R&D 과제·특허를 기초 개념부터 해부하고 320문항 이상의 예상 질문을 담은 면접 학습 문서 32개를 `docs/interview/` 아래에 작성한다.

**Architecture:** 순수 Markdown 문서 세트다. 실행 코드는 검증 스크립트 하나뿐이다. 검증 스크립트가 문서 규약(필수 절, 플레이스홀더 금지, 질문 수, 링크 유효성)을 기계적으로 검사하고, 각 작업은 "검증 실패 확인 → 문서 작성 → 검증 통과 확인 → 커밋" 순서로 진행한다. 문서는 `01_foundations`(토대) → `03_papers`(논문) → `02_projects`(프로젝트) → `04_qa`(질문 뱅크) 순으로 쌓이며, 뒤 문서가 앞 문서를 상대 경로로 참조한다.

**Tech Stack:** Markdown, Python 3 (검증 스크립트), `pdftotext` (poppler-utils, 논문 원문 추출), git

## Global Constraints

- 문서 언어는 한국어. 기술 용어는 한글(영문) 병기 — 예: 배치 정규화(Batch Normalization).
- 논문 문서의 수치·데이터셋·실험 설정은 전부 원문 PDF에서 인용한다. 원문에 없는 값은 쓰지 않는다.
- 배경지식으로 보충한 설명은 `※ 배경 보충` 으로 시작하는 줄에 넣어 원문 내용과 구분한다.
- 원문에서 확인되지 않는 항목은 `원문에 명시되지 않음` 이라고 적는다. 비워 두지 않는다.
- Reference의 DOI/arXiv ID는 확신하는 것만 적는다. 불확실하면 식별자를 생략하고 제목 뒤에 `(검색 필요)` 를 붙인다. 존재하지 않는 링크를 만들지 않는다.
- 특정 지원 기관명(병원·회사 이름)을 문서에 쓰지 않는다. 범용 면접 자료다.
- 최종 파일 수 32개: INDEX 1 + foundations 6 + projects 5 + papers 13 + qa 6 + cheatsheet 1.
- 예상 질문 총합 320문항 이상.
- 수학 깊이는 직관 우선 + 핵심 수식만. 유도 과정은 넣지 않는다.
- 논문 PDF 상대 경로 링크는 `../../../papers/<파일명>.pdf` 형식을 쓴다 (`docs/interview/03_papers/` 기준).

## 문서 규약 (모든 작업이 지킨다)

**질문 형식** — 검증 스크립트가 이 형식으로 문항 수를 센다.

```markdown
#### Q001. 배치 정규화가 학습을 안정시키는 이유가 무엇인가요? 🟡

**의도:** 개념을 외웠는지, 원리를 이해했는지 구분하려는 질문이다.

**답변:** 각 층의 입력 분포가 학습 도중 계속 바뀌면 뒤쪽 층이 매번 새로운
분포에 적응해야 합니다. 배치 정규화는 미니배치 단위로 입력을 평균 0, 분산 1로
맞춰 이 변동을 줄입니다. 덕분에 더 큰 학습률을 쓸 수 있고 초기값에 덜
민감해집니다.

**꼬리질문:** 추론할 때는 미니배치가 없는데 어떻게 정규화합니까?
```

- 번호는 파일 안에서 `Q001` 부터 3자리 연속. 파일이 달라지면 다시 `Q001` 부터 시작한다.
- 난이도 이모지는 🟢(기초) / 🟡(실무) / 🔴(압박) 중 하나를 질문 끝에 붙인다.
- `**의도:**`, `**답변:**`, `**꼬리질문:**` 세 항목은 모두 필수다.

**논문 문서 필수 절** — 아래 12개 제목을 정확히 이 문자열로 쓴다.

```
## 0. 30초 요약
## 1. 서지정보
## 2. 왜 이 연구를 했나
## 3. 사전지식 (A to Z)
## 4. 방법론 단계별 해부
## 5. 핵심 수식
## 6. 실험 세팅
## 7. 결과 읽기
## 8. 한계와 반박 대응
## 9. 기여도 질문 대응
## 10. 예상 질문
## 11. Reference
```

**프로젝트 문서 필수 절**

```
## 0. 30초 요약
## 1. 개요
## 2. 사전지식 (A to Z)
## 3. STAR
## 4. 기술 선택의 근거
## 5. 실패한 시도와 원인
## 6. 다시 한다면
## 7. 예상 질문
## 8. Reference
```

**기초개념 문서 필수 절**

```
## 이 문서를 읽는 법
## 개념 목록
## 내 논문·프로젝트와의 연결
## 예상 질문
## Reference
```

개별 개념은 `### <개념명>` 아래에 `**직관**`, `**정의**`, `**핵심 수식**`(없으면 생략 가능), `**면접 포인트**` 를 둔다.

**기여도 빈칸** — 논문 문서 9절에는 아래 네 줄을 그대로 넣는다. 작성자가 직접 채울 자리이므로 검증 스크립트의 플레이스홀더 검사에서 예외로 둔다.

```markdown
- 내가 직접 한 것: `[ 직접 작성 ]`
- 옆에서 지켜본 것: `[ 직접 작성 ]`
- 논문 작성 후 이해한 것: `[ 직접 작성 ]`
- 이 논문에서 배운 것: `[ 직접 작성 ]`
```

---

## File Structure

| 경로 | 책임 |
|------|------|
| `tools/check_interview_docs.py` | 문서 규약 검증. 파일 존재·필수 절·플레이스홀더·질문 수·링크 검사 |
| `docs/interview/00_INDEX.md` | 전체 지도, 학습 순서, D-day 플랜, 상호 참조표 |
| `docs/interview/01_foundations/01_통계·머신러닝_기초.md` | 회귀·정규화·편향분산·트리앙상블·PLS-DA·평가지표 |
| `docs/interview/01_foundations/02_딥러닝·CNN_기초.md` | 역전파·옵티마이저·BN·백본 계보·전이학습·경량화 |
| `docs/interview/01_foundations/03_비전_검출·분할·키포인트.md` | YOLO·IoU/NMS/mAP·세그멘테이션·준지도·HRNet |
| `docs/interview/01_foundations/04_3D·PointCloud·LiDAR.md` | LiDAR 원리·깊이맵·카메라 파라미터·역투영·정합·B-Rep |
| `docs/interview/01_foundations/05_생성모델_GAN·Diffusion.md` | GAN·pix2pix/CycleGAN·DDPM·조건부 생성·생성 평가지표 |
| `docs/interview/01_foundations/06_강화학습·시계열·기타.md` | MDP/DQN/Replay·시계열 기술지표·블록체인/SBT/IPFS·LLM 기초 |
| `docs/interview/02_projects/P1_모바일LiDAR_3차원계측.md` | 프로젝트 P1 |
| `docs/interview/02_projects/P2_가스배관_센서탐지.md` | 프로젝트 P2 |
| `docs/interview/02_projects/P3_상품추천_멀티모달.md` | 프로젝트 P3 |
| `docs/interview/02_projects/P4_영상기반_미세먼지추정.md` | 프로젝트 P4 |
| `docs/interview/02_projects/P5_국가RnD과제·특허.md` | 국가 R&D 8건 + 특허 2건 |
| `docs/interview/03_papers/T01_상품추천_멀티모달.md` | T8 논문 (제1저자) |
| `docs/interview/03_papers/T02_전후면의류_확산모델.md` | T5 논문 (교신저자) |
| `docs/interview/03_papers/T03_모바일LiDAR_인체계측.md` | T1 논문 |
| `docs/interview/03_papers/T04_의류치수_포인트클라우드.md` | T2 논문 |
| `docs/interview/03_papers/T05_딸기_크기무게추정.md` | T3 논문 |
| `docs/interview/03_papers/T06_NeuroBRep_CAD복원.md` | T4 논문 |
| `docs/interview/03_papers/T07_멀티뷰앙상블_준지도분할.md` | T7 논문 |
| `docs/interview/03_papers/T08_치과영상_GAN생성.md` | T6 논문 |
| `docs/interview/03_papers/T09_미세먼지_디헤이징.md` | T9 논문 |
| `docs/interview/03_papers/T10_강화학습_이중리플레이.md` | T10 논문 |
| `docs/interview/03_papers/T11_헤드앤숄더_투자모델.md` | T11 논문 |
| `docs/interview/03_papers/T12_SBT_분산스토리지.md` | T12 논문 |
| `docs/interview/03_papers/T13_SBT_복구메커니즘.md` | T13 논문 |
| `docs/interview/04_qa/01_기초개념_QA.md` | 기초 개념 질문 80+ |
| `docs/interview/04_qa/02_프로젝트_QA.md` | 프로젝트 질문 80+ |
| `docs/interview/04_qa/03_논문_QA.md` | 논문 질문 150+ (각 논문 파일에서 통합) |
| `docs/interview/04_qa/04_기여도·공저자_QA.md` | 기여도 압박 질문 25+ |
| `docs/interview/04_qa/05_인성·직무·커리어_QA.md` | 인성·직무 질문 40+ |
| `docs/interview/04_qa/06_역질문_리스트.md` | 역질문 20+ |
| `docs/interview/05_cheatsheet.md` | 전날 1시간 압축본 |

파일명의 `T01`~`T13`은 **작성 순서(본인 기여 큰 순)** 를 따르며, 스펙의 논문 ID(T1~T13, 게재 순)와 다르다. 대응표는 Task 1에서 `00_INDEX.md`에 기록한다.

---

## Task 1: 검증 스크립트와 문서 골격

**Files:**
- Create: `tools/check_interview_docs.py`
- Create: `docs/interview/00_INDEX.md`

**Interfaces:**
- Consumes: 없음 (첫 작업)
- Produces: `python3 tools/check_interview_docs.py` — 문서 트리를 검사하고 위반 사항을 stdout에 출력, 위반이 있으면 exit code 1. 이후 모든 작업이 이 명령으로 검증한다.

- [ ] **Step 1: 검증 스크립트를 작성한다 (아직 문서가 없으므로 실패해야 한다)**

`tools/check_interview_docs.py`:

```python
#!/usr/bin/env python3
"""docs/interview/ 문서 세트의 규약을 검사한다.

검사 항목:
  1. 필수 파일 32개가 모두 존재하는가
  2. 각 문서에 필수 절 제목이 모두 있는가
  3. 금지된 플레이스홀더가 남아 있는가
  4. 질문 형식이 규약을 지키는가 / 파일별 최소 문항을 채웠는가
  5. 상대 경로 링크가 실제 파일을 가리키는가
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "interview"

PAPER_SECTIONS = [
    "## 0. 30초 요약",
    "## 1. 서지정보",
    "## 2. 왜 이 연구를 했나",
    "## 3. 사전지식 (A to Z)",
    "## 4. 방법론 단계별 해부",
    "## 5. 핵심 수식",
    "## 6. 실험 세팅",
    "## 7. 결과 읽기",
    "## 8. 한계와 반박 대응",
    "## 9. 기여도 질문 대응",
    "## 10. 예상 질문",
    "## 11. Reference",
]

PROJECT_SECTIONS = [
    "## 0. 30초 요약",
    "## 1. 개요",
    "## 2. 사전지식 (A to Z)",
    "## 3. STAR",
    "## 4. 기술 선택의 근거",
    "## 5. 실패한 시도와 원인",
    "## 6. 다시 한다면",
    "## 7. 예상 질문",
    "## 8. Reference",
]

FOUNDATION_SECTIONS = [
    "## 이 문서를 읽는 법",
    "## 개념 목록",
    "## 내 논문·프로젝트와의 연결",
    "## 예상 질문",
    "## Reference",
]

PAPERS = [
    ("T01_상품추천_멀티모달.md", 10),
    ("T02_전후면의류_확산모델.md", 10),
    ("T03_모바일LiDAR_인체계측.md", 10),
    ("T04_의류치수_포인트클라우드.md", 10),
    ("T05_딸기_크기무게추정.md", 10),
    ("T06_NeuroBRep_CAD복원.md", 10),
    ("T07_멀티뷰앙상블_준지도분할.md", 10),
    ("T08_치과영상_GAN생성.md", 10),
    ("T09_미세먼지_디헤이징.md", 10),
    ("T10_강화학습_이중리플레이.md", 10),
    ("T11_헤드앤숄더_투자모델.md", 10),
    ("T12_SBT_분산스토리지.md", 10),
    ("T13_SBT_복구메커니즘.md", 10),
]

FOUNDATIONS = [
    "01_통계·머신러닝_기초.md",
    "02_딥러닝·CNN_기초.md",
    "03_비전_검출·분할·키포인트.md",
    "04_3D·PointCloud·LiDAR.md",
    "05_생성모델_GAN·Diffusion.md",
    "06_강화학습·시계열·기타.md",
]

PROJECTS = [
    "P1_모바일LiDAR_3차원계측.md",
    "P2_가스배관_센서탐지.md",
    "P3_상품추천_멀티모달.md",
    "P4_영상기반_미세먼지추정.md",
    "P5_국가RnD과제·특허.md",
]

QA_FILES = [
    ("01_기초개념_QA.md", 80),
    ("02_프로젝트_QA.md", 80),
    ("03_논문_QA.md", 150),
    ("04_기여도·공저자_QA.md", 25),
    ("05_인성·직무·커리어_QA.md", 40),
    ("06_역질문_리스트.md", 20),
]

# 문서에 남아 있으면 안 되는 문자열
FORBIDDEN = ["TBD", "TODO", "작성 예정", "추후 작성", "내용 없음", "lorem ipsum"]
# 의도적으로 허용하는 빈칸·불확실 표기
ALLOWED = ["[ 직접 작성 ]", "(검색 필요)", "원문에 명시되지 않음"]

Q_RE = re.compile(r"^#### Q(\d{3})\. (.+?) ([🟢🟡🔴])\s*$")
LINK_RE = re.compile(r"\[[^\]]*\]\((?!https?:)([^)#]+)")


def expected_files():
    yield DOCS / "00_INDEX.md"
    for name in FOUNDATIONS:
        yield DOCS / "01_foundations" / name
    for name in PROJECTS:
        yield DOCS / "02_projects" / name
    for name, _ in PAPERS:
        yield DOCS / "03_papers" / name
    for name, _ in QA_FILES:
        yield DOCS / "04_qa" / name
    yield DOCS / "05_cheatsheet.md"


def check_sections(path, text, required, errors):
    for section in required:
        if section not in text:
            errors.append(f"{path.relative_to(ROOT)}: 필수 절 누락 -> {section}")


def check_questions(path, text, minimum, errors):
    lines = text.splitlines()
    numbers = []
    for i, line in enumerate(lines, start=1):
        if not line.startswith("#### Q"):
            continue
        m = Q_RE.match(line)
        if not m:
            errors.append(f"{path.relative_to(ROOT)}:{i}: 질문 형식 위반 -> {line.strip()}")
            continue
        numbers.append(int(m.group(1)))
        block = "\n".join(lines[i : i + 40])
        for field in ("**의도:**", "**답변:**", "**꼬리질문:**"):
            if field not in block:
                errors.append(
                    f"{path.relative_to(ROOT)}:{i}: {field} 항목 없음 -> Q{m.group(1)}"
                )
    if minimum and len(numbers) < minimum:
        errors.append(
            f"{path.relative_to(ROOT)}: 질문 {len(numbers)}개, 최소 {minimum}개 필요"
        )
    if numbers != list(range(1, len(numbers) + 1)):
        errors.append(f"{path.relative_to(ROOT)}: 질문 번호가 001부터 연속이 아님")
    return len(numbers)


def check_forbidden(path, text, errors):
    scrubbed = text
    for token in ALLOWED:
        scrubbed = scrubbed.replace(token, "")
    lowered = scrubbed.lower()
    for token in FORBIDDEN:
        if token.lower() in lowered:
            errors.append(f"{path.relative_to(ROOT)}: 금지 문자열 발견 -> {token}")


def check_links(path, text, errors):
    for m in LINK_RE.finditer(text):
        target = unquote(m.group(1).strip())
        if not target or target.startswith("mailto:"):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: 깨진 링크 -> {target}")


def main():
    errors = []
    total_questions = 0

    for path in expected_files():
        if not path.exists():
            errors.append(f"{path.relative_to(ROOT)}: 파일 없음")

    for path in expected_files():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        check_forbidden(path, text, errors)
        check_links(path, text, errors)

        parent = path.parent.name
        if parent == "03_papers":
            check_sections(path, text, PAPER_SECTIONS, errors)
            minimum = dict(PAPERS)[path.name]
            total_questions += check_questions(path, text, minimum, errors)
        elif parent == "02_projects":
            check_sections(path, text, PROJECT_SECTIONS, errors)
            total_questions += check_questions(path, text, 0, errors)
        elif parent == "01_foundations":
            check_sections(path, text, FOUNDATION_SECTIONS, errors)
            total_questions += check_questions(path, text, 0, errors)
        elif parent == "04_qa":
            minimum = dict(QA_FILES)[path.name]
            total_questions += check_questions(path, text, minimum, errors)

    qa_total = 0
    for name, _ in QA_FILES:
        p = DOCS / "04_qa" / name
        if p.exists():
            qa_total += len(
                [l for l in p.read_text(encoding="utf-8").splitlines() if Q_RE.match(l)]
            )
    if qa_total < 320:
        errors.append(f"04_qa 질문 총합 {qa_total}개, 최소 320개 필요")

    if errors:
        print(f"검증 실패: {len(errors)}건")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"검증 통과. 04_qa 질문 {qa_total}개, 전체 질문 {total_questions}개.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: 검증 스크립트가 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL (exit 1). 총 33건 — "파일 없음" 32건 + "04_qa 질문 총합 0개, 최소 320개 필요" 1건.

- [ ] **Step 3: 디렉터리와 00_INDEX.md를 만든다**

```bash
cd /mnt/nas4/lyh/github/portfolio-static
mkdir -p docs/interview/01_foundations docs/interview/02_projects docs/interview/03_papers docs/interview/04_qa
```

`docs/interview/00_INDEX.md`에 다음을 담는다:

1. **이 자료의 사용법** — 무엇을 위해 만들었는지, 어떤 순서로 읽는지 3~4문단.
2. **파일 지도** — 위 File Structure 표를 그대로 옮기되, 각 행에 상대 경로 링크를 건다. 아직 없는 파일을 링크하면 Step 4 검증이 실패하므로, **이 단계에서는 링크 없이 경로 문자열만 적고**, Task 13에서 링크로 바꾼다.
3. **논문 파일명 ↔ 스펙 ID ↔ 원문 PDF 대응표** — 아래 표를 그대로 넣는다.

| 문서 | 스펙 ID | 논문 제목 | 게재처·연도 | 저자 위치 |
|------|---------|-----------|-------------|-----------|
| T01 | T8 | Integrated Analytic Methodology Using Visual Image and Meta-Data for Product Recommendation | Quant. Bio-Science 2022 | 제1저자 |
| T02 | T5 | A Two-Stage Diffusion Pipeline for Consistent Front-Back Clothing Generation | Quant. Bio-Science 2025 | 교신저자 |
| T03 | T1 | A Mobile LiDAR-Based Deep Learning Approach for Real-Time 3D Body Measurement | Applied Sciences 2025 | 공저 |
| T04 | T2 | Automatic Measurements of Garment Sizes Using Computer Vision Deep Learning Models and Point Cloud Data | Applied Sciences 2022 | 공저 |
| T05 | T3 | Automated Technology for Strawberry Size Measurement and Weight Prediction Using AI | IEEE Access 2024 | 공저 |
| T06 | T4 | Topology-Constrained NeuroB-Rep: Contact-Aware CAD Reconstruction From 3D Point Clouds | IEEE Access 2026 | 3/4저자 |
| T07 | T7 | A Multi-View Integrated Ensemble for the Background Discrimination of Semi-Supervised Semantic Segmentation | Applied Sciences 2023 | 공저 |
| T08 | T6 | Dental Image Data Generation for Instance Segmentation using Generative Adversarial Networks | Quant. Bio-Science 2023 | 공저 |
| T09 | T9 | Estimation of Particulate Levels Using Deep Dehazing Network and Temporal Prior | Journal of Sensors 2020 | 공저 |
| T10 | T10 | Reinforcement Learning Guided by Double Replay Memory | Journal of Sensors 2020 | 공저 |
| T11 | T11 | An Investment Model Based on a Head-And-Shoulder Pattern with Multiple Moving Average Technical Indicators for Future Markets | Quant. Bio-Science 2022 | 공저 |
| T12 | T12 | Implementation of SoulBound Token Using Economical and Efficient Decentralized File Storage Methods | 정보보호학회논문지 2024 | 공저 |
| T13 | T13 | SoulBound Token Recovery Mechanism and the Application of a Customer-Centric Guardian System | 정보보호학회논문지 2025 | 공저 |

4. **권장 학습 순서** — 기초 6종 → 논문 T01~T13 → 프로젝트 P1~P5 → QA. 각 단계 예상 소요 시간을 적는다.
5. **남은 기간별 플랜** — D-14 / D-7 / D-3 / D-1 각각 무엇을 읽을지. D-1은 `05_cheatsheet.md`만.
6. **문서 규약 요약** — 질문 형식, 난이도 이모지, `※ 배경 보충` 표기의 의미를 독자가 알 수 있게 설명한다.

- [ ] **Step 4: 검증을 다시 돌려 남은 실패가 "파일 없음" 31건뿐인지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL (exit 1). 총 32건 — `00_INDEX.md` 관련 오류는 없고, 나머지 31개 파일의 "파일 없음" 31건 + 질문 총합 부족 1건.

- [ ] **Step 5: 커밋**

```bash
git add tools/check_interview_docs.py docs/interview/00_INDEX.md
git commit -m "docs: add interview prep index and structure checker"
```

---

## Task 2: 기초개념 1·2 (통계·머신러닝 / 딥러닝·CNN)

**Files:**
- Create: `docs/interview/01_foundations/01_통계·머신러닝_기초.md`
- Create: `docs/interview/01_foundations/02_딥러닝·CNN_기초.md`

**Interfaces:**
- Consumes: Task 1의 검증 스크립트, `00_INDEX.md`의 문서 규약
- Produces: 이후 논문·프로젝트 문서 3절에서 `../01_foundations/01_통계·머신러닝_기초.md#<앵커>` 로 참조할 개념 정의. 앵커는 `### <개념명>` 제목에서 생성되므로 개념명을 아래 목록 그대로 쓴다.

- [ ] **Step 1: 검증이 두 파일에 대해 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. `01_통계·머신러닝_기초.md: 파일 없음`, `02_딥러닝·CNN_기초.md: 파일 없음` 포함.

- [ ] **Step 2: `01_통계·머신러닝_기초.md`를 작성한다**

필수 절 5개(`## 이 문서를 읽는 법`, `## 개념 목록`, `## 내 논문·프로젝트와의 연결`, `## 예상 질문`, `## Reference`)를 갖추고, `## 개념 목록` 아래에 다음 개념을 이 이름 그대로 `### ` 제목으로 쓴다.

```
### 지도학습과 비지도학습
### 선형회귀
### 로지스틱 회귀
### 손실함수와 최적화
### 과적합과 편향-분산 트레이드오프
### 정규화 (L1 / L2)
### 교차검증
### 결정트리
### 랜덤 포레스트
### 그래디언트 부스팅과 LightGBM
### 특징 공학과 파생변수
### 차원축소 (PCA)
### PLS와 PLS-DA
### 분류 평가지표 (정확도·정밀도·재현율·F1·AUC)
### 회귀 평가지표 (MAE·RMSE·MAPE·R²)
### 클래스 불균형 다루기
### 통계적 가설검정과 p-value
```

각 개념 아래에 `**직관**`(비유 중심 3~5문장), `**정의**`, `**핵심 수식**`(필요한 것만), `**면접 포인트**`를 둔다. 수식은 유도 없이 결과식만 쓰고 기호를 하나씩 풀이한다.

`## 내 논문·프로젝트와의 연결` 절에는 표를 만든다 — 개념명 / 쓰인 논문·프로젝트 / 어떻게 쓰였는지. 예: 랜덤 포레스트·LightGBM → P2 가스배관, PLS-DA → P4 미세먼지, 회귀 평가지표 → T03/T04/T05 치수 측정.

`## 예상 질문` 절에 문서 규약 형식으로 최소 12문항을 쓴다.

`## Reference` 절에는 각 개념의 학습자료를 쓴다. 한국어 자료를 먼저 두고 영문을 뒤에 둔다. 확신 없는 URL은 쓰지 말고 자료명 + `(검색 필요)` 로 남긴다.

- [ ] **Step 3: `02_딥러닝·CNN_기초.md`를 작성한다**

같은 5개 필수 절을 갖추고, `## 개념 목록` 아래 개념:

```
### 퍼셉트론과 다층 신경망
### 활성함수
### 역전파
### 경사하강법과 옵티마이저
### 배치 정규화
### 드롭아웃과 데이터 증강
### 합성곱 연산
### 풀링과 수용영역
### CNN 백본의 계보 (VGG → ResNet → EfficientNet)
### 잔차 연결
### MobileNet 계열과 경량화
### 전이학습과 파인튜닝
### 학습률 스케줄링
### 온디바이스 추론과 양자화
### 트랜스포머 개요
```

`## 내 논문·프로젝트와의 연결`: MobileNetV3 → T01/P3, 전이학습 → 다수, 온디바이스 추론 → P1/T03, 잔차 연결 → 백본 전반.

`## 예상 질문` 최소 12문항.

- [ ] **Step 4: 검증을 돌려 두 파일의 오류가 사라졌는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL이지만 `01_통계·머신러닝_기초.md`와 `02_딥러닝·CNN_기초.md` 관련 오류는 한 건도 없다. 남은 오류는 아직 만들지 않은 29개 파일의 "파일 없음"과 질문 총합 부족뿐이다.

- [ ] **Step 5: 커밋**

```bash
git add docs/interview/01_foundations/
git commit -m "docs: add statistics/ML and deep learning foundations"
```

---

## Task 3: 기초개념 3·4 (비전 / 3D·PointCloud·LiDAR)

**Files:**
- Create: `docs/interview/01_foundations/03_비전_검출·분할·키포인트.md`
- Create: `docs/interview/01_foundations/04_3D·PointCloud·LiDAR.md`

**Interfaces:**
- Consumes: Task 2가 정의한 CNN 개념 (`02_딥러닝·CNN_기초.md`의 `### 합성곱 연산`, `### CNN 백본의 계보 (VGG → ResNet → EfficientNet)`)
- Produces: T03~T08 논문 문서와 P1 프로젝트 문서가 참조할 검출·분할·키포인트·3D 개념 앵커

- [ ] **Step 1: 검증이 두 파일에 대해 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. 두 파일의 "파일 없음" 포함.

- [ ] **Step 2: `03_비전_검출·분할·키포인트.md`를 작성한다**

필수 절 5개. `## 개념 목록` 아래 개념:

```
### 컴퓨터 비전 과제의 분류
### 객체 검출의 기본 구조
### 앵커 기반과 앵커 프리
### YOLO 계열의 발전
### IoU
### NMS
### mAP
### 시맨틱 분할
### 인스턴스 분할과 파놉틱 분할
### U-Net과 인코더-디코더
### DeepLab과 확장 합성곱
### 준지도 학습과 의사 레이블
### 키포인트 검출과 자세 추정
### 히트맵 회귀
### HRNet의 고해상도 유지
### 이미지 전처리와 데이터 증강
```

`## 내 논문·프로젝트와의 연결`: YOLO → T03/T04/T05, HRNet·히트맵 회귀 → T03/P1, 준지도 분할 → T07, 인스턴스 분할 → T08.

`## 예상 질문` 최소 12문항. IoU와 mAP는 수식과 계산 예시를 넣는다.

- [ ] **Step 3: `04_3D·PointCloud·LiDAR.md`를 작성한다**

필수 절 5개. `## 개념 목록` 아래 개념:

```
### 깊이 정보가 왜 필요한가
### LiDAR와 ToF 센서의 원리
### 모바일 LiDAR의 특성과 한계
### 깊이 맵
### 카메라 내부 파라미터
### 카메라 외부 파라미터와 좌표계
### 2D 픽셀에서 3D 점으로 역투영
### 포인트 클라우드 자료구조
### 다운샘플링 (복셀 그리드)
### 이상치 제거와 노이즈 필터링
### 법선 벡터 추정
### 정합 (ICP)
### 표면 재구성과 메시
### B-Rep과 CAD 표현
### 3D 계측에서의 오차 원인
### 3D 딥러닝 모델 개요 (PointNet 계열)
```

`### 2D 픽셀에서 3D 점으로 역투영` 절에는 핀홀 카메라 모델 역투영식을 쓰고 각 기호(초점거리, 주점, 깊이값)를 풀이한다. 이 개념이 P1과 T03~T05의 핵심이므로 다른 개념보다 두 배 분량으로 쓴다.

`## 내 논문·프로젝트와의 연결`: 역투영 → T03/T04/T05/P1, B-Rep → T06, 노이즈 필터링 → P1, 3D 계측 오차 → P1/특허 2건.

`## 예상 질문` 최소 15문항.

- [ ] **Step 4: 검증을 돌려 두 파일의 오류가 사라졌는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL이지만 `03_비전_검출·분할·키포인트.md`와 `04_3D·PointCloud·LiDAR.md` 관련 오류는 없다.

- [ ] **Step 5: 커밋**

```bash
git add docs/interview/01_foundations/
git commit -m "docs: add vision and 3D/LiDAR foundations"
```

---

## Task 4: 기초개념 5·6 (생성모델 / 강화학습·시계열·블록체인·LLM)

**Files:**
- Create: `docs/interview/01_foundations/05_생성모델_GAN·Diffusion.md`
- Create: `docs/interview/01_foundations/06_강화학습·시계열·기타.md`

**Interfaces:**
- Consumes: Task 2의 `### 손실함수와 최적화`, `### 트랜스포머 개요`
- Produces: T02·T08 논문이 참조할 생성모델 앵커, T10~T13 논문이 참조할 강화학습·시계열·블록체인 앵커

- [ ] **Step 1: 검증이 두 파일에 대해 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. 두 파일의 "파일 없음" 포함.

- [ ] **Step 2: `05_생성모델_GAN·Diffusion.md`를 작성한다**

필수 절 5개. `## 개념 목록` 아래 개념:

```
### 생성모델이란
### GAN의 원리
### GAN의 학습 불안정성과 모드 붕괴
### 조건부 GAN
### pix2pix
### CycleGAN
### StyleGAN 계열
### 확산모델의 직관
### DDPM의 순방향과 역방향 과정
### 노이즈 스케줄
### 잠재 확산모델 (Latent Diffusion)
### 텍스트 조건부 생성과 CLIP
### ControlNet
### LoRA와 파인튜닝
### 인페인팅과 이미지 편집
### 생성 품질 평가 (FID·LPIPS·SSIM·PSNR)
### 합성 데이터로 학습하기
```

`### DDPM의 순방향과 역방향 과정`에는 순방향 노이즈 추가식과 역방향 예측 목표를 쓰고 기호를 풀이한다. 유도는 하지 않는다.

`## 내 논문·프로젝트와의 연결`: 확산모델·ControlNet·LoRA → T02, GAN·합성 데이터 → T08, 평가지표 → T02/T08.

`## 예상 질문` 최소 15문항. "GAN 대신 확산모델을 쓰는 이유"는 반드시 포함한다.

- [ ] **Step 3: `06_강화학습·시계열·기타.md`를 작성한다**

필수 절 5개. `## 개념 목록` 아래 개념:

```
### 강화학습의 구성 요소
### 마르코프 결정 과정
### 가치함수와 벨만 방정식
### Q-learning
### DQN과 타깃 네트워크
### 경험 리플레이
### 우선순위 경험 리플레이
### 탐험과 활용
### 시계열 데이터의 특성
### 이동평균과 기술적 지표
### 차트 패턴 (헤드앤숄더)
### 백테스팅과 과최적화
### 블록체인 기초
### 스마트 컨트랙트와 토큰 표준
### NFT와 SoulBound Token
### 분산 파일 저장 (IPFS·아르위브)
### 키 분실과 소셜 리커버리
### LLM 기초와 트랜스포머 디코더
### 프롬프팅과 Chain-of-Thought
### Instruction Tuning
```

마지막 세 개념(LLM)은 T02 교신저자 논문이 Llama3-Instruct에 CoT와 instruction tuning을 결합했기 때문에 넣는다. 이 배경을 절 도입부에 명시한다.

`## 내 논문·프로젝트와의 연결`: DQN·경험 리플레이 → T10, 기술적 지표·헤드앤숄더 → T11, SBT·IPFS·소셜 리커버리 → T12/T13, LLM·CoT → T02.

`## 예상 질문` 최소 15문항.

- [ ] **Step 4: 검증을 돌려 foundations 6개 파일 전체가 통과하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL이지만 `01_foundations/` 아래 6개 파일 관련 오류가 한 건도 없다. 남은 오류는 `02_projects`, `03_papers`, `04_qa`, `05_cheatsheet.md` 관련뿐이다.

- [ ] **Step 5: 커밋**

```bash
git add docs/interview/01_foundations/
git commit -m "docs: add generative model and RL/timeseries/blockchain/LLM foundations"
```

---

## Task 5: 논문 T01·T02 (제1저자·교신저자)

**Files:**
- Create: `docs/interview/03_papers/T01_상품추천_멀티모달.md`
- Create: `docs/interview/03_papers/T02_전후면의류_확산모델.md`

**Interfaces:**
- Consumes: `01_foundations/02_딥러닝·CNN_기초.md`(MobileNet·전이학습), `01_foundations/05_생성모델_GAN·Diffusion.md`(확산모델·ControlNet·LoRA), `01_foundations/06_강화학습·시계열·기타.md`(LLM·CoT)
- Produces: `04_qa/03_논문_QA.md`가 통합할 논문 질문 20문항 이상

- [ ] **Step 1: 검증이 두 파일에 대해 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. 두 파일의 "파일 없음" 포함.

- [ ] **Step 2: 원문 두 편을 전문 추출해 읽는다**

```bash
cd /mnt/nas4/lyh/github/portfolio-static/papers
pdftotext "Integrated Analytic Methodology Using Visual Image and Meta-Data for Product Recommendation.pdf" -
pdftotext "A Two-Stage Diffusion Pipeline for Consistent Front-Back Clothing Generation.pdf" -
```

Expected: 각각 약 4,000단어 / 28,800단어의 텍스트가 출력된다. 표와 수식은 줄바꿈이 깨져 나오므로, 수치를 옮길 때 원문 페이지 번호를 확인한다.

- [ ] **Step 3: 두 논문 문서를 필수 절 12개 형식으로 작성한다**

각 문서는 File Structure의 논문 문서 필수 절을 정확한 문자열로 갖춘다.

T01(제1저자)에서 특히 다룰 것: 이미지 특징과 텍스트 메타데이터를 각각 어떻게 벡터화했는지, 두 특징의 결합 방식, 한국어·영어 혼합 데이터를 언어별 분리와 통합으로 나눠 비교한 실험, 관계 모델로 추천을 만드는 구조. 제1저자이므로 9절은 빈칸 프레임 대신 "이 논문은 본인이 주도했다"는 전제로 연구 동기·설계 판단·직접 수행한 실험을 서술할 수 있는 자리를 만든다. 단, 사실을 지어내지 말고 원문에서 확인되는 내용만 쓰고 개인 회고가 필요한 부분은 `[ 직접 작성 ]` 빈칸을 둔다.

T02(교신저자)에서 특히 다룰 것: Llama3-Instruct + CoT + instruction tuning으로 텍스트 설명을 만드는 1단계, flux 기반 확산으로 이미지를 만드는 2단계, 전면과 후면의 속성 일관성을 어떻게 유지했는지, VTON 데이터셋의 기존 한계. 교신저자의 역할(연구 방향 설정·최종 책임)을 9절에서 설명할 수 있게 구성한다.

11절 Reference에는 원문 PDF 링크를 상대 경로로 건다:

```markdown
- 원문: [Integrated Analytic Methodology Using Visual Image and Meta-Data for Product Recommendation](../../../papers/Integrated%20Analytic%20Methodology%20Using%20Visual%20Image%20and%20Meta-Data%20for%20Product%20Recommendation.pdf) — DOI: 10.22283/qbs.2022.41.1.27
- 원문: [A Two-Stage Diffusion Pipeline for Consistent Front-Back Clothing Generation](../../../papers/A%20Two-Stage%20Diffusion%20Pipeline%20for%20Consistent%20Front-Back%20Clothing%20Generation.pdf) — DOI: 10.22283/qbs.2025.44.1.9
```

10절 예상 질문은 각 문서 최소 12문항.

- [ ] **Step 4: 검증을 돌려 두 파일의 오류가 사라졌는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL이지만 `T01_상품추천_멀티모달.md`와 `T02_전후면의류_확산모델.md` 관련 오류는 없다. 특히 "깨진 링크" 오류가 없어야 한다 (PDF 경로 확인).

- [ ] **Step 5: 커밋**

```bash
git add docs/interview/03_papers/
git commit -m "docs: add paper deep-dives for first-author and corresponding-author papers"
```

---

## Task 6: 논문 T03·T04·T05 (3D 계측 3부작)

**Files:**
- Create: `docs/interview/03_papers/T03_모바일LiDAR_인체계측.md`
- Create: `docs/interview/03_papers/T04_의류치수_포인트클라우드.md`
- Create: `docs/interview/03_papers/T05_딸기_크기무게추정.md`

**Interfaces:**
- Consumes: `01_foundations/03_비전_검출·분할·키포인트.md`(YOLO·HRNet·히트맵), `01_foundations/04_3D·PointCloud·LiDAR.md`(역투영·깊이맵·노이즈 필터링)
- Produces: P1 프로젝트 문서가 인용할 3D 계측 파이프라인 설명과 정량 결과

- [ ] **Step 1: 검증이 세 파일에 대해 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. 세 파일의 "파일 없음" 포함.

- [ ] **Step 2: 원문 세 편을 전문 추출해 읽는다**

```bash
cd /mnt/nas4/lyh/github/portfolio-static/papers
pdftotext "A Mobile LiDAR-Based Deep Learning Approach for Real-Time 3D Body Measurement.pdf" -
pdftotext "Automatic Measurements of Garment Sizes Using Computer Vision Deep Learning Models and Point Cloud Data.pdf" -
pdftotext "Automated Technology for Strawberry Size Measurement and Weight Prediction Using AI.pdf" -
```

Expected: 약 11,700 / 6,600 / 8,500단어.

- [ ] **Step 3: 세 논문 문서를 작성한다**

세 편은 같은 계보의 연구이므로 4절(방법론 해부)에서 **공통 파이프라인과 각 논문의 차이**를 드러내는 것이 중요하다. 각 문서 4절 끝에 "세 논문의 차이" 표를 동일하게 넣는다 — 대상(인체/의류/딸기), 검출 모델, 키포인트 정의 방식, 깊이 활용 방식, 추정 대상(길이/둘레/무게), 평가 방식.

특히 다룰 것:
- T03: 2D 키포인트가 3D 경계와 어긋나는 문제를 깊이 맵 경계선으로 보정한 방법, 실시간 동작을 위한 연산 절감, 인체 계측 항목 정의.
- T04: 의류를 펼쳐 놓고 재는 상황의 제약, 포인트 클라우드에서 치수 기준점을 잡는 방법, 참조물 없는 측정의 정확도.
- T05: 크기에서 무게로 가는 회귀식, 딸기라는 비정형 대상의 특성, 농업 현장 적용 조건.

6절 실험 세팅에는 데이터 수집 방법(촬영 기기·개체 수·촬영 조건)과 오차 지표(MAE/MAPE 등)를 원문 수치 그대로 옮긴다. 7절에는 주요 표의 숫자와 그 해석을 쓴다.

11절 Reference 원문 링크:

```markdown
- 원문: [A Mobile LiDAR-Based Deep Learning Approach for Real-Time 3D Body Measurement](../../../papers/A%20Mobile%20LiDAR-Based%20Deep%20Learning%20Approach%20for%20Real-Time%203D%20Body%20Measurement.pdf)
- 원문: [Automatic Measurements of Garment Sizes Using Computer Vision Deep Learning Models and Point Cloud Data](../../../papers/Automatic%20Measurements%20of%20Garment%20Sizes%20Using%20Computer%20Vision%20Deep%20Learning%20Models%20and%20Point%20Cloud%20Data.pdf)
- 원문: [Automated Technology for Strawberry Size Measurement and Weight Prediction Using AI](../../../papers/Automated%20Technology%20for%20Strawberry%20Size%20Measurement%20and%20Weight%20Prediction%20Using%20AI.pdf)
```

각 문서 10절 최소 12문항.

- [ ] **Step 4: 검증을 돌려 세 파일의 오류가 사라졌는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL이지만 T03·T04·T05 관련 오류는 없다.

- [ ] **Step 5: 커밋**

```bash
git add docs/interview/03_papers/
git commit -m "docs: add paper deep-dives for 3D measurement trilogy"
```

---

## Task 7: 논문 T06·T07·T08 (CAD 복원 / 준지도 분할 / GAN 데이터 생성)

**Files:**
- Create: `docs/interview/03_papers/T06_NeuroBRep_CAD복원.md`
- Create: `docs/interview/03_papers/T07_멀티뷰앙상블_준지도분할.md`
- Create: `docs/interview/03_papers/T08_치과영상_GAN생성.md`

**Interfaces:**
- Consumes: `01_foundations/04_3D·PointCloud·LiDAR.md`(B-Rep·표면 재구성), `01_foundations/03_비전_검출·분할·키포인트.md`(준지도·인스턴스 분할), `01_foundations/05_생성모델_GAN·Diffusion.md`(GAN·합성 데이터)
- Produces: 세 논문의 예상 질문 36문항 이상

- [ ] **Step 1: 검증이 세 파일에 대해 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. 세 파일의 "파일 없음" 포함.

- [ ] **Step 2: 원문 세 편을 전문 추출해 읽는다**

```bash
cd /mnt/nas4/lyh/github/portfolio-static/papers
pdftotext "Topology-Constrained NeuroB-Rep, Contact-Aware CAD Reconstruction From 3-D Point Clouds.pdf" -
pdftotext "A Multi-View Integrated Ensemble for the Background Discrimination of Semi-Supervised Semantic Segmentation.pdf" -
pdftotext "Dental Image Data Generation for Instance Segmentation using Generative Adversarial Networks.pdf" -
```

Expected: 약 11,300 / 7,700 / 7,300단어.

- [ ] **Step 3: 세 논문 문서를 작성한다**

특히 다룰 것:
- T06: 위상 제약(topology constraint)이 무엇이고 왜 필요한가, 접촉 인식(contact-aware)이 해결하는 문제, watertight·manufacturable이라는 요구조건의 의미, 포인트 클라우드에서 B-Rep으로 가는 단계. 저자 위치는 4인 중 3저자이고 교신저자는 양성민이다 — 1절 서지정보에 정확히 적는다. 2026년 IEEE Access 게재이고 DOI는 10.1109/ACCESS.2026.3719250이다.
- T07: 준지도 시맨틱 분할에서 배경(background)을 구분하는 것이 왜 어려운가, 멀티뷰 앙상블의 구성, 의사 레이블의 신뢰도 문제.
- T08: 치과 영상 데이터가 부족한 이유(개인정보·라벨링 비용), GAN으로 생성한 데이터가 인스턴스 분할 성능에 기여하는지 검증한 방법, 합성 데이터의 함정.

각 문서 10절 최소 12문항. T06은 3저자 공저이므로 9절 기여도 프레임을 충실히 채운다.

- [ ] **Step 4: 검증을 돌려 세 파일의 오류가 사라졌는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL이지만 T06·T07·T08 관련 오류는 없다.

- [ ] **Step 5: 커밋**

```bash
git add docs/interview/03_papers/
git commit -m "docs: add paper deep-dives for CAD reconstruction, semi-supervised segmentation, GAN data generation"
```

---

## Task 8: 논문 T09·T10·T11 (미세먼지 / 강화학습 / 투자모델)

**Files:**
- Create: `docs/interview/03_papers/T09_미세먼지_디헤이징.md`
- Create: `docs/interview/03_papers/T10_강화학습_이중리플레이.md`
- Create: `docs/interview/03_papers/T11_헤드앤숄더_투자모델.md`

**Interfaces:**
- Consumes: `01_foundations/06_강화학습·시계열·기타.md`(DQN·경험 리플레이·기술적 지표), `01_foundations/01_통계·머신러닝_기초.md`(PLS-DA)
- Produces: P4 프로젝트 문서가 인용할 미세먼지 추정 방법론

- [ ] **Step 1: 검증이 세 파일에 대해 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. 세 파일의 "파일 없음" 포함.

- [ ] **Step 2: 원문 세 편을 전문 추출해 읽는다**

```bash
cd /mnt/nas4/lyh/github/portfolio-static/papers
pdftotext "Estimation of Particulate Levels Using Deep Dehazing Network and Temporal Prior.pdf" -
pdftotext "Reinforcement Learning Guided by Double Replay Memory.pdf" -
pdftotext "An Investment Model Based on a Head-And-Shoulder Pattern with Multiple Moving Average Technical Indicators for Future Markets.pdf" -
```

Expected: 약 6,100 / 5,300 / 6,600단어.

- [ ] **Step 3: 세 논문 문서를 작성한다**

특히 다룰 것:
- T09: 디헤이징 네트워크가 왜 미세먼지 추정에 쓰이는가(대기 산란 모델과 투과율), temporal prior가 무엇이고 단일 이미지 방식 대비 무엇이 나아지는가, P4 프로젝트와의 관계.
- T10: 경험 리플레이 하나를 둘로 나눈 이유(중요한 전이 vs 새로운 전이), 우선순위 리플레이와의 차이, 실험 환경과 baseline. 저자 목록에 Yonghak Lee가 4번째로 들어가 있다 — 1절에 정확히 적는다.
- T11: 헤드앤숄더 패턴을 어떻게 수치적으로 정의했는가, 다중 이동평균과의 결합, 백테스팅 설계와 과최적화 위험.

각 문서 10절 최소 12문항.

- [ ] **Step 4: 검증을 돌려 세 파일의 오류가 사라졌는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL이지만 T09·T10·T11 관련 오류는 없다.

- [ ] **Step 5: 커밋**

```bash
git add docs/interview/03_papers/
git commit -m "docs: add paper deep-dives for dehazing, double replay memory, investment model"
```

---

## Task 9: 논문 T12·T13 (SoulBound Token 2편)

**Files:**
- Create: `docs/interview/03_papers/T12_SBT_분산스토리지.md`
- Create: `docs/interview/03_papers/T13_SBT_복구메커니즘.md`

**Interfaces:**
- Consumes: `01_foundations/06_강화학습·시계열·기타.md`(블록체인·SBT·IPFS·소셜 리커버리)
- Produces: 두 논문의 예상 질문 24문항 이상

- [ ] **Step 1: 검증이 두 파일에 대해 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. 두 파일의 "파일 없음" 포함.

- [ ] **Step 2: 원문 두 편을 전문 추출해 읽는다**

```bash
cd /mnt/nas4/lyh/github/portfolio-static/papers
pdftotext "Implementation of SoulBound Token Using Economical and Efficient Decentralized File Storage Methods.pdf" -
pdftotext "SoulBound Token Recovery Mechanism and the Application of a Customer-Centric Guardian System.pdf" -
```

Expected: 약 4,900 / 4,000단어. 한국어 논문일 수 있으므로 추출 결과의 언어를 확인하고, 한국어면 원문 표현을 그대로 인용한다.

- [ ] **Step 3: 두 논문 문서를 작성한다**

이 두 편은 다른 11편과 도메인이 완전히 다르다. 면접에서 "왜 블록체인 논문도 있나요"라는 질문이 반드시 나오므로, 2절에 연구 맥락(어떤 과제·연구실 협업으로 참여했는지)을 쓰고 8절에 이 질문에 대한 답변 논리를 넣는다.

특히 다룰 것:
- T12: SBT가 일반 NFT와 다른 점(양도 불가), 온체인 저장 비용 문제, IPFS 등 분산 스토리지로 비용을 낮춘 방식과 그 트레이드오프(가용성·영속성).
- T13: 지갑 키를 잃으면 SBT를 되찾을 수 없는 문제, 가디언 시스템의 구조, 고객 중심(customer-centric)이라는 설계 원칙이 의미하는 것, 보안상 새로 생기는 위험.

각 문서 10절 최소 12문항.

- [ ] **Step 4: 검증을 돌려 03_papers 13개 파일 전체가 통과하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL이지만 `03_papers/` 아래 13개 파일 관련 오류가 한 건도 없다. 남은 오류는 `02_projects`, `04_qa`, `05_cheatsheet.md`뿐이다.

- [ ] **Step 5: 커밋**

```bash
git add docs/interview/03_papers/
git commit -m "docs: add paper deep-dives for SoulBound Token papers"
```

---

## Task 10: 프로젝트 문서 5종

**Files:**
- Create: `docs/interview/02_projects/P1_모바일LiDAR_3차원계측.md`
- Create: `docs/interview/02_projects/P2_가스배관_센서탐지.md`
- Create: `docs/interview/02_projects/P3_상품추천_멀티모달.md`
- Create: `docs/interview/02_projects/P4_영상기반_미세먼지추정.md`
- Create: `docs/interview/02_projects/P5_국가RnD과제·특허.md`
- Read: `asan_hospital/career_statement.html`, `asan_hospital/cover_letter.md`

**Interfaces:**
- Consumes: Task 5~9의 논문 문서 (P1↔T03/T04/T05, P3↔T01, P4↔T09), `01_foundations/` 전체
- Produces: `04_qa/02_프로젝트_QA.md`가 통합할 프로젝트 질문 80문항의 근거

- [ ] **Step 1: 검증이 다섯 파일에 대해 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. 다섯 파일의 "파일 없음" 포함.

- [ ] **Step 2: 경력기술서와 자기소개서에서 사실을 확인한다**

```bash
cd /mnt/nas4/lyh/github/portfolio-static
python3 -c "
import re
s=open('asan_hospital/career_statement.html',encoding='utf-8').read()
s=re.sub(r'<(style|script)[^>]*>.*?</\1>','',s,flags=re.S)
s=re.sub(r'<[^>]+>',' ',s)
print('\n'.join(l.strip() for l in s.split('\n') if l.strip()))
"
cat asan_hospital/cover_letter.md
```

Expected: 프로젝트 4건의 기간·역할·기술 스택, 국가 R&D 8건 목록, 특허 2건 정보가 출력된다. 문서에 쓰는 모든 날짜·기간·기술명은 여기서 옮긴다.

- [ ] **Step 3: 프로젝트 문서 5종을 작성한다**

필수 절 9개(`## 0. 30초 요약` ~ `## 8. Reference`)를 정확한 문자열로 갖춘다.

`## 3. STAR` 절은 아래 네 소제목을 반드시 포함한다:

```markdown
### 상황 (Situation)
### 과제 (Task)
### 행동 (Action)
### 결과 (Result)
```

프로젝트별로 강조할 것:
- P1: 참조물 없는 측정이라는 요구, 2D 키포인트와 3D 경계 불일치 문제, 실시간 제약, 대상(의류·농산물·인체)이 달라도 같은 구조를 쓴 이유. 관련 논문 T03/T04/T05와 특허 2건으로 링크한다.
- P2: 다층 신경망이 실패한 원인(입력 크기 고정 제약)과 트리 모델로 전환한 판단, 파생변수 설계(분산·최대-최소 차이·행간 변화량), 접합부→만곡부 단계적 문제 분할, 후처리로 구간 경계 보정, 패키징. 이 프로젝트는 논문이 없으므로 8절 Reference는 관련 기법의 외부 자료로 채운다.
- P3: 이미지·텍스트 결합, 모바일 연산 제약 때문에 경량 백본을 쓴 판단, 한국어·영어 혼합 데이터 처리. T01로 링크한다.
- P4: 국가 측정망의 한계, 단일 이미지 대신 연속 프레임을 쓴 이유, 프레임 간 광도 변화 수치화, 이동평균·PLS-DA, 라즈베리 파이 실시간 제약, 실내·실외 검증. T09로 링크한다.
- P5: 국가 R&D 과제 8건을 각각 3~5문장으로 (과제명·기간·본인 역할·산출물), 특허 2건은 등록/출원 상태·출원번호·공동발명자 여부와 청구 요지를 쓴다. 특허 2건은 P1과 직접 이어지므로 상호 링크한다.

각 문서 7절 예상 질문 최소 15문항. P2는 "실패에서 배운 것"을 묻기 좋은 소재이므로 압박 질문(🔴) 비중을 높인다.

- [ ] **Step 4: 검증을 돌려 다섯 파일의 오류가 사라졌는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL이지만 `02_projects/` 아래 5개 파일 관련 오류가 없다. 남은 오류는 `04_qa` 6개 파일과 `05_cheatsheet.md`뿐이다.

- [ ] **Step 5: 커밋**

```bash
git add docs/interview/02_projects/
git commit -m "docs: add project deep-dives and national R&D/patent summary"
```

---

## Task 11: 질문 뱅크 1 (기초개념·프로젝트·논문)

**Files:**
- Create: `docs/interview/04_qa/01_기초개념_QA.md`
- Create: `docs/interview/04_qa/02_프로젝트_QA.md`
- Create: `docs/interview/04_qa/03_논문_QA.md`

**Interfaces:**
- Consumes: Task 2~10이 만든 모든 문서의 예상 질문 절
- Produces: 검증 스크립트가 요구하는 최소 문항 — 01은 80, 02는 80, 03은 150

- [ ] **Step 1: 검증이 세 파일에 대해 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. 세 파일의 "파일 없음"과 `04_qa 질문 총합 0개, 최소 320개 필요` 포함.

- [ ] **Step 2: 기존 문서의 질문을 모아 현재 개수를 센다**

```bash
cd /mnt/nas4/lyh/github/portfolio-static
grep -rc "^#### Q" docs/interview/01_foundations docs/interview/02_projects docs/interview/03_papers
```

Expected: foundations 6개 파일 합 80문항 이상, projects 5개 파일 합 75문항 이상, papers 13개 파일 합 156문항 이상이 나온다. 부족하면 해당 문서에 질문을 보충한 뒤 진행한다.

- [ ] **Step 3: 세 개의 통합 질문 뱅크를 작성한다**

각 파일은 `# 제목` 다음에 `## 사용법` 절을 두고, 이어서 주제별 `## ` 절 안에 질문을 넣는다. 질문 번호는 파일 안에서 `Q001`부터 연속이어야 한다 (검증 스크립트가 확인한다).

- `01_기초개념_QA.md` — 80문항 이상. 주제 절: 통계·머신러닝 / 딥러닝·CNN / 비전 / 3D·LiDAR / 생성모델 / 강화학습·시계열·블록체인·LLM. foundations 문서의 질문을 옮기되, 옮기는 과정에서 답변을 구어체로 다듬고 꼬리질문을 추가한다.
- `02_프로젝트_QA.md` — 80문항 이상. 주제 절: P1 / P2 / P3 / P4 / P5 / 프로젝트 공통(재현성·협업·일정·데이터 품질). 프로젝트 문서의 질문 75문항에 공통 질문을 더해 80을 넘긴다.
- `03_논문_QA.md` — 150문항 이상. 주제 절: T01 ~ T13 각각. 논문 문서의 질문을 그대로 옮기고, 부족하면 논문 간 비교 질문("T03과 T04의 차이는", "왜 도메인이 이렇게 다양한가")을 추가한다.

각 질문 뒤에 원 문서로 돌아가는 링크를 한 줄 붙인다:

```markdown
**참조:** [T03 모바일 LiDAR 인체계측](../03_papers/T03_모바일LiDAR_인체계측.md)
```

- [ ] **Step 4: 검증을 돌려 세 파일의 형식 오류가 없는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL이지만 `01_기초개념_QA.md`·`02_프로젝트_QA.md`·`03_논문_QA.md`의 형식·문항수 오류가 없다. 남은 오류는 `04_qa` 나머지 3개 파일, `05_cheatsheet.md`, 그리고 질문 총합 부족(310개 수준)뿐이다.

- [ ] **Step 5: 커밋**

```bash
git add docs/interview/04_qa/
git commit -m "docs: add QA banks for foundations, projects, papers"
```

---

## Task 12: 질문 뱅크 2 (기여도·인성·역질문)

**Files:**
- Create: `docs/interview/04_qa/04_기여도·공저자_QA.md`
- Create: `docs/interview/04_qa/05_인성·직무·커리어_QA.md`
- Create: `docs/interview/04_qa/06_역질문_리스트.md`
- Read: `asan_hospital/cover_letter.md`

**Interfaces:**
- Consumes: Task 5~9 논문 문서의 9절(기여도 프레임), `asan_hospital/cover_letter.md`
- Produces: `04_qa` 질문 총합 320개 돌파 — 검증 스크립트의 마지막 수치 조건

- [ ] **Step 1: 검증이 세 파일에 대해 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. 세 파일의 "파일 없음"과 질문 총합 부족 포함.

- [ ] **Step 2: 세 파일을 작성한다**

`04_기여도·공저자_QA.md` — 25문항 이상. 다뤄야 할 질문 유형:
- 논문 13편 중 제1저자가 1편인 이유
- 특정 공저 논문의 본인 기여 (T06·T10·T12 등 도메인이 먼 논문 위주)
- 교신저자로서 한 일
- 공저자 논문의 내용을 지금 설명할 수 있는지
- 연구실 관행과 저자 순서에 대한 견해

답변 전략의 원칙을 파일 상단 `## 답변 원칙` 절에 명시한다: 기여를 부풀리지 않는다, 모르는 것은 모른다고 말하되 지금 이해한 만큼은 설명한다, 자신이 실제로 한 부분을 구체적인 행위로 말한다(예: "데이터 수집과 전처리를 맡았고 실험 표 3의 재현을 담당했습니다"). 실제 기여 내용은 `[ 직접 작성 ]` 빈칸으로 둔다.

`05_인성·직무·커리어_QA.md` — 40문항 이상. 자기소개서(`cover_letter.md`)의 서사를 근거로 답변을 만든다. 다뤄야 할 것: 자기소개, 지원 동기(기관 무관 범용 틀), 이직 사유, 2023.03–2026.06 재직 기간, 박사 과정과 직장 병행, 도메인이 계속 바뀐 이력을 강점으로 설명하기, 실패 경험(P2가 좋은 소재), 갈등 상황, 협업 방식, 새 도메인 학습 방법, 5년 후 계획, 연봉·처우, 마지막 한마디.

`06_역질문_리스트.md` — 20문항 이상. 연구직용과 실무직용으로 절을 나눈다. 질문 형식은 같은 규약을 쓰되, `**의도:**`는 "이 질문으로 무엇을 알아내려는가", `**답변:**`은 "돌아올 답을 어떻게 해석할 것인가", `**꼬리질문:**`은 후속 질문으로 채운다. 파일 상단에 이 용법 차이를 `## 사용법` 절로 명시한다.

- [ ] **Step 3: 검증을 돌려 04_qa 전체와 질문 총합을 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL이지만 `04_qa/` 관련 오류가 한 건도 없고 질문 총합 오류도 사라진다. 남은 오류는 `05_cheatsheet.md: 파일 없음` 한 건뿐이다.

- [ ] **Step 4: 총 문항 수를 눈으로 확인한다**

```bash
grep -rc "^#### Q" docs/interview/04_qa/ | awk -F: '{s+=$2; print} END {print "합계:", s}'
```

Expected: 합계 320 이상.

- [ ] **Step 5: 커밋**

```bash
git add docs/interview/04_qa/
git commit -m "docs: add QA banks for contribution, personality, reverse questions"
```

---

## Task 13: 치트시트와 INDEX 링크 완성

**Files:**
- Create: `docs/interview/05_cheatsheet.md`
- Modify: `docs/interview/00_INDEX.md` (파일 지도의 경로 문자열을 상대 경로 링크로 교체)

**Interfaces:**
- Consumes: Task 1~12이 만든 31개 문서 전체
- Produces: 검증 스크립트 전체 통과 (exit 0)

- [ ] **Step 1: 검증이 마지막 한 건으로 실패하는지 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: FAIL. `docs/interview/05_cheatsheet.md: 파일 없음` 한 건만 출력된다.

- [ ] **Step 2: `05_cheatsheet.md`를 작성한다**

면접 전날 1시간 안에 훑는 압축본이다. 다음 절을 둔다:

```
## 논문 13편 한 줄 요약
## 프로젝트 4건 30초 스크립트
## 반드시 외울 숫자
## 자주 헷갈리는 개념 구분
## 답하기 어려운 질문 Top 10
## 면접 직전 체크리스트
```

- `## 논문 13편 한 줄 요약`: 표로. 문서 / 한 줄 요약 / 본인 위치 / 링크.
- `## 프로젝트 4건 30초 스크립트`: 그대로 읽으면 30초가 되는 구어체 문단 4개.
- `## 반드시 외울 숫자`: 논문의 핵심 성능 지표, 데이터셋 규모, 경력 연차, 논문·특허·과제 건수. 원문에서 확인된 값만.
- `## 자주 헷갈리는 개념 구분`: 표로. 시맨틱 vs 인스턴스 분할, GAN vs 확산모델, 정밀도 vs 재현율, MAE vs RMSE, L1 vs L2 정규화 등 최소 10쌍.
- `## 답하기 어려운 질문 Top 10`: 질문과 한 문장 대응 요지만. 상세 답변은 `04_qa/`로 링크.
- `## 면접 직전 체크리스트`: 실무적인 준비 항목.

- [ ] **Step 3: `00_INDEX.md`의 파일 지도를 링크로 바꾼다**

Task 1에서 경로 문자열로만 적어 둔 파일 지도 표의 각 경로를 상대 경로 링크로 교체한다. 예:

```markdown
| [01_통계·머신러닝_기초.md](01_foundations/01_통계·머신러닝_기초.md) | 회귀·정규화·편향분산·트리앙상블·PLS-DA·평가지표 |
```

파일명에 `·` 같은 문자가 들어가므로, 링크가 깨지지 않는지 Step 4에서 검증 스크립트로 확인한다.

- [ ] **Step 4: 검증 전체 통과를 확인한다**

Run: `python3 tools/check_interview_docs.py`
Expected: PASS (exit 0). `검증 통과. 04_qa 질문 NNN개, 전체 질문 NNN개.` 출력.

- [ ] **Step 5: 파일 수를 확인한다**

```bash
find docs/interview -name "*.md" | wc -l
```

Expected: `32`

- [ ] **Step 6: 커밋**

```bash
git add docs/interview/
git commit -m "docs: add interview cheatsheet and complete index links"
```

---

## 완료 조건 체크리스트

- [ ] `python3 tools/check_interview_docs.py` 가 exit 0으로 통과한다
- [ ] `find docs/interview -name "*.md" | wc -l` 가 32를 출력한다
- [ ] `04_qa/` 질문 총합이 320개 이상이다
- [ ] 논문 13편 문서에 원문 기반 수치가 들어가 있고, 확인 불가 항목은 `원문에 명시되지 않음`으로 표기돼 있다
- [ ] Reference에 지어낸 DOI/arXiv ID가 없다 (불확실한 것은 `(검색 필요)` 표기)
- [ ] 문서 어디에도 특정 지원 기관명이 없다 — `grep -ri "아산\|병원" docs/interview/` 결과가 비어 있다
