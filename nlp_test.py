#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("Request",  "language_syntax_text")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-language

# sample-metadata
#   title: Analyzing Syntax
#   description: Analyzing Syntax in a String
#   usage: python3 samples/v1/language_syntax_text.py [--text_content "This is a short sentence."]

# [START language_syntax_text]
from google.cloud import language_v1
from google.oauth2 import service_account


def sample_analyze_sentiment(text_content):
    service_account_file = './haniumtest-388405-962079b128fd.json'
    credentials = service_account.Credentials.from_service_account_file(service_account_file)
    client = language_v1.LanguageServiceClient(credentials=credentials)

    type_ = language_v1.Document.Type.PLAIN_TEXT

    document = {"content": text_content, "type_": type_, "language": "ko"}

    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(
        request={"document": document, "encoding_type": encoding_type}
    )

    print(f"텍스트의 감정 점수: {response.document_sentiment.score}")
    print(f"텍스트의 감정 크기: {response.document_sentiment.magnitude}")

    for sentence in response.sentences:
        print(f"문장: {sentence.text.content}")
        print(f"문장의 감정 점수: {sentence.sentiment.score}")
        print(f"문장의 감정 크기: {sentence.sentiment.magnitude}")

        if sentence.sentiment.score >= 0.25:
            print("긍정")
        elif sentence.sentiment.score <= -0.25:
            print("부정")
        else:
            print("노멀")
    return response.document_sentiment.score
    


def separate_sentences(text_content):
    service_account_file = './haniumtest-388405-962079b128fd.json'
    credentials = service_account.Credentials.from_service_account_file(service_account_file)
    client = language_v1.LanguageServiceClient(credentials=credentials)

    type_ = language_v1.Document.Type.PLAIN_TEXT

    document = {"content": text_content, "type_": type_, "language": "ko"}

    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_syntax(
        request={"document": document, "encoding_type": encoding_type}
    )

    sentences = []
    current_sentence = []

    for token in response.tokens:
        text = token.text.content
        part_of_speech = language_v1.PartOfSpeech.Tag(token.part_of_speech.tag).name

        if part_of_speech in ["ADJ", "VERB"] and current_sentence:
            current_sentence.append(text)
            sentences.append(' '.join(current_sentence))
            current_sentence = []

        elif part_of_speech == "PUNCT" and current_sentence:
            sentences.append(' '.join(current_sentence + [text]))
            current_sentence = []

        else:
            current_sentence.append(text)

    if current_sentence:
        sentences.append(' '.join(current_sentence))

    return sentences

def analyze_sentiment_for_sentences(sentences):
    count=0;
    sentiment_scores = []  # 감정 점수 저장 리스트
    for sentence in sentences:
        print(f"{count}번째 문장----------")
        print(f"문장: {sentence}")
        sentiment_score = sample_analyze_sentiment(sentence)
        sentiment_scores.append(sentiment_score)
        count+=1
    
    # 평균 점수 구하기 
    if sentiment_scores: 
        filtered_scores = [score for score in sentiment_scores if abs(score) >= 0.25] #노멀 해당 점수 빼고 평균 구하기
        if filtered_scores:
            average_score = sum(filtered_scores) / len(filtered_scores)
            print("----------------")
            print(f"평균 감정 점수: {average_score}")
            if average_score >= 0.25:
                print("긍정")
            elif average_score <= -0.25:
                print("부정")


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--text_content", type=str)
    args = parser.parse_args()

    while True:
        text = input("문자열을 입력하세요 ('q'를 입력하면 종료): ")
        if text.lower() == 'q':
            break

        separated_sentences = separate_sentences(text)  # 문장 구분
        analyze_sentiment_for_sentences(separated_sentences)  # 구분된 문장에 대한 감정 분석 수행


if __name__ == "__main__":
    main()
