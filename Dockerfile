FROM python:3.7-alpine

RUN addgroup -S clearshark && adduser -S doctorruin -G clearshark &&\
    mkdir /app &&\
    chown -R doctorruin:clearshark /app

COPY src/HelloClearShark.py /app

USER doctorruin

WORKDIR /app

CMD ["python", "HelloClearShark.py"]