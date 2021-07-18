# Open_CV

opencv를 이용하여 카메라 어플 기능 구현

얼굴 인식 -> 동물 얼굴로 변형

# 기능
- 카메라를 통해 얼굴 인식 후 동물 탈을 씌웁니다.
- 동물 탈은 돼지, 강아지, 당나귀, 팬더 4가지가 있습니다.
- 카메라 영상 뿐만 아니라 자신이 원하는 이미지에 대해서도 씌울 수 있습니다.
- 동물 탈의 비중을 0 ~ 100 % 로 설정 가능합니다.
- 카메라 영상 중 원하는 프레임을 저장할 수 있습니다.
- 원하는 이미지에 대해서도 여러 가지 편집 후 저장할 수 있습니다.
- 저장된 이미지에 대해 확대, 축소와 같은 편집을 할 수 있습니다.

(저장되는 프레임은 'img' 폴더에 저장됩니다.)

# 샘플 이미지에 동물 탈을 씌우는 영상

(S키를 3번 누르고 -> 이미지 모드로 변경 하여 저장한 이미지를 본 후 -> D키 누름)

(실시간 영상에 대해서도 얼굴 인식 후 동물 탈을 씌울 수 있습니다.)

![ezgif com-gif-maker](https://user-images.githubusercontent.com/86474141/126073171-489f2f33-254e-4d23-b54b-c41b67b5e181.gif)

# 샘플 이미지, 저장 이미지를 편집한 후 저장 가능

<img width="189" alt="2" src="https://user-images.githubusercontent.com/86474141/126073346-f6b741e6-50ab-45c9-9914-74c13ce8ef3a.PNG"> <img width="189" alt="3" src="https://user-images.githubusercontent.com/86474141/126073350-564f8bbf-7927-448d-a90c-87aba4a036a2.PNG">

('img' 폴더에 저장됨)

<img width="365" alt="1" src="https://user-images.githubusercontent.com/86474141/126073352-4c667cfd-67cd-49bf-a200-23be8cb22372.PNG">



# 단축키
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


# 알고리즘 간단 설명
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


# 보완점
- open cv의 'haarcascade_frontalface_alt.xml' 얼굴 인식 모델이 사람의 얼굴을 아주 잘 인식하지는 못합니다.

ex) 정면이 아닌 얼굴, 안경을 쓴 얼굴, 눈썹이 안보이는 얼굴 등은 잘 인식하지 못함
- 표정이 변하더라도 동물 표정은 변하지 않고 일정합니다.

ex) 눈 깜빡임, 웃는 표정은 인식하지 못함

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FJ-DongHyeon%2FOpen_CV.git&count_bg=%2379C83D&title_bg=%23555555&icon=grav.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

