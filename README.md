# HappyHome Backend

행복주택 API를 활용한 주택 정보 조회 서비스

## 기능

- 행복주택 공고 목록 조회
- 주택 상세 정보 조회
- 지역별 주택 정보 필터링

## 기술 스택

- Python 3.11
- requests
- urllib3
- python-dotenv

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

## API 문서

### 행복주택 공고 목록 조회

- 엔드포인트: `/rsdtRcritNtcList`
- 메서드: GET
- 파라미터:
  - serviceKey: API 인증키 (환경 변수에서 설정)
  - pageNo: 페이지 번호 (기본값: 1)
  - numOfRows: 페이지당 행 수 (기본값: 10)

## 환경 변수

프로젝트를 실행하기 위해서는 다음 환경 변수가 필요합니다:

- `HAPPYHOME_API_KEY`: 행복주택 API 인증키
