# brl-converter-server

### main action

- request:  `/convert` (method = `POST`, form data = img) 
- response: `brl plain text` that angerinaReader algorithm convert img

### Environment requirements
- python 3.8.10
- pip 21.2.2
- mac, ubuntu
- `pip install -r requirements.txt`
- submodule Environment requirements 
    - `cd deploy/converter/angerinaReader` (in angerinaReader dir)
        - `wget -O weights/model.t7 http://angelina-reader.ovdv.ru/retina_chars_eced60.clr.008`
- `python manage.py runserver` (development)

### deploy environment
- ubuntu
- CUDA 10.2

### ec2 deployment setup
- web server
  - https://github.com/parkhojeong/brl-converter-server/issues/11
- WSGI
  - https://github.com/parkhojeong/brl-converter-server/issues/13
