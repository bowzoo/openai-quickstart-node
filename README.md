# OpenAI API Quickstart - Python example app

This is an example pet name generator app used in the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).


9. Build Docker image


  ```bash
  $ docker build -t flaskgpt .
  ```

10. Run a container named: omg and since i like complicate things so port = 5008

  ```bash
  $ docker run -d  -p 5002:5008 --name omg flaskgpt -- -h 0.0.0.0 -p 5008
  ```

  ```bash
  $ docker ps
  CONTAINER ID   IMAGE      COMMAND               CREATED         STATUS         PORTS                    NAMES
  497c15cbc2ba   flaskgpt   "flask run -p 5008"   2 minutes ago   Up 2 minutes   0.0.0.0:5002->5008/tcp   omg
  ```


11. Visit where when setup with docker ?

    http://0.0.0.0:5002/qa


12. What about kubernetes

    make sure delete the container omg we previously run

    ```
    docker rm omg -f
    kubectl create -f deployment.yaml
    kubectl create -f service.yaml
    ```

13. where to visit when using kubernetes?

    http://0.0.0.0:30888/qa
