# HappyHome Backend

행복주택 API를 활용한 주택 정보 조회 및 공고문 PDF 다운로드 서비스

## 기능

- 행복주택 공고 목록 조회 (경기도 지역)
- 공고문 PDF 자동 다운로드
- 중복 공고 제외 처리
- 상세 정보 표시 (임대료, 보증금, 위치 등)

## 기술 스택

- Python 3.13
- requests
- python-dotenv
- playwright
- beautifulsoup4
- urllib3

## 설치 방법

1. 저장소 클론

```bash
git clone https://github.com/Fine-Tuner/HappyHome_BE.git
cd HappyHome_BE
```

2. 가상환경 생성 및 활성화

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는
.\venv\Scripts\activate  # Windows
```

3. 의존성 설치

```bash
pip install -r requirements.txt
playwright install chromium  # Playwright 브라우저 설치
```

4. 환경 변수 설정

```bash
# .env 파일 생성
cp .env.example .env
# .env 파일을 열고 API 키를 설정
```

## 사용 방법

```bash
python3 api_client.py
```

실행하면 다음과 같은 작업이 수행됩니다:
1. 경기도 지역의 행복주택 공고 목록을 조회합니다.
2. 각 공고의 상세 정보를 출력합니다.
3. 공고문 PDF를 자동으로 다운로드합니다 (downloads 디렉토리에 저장).
4. 중복된 공고는 자동으로 제외됩니다.

## API 문서

### 행복주택 공고 목록 조회

- 엔드포인트: `/rsdtRcritNtcList`
- 메서드: GET
- 파라미터:
  - serviceKey: API 인증키 (환경 변수에서 설정)
  - pageNo: 페이지 번호 (기본값: 1)
  - numOfRows: 페이지당 행 수 (기본값: 10)
  - brtcCode: 지역 코드 (41: 경기도)

### 출력 정보

- 공고명
- 주택명
- 위치
- 공급세대수
- 임대보증금
- 월임대료
- 모집기간
- PDF 다운로드 상태

## 환경 변수

프로젝트를 실행하기 위해서는 다음 환경 변수가 필요합니다:

- `HAPPYHOME_API_KEY`: 행복주택 API 인증키

## 주의사항

1. PDF 다운로드를 위해 Playwright와 Chromium 브라우저가 필요합니다.
2. 다운로드된 PDF 파일은 `downloads` 디렉토리에 저장됩니다.
3. 파일명 형식: `공고문_[공고ID]_[타임스탬프].pdf`
