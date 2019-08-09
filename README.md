![fangfangfang](images/logo.png | width=300)

# fangfangfang

fangfangfang is a web application that allows you to defang and refang URLs in text.

Many applications convert URLs in documents to clickable links. These links could be malicious, and users may accidentally click on them. The goal of defanging is to prevent these URLs from being clickable but still human-readable. Refanging, on the other hand, involves taking a defanged piece of text and converting it back to the original text.

## Disclaimer

All information and code are provided for educational purposes only. The author is not responsible for any direct or consequential damage or loss arising from any person or organization acting or failing to act on the basis of information contained in this repository.

Please refer to the [LICENSE](LICENSE.md).

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Usage

Start the docker container:

```
docker-compose up
```

Open your browser and navigate to:

[http://localhost:56732/](http://localhost:56732/)

If everything is working, you should see the following page:

TODO

To stop the application, press `Ctrl+C` from your terminal.

## Known Issues

- In the generated documentation, examples like `hxxp:\/\/somewebsite[dot]com` are showing up as `hxxp:\\/\\/somewebsite[dot]com` where the backslash is repeated twice. Appears to be a bug in Swagger UI.

## Credits

- [uwsgi-nginx-flask-docker](https://github.com/tiangolo/uwsgi-nginx-flask-docker)
- [openapi-generator](https://github.com/OpenAPITools/openapi-generator)
- [defang](https://pypi.org/project/defang/)
- [IOC Fanger](https://github.com/ioc-fang/ioc_fanger)
