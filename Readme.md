Ollama Python Chat Bot with Voice Recognition and TTS

As impressive as AI chatbots were at first, conversing with them vocally on the ChatGPT app on the phone took it to the next level.

I mainly use the computer and not much of a phone user other than some Youtube binging sometimes.

I knew I wanted that capability to just be able to speak to a ChatBOt on a whim to discuss something on my mind and process ideas in an interractive way.

When I started coding this and got to the TTS part, I also needed to find voices that were not as robotic as the typical Google or Microsoft default voices.

Thank to ChatBots themselves, I learned how to solve many problems along the way, building this project one piece at a time.
It only took a plan, and a systematic approach to complement things to eachother like a puzzle.

To start being technical, this project is based on Ollama for the AI server and LLMs that come with it specifically, I went with Llama3.1:8b.

I tried using GGUFs I had downloaded before with Llama.CPP but it was just too much for me as I struggled to compile source code at first. But I learned a lot even though I didn't end up going with it.

INSTALLATION

This project requires the following:

- Ollama itself :https://ollama.com/
- To download a Language model, Run in cmd: ollama run llama3.1:8b
- FFMPEG : You could download chocolatey and run 'choco install ffmpeg' or get it some other way.
- Pytorch (Optimally CUDA version if you have an NVIDIA GPU) using this pip command that you can customize through https://pytorch.org/get-started/locally/:
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
- Important:
      Make sure your Virtual Environment folder is named 'venv', since text-to-speech.py needs to run using that directory with python.exe and the packages within it.
      ! Currently, PyTorch on Windows only supports Python 3.8-3.11; Python 2.x is not supported.
      Install python 3.11 : winget install 'python3.11'
      then make a virtual environemt with it:
      python3.11 -m venv venv
  Make sure your newly installed python version was added to Environemnt Variables in user Variable -> PATH liek shown in the screenshot bellow.
  ![image](https://github.com/user-attachments/assets/845815ba-6633-469a-a4c9-6b8fc06dda55)



- And of course, use : 
    pip install requirements.txt 

USAGE

- Run project.py

Thank you [edx](https://www.edx.org/cs50) and [the Harvard University](https://cs50.harvard.edu/)
