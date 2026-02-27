# install
## install sdsl
- `git submodule update --init --recursive`
- `cd sdsl-lite`
- `module load cmake/3.30.2`
- `./install.sh`
## Install mantis
- `module pugre`
- `module load cmake/4.2.3`
- `mkdir build`
- `cd build`
- ```
  cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=../ \ -DCMAKE_PREFIX_PATH=~ ..
  ```
- `make install`
