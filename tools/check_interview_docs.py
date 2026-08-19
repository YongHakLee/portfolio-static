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
