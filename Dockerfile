FROM python:3.10
EXPOSE 5009
RUN mkdir -p /opt/services/bot/LTCbot1
WORKDIR /opt/services/bot/LTCbot1

RUN mkdir -p /opt/services/bot/LTCbot1/requirements
ADD requirements.txt /opt/services/bot/LTCbot1/

COPY . /opt/services/bot/LTCbot1/

RUN pip install -r requirements.txt
CMD ["python", "/opt/services/bot/LTCbot1/main.py"]