# google-nlp
https://cloud.google.com/natural-language?hl=ko
구글 nlp 테스트 한 Repository입니다. 

# Test 결과 
<img width="490" alt="image" src="https://github.com/Hanium2023/google-nlp/assets/80878955/187fc2eb-74b6-4b04-a834-3469ce063d72">

# 실제 구현
POST https://language.googleapis.com/v1/documents:analyzeSentiment

<p>설정 방법</br>
<Params></br>
key                            Value </br>
key                            myapikey</br></br>
<Headers></br>
Key                            Value</br>
Content-Type                   application/json</br>
<Body></br>
raw     Json</br>
{</br>
"document": {</br>
"type": "PLAIN_TEXT",</br>
"content": "오늘은 기분이 좋네요"</br>
}</br>
}</br>
</p>
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/8ef701e3-08c4-4732-8730-a5b7f32a65da/3ff31c81-748b-4601-8954-2a1a9315b017/Untitled.png)
