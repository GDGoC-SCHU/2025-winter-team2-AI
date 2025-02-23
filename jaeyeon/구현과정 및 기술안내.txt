# 2025-winter-team2-AI AI Part
-> 사용자가 입력한 여행지, 기간, 테마에 맞는 여행 일정을 자동 생성하는 AI 기반 API 제공

* 프로젝트명: 여행 일정 추천 API
* 목적: 사용자가 입력한 여행지, 기간, 테마에 맞는 여행 일정을 자동 생성하는 AI 기반 API 제공
* 주요 기능: AI 모델을 활용한 여행 일정 자동 생성, 네이버 지도 및 구글 검색 URL 자동 생성,FastAPI 기반 API 제공

* 기술 스택
Python -> API 및 데이터 처리
FastAPI -> 웹 프레임워크
Google Generative Ai(Gemini 1.5 Flash) -> 여행 일정 생성 AI모델
dotenv -> 환경 변수 관리
re, json, urllib.parse -> 데이터 처리 및 URL 인코딩
Uvicorn -> FastAPI 서버 실행

* 구현 방식
FastAPI를 사용하여 API 엔드포인트(/generate_itinerary) 생성
사용자가 여행지(location), 여행 기간(days), 테마(theme)를 입력
AI 모델(Gemini 1.5 Flash)에 적절한 프롬프트를 전송하여 일정 생성 요청
응답된 JSON 데이터에서 불필요한 텍스트 제거 후 파싱
각 추천 장소에 대해 네이버 지도 및 구글 검색 URL을 생성하여 추가
최종적으로 JSON 형식으로 변환하여 반환

# 모델 생성
model = genai.GenerativeModel('gemini-1.5-flash')

# AI 모델에 요청
response = model.generate_content(query)

# 응답 텍스트 처리
response_text = response.text.strip()

* 환경 변수 로드 및 AI 모델 설정
AI 모델과의 통신을 위해 Google Generative AI API 키 필요
API 키는 .env 파일에 저장하고, dotenv 라이브러리를 사용해 로드
(GOOGLE_API_KEY=your_api_key_here)


*  AI 프롬프트 구성
query = f"""
당신은 여행 일정 생성 AI입니다.
사용자의 요청에 맞춰 {location}에서 {days}일 동안 '{theme}' 테마 여행 일정을 생성하세요.

반드시 3개 장소를 추천하세요.

응답은 JSON 코드 블록 내에서 반환하세요.
{{
    "itinerary": [
        {{"day": 1, "places": [
            {{"name": "장소1", "type": "{theme}"}}
        ]}}
    ]
}}
"""

* API 응답 예시
{
    "itinerary": [
        {
            "day": 1,
            "places": [
                {
                    "name": "광장시장",
                    "type": "맛집",
                    "naver_map_url": "https://map.naver.com/v5/search/광장시장",
                    "google_search_url": "https://www.google.com/search?q=광장시장"
                },
                {
                    "name": "북촌 한옥마을",
                    "type": "맛집",
                    "naver_map_url": "https://map.naver.com/v5/search/북촌 한옥마을",
                    "google_search_url": "https://www.google.com/search?q=북촌 한옥마을"
                }
            ]
        }
    ]
}

* 결론 및 기대 효과
자동화된 여행 일정 생성
사용자 맞춤형 추천 제공
실제 검색 링크 포함으로 편리한 활용 가능
FastAPI를 활용한 경량화된 API 제공
AWS 또는 Docker 기반 클라우드 배포 가능