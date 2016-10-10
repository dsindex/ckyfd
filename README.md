ckyfd
===

- description
  - c, python interface for kyfd

- prerequisite
  - aclocal, automake, libtoolize, autoheader, autoconf
  ```
  aclocal (GNU automake) 1.11.1
  automake (GNU automake) 1.11.1
  libtoolize (GNU libtool) 2.2.6b 
  autoheader (GNU Autoconf) 2.63
  autoconf (GNU Autoconf) 2.63
  ```
  - [xerces-c](http://xerces.apache.org/xerces-c/download.cgi)
  ```
  $ cd xerces-c-3.1.4
  $ ./configure ; make ; sudo make install
  ```
  - [openfst](http://www.openfst.org/twiki/bin/view/FST/WebHome)
  ```
  # you should download 'openfst-1.3.2' 
  $ openfst-1.3.2
  $ ./configure ; make ; sudo make install
  ```
  - install [kyfd](https://github.com/dsindex/kyfd)
  ```
  $ pwd
  $ /home
  $ git clone https://github.com/dsindex/kyfd
  $ cd kyfd
  $ ./buildconf
  $ ./configure ; make ; make install
  $ ls install
  bin include lib
  ```

- how to compile
```
$ git clone https://github.com/dsindex/ckyfd
$ cd ckyfd
$ ./buildconf
$ ./configure --with-kyfd=/home/kyfd/install --enable-python=yes --pythoninc=/usr/include/python2.7
$ make ; make install
```

- how to test
  - download prebuilt FST and config file
  ```
  $ cd ckyfd/src
  $ curl -OL https://shleekr.github.io/public/data/rouzeta.tar.gz
  $ tar -zxvf rouzeta.tar.gz
  $ cp -rf KFST/Tagger/* .
  $ cat testme.txt | ./test_ckyfd koreanuni.xml
  --------------------------
  -- Started Kyfd Decoder --
  --------------------------
  Loading fst korfinaluni.fst...
  Loaded configuration, initializing decoder...
  elapsed time = 0.472973 sec
  나 /np 는 /pt <space> 학 교 /nc 에 서 /pa <space> 공 부 /na 하 /xv _ㅂ 니 다 /ef . /sf
  선 /nc 을 /po <space> 긋 /irrs /vb 어 /ex <space> 버 리 /vx 었 /ep 다 /ef . /sf
  고 맙 /irrb /vj 었 /ep 다 /ef . /sf
  나 /np 는 /pt <space> 답 /nc 을 /po <space> 모 르 /irrl /vb 아 /ec . /sf
  지 나 /vb _ㄴ /ed <space> 1 8 /nb 일 /nc <space> 하 오 /nc <space> 3 /nb 시 /nc <space> 경 남 /nr <space> 마 산 시 /nr
  색 /nc 이 /ps <space> 하 얗 /irrh /vj 어 서 /ef <space> 예 쁘 /vj 었 /ep 다 /ef . /sf
  일 찍 /ad <space> 일 어 나 /vb 는 /ed <space> 새 /nc 가 /ps <space> 피 곤 /ns 하 /xj 다 /ef ( /sl 웃 음 /nc ) /sr . /sf
  꽃 /nc 이 /ps <space> 핀 /nc <space> 곳 /nc 을 /po <space> 알 /vb 고 /ec 있 /vj 다 /ef . /sf
  이 것 /nm 은 /pt <space> 사 과 /nc 이 /pp 다 /ef . /sf
  상 자 /nc 를 /po <space> 연 /nc <space> 사 람 /nc 은 /pt <space> 그 /np 이 /pp 다 /ef . /sf
  사 과 /nc _ㄹ /po <space> 먹 /vb 겠 /ep 다 /ef . /sf
  향 약 /nc 은 /pt <space> 향 촌 /nc 의 /pd <space> 교 육 /nc 과 /pc <space> 경 제 /nc 를 /po <space> 관 장 /nc 해 /nc <space> 서 원 /nc 을 /po <space> 운 영 /na 하 /xv 면 서 /ef <space> 중 앙 /nc <space> 정 부 /nc <space> 등 용 문 /nc 인 /nc <space> 대 과 /nc <space> 응 시 자 격 /nc 을 /po <space> 부 여 /na 하 /xv 는 /ed <space> 향 시 /nc 를 /po <space> 주 관 /nc 하 고 /pq <space> 흉 년 /nc 이 /ps <space> 들 /vb 면 /ex <space> 곡 식 /nc 을 /po <space> 나 누 /vb 는 /ed <space> 상 호 부 조 /nc 와 /pc <space> 작 황 /nc 에 /pa <space> 따 르 /vb _ㄴ /ed <space> 소 작 료 /nc <space> 연 동 적 용 /nc 을 /po <space> 정 하 /vb 는 가 /ef <space> 하 /vb 면 /ex <space> 풍 속 사 범 /nc 에 /pa <space> 대 하 /vb 어 /ex <space> 형 벌 /nc 을 /po <space> 가 하 /vb 는 /ed <space> 사 법 부 /nc <space> 역 할 /nc 까 지 /px <space> 담 당 /na 하 /xv 었 었 /ep 다 /ef . /sf
  elapsed time = 0.539626 sec
  ```
  - options
  ```
  # you can use kyfd options(-nbest, -output)
  $ vi test_ckyfd.cc
  char* nbest = "3";
  char* oformat = "score"; // text | score | component
  $ cat testme.txt | ./test_ckyfd koreanuni.xml
  0||| 나 /np 는 /pt <space> 학 교 /nc 에 서 /pa <space> 공 부 /na 하 /xv _ㅂ 니 다 /ef . /sf ||| 47.8457	0||| 나 /vb 는 /ed <space> 학 교 /nc 에 서 /pa <space> 공 부 /na 하 /xv _ㅂ 니 다 /ef . /sf ||| 49.541	0||| 나 /vx 는 /ed <space> 학 교 /nc 에 서 /pa <space> 공 부 /na 하 /xv _ㅂ 니 다 /ef . /sf ||| 50.4482
  1||| 선 /nc 을 /po <space> 긋 /irrs /vb 어 /ex <space> 버 리 /vx 었 /ep 다 /ef . /sf ||| 48.1826	1||| 선 /nc 을 /po <space> 긋 /irrs /vb 어 /ex <space> 버 리 /vb 었 /ep 다 /ef . /sf ||| 49.6631	1||| 선 /nu 을 /po <space> 긋 /irrs /vb 어 /ex <space> 버 리 /vx 었 /ep 다 /ef . /sf ||| 49.9336

  # sentence_id ||| result ||| score \t ... sentence_id ||| result ||| score \t ...
  ```

- how to test in python
```
$ cd wrapper/python
$ cat testme.txt | python test.py -c koreanuni.xml
Loading fst korfinaluni.fst...
나 /np 는 /pt <space> 학 교 /nc 에 서 /pa <space> 공 부 /na 하 /xv _ㅂ 니 다 /ef . /sf ||| 47.8457
선 /nc 을 /po <space> 긋 /irrs /vb 어 /ex <space> 버 리 /vx 었 /ep 다 /ef . /sf ||| 48.1826
고 맙 /irrb /vj 었 /ep 다 /ef . /sf ||| 21.123
나 /np 는 /pt <space> 답 /nc 을 /po <space> 모 르 /irrl /vb 아 /ec . /sf ||| 41.7686
...
```

- tutorial
  - [kyfd tutorial](http://www.phontron.com/kyfd/tut1/)
  - building lexicon fst and test decoding
  ```
  $ cd script
  $ ./lexicon_fst.sh train.txt -v -v
  # 숨은 가계부채로 불리는 자영업자(개인사업자) 대출이 은행권에서만 1년 새 24조원 넘게 증가했다.
  # -> encoding
  # 숨 은 가 계 부 채 로 불 리 는 자 영 업 자 ( 개 인 사 업 자 ) 대 출 이 은 행 권 에 서 만 1 년 새 2 4 조 원 넘 게 증 가 했 다 .
  # -> decoding
  # 숨은 가계부채로 불리는 자영업자(개인사업자) 대출이 은행권에서만 1년새 24조원 넘게 증가했다.
  ```
  - building auto-spacing model
    - let's try to build an auto-spacer. this is somewhat different from the lexicon example. first, i use a character-based model. so, the size of output symbols should be small. second, transition probabilities are calcuated by `p(a,b)/p(a)` for `n m b b prob` where `n` stands for `a`
    ```
    예) <b> 다 음 검 색 <w>
    0 1 다 다       p(<b>, 다) / p(<b>)
    1 2 음 음       p(다, 음)  / p(다)
    2 3 검 검       p(음, 검)  / p(음)
    3 4 색 색       p(검, 색)  / p(검)
    4 5 <eps> <w>   p(색, <w>) / p(색)
    5 0 <eps> <eps>
    ```
    - run
    ```
    $ ./autospacer_fst.sh train.txt -v -v
    # © News1 <쥐띠> 과로와 과음을 하게 되면 후유증이 심하게 가는 날.
    # -> encoding
    # © n e w s 1 < 쥐 띠 > 과 로 와 과 음 을 하 게 되 면 후 유 증 이 심 하 게 가 는 날 .
    # -> decoding
    # © <w> n e w s 1 <w> < 쥐 띠 > <w> 과 로 와 <w> 과 <w> 음 을 <w> 하 게 <w> 되 면 <w> 후 유 증 이 <w> 심 하 게 <w> 가 는 <w> 날 .
    # -> recovering
    # © news1 <쥐띠> 과로와 과 음을 하게 되면 후유증이 심하게 가는 날.
    ```

- [Rouzeta](https://shleekr.github.io/) in python
```
$ cd wrapper/python
$ python test_rouzeta.py -c koreanuni.xml
Loading fst korfinaluni.fst...
나는 학교에서 공부합니다.
0	나는
1	학교에서
2	공부합니다.
나	np	None	NP	0	0
는	pt	None	JX	0	1
학교	nc	None	NNG	1	2
에서	pa	None	JKB	1	3
공부	na	None	NNG	2	4
하	xv	None	XSV	2	5
_ㅂ니다	ef	None	EF	2	6
.	sf	None	SF	2	7
나는 답을 몰라.
0	나는
1	답을
2	몰라.
나	np	None	NP	0	0
는	pt	None	JX	0	1
답	nc	None	NNG	1	2
을	po	None	JKO	1	3
모르	vb	irrl	VV	2	4
아	ec	None	EC	2	5
.	sf	None	SF	2	6
$ python test_rouzeta.py -c koreanbi.xml
Loading fst korinvertwordbifinal.fst...
한국과 이란이 피할 수 없는 맞대결을 앞두고 있다.
0	한국과
1	이란이
2	피할
3	수
4	없는
5	맞대결을
6	앞두고
7	있다.
한국	nr	None	NNP	0	0
과	pc	None	JC	0	1
이란	nr	None	NNP	1	2
이	ps	None	JKS	1	3
피하	vb	None	VV	2	4
_ㄹ	ed	None	ETM	2	5
수	nd	None	NNB	3	6
없	vb	None	VV	4	7
는	ed	None	ETM	4	8
맞대결	nc	None	NNG	5	9
을	po	None	JKO	5	10
앞두	vb	None	VV	6	11
고	ex	None	EC	6	12
있	vx	None	VX	7	13
다	ef	None	EF	7	14
.	sf	None	SF	7	15
```
