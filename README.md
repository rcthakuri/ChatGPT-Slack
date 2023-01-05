![Logo](https://avatars.slack-edge.com/2022-12-31/4581005794163_f7856fa31e956e9807d7_192.png)


# ChatGPT-Slack

This project integrates `ChatGPT`, a powerful language processing AI, into Slack to provide instant answers to user questions. This chatbot, can be hosted on your local server and tunnel it via `NgRok`. It leverages ChatGPT's natural language understanding capabilities to deliver accurate responses in real-time. With this integration, users can easily access a wealth of knowledge and information directly through their Slack workspace.
Give it a try and see how ChatGPT can enhance your team's productivity!



## Usage Instructions:


#### Create Slack Bolt 

```
    Follow API Reference: (https://api.slack.com/start/building/bolt-python
```

#### Setup Ngrok account

```
    https://dashboard.ngrok.com/signup
```

#### Clone the project

```bash
  git clone https://github.com/rcthakuri/ChatGPT-Slack/
```

#### Go to the project directory

```bash
  cd ChatGPT-Slack
```

#### Install dependencies

```bash
   pip install -r requirements.txt
```



#### Create `.env` for your app
````
# SLACK KEY

SLACK_BOT_TOKEN=
PORT_FOR_SLACK_APP=
SLACK_SIGNING_SECRET=

# SLACK MANIFEST KEY

SLACK_APP_ID=
SLACK_CONFIG_REFRESH_TOKEN=

# OPEN AI KEY

OPENAI_API_KEY=
OPENAI_MODEL_ENGINE=

# NGROK KEY

NGROK_PORT=
NGROK_AUTH_TOKEN=
NGROK_REQUEST_TYPE=
````
### Start the server

```bash
  python app.py
```

### Tunnel `localhost` server via `Ngrok`

```bash
  python ngrok_tunnel_updator.py
```
## Authors

- [@rcthakuri](https://www.github.com/rcthakuri)
- [@anjanthapa26](https://www.github.com/anjanthapa26)
## Contributing

Contributions are always welcome! 

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Acknowledgements
 - [OpenAI API](https://openai.com/api/)
 - [Building an app with Bolt for Python](https://api.slack.com/start/building/bolt-python)

 - [Icon Credit](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)