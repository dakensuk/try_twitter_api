# How to use

## Case : Python
```
cd python; ls
--> please check Dockerfile exists

# Build docker image
docker image build -t <name> .

# Prepare Twitter API configuration file
vim config.py
--> write the following configuration

consumer_key = '< your consumer_key >'
consumer_secret = '< your consumer_secret >'
access_token = '< your access_token >'
access_token_secret = '< your access_token_secret >'

# Execute command
docker run --rm  -v $PWD:/usr/src/app -it <name> python keyword_search.py

# You can check file output as well.
cat result.txt

```
