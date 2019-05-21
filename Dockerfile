FROM python:3.7-alpine

RUN addgroup -S clearshark && adduser -S doctorruin -G clearshark &&\
    mkdir /app &&\
    chown -R doctorruin:clearshark /app &&\
    for i in `find / -perm +6000`; do chmod a-s $i; done

COPY src/HelloClearShark.py /app

USER doctorruin

WORKDIR /app

CMD ["python", "HelloClearShark.py"]

HEALTHCHECK CMD python HelloClearShark.py || exit 1