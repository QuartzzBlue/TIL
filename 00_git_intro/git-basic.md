# 마크다운(MarkDown)

> 일반 텍스트 형식 구문을 사용하는 마크업 언어의 일종으로 사용이 쉽고 간결하다.
>
> 단, 모든 HTML 마크업을 대체하지 않는다.

## 1.문법

### 1.1 Header

> 헤더는 제목을 표현할 때 사용합니다.
>
> 단순히 글자의 크기를 나타낼 때 사용하는 것이 아니라 의미론적인

- h1~h6 까지 표현이 가능합니다.
- #의 개수로 표현하거나 <h1></h1> 형태로 표현 가능합니다.



### 1.2 List

>목록을 나열할 때 사용합니다.
>
>순서가 필요한 항목과 그렇지 않은 항목으로 구분할 수 있습니다.
>
>순서/순서x 항목을 같이 사용할 수 있습니다.

- 순서가 없는 항목 (-)
  - 순서가 없는 하위 항목 (tab)
  - 순서가 없는 하위 항목

1. 순서가 있는 항목
   1. 순서가 없는 하위 항목 (tab)
   2. 순서가 없는 하위 항목
2. 순서가 있는 항목 (enter)

- 순서가 없는 항목 
  1. 순서가 있는 하위 항목 (tab, esc)



### 1.3 Code Block

> 코드 블럭은 작성한 코드를 정리하거나 강조하고 싶을 때 사용합니다.
>
> 코드 블럭은 인라인과 블럭 단위로 구분할 수 있습니다.

- Inline

  - `인라인으로 처리하고 싶은 부분`을 `(백틱) 으로 감싸줍니다.	ex) 코드를 강조하고 싶을 때!

- Block

  - `(백틱)을 3번 입력하고 Enter를 눌러서 생성합니다.

  - ```bash
    $ git add.
    $ git commit -m "commit message"
    $ git push origin master
    ```

  - 코드를 쓸 때 Block 안에 language를 선택하면 하이라이트까지 가능! 

    또는 ```bash 이렇게 쓰면 처음부터 언어 지정 가능



### 1.4 Image

> 로컬에 있는 이미지를 삽입하거나 이미지 링크를 활용하여 표시합니다.

- `![]()` 를 작성하고 `()` 안에 주소를 입력합니다.
  - 이 때 `[]`안에는 이미지 이름을 입력합니다.

- 로컬에 있는 이미지 파일을 로드할 때는 절대 경로가 아닌 **상대경로**를 사용합니다!

  why? 절대경로를 사용하면 나중에 폴더채로 이동했을 때 에러 생성!

![kimjaehwan-image](data:image/jpeg;base64,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)

​																			<인터넷 주소 url 사용>

![](.\images\kimjaehwan-image.jpg)

​																	<로컬에 있는 이미지 파일 로드>



### 1.5 Link

> 특정 주소로 링크를 걸 때 사용합니다.

- `[]()`를 작성하고 `[]` 안에는 링크 이름 ,`()` 안에는 링크를 걸 주소를 입력합니다.

[네이버](https://www.naver.com/)



### 1.6 Table

> 표를 작성하여 요소를 구분할 수 있습니다.

- `|(파이프)` 사이에 컬럼을 작성하고 `Enter`를 입력합니다.
- 마지막 컬럼을 작성하고 뒤에 `|`를 붙여 줍니다.
- 표를 클릭하고 '표 크기 조정'으로 row 를 늘릴 수 있습니다.

| Working Directory | Staging Area | Remote Repository |
| ----------------- | ------------ | ----------------- |
| working tree      | INDEX        | history           |
| working copy      | cache        | tree              |



### 1.7 기타

`인용문`

- `>`를 입력하고 `Enter`키를 누릅니다.

  > git은 컴퓨터의 파일 변경 사항을 추적합니다.

- 중첩된 인용문을 사용할 수 있습니다.

  > `$ git add.`
  >
  > > 
  > >
  > > `$ git commit -m "first commit"`

`수평선`

- `---`, `***`, `___`를 입력하여 작성합니다.

  `Working Directory`

---

   	`Staging area`

***

​	   `Remote Repository(Github)`

**강조**

- 이탤릭체는 해당 부분을 `*`, `_` 로 감싸줍니다.
- 볼드체는 해당 부분을 `**`, `__`로 감싸줍니다.
- 취소선은 `~~`로 감싸줍니다.

이것은 *이탤릭체* 입니다.

이것은 **볼드체** 입니다.

이것은 ~~취소선~~ 입니다.









