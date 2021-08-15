# brl-converter-server

### main action

- request:  `/convert` (method = `POST`, form data = img) 
- response: `brl plain text` that angerinaReader algorithm convert img

### Environment requirements
- python 3.8.10
- pip 21.2.2
- submodule Environment requirements 
    - `cd deploy/converter/angerinaReader` (in angerinaReader dir)
        - pip install -r requirements.txt 
        - `wget -O weights/model.t7 http://angelina-reader.ovdv.ru/retina_chars_eced60.clr.008`
