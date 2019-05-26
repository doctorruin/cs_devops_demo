# Use base python alpine image
FROM python:3.7-alpine

# Create user and group for security
RUN addgroup -S clearshark && adduser -S shark -G clearshark &&\
    mkdir /app &&\
    chown -R shark:clearshark /app &&\
    for i in `find / -perm +6000`; do chmod a-s $i; done

# Copy code into container
COPY src/HelloClearShark.py /app

# Become non-root user for security
USER shark

# set working directory
WORKDIR /app

# run this code when container is run or started
CMD ["python", "HelloClearShark.py"]

# Create Helthcheck for best practices
HEALTHCHECK CMD python HelloClearShark.py || exit 1
