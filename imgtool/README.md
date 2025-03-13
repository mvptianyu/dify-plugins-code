# ImgTool Dify Plugin

- **Author:** mvptianyu
- **Version:** 1.0.0
- **Type:** tool


## Overview

A powerful image tool plugin for Dify, designed to convert image file or url into bytes or base64 string.

## Supported Sub Toolkits

- **ImgFileContent**

  Can convert local uploaded or genenrate image file into bytes or base64 string.
  
  > Inputs:
  - Local image file (`.jpg|.png`)
  - Return base64 choice (`true|false`)

  > Output:
  - Text string (`bytes|base64`)

    ```json
    {
        "text": "bytes or base64 string"
    }
    ```

- **ImgUrlContent**

  Can convert remote image url into bytes or base64 string.
  
  > Inputs:
  - Remote image url (`.jpg|.png`)
  - Return base64 choice (`true|false`)

  > Output:
  - Text string (`bytes|base64`)

    ```json
    {
        "text": "bytes or base64 string"
    }
    ```