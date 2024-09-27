# Ollama Python Chat Bot with Voice Recognition and TTS
### [Video Demo](https://youtu.be/a1BGg6XoiQ8?si=5tQEy0_8Blsf2NFf)
#### Description:
This project is my attempt to recreate the voice-chat feature found on the smartphone version of OpenAI's ChatGPT.

I tried unsing llama.cpp but I ended up using Ollama to run their already curated GGUF LLMs (I chose Llama3.1)
This python script, takes your voice input or a text prompt, sends it to the localhost URL where Ollama is running, and then returns a series of words/chunks that are then printed one after the other.

WHen using the voice recognition feature, a sound file is recorded while holding the 'left shift' button and on release is then saved to the root directory.

Right after that, the voice is converted to text using 'whisper' a library that recognizes both the text and detects the language (I didn't use it for that, used langdetect instead in the text_to_speech module.).

The transcript is then fed as normal text to the Ollama server as if it were typed, and the response is served.

After each response, the script reads the content of it using the module 'edge_tts'. Like I said earlier,(not using whisper to detect language at voice-to-text phase) language detection is performed on this level and the narration voice is then chosen accordingly.

The prompting keeps going in a loop after each response, until the user exits.

Upon exit a function called 'clean_up' deletes any remenants of the recorded user's voice and the chat-bot's audio response.

I'm not yet satisfied untill I manage to add short memory context, and store history of older conversations to make the chat-bot's experience customised to the user.

## INSTALLATION

This project requires the following:

- Download and install Ollama on your machine :https://ollama.com/
- To download a Language model, Run in cmd: `ollama run llama3.1:8b`
- FFMPEG : You could download chocolatey and run `choco install ffmpeg` or get it some other way.
-  ` pip install -r requirements.txt`
- Pytorch (Optimally CUDA version if you have an NVIDIA GPU) using this pip command that you can customize through https://pytorch.org/get-started/locally/:
    `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`
- Important:
      Make sure your Virtual Environment folder is named 'venv', since text-to-speech.py needs to run using that directory with python.exe and the packages within it.
      ! Currently, PyTorch on Windows only supports Python 3.8-3.11; Python 2.x is not supported.
      Install python 3.10 then make a virtual environemt with it.
      
  Use `pip install --upgrade setuptools wheel` in case you encounter the following error:
  
  `× Getting requirements to build wheel did not run successfully.
  │ exit code: 1`

## USAGE

- Run `project.py`
  #### To get rid of a long unnecessary message concerning Whisper and Torch, CTRL+CLICK on the code line in the image bellow:
  ![image](https://github.com/user-attachments/assets/6184bf20-e385-48ba-a8bf-2dd27e6d753b)
  #### Then add the argument underlined in green:
  ![image](https://github.com/user-attachments/assets/505ce6bc-a31d-40df-a479-a14a9052b876)

- Press and hold 'Left Shift' then speak, on release an answer will be generated in text then spoken outloud.
- If you press 'Escape' you'll be able to text chat with the bot.
- CTRL+C to interrupt audio.
- You can type exit() and Enter to close the script.

Thank you [edx](https://www.edx.org/cs50) and [the Harvard University](https://cs50.harvard.edu/)
