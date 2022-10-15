FROM python:3.7
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
COPY . .
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
