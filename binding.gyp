{
  "targets": [
    {
      "target_name": "libnut",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [
        "src/main.cc",
        "src/deadbeef_rand.c",
        "src/MMBitmap.c"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "defines": [
        "NAPI_CPP_EXCEPTIONS",
        "NAPI_VERSION=3"
      ],
     
      "conditions": [
        ['OS=="linux"', {
          "sources": [
            "src/linux/keycode.c",
            "src/linux/keypress.c",
            "src/linux/mouse.c",
            "src/linux/screen.c",
            "src/linux/screengrab.c",
            "src/linux/xdisplay.c",
            "src/linux/highlightwindow.c",
            "src/linux/window_manager.cc"
          ],
          "libraries": [
            "-lX11",
            "-lXtst"
          ]
        }],
        ['OS=="mac"', {
          "sources": [
            "src/macos/keycode.c",
            "src/macos/keypress.c",
            "src/macos/mouse.c",
            "src/macos/mouse_utils.mm",
            "src/macos/screen.c",
            "src/macos/screengrab.m",
            "src/macos/highlightwindow.m",
            "src/macos/window_manager.mm"
          ],
          "link_settings": {
            "libraries": [
              "$(SDKROOT)/System/Library/Frameworks/ApplicationServices.framework",
              "$(SDKROOT)/System/Library/Frameworks/Cocoa.framework"
            ]
          }
        }],
        ['OS=="win"', {
          "sources": [
            "src/win32/keycode.c",
            "src/win32/keypress.c",
            "src/win32/mouse.c",
            "src/win32/screen.c",
            "src/win32/screengrab.c",
            "src/win32/highlightwindow.c",
            "src/win32/window_manager.cc"
          ],
          "msvs_settings": {
            "VCCLCompilerTool": {
              "ExceptionHandling": 1,
              "AdditionalOptions": ["/EHsc"]
            }
          },
        
          "copies": [
            {
              "destination": "<(PRODUCT_DIR)",
              "files": [
                "3rdparty/win32/api-ms-win-crt-heap-l1-1-0.dll",
                "3rdparty/win32/api-ms-win-crt-runtime-l1-1-0.dll",
                "3rdparty/win32/api-ms-win-crt-string-l1-1-0.dll",
                "3rdparty/win32/msvcp140.dll",
                "3rdparty/win32/vcruntime140.dll",
                "3rdparty/win32/vcruntime140_1.dll"
              ]
            }
          ]
        }]
      ]
    }
  ]
} 