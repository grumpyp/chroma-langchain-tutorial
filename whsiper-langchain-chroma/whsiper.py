import os
import openai
import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")


class WhisperExporter:

    def __init__(self):
        self._textes = []

    def whisper_to_text(self, path: str):
        f = open(f".{path}", "rb")
        transcript = openai.Audio.transcribe("whisper-1", file=f)
        self.textes.append(transcript["text"])
        return f"transcribed {path}"

    @staticmethod
    def to_txt(text: str, path: str = str(datetime.datetime.now())):
        with open(f"{path}.txt", "w") as f:
            f.write("".join(text))
            f.close()
        return f"saved to {path}"

    @property
    def textes(self):
        return self._textes



if __name__ == "__main__":
    exporter = WhisperExporter()
    # loop over all files if they end with the allowed endings
    for file in [f for f in os.listdir("./files") if os.path.splitext(f)[1] in [".m4a", ".mp3", ".mp4", ".mpeg", ".mpga", ".wav", ".webm"]]:
        exporter.whisper_to_text(f"/files/{file}")
    exporter.to_txt(exporter.textes)
