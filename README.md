[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/4hPMH1rV)

## Run 
- Make sure python & pipenv is installed in your local
- cd to folder `src` & run `pipenv install`
- Instead of `flask run --debug` run `python app.py` instead
- Code should now run at port 5000
- Check API documentation at `localhost:5000/apidocs`


## Run using Docker & Gunicorn
- run `chmod +x deploy.sh` for the first time only to give permission to the file
- run `./deploy.sh` it will build docker image and eventually run it
- notes: it may take some time to download all the docker image dependencies
- code should now run at port 5001

## Docker Installation
- Windows: https://docs.docker.com/desktop/install/windows-install/
- Mac: https://docs.docker.com/desktop/install/mac-install/
- Linux: https://docs.docker.com/desktop/install/linux-install/