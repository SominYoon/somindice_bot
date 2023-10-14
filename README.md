# somindice_bot
discord dice bot with discord.py

퍼지주사위 예쁘게 굴려주는 주사위가 없고 엠배드를 사용한 인터페이스의 주사위 봇도 없길래 한번 만들어 봄

깃헙도 잘 쓸줄 모르고, 디스코드 봇 처음 만들어서, 부족하지만 mit라이센스니까 알아서 복붙하든 말든 상관없고 훈수환영이지만 수정은 하고 싶을때 함
디스코드 엠베드 특인지 모바일로 보았을 땐 별로안예쁨 

COC 사람들이 좋아하니까 100면체로 설정하면 특별히 100 -> 00으로 나오고 10 미만의 수는 앞에 03, 04 이런식으로 나오게 조정했는데 코드가 개떡같음


# 사용법
 ## /roll [amount] [side] ~[repeat]

 [amount]          주사위 개수

 [side]            주사위 종류 (n면체의 주사위) 

 ~[repeat]         반복 횟수 (주사위 여러번 굴려야 할때 구지 합산된 값 뜨면 안 이쁘니까 쓰는거) (기본 : 1)

 ~[highlight]      강조 여부 (주사위 최소값 & 최대값 강조해줌) (기본 : True) 

  ### 예시
![스크린샷 2023-10-14 15-36-02](https://github.com/SominYoon/somindice_bot/assets/59977972/edc4f62a-4e98-4067-a98f-b74665f05781) 명령어 채팅 ![image](https://github.com/SominYoon/somindice_bot/assets/59977972/96c2997e-1e7f-4ced-af2d-d86a9ea8e72b) 결과 ![image](https://github.com/SominYoon/somindice_bot/assets/59977972/c2388384-d4ef-49d2-9761-04f4c2754cb4) 5번 반복 적용 ![image](https://github.com/SominYoon/somindice_bot/assets/59977972/1f8c95ba-62d5-47b6-9df2-26537bf705cb) 오 100펌블


 ## /fudge [amount] ~[repeat]


 [amount]          주사위 개수

 ~[repeat]         반복 횟수 (주사위 여러번 굴려야 할때 구지 합산된 값 뜨면 안 이쁘니까 쓰는거) (기본 : 1)

 ~[sum_highlight]  합산한 결과값 강조 (기본 : 0) (특별히 보고싶은 결과값 있으면 정수로 기입하고 0이 강조되는 거 싫으면 그냥 거의 뜰일없는 10으로 해놓으면 됨 굳

 ### 예시
![image](https://github.com/SominYoon/somindice_bot/assets/59977972/d4d24e40-6436-460a-83c8-46fcea5e9b2b) ![image](https://github.com/SominYoon/somindice_bot/assets/59977972/0fc31b7e-15bf-4ee2-80e8-e7ccc15b3ac1) ![image](https://github.com/SominYoon/somindice_bot/assets/59977972/8c1633be-f0f7-4610-a405-1c90bfcf2045)

### 여담 
반복이랑 한번에 굴리는 주사위 갯수가 많으면, 화면비가 잘 맞아야지만 이쁨

![image](https://github.com/SominYoon/somindice_bot/assets/59977972/3f7208c9-009b-4c6a-8dea-0732847b1f87)
