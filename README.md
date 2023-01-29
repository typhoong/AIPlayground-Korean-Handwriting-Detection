담당자 : 김태훈 (thkim@mnc.ai)

# 2021 NIPA 인공지능 놀이터

### Task01
[이지AI/자연어] 한국어 손글씨 탐지


## 상세 설명

### 과제 설명

손글씨로 쓰여진 텍스트 이미지에서 텍스트를 탐지하는 과제

- 의의
  - 인공지능 기반 한글 광학글자인식 (OCR, Optical Character Recognition) 성능 개선 촉진
  - 손글씨와 인쇄체 등 AI OCR을 연구하거나, 적용하려는 산업 분야에서의 활용 가능성
  - AI OCR 인식엔진 학습 모델 및 학습 알고리즘을 선택, 비교, 분석하는 연구에서의 활용 가능성

### 채점 방식

**WER (Word Error Rate)**

WER = (S+D+I)/N = (S+D+I)/(S+D+C)  
  where
  - S is the number of substitutions,
  - D is the number of deletions,
  - I is the number of insertions,
  - C is the number of correct words,
  - N is the number of words in the reference (N=S+D+C)



## 데이터

### 데이터 설명

- 입출력
  - Input : 다양한 크기의 손글씨 이미지 파일(.png)
  - Output : 이미지 크기, 파일명, 텍스트 정보가 담긴 파일(.json)
- 데이터셋 구성 : zip 기준 총 약 1.54GB
  - train: 5772개의 png 파일과 1개의 json 파일
  - test: 1077개의 png 파일

### 데이터 링크
- 데이터 다운로드 : [링크](https://aihub.or.kr/problem_contest/nipa-learning-platform)  
- AI hub 참고 데이터 : [한국어 글자체 이미지](https://aihub.or.kr/aidata/133)
