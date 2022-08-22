FROM python:3
COPY . /python
WORKDIR /python
RUN pip install pyTelegramBotAPI
CMD [ "python3", "bot.py" ]