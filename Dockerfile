FROM alpine:3.7

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY app.py /src/app.py

EXPOSE  8081
CMD ["python", "/src/app.py", "-p 8081"]
