![DeskGPT](https://raw.githubusercontent.com/jNsatiable/DeskGPT/main/resources/DeskGPT.ico)

# DeskGPT
A simple app that allows you to run 'ChatGPT' on your desktop using OpenAI's GPT-3 family of Large Language Models. 
## Dependencies
* [Python](https://www.python.org/downloads/)
* Python modules
  * [openai](https://platform.openai.com/docs/api-reference?lang=python) `pip install openai`
  * [configparser](https://docs.python.org/3/library/configparser.html) `pip install configparser`
## Installation
  1. Download source code from the [release page](https://github.com/jNsatiable/DeskGPT/releases).
  2. Extract files on your computer.
## Running the program
  1. Double click on DeskGPT.py
  2. On initial run, the program will ask for the OpenAI API Key which you can find [here](https://platform.openai.com/account/api-keys).
  ![image](https://user-images.githubusercontent.com/125757323/222952570-1192c447-1f79-41c7-8ae6-3e40e929cbd9.png)
  3. Done. You may now ask DeskGPT anything :)
  ![image](https://user-images.githubusercontent.com/125757323/222954232-3b638aaa-e31e-4309-bd69-69dbbca43127.png)
## Modifying Parameters
The app pretty much works straight out of the box with four of the more prominent parameters set to the following settings:
```
engine = text-davinci-003
max_tokens = 200
n = 1
temperature = 0.7
```
If you want to modify these settings:
 1. Open `config.cfg` file from resources folder.
 2. Modify the entries after the equal sign. 
<video src=https://user-images.githubusercontent.com/125757323/222954900-f91d87d1-48b0-4682-a4d0-89dfe43519ce.mp4> </video>
For more information regarding these settings: Visit [OpenAI API Reference](https://platform.openai.com/docs/api-reference/models/retrieve)
## JUST NEED A QUICK FIX?
If you're just looking for a hassle-free setup without having to mess with Python installations, etc., you may download the executable version [here](https://bit.ly/DeskGPT). Make sure to download the whole DeskGPT zip folder. Installing and running would be similar to the above.
## Authors
[jNsatiable](https://www.linkedin.com/in/joefer-traya/)

