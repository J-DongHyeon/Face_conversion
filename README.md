
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

* OpenCV에서 제공하는 Haar-cascade 학습 데이터를 이용하여 얼굴 검출을 진행하였다.
* 얼굴 검출을 위한 데이터로는 `haarcascade_frontalface_alt.xml` 을 이용하였다. 이는 정면 얼굴 데이터이다.
<br><br>

------------------------------------------

# 3. 동작 과정

<p align= "center">
<img width="200" height="200" alt="1" src="https://user-images.githubusercontent.com/86474141/126073528-84213bd9-f621-4e25-959f-0c0916b2b629.PNG"></p>

>OpenCV의 얼굴 인식 모델로 이미지에서 얼굴 인식 후 사각형의 좌표를 구한다.
</br></br>

<p align= "center">
<img width="200" height="200" alt="2" src="https://user-images.githubusercontent.com/86474141/126073537-f6cbcb4f-e5ae-47af-be81-1c997d521efe.PNG">  &nbsp;&nbsp;&nbsp;&nbsp;
<img width="200" height="200" alt="3" src="https://user-images.githubusercontent.com/86474141/126073551-7cc9d74d-d69f-4a15-80b6-7f8c7cf272db.PNG"></p>

> `docs/Imgs` 폴더에서 동물 원본 이미지를 가져오고, 동물 원본 이미지의 크기를 얼굴 인식 사각형의 크기에 맞춘다.<br>
> 동물 원본 이미지를 흑백 모델로 변환 시키고, threshold() 함수를 이용하여 완전히 이진화 시킴으로써 마스크를 구한다.
</br></br>

<p align= "center">
<img width="200" height="200" alt="4" src="https://user-images.githubusercontent.com/86474141/126073555-d37deee5-b91e-413b-b3b3-c2f9d93b2b73.PNG"></p>

> 마스크를 동물 원본 이미지에 적용하여 동물 탈을 구한다.
</br></br>

<p align= "center">
<img width="200" height="200" alt="5" src="https://user-images.githubusercontent.com/86474141/126073568-8da1df79-66c1-42d1-bc4c-908a222f1d26.PNG"> </p>

> 사람 이미지와 동물 탈 이미지를 OR 연산하여 사람 얼굴에 동물 탈을 씌운다.
</br></br>

------------------------------------------

# 4. 프로그램 기능 & 단축키

* ## 기능

<p align= "center">
<img src=/docs/readme_Imgs/readme_gif1.gif width=300 height=300></p> 

> 카메라를 통해 실시간 영상에서 얼굴 인식 후 동물 탈을 씌운다.
> </br></br>

<p align= "center">
<img src=/docs/Imgs/pig_inked.jpg width=200 height=200>
<img src=/docs/Imgs/dog_inked.jpg width=200 height=200>
<img src=/docs/Imgs/dng_inked.jpg width=200 height=200>
<img src=/docs/Imgs/pnd_inked.jpg width=200 height=200>
</p> 

> 동물 탈은 돼지, 강아지, 당나귀, 팬더 4가지가 있다.
> </br></br>

<p align= "center">
<img src=/docs/readme_Imgs/readme_img4.PNG width=300 height=300></p> 

> 실시간 카메라 영상 뿐만 아니라 자신이 원하는 이미지에 대해서도 씌울 수 있다.
> </br></br>

<p align= "center">
<img src=/docs/readme_Imgs/readme_img5.PNG width=300 height=300></p> 

> 동물 탈의 투명도를 0 ~ 100 % 로 설정 가능하다.
> </br></br>

<p align= "center">
<img src=/docs/readme_Imgs/readme_img6.PNG width=220 height=220>  &nbsp;&nbsp;&nbsp;&nbsp; <img src=/docs/readme_Imgs/readme_img7.PNG width=220 height=220>
</p> 

> 카메라 영상 중 원하는 프레임을 저장할 수 있고, 원하는 이미지에 대해 여러 가지 편집 후 저장할 수 있다.
> </br></br>

<p align= "center">
<img src=/docs/readme_Imgs/readme_img8.PNG width=300 height=180></p> 

> 편집 후 저장되는 이미지는 `docs/Imgs` 경로에 저장된다.
> </br></br>

* ## 기본 단축키

<p align= "center">
<img src=/docs/readme_Imgs/readme_img9.PNG width=300 height=300></p> 

  - Esc : 윈도우 창 종료
  - S : 현재 프레임 저장
  - 0번 : 오리지널 영상
  - 1번 : 돼지 탈
  - 2번 : 강아지 탈
  - 3번 : 당나귀 탈
  - 4번 : 팬더 탈
  - 트랙바1 : 0 ~ 100 까지 조절함으로써 동물 탈 투명도 조절
  - 트랙바2 : 0 or 1 을 선택함으로써 이미지 모드, 동영상 모드 설정 가능

* ## 이미지 모드일 경우의 추가 단축키

<p align= "center">
<img width="300" height="300" alt="5" src="https://user-images.githubusercontent.com/86474141/126073568-8da1df79-66c1-42d1-bc4c-908a222f1d26.PNG"> </p>

  - N : 다음 이미지
  - P : 이전 이미지
  - D : 샘플 이미지를 보여줌
  - F : 직접 저장한 이미지를 보여줌
  - 마우스 드래그 : 이미지 확대
  - 우 클릭 : 이미지 축소
</br></br>

------------------------------------------

# 5. 실행 결과

<p align= "center">
<img width="300" height="300" src="https://user-images.githubusercontent.com/86474141/126073171-489f2f33-254e-4d23-b54b-c41b67b5e181.gif"> </p>

> &nbsp;실시간 영상에서 S키를 3번 누르고, 이미지 모드로 변경 하여 저장한 이미지를 본 후, D키 누른 것이다. 그 후 샘플 이미지에 동물 탈을 씌운 것이다.
> <br> 실시간 영상에 대해서도 얼굴 인식 후 동물 탈을 씌울 수 있다.
</br></br>

<p align= "center">
<img width="300" height="300" alt="2" src="https://user-images.githubusercontent.com/86474141/126073346-f6b741e6-50ab-45c9-9914-74c13ce8ef3a.PNG"> 
&nbsp;&nbsp;
<img width="300" height="300" alt="3" src="https://user-images.githubusercontent.com/86474141/126073350-564f8bbf-7927-448d-a90c-87aba4a036a2.PNG">
&nbsp;&nbsp;
<img width="300" height="200" alt="1" src="https://user-images.githubusercontent.com/86474141/126073352-4c667cfd-67cd-49bf-a200-23be8cb22372.PNG">
</p>

> &nbsp;원하는 이미지에 대해 편집한 후 저장 가능하다.
</br></br>

------------------------------------------

# 6. 한계점

> OpenCV의 'haarcascade_frontalface_alt.xml' 얼굴 인식 모델이 사람의 얼굴을 아주 잘 인식하지는 못한다.
> > ex) 정면이 아닌 얼굴, 안경을 쓴 얼굴, 눈썹이 안보이는 얼굴 등은 잘 인식하지 못함.
  
> 표정이 변하더라도 동물 표정은 변하지 않고 일정하다.
> > ex) 눈 깜빡임, 웃는 표정 등은 동물 탈이 따라하지 못함.
</br></br>

------------------------------------------

# 7. 참고 사이트

#### 📙 https://signal.sedaily.com/NewsView/1Z7XH7KGX5/GX15
