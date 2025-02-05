- myeonghoon 브렌치
  기능 구현 목표: 추천한 장소들을 기반으로 장소들의 위치, 정보 그리고 경로를 생성 및 제공하는 기능 구현
  
# 2025 GDGoC Winter 프로젝트 Team2. AI Part
-> 추천한 장소들을 기반으로 장소들의 추천 경로를 제공하는 기능 구현

Google Colab 환경 - 파이썬 사용
Naver Map API
- Web Dynamic Map
- Direction 5
- Geocoding

* 장소명 인식을 하지 못 함 ex) 남산타워 / 
주소로 입력해야 인식 가능 ex) 서울 용산구 남산공원길 105
-> 장소명 인식으로 바꾸고 싶지만 장소명 입력 받으면 주소로 변환해서 인식할 수 있도록 추가 구현 필요할 듯

* 길찾기 기능 이용해서 네이버 지도 웹에서 장소 간 경로를 볼 수 있도록 기능 구현하는 중
하지만 네이버 지도 웹에 장소(출발지, 목적지, 경유지) 설정이 안 되어있는 문제 발생
-> 출발지, 도착지 설정까지는 완료(o)

* 하지만 경유지 기능 추가하면 네이버 지도 웹에서 도로 인근 주소로 입력하라는 문구가 발생하고 경로 찾기 불가능 문제 발생
-> 경유지 추가 기능(최대 5개) 구현
-> 더 나아가 장소 간 최적 경로 찾기 기능 구현 목표 

* 대중교통 길 찾기로는 경유지 추가할 수 없음 -> 그래서 자가용으로 검색되도록 시도중(해결 완료 o)

@@@25.02.05 현재 최종 상황@@@
- 출발지, 도착지 입력 받아서 두 장소 간 경로를 네이버 지도 웹 링크를 통해 들어가서 확인 가능

* 장소명(건물명) 인식 못 하고 주소로 입력해야 인식 함. 제한적인 문제로 추측
-> 추후 장소명을 주소로 변환 후 그 주소 값으로 활용하도록 수정 예정

* 경유지 추가 기능 추가시 현재 네이버 지도 웹을 들어가면 "도로 인근으로 지정 후 다시 시도해 달라"는 메세지 나타나고 있음
-> 두 장소 간 경로를 받을때는 이런 현상이 안 나타나고 있는데 뭐가 문제인지 확인 불가능

=> 경유지 추가 기능, 경로 찾기 기능 정상적으로 작동되도록 구현되면 그 코드 기반으로 AI 추천 기능 코드와 연결시켜 추천 받은 장소들을 가지고 추천 경로 제공하도록 기능 구현 예정
+ API Key 값도 현재 코랩 코드 상에 업로드하고 구현중이지만 배포 전에는 Key 값 숨길 예정
