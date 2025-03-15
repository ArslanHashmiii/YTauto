# 🚀🎬 YTauto 
## AI video automation framework
<p align="center">
  <a href="https://discord.gg/uERx39ru3R">
    <img src="https://dcbadge.vercel.app/api/server/uERx39ru3R?compact=true&style=flat">
  </a>
  <a href="https://star-history.com/#ArslanHashmmiii/YTauto)">
    <img src="https://img.shields.io/github/stars/ArslanHashmmiii/YTauto?style=social">
  </a>
  <a href="https://pypi.org/project/YTauto/">
    <img src="https://static.pepy.tech/personalized-badge/YTauto?period=month&units=international_system&left_color=blue&right_color=green&left_text=Downloads/month">
  </a>
  <a href="https://docs.YTauto.ai/">
    <img src="https://img.shields.io/badge/docs-visit-blue">
  </a>  
</p>

<div align="center" style="border-radius: 20px;" width="18%">
    <img src="https://github.com/ArslanHashmmiii/YTauto/assets/121462835/083c8dc3-bac5-42c1-a08d-3ff9686d18c5" alt="YTauto-logo" style="border-radius: 20px;" width="18%"/>
</div>
<div align="center">
  <a href="https://discord.gg/uERx39ru3R">
    <img src="https://img.shields.io/discord/1126042224979886160?color=7289da&logo=discord&logoColor=blue&labelColor=white&color=cyan" alt="Join our Discord" height="34">
  </a>
</div>

<div align="center">
⚡ Automating video and short content creation with AI ⚡
</div>
</br>

Follow the installation steps below for running the web app locally (running the google Colab is highly recommanded). 
Please read "installation-notes.md" for more details.
## 🎥 Showcase ([Full video on YouTube](https://youtu.be/hpoSHq-ER8U))

https://github.com/ArslanHashmmiii/YTauto/assets/121462835/a802faad-0fd7-4fcb-aa82-6365c27ea5fe
## 🎥 Voice Dubbing


https://github.com/ArslanHashmmiii/YTauto/assets/121462835/06f51b2d-f8b1-4a23-b299-55e0e18902ef

## 🌟 Show Your Support
We hope you find YTauto helpful! If you do, let us know by giving us a star ⭐ on the repo. It's easy, just click on the 'Star' button at the top right of the page. Your support means a lot to us and keeps us motivated to improve and expand YTauto. Thank you and happy content creating! 🎉 

[![GitHub star chart](https://img.shields.io/github/stars/ArslanHashmmiii/YTauto?style=social)](https://github.com/ArslanHashmmiii/YTauto/stargazers)
## 🛠️ How it works
![alt text](https://github.com/ArslanHashmmiii/YTauto/assets/121462835/fcee74d4-f856-4481-949f-244558bf3bfa)
## 📝 Introduction to YTauto 
YTauto is a powerful framework for automating content creation. It simplifies video creation, footage sourcing, voiceover synthesis, and editing tasks. Of the most popular use-cases of YTauto is youtube automation and Tiktok creativity program automation.

- 🎞️ **Automated editing framework**: Streamlines the video creation process with an LLM oriented video editing language.

- 📃 **Scripts and Prompts**: Provides ready-to-use scripts and prompts for various LLM automated editing processes.

- 🗣️ **Voiceover / Content Creation**: Supports multiple languages including English 🇺🇸, Spanish 🇪🇸, Arabic 🇦🇪, French 🇫🇷, Polish 🇵🇱, German 🇩🇪, Italian 🇮🇹, Portuguese 🇵🇹, Russian 🇷🇺, Mandarin Chinese 🇨🇳, Japanese 🇯🇵, Hindi 🇮🇳,Korean 🇰🇷, and way over 30 more languages (with EdgeTTS)

- 🔗 **Caption Generation**: Automates the generation of video captions.

- 🌐🎥 **Asset Sourcing**: Sources images and video footage from the internet, connecting with the web and Pexels API as necessary.

- 🧠 **Memory and persistency**: Ensures long-term persistency of automated editing variables with TinyDB.

## 🚀 Quick Start: Run YTauto on Google Colab (https://colab.research.google.com/drive/1_2UKdpF6lqxCqWaAcZb3rwMVQqtbisdE?usp=sharing)

If you prefer not to install the prerequisites on your local system, you can use the Google Colab notebook. This option is free and requires no installation setup.

1. Click on the link to the Google Colab notebook: [https://colab.research.google.com/drive/1_2UKdpF6lqxCqWaAcZb3rwMVQqtbisdE?usp=sharing](https://colab.research.google.com/drive/1_2UKdpF6lqxCqWaAcZb3rwMVQqtbisdE?usp=sharing)

2. Once you're in the notebook, simply run the cells in order from top to bottom. You can do this by clicking on each cell and pressing the 'Play' button, or by using the keyboard . Enjoy using YTauto!

# Instructions for running YTauto locally
This guide provides step-by-step instructions for installing YTauto and its dependencies.
To run YTauto locally, you need Docker.

## Installation Steps

To run YTauto, you need to have docker. Follow the instructions "installation-notes.md" for more details.

1. For running the Dockerfile, do this:
```bash
docker build -t short_gpt_docker:latest .
docker run -p 31415:31415 --env-file .env short_gpt_docker:latest
```
## Running runYTauto.py Web Interface

2. After running the script, a Gradio interface should open at your local host on port 31415 (http://localhost:31415)
 

## Framework overview

- 🎬 The `ContentShortEngine` is designed for creating shorts, handling tasks from script generation to final rendering, including adding YouTube metadata.

- 🎥 The `ContentVideoEngine` is ideal for longer videos, taking care of tasks like generating audio, automatically sourcing background video footage, timing captions, and preparing background assets.

- 🗣️ The `ContentTranslationEngine` is designed to dub and translate entire videos, from mainstream languages to more specific target languages. It takes a video file, or youtube link, transcribe it's audio, translates the content, voices it in a target language, adds captions , and gives back a new video, in a totally different language.

- 🎞️ The automated `EditingEngine`, using Editing Markup Language and JSON, breaks down the editing process into manageable and customizable blocks, comprehensible to Large Language Models.

💡 YTauto offers customization options to suit your needs, from language selection to watermark addition.

🔧 As a framework, YTauto is adaptable and flexible, offering the potential for efficient, creative content creation.

More documentation incomming, please be patient.


## Technologies Used

YTauto utilizes the following technologies to power its functionality:

- **Moviepy**: Moviepy is used for video editing, allowing YTauto to make video editing and rendering

- **Openai**: Openai is used for automating the entire process, including generating scripts and prompts for LLM automated editing processes.

- **ElevenLabs**: ElevenLabs is used for voice synthesis, supporting multiple languages for voiceover creation.

- **EdgeTTS**: Microsoft's FREE EdgeTTS is used for voice synthesis, supporting way many more language than ElevenLabs currently.

- **Pexels**: Pexels is used for sourcing background footage, allowing YTauto to connect with the web and access a wide range of images and videos.

- **Bing Image**: Bing Image is used for sourcing images, providing a comprehensive database for YTauto to retrieve relevant visuals.

These technologies work together to provide a seamless and efficient experience in automating video and short content creation with AI.

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it would be in the form of a new feature, improved infrastructure, or better documentation.
<p align="center">
  <a href="https://star-history.com/#ArslanHashmmiii/YTauto&Date">
    <img src="https://api.star-history.com/svg?repos=ArslanHashmmiii/YTauto&type=Date" alt="Star History Chart">
  </a>
</p>
