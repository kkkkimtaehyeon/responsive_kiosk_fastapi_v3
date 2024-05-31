## 👀 TODO
- [x] 나이 측정 CORS 에러
- [x] s3에 오디오 객체 처리 방식
+ TTS 성능 비교 및 테스트x
  - [x] AWS Polly + WebSocket
  - [ ] OPEN AI TTS(https://platform.openai.com/docs/guides/text-to-speech)
- [x] 오디오 출력 방식 비교 (s3 업로드 vs 오디오 객체 반환) -> WebSocket을 이용한 오디오 스트리밍
- [ ] 주문 생성 시 전달하는 데이터 포맷 수정
- [x] GPT 음성 답변 반환 시 텍스트 답변도 반환
- [x] GPT 음성 스트리밍 버퍼링 개선 -> 전체 오디오 데이터 전달 or 청크 사이즈 32kb로 수정
- [ ] 서버 재시작 시 GPT 저장된 메뉴들 백업
- [ ] 음성인식 중지 버튼 누르면 재생되는 오디오 중단


## :tada: 추가 요구사항
- [x] 키워드 검색 성능 개선
  
  + [ 우유 ]로 검색 -> 결과 X
  +  [커피, 우유]로 검색 -> 아메리카노 포함
  +  [커피] 검색을 제외한 정확도 낮음
- [x] 포장/매장 물어보기 전에 총 주문메뉴 알려주고 확인하기 
- [x] 가격 알려줄 필요 없음. 포장/매장 여부 확인하면 바로 주문 json 포맷'만' 반환

## :star: 피드백
+ 
+ 
+ 


## :+1: 성능 개선 사항
+ **WebSocket + gpt-3.5-turbo**
  + 조건: 텍스트 송신 - gpt 답변 받기 - 텍스트 수신
  + 입력: "안녕하세요"
  + 시간🕥: 01:18:03 
+ ** TTS **
  + AWS Polly & streaming audio data(32kb)
  + OPEN AI TTS & streaming audio data(32kb) 
  + OPEN AI TTS & whole audio data  
