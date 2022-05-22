# FTP-Deploy-Action-Python

This is the Python version of FTP Deploy Action, inspired by Node.js version [FTP-Deploy-Action](https://github.com/SamKirkland/FTP-Deploy-Action).  
This package is a [Composite Action](https://docs.github.com/en/actions/creating-actions/creating-a-composite-action) that relies on [actions/setup-python@v3](https://github.com/actions/setup-python).

# Usage Example

Place the following scripts in `./.github/workflows/main,yml`

```yml
on: 
  push:
    branches: [master]

name: 🚀 Deploy on push - Python

jobs:
  Deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python3.9
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'
        architecture: 'x64'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install pyftpsync==4.0.0a3
    - name: FTP Deploy
      uses: lujiaying/FTP-Deploy-Action-Py3.9@v1.0
      with:
        host: ${{ secrets.ftp_host }}
        user: ${{ secrets.ftp_username }}
        passwd: ${{ secrets.ftp_password }}
        port: 21
        local_dir: ./
        remote_dir: /
        exclude: .git,.github,.DS_Store,README*,LICENSE
        dry_run: False
```
