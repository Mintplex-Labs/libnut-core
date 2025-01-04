## Building

Please ensure you have the required dependencies before installing:

* Windows
  * windows-build-tools npm package (`npm install --global --production windows-build-tools` from an elevated PowerShell or CMD.exe)
* Mac
  * Xcode Command Line Tools.
* Linux
  * cmake
  * A C/C++ compiler like GCC.
  * libxtst-dev and libpng++-dev (`sudo apt-get install libxtst-dev libpng++-dev`).

### Build

```
npm install
npm run build
```

### Release build

```
npm run npm:prepare
```

This will push `@mintplex-labs/libnut-{platform}-{arch}` to npm registry. When on ARM Windows, it will push `@mintplex-labs/libnut-winarm64` to npm registry.