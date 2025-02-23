import os
from dotenv import load_dotenv
import google.generativeai as genai
import json
import re
from urllib.parse import quote
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("GOOGLE_API_KEY")

# API 키 설정
if api_key:
    genai.configure(api_key=api_key)
else:
    print("API 키가 설정되지 않았습니다. .env 파일을 확인하세요.")
    exit()

# 모델 생성
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_map_urls(place_name):
    """ 장소명을 받아 네이버 지도 및 구글 검색 URL을 생성 """
    encoded_place = quote(place_name)  # URL 인코딩
    naver_map_url = f"https://map.naver.com/v5/search/{encoded_place}"
    google_search_url = f"https://www.google.com/search?q={encoded_place}"
    return naver_map_url, google_search_url

# FastAPI 애플리케이션 생성
app = FastAPI()

@app.get("/generate_itinerary")
async def generate_itinerary(location: str, days: int, theme: str):
    # AI에 메시지 전송
    query = f"""
    당신은 여행 일정 생성 AI입니다.
    사용자의 요청에 맞춰 {location}에서 {days}일 동안 '{theme}' 테마 여행 일정을 생성하세요.

    각 날짜마다 정확히 3개의 장소를 추천하세요.

    응답은 아래 JSON 형식을 따르세요:
    {{
        "itinerary": [
            {{"day": 1, "places": [
                {{"name": "장소1", "type": "{theme}"}},
                {{"name": "장소2", "type": "{theme}"}},
                {{"name": "장소3", "type": "{theme}"}}
            ]}},
            ... (각 날짜별 반복)
        ]
    }} 
    """

    # 모델로 응답 생성
    response = model.generate_content(query)

    try:
        # 응답 텍스트에서 코드 블록 및 불필요한 공백 제거
        response_text = re.sub(r'`json\n|`', '', response.text).strip()

        # JSON 파싱
        response_data = json.loads(response_text)

        # 각 장소 정보에 URL 추가
        for day in response_data["itinerary"]:
            day["places"] = day["places"][:3]
            for place in day["places"]:
                place_name = place["name"]
                naver_url, google_url = generate_map_urls(place_name)
                place["naver_map_url"] = naver_url
                place["google_search_url"] = google_url

        return JSONResponse(content=response_data)

    except json.JSONDecodeError:
        return {"error": "응답이 JSON 형식이 아닙니다.", "response_text": response.text}
    except Exception as e:
        return {"error": f"예상치 못한 오류가 발생했습니다: {e}", "response_text": response.text}