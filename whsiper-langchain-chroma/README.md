# OpenAI Whisper API ChromaDB and LangChain Demo
This repository contains code and resources for demonstrating the power of OpenAI's Whisper API in combination with ChromaDB and LangChain for asking questions about your audio data. 
The demo showcases how to transcribe audio data into natural language with the Whisper API. The project also demonstrates how to vectorize data in chunks and get embeddings using OpenAI embeddings model.

We then use [LangChain](https://github.com/hwchase17/langchain) to ask questions based on our data which is vectorized using OpenAI embeddings model. 
I used [Chroma](https://github.com/chroma-core/chroma) a database for storing and querying vectorized data.

## Getting Started
To get started with the demo, you will need to have Python (I use Python 3.8) installed on your machine. You will also need to install the required Python packages by running the following command:
`pip install -r requirements.txt`

All the `(m4a, mp3, mp4, mpeg, mpga, wav, webm)` files need to be in the `/files` folder.

 **Run the `whisper.py` file to generate a .txt file out of your audio data**

Now you can run `ask_the_audio.py`.

**Simply change the `print(genie.ask("Can you tell me the formula for Linear Regression?"))` in the `ask_the_audio.py` file to whatever question you want to ask.**


## Note
If you videos which exceed approx 25 MB you'd need to chunk the videos into smaller videos because of the API characters limit.


## Video

In my video I use the following video audio: https://youtu.be/4qpI4T6_bUw and three other audio files I recorded myself.
[![Screenshot](https://i.ibb.co/LCzVkff/embedding-vid.jpg)](https://youtu.be/ytt4D5br6Fk)
