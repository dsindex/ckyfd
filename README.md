ckyfd
===

- description
  - c interface for kyfd

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
$ ./configure --with-kyfd=/home/kyfd/install --enable-python=yes
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
  cnt_line = 0
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
