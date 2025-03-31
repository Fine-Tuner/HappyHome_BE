import json
import ssl
import os
from typing import Dict, List, Optional
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.parse import quote_plus, urlencode
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class HappyHomeClient:
    BASE_URL = "http://apis.data.go.kr/1613000/HWSPR02"
    ENDPOINT = "/rsdtRcritNtcList"
    SERVICE_KEY = os.getenv('HAPPYHOME_API_KEY')

    def __init__(self):
        if not self.SERVICE_KEY:
            raise ValueError("API 키가 설정되지 않았습니다. .env 파일을 확인해주세요.")
            
        # SSL 컨텍스트 생성
        self.context = ssl.create_default_context()
        self.context.check_hostname = False
        self.context.verify_mode = ssl.CERT_NONE

    def get_housing_list(self, page_no: int = 1, num_of_rows: int = 10) -> Dict:
        """주택 공고 목록을 가져옵니다."""
        params = {
            "serviceKey": self.SERVICE_KEY,  # 이미 인코딩된 키를 그대로 사용
            "pageNo": str(page_no),
            "numOfRows": str(num_of_rows)
        }
        
        query_string = urlencode(params, quote_via=quote_plus, safe='%')  # % 문자는 인코딩하지 않음
        url = f"{self.BASE_URL}{self.ENDPOINT}?{query_string}"
        
        print(f"요청 URL: {url}")
        
        request = Request(url)
        with urlopen(request, context=self.context) as response:
            response_data = response.read().decode('utf-8')
            print(f"응답 내용: {response_data[:500]}")  # 처음 500자만 출력
            return json.loads(response_data)

    def format_price(self, price: int) -> str:
        """가격을 보기 좋게 포맷팅합니다."""
        return f"{price:,}원"

    def format_date(self, date_str: str) -> str:
        """날짜를 보기 좋게 포맷팅합니다."""
        if not date_str:
            return "날짜 정보 없음"
        try:
            date = datetime.strptime(date_str, "%Y%m%d")
            return date.strftime("%Y년 %m월 %d일")
        except ValueError:
            return date_str

def main():
    client = HappyHomeClient()
    
    try:
        # 주택 공고 목록 가져오기
        print("=== 행복주택 공고 목록 ===")
        result = client.get_housing_list()
        
        if "response" in result and "header" in result["response"]:
            header = result["response"]["header"]
            if header["resultCode"] == "00":
                items = result["response"]["body"]["item"]
                if not isinstance(items, list):
                    items = [items]  # 단일 아이템인 경우 리스트로 변환
                    
                for item in items:
                    print(f"\n공고명: {item.get('pblancNm', '정보없음')}")
                    print(f"주택명: {item.get('hsmpNm', '정보없음')}")
                    print(f"위치: {item.get('fullAdres', '정보없음')}")
                    print(f"공급세대수: {item.get('sumSuplyCo', '정보없음')}세대")
                    print(f"임대보증금: {client.format_price(item.get('rentGtn', 0))}")
                    print(f"월임대료: {client.format_price(item.get('mtRntchrg', 0))}")
                    print(f"모집기간: {client.format_date(item.get('beginDe', ''))} ~ {client.format_date(item.get('endDe', ''))}")
                    print("---")
            else:
                print(f"API 호출 실패: {header.get('resultMsg', '알 수 없는 오류')}")
        else:
            print("API 응답 형식이 올바르지 않습니다.")
            print(f"받은 응답: {result}")

    except Exception as e:
        print(f"처리 중 오류 발생: {e}")

if __name__ == "__main__":
    main() 