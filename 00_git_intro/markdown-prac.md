# Git

### 1. Git 개념

git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 **분산 버전 관리 시스템**이다.



### 2. Git 설정

전역 영역에서 commit 기록의 주인을 등록한다.

 	=> *Why?*  git을 사용했을 때 누가 사용했는지 로그를 남겨야 하기 때문

```bash
$ git config --global user.name "seulee95"	
$ git config --global user.email "seulee95@naver.com"
```



### 3. Git 기본

Git 기본 설정은 아래와 같다.

```bash
$ git init 		# 해당 디렉토리를 Git이 관리하도록 초기화
$ git add "file name"		# commit 할 목록을 staging area로 옮긴다.
$ git commit -m "commit message"	# 어떤 부분이 바뀌었는지 commit message를 남긴다. 
									#"커밋 메세지" == 히스토리의 한 단위
$ git push origin master	
					# 현재까지의 역사(commmits) 가 기록되어 있는 곳에 새로운 commit 반영
```



### 4. Git 저장소

| 로컬(Working Directory) | Staging Area             | Remote Repository(github, bitbucket, gitlab) |
| :---------------------- | ------------------------ | -------------------------------------------- |
| 로컬 컴퓨터 저장소      | 해당 버전의 스냅샷(기록) | 원격 저장소                                  |



### 5. Git branch

- 같은 작업물을 기반으로 동시에 다양한 작업을 할 수 있게 만들어 주는 기능
  - 독립적인 작업 영역 안에서 마음대로 소스코드를 변경할 수 있다. 
  - 분리된 작업 영역에서 변경된 내용은 추후에 기존 버전과 비교해서 새로운 하나의 버전을 만들어 낼 수 있다.



### 6. Git Push

```bash
$ git remote add origin [Github Repo Url]
							# https://github.com/QuartzzBlue/TIL.git 이라는
							# repository를 origin으로 등록
$ git push origin master	# origin에 master 자격으로 push
```



### ** 기타

```bash
$ git status	# git status 확인! commit 상황
$ git log		# 이제까지의 git log 확인! 랜덤 hash로 commit 관리!
```

