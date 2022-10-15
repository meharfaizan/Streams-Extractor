FROM python:3.1
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
COPY . .
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
