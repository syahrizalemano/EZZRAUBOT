# We're using Ubuntu 20.10
FROM alfianandaa/alf:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/syahrizalemano/EZZRAUBOT /home/EZZRAUBOT/
RUN mkdir /home/EZZRAUBOT/bin/
WORKDIR /home/EZZRAUBOT/

CMD ["python3","-m","userbot"]
