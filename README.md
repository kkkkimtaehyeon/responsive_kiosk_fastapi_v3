- [x] 나이 측정 CORS 에러
- [x] s3에 오디오 객체 처리 방식
+ TTS 성능 비교 및 테스트
  - [x] AWS Polly + WebSocket
  - [ ] OPEN AI TTS(https://platform.openai.com/docs/guides/text-to-speech)
- [x] 오디오 출력 방식 비교 (s3 업로드 vs 오디오 객체 반환) -> WebSocket을 이용한 오디오 스트리밍
- [ ] 주문 생성 시 전달하는 데이터 포맷 수정


## :+1: 성능 개선 사항
+ **WebSocket + gpt-3.5-turbo**
  + 조건: 텍스트 송신 - gpt 답변 받기 - 텍스트 수신
  + 입력: "안녕하세요"
  + 시간🕥: 01:18:03 
