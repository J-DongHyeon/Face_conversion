<h1 align="center"> Face Conversion </h1>

<h4 align="center"> 사람 얼굴 인식 후 동물 탈로 변환시키는 프로젝트 </h4>

<p align= "center">
<img src=/docs/readme_Imgs/readme_img1.PNG width=500 height=350></p> 
</br></br>

------------------------------------------

# 1. 기획 계기

<p align= "center">
<img src=/docs/readme_Imgs/readme_img2.PNG width=500 height=300></p> 

> &nbsp;최근 사진 보정, 영상 꾸미기 등 카메라 보정 어플의 인기가 날로 높아지고 있으며 포털 업계 카메라 시장도 경쟁이 치열하다. 쇼설 네트워크 서비스 (SNS) 에서는 스토리 기능을 이용해 짧은 영상을 올리는 것이 일상화되어 영상 수요는 더욱 늘고 있다. 관련 업계 관계자는 "최근 젊은 층들은 함께 사진을 찍을 때 스마트폰 기종이 아닌 어떤 카메라 앱을 쓰는 지에 따라 사진을 찍을 사람을 결정하는 분위기" 라고 말했다. <br> 이러한 추세에 발맞추어, `사람 얼굴을 인식하여 동물 탈로 변환시키는 재미있는 기능`을 구현하고자 본 프로젝트를 진행하였다.
<br><br>

------------------------------------------

# 2. 개발환경 & 얼굴 검출 모델

<p align= "center">
<img src=/docs/readme_Imgs/readme_img3.PNG width=500 height=200></p> 

> &nbsp;OpenCV에서 제공하는 Haar-cascade 학습 데이터를 이용하여 얼굴 검출을 진행하였습니다. <br> 얼굴 검출을 위한 데이터로는 `haarcascade_frontalface_alt.xml` 을 이용하였습니다. 이는 정면 얼굴 데이터 입니다.
<br><br>

------------------------------------------

### 기능
- 카메라를 통해 얼굴 인식 후 동물 탈을 씌웁니다.
- 동물 탈은 돼지, 강아지, 당나귀, 팬더 4가지가 있습니다.
- 카메라 영상 뿐만 아니라 자신이 원하는 이미지에 대해서도 씌울 수 있습니다.
- 동물 탈의 비중을 0 ~ 100 % 로 설정 가능합니다.
- 카메라 영상 중 원하는 프레임을 저장할 수 있습니다.
- 원하는 이미지에 대해서도 여러 가지 편집 후 저장할 수 있습니다.
- 저장된 이미지에 대해 확대, 축소와 같은 편집을 할 수 있습니다.

(저장되는 프레임은 'img' 폴더에 저장됩니다.)

### 샘플 이미지에 동물 탈을 씌우는 영상

(S키를 3번 누르고 -> 이미지 모드로 변경 하여 저장한 이미지를 본 후 -> D키 누름)

(실시간 영상에 대해서도 얼굴 인식 후 동물 탈을 씌울 수 있습니다.)

![ezgif com-gif-maker](https://user-images.githubusercontent.com/86474141/126073171-489f2f33-254e-4d23-b54b-c41b67b5e181.gif)

### 샘플 이미지, 저장 이미지를 편집한 후 저장 가능

<img width="189" alt="2" src="https://user-images.githubusercontent.com/86474141/126073346-f6b741e6-50ab-45c9-9914-74c13ce8ef3a.PNG"> <img width="189" alt="3" src="https://user-images.githubusercontent.com/86474141/126073350-564f8bbf-7927-448d-a90c-87aba4a036a2.PNG">

('img' 폴더에 저장됨)

<img width="365" alt="1" src="https://user-images.githubusercontent.com/86474141/126073352-4c667cfd-67cd-49bf-a200-23be8cb22372.PNG">



### 단축키
- Esc : 윈도우 종료
- S : 현재 프레임 저장
- 0번 : 오리지널 영상
- 1번 : 돼지 탈
- 2번 : 강아지 탈
- 3번 : 당나귀 탈
- 4번 : 팬더 탈
- 트랙바1 : 0 ~ 100 까지 조절함으로써 동물 탈 비중 조절
- 트랙바2 : 0 or 1 을 선택함으로써 이미지 모드, 동영상 모드 설정 가능

이미지 모드일 경우 추가 단축키
- N : 다음 이미지
- P : 이전 이미지
- D : 샘플 이미지를 보여줌
- F : 저장한 이미지를 보여줌
- 마우스 드래그 : 이미지 확대
- 우 클릭 : 이미지 축소


### 알고리즘 간단 설명
- CV2의 얼굴 인식 모델로 얼굴 인식 후 사각형의 좌표를 구합니다.

<img width="100" alt="1" src="https://user-images.githubusercontent.com/86474141/126073528-84213bd9-f621-4e25-959f-0c0916b2b629.PNG">

- 'img' 폴더에서 동물 원본 이미지를 가져옵니다.

- 동물 원본 이미지를 사각형의 크기에 맞춥니다.
 
<img width="100" alt="2" src="https://user-images.githubusercontent.com/86474141/126073537-f6cbcb4f-e5ae-47af-be81-1c997d521efe.PNG">

- 동물 원본 이미지의 마스크를 구합니다.

<img width="100" alt="3" src="https://user-images.githubusercontent.com/86474141/126073551-7cc9d74d-d69f-4a15-80b6-7f8c7cf272db.PNG">

- 마스크를 동물 원본 이미지에 적용하여 동물 탈을 구합니다.

<img width="100" alt="4" src="https://user-images.githubusercontent.com/86474141/126073555-d37deee5-b91e-413b-b3b3-c2f9d93b2b73.PNG">

- 사람 원본 이미지에 동물 탈을 씌웁니다.

<img width="100" alt="5" src="https://user-images.githubusercontent.com/86474141/126073568-8da1df79-66c1-42d1-bc4c-908a222f1d26.PNG">


### 보완점
- open cv의 'haarcascade_frontalface_alt.xml' 얼굴 인식 모델이 사람의 얼굴을 아주 잘 인식하지는 못합니다.

ex) 정면이 아닌 얼굴, 안경을 쓴 얼굴, 눈썹이 안보이는 얼굴 등은 잘 인식하지 못함
- 표정이 변하더라도 동물 표정은 변하지 않고 일정합니다.

ex) 눈 깜빡임, 웃는 표정은 인식하지 못함

