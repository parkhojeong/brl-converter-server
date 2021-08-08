1. .brl 또는 .brf 포맷 파일 업로드하여 가시화 (frontend)
2. 점자 이미지파일(png, jpg, jpeg 등) 업로드 (frontend)
3. 이미지 서버로 전송(frontend -> backend)
4. C의 이미지를 AngelinaReader 알고리즘을 통해 .brl포맷 텍스르 변환
5. 변환된 brl 포맷 텍스르를 응답 (backend -> frontend)
6. 1와 5를 비교하여 서로 다른 부분을 하이라이트 (frontend)