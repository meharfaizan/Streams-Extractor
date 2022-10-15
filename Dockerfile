FROM python:3.9.2-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
COPY . .
RUN git clone https://github.com/TroJanzHEX/Streams-Extractor
cd Streams-Extractor
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
