from python:3.7.6

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user


# Set the working directory
WORKDIR /opt/mobile-prices-api


# Install requirements
ADD ./api /opt/mobile-prices-api/
RUN pip install --upgrade pip
RUN pip install -r /opt/mobile-prices-api/requirements.txt

RUN chmod +x /opt/mobile-prices-api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
