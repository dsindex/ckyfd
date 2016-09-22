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
