# google-nlp
<p>구글 nlp 테스트 한 Repository입니다.</br>
  https://cloud.google.com/natural-language?hl=ko
 </p>

# Test 결과 
<img width="490" alt="image" src="https://github.com/Hanium2023/google-nlp/assets/80878955/187fc2eb-74b6-4b04-a834-3469ce063d72">

# 실제 구현
POST https://language.googleapis.com/v1/documents:analyzeSentiment


**설정방법**


[Params]
|key |Value|
|:---:|:---:|
|key|myapikey|



[Headers]
|key |Value|
|:---:|:---:|
|Content-Type   |application/json|



[Body]</br>
|raw - Json|
|:------:|
|{ "document": {"type": "PLAIN_TEXT","content": "오늘은 기분이 좋네요"}}  |




  <img width="490" alt="image" src="https://user-images.githubusercontent.com/80878955/276922028-f7aa9657-8e79-4075-822d-98072f8c2d99.png">

