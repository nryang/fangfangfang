<img src="/images/logo.png" width="300">

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

Build the docker container:

```
docker-compose build
```

Start the docker container:

```
docker-compose up
```

Open your browser and navigate to:

[http://localhost:56732/](http://localhost:56732/)

If everything is working, you should see the following page:

TODO

fangfangfang also provides API endpoints for defanging or refanging text. You
can access the API documentation in your browser by navigating to:

[http://localhost:56732/api/ui](http://localhost:56732/api/ui)

If the API docs are working, you should see the following page:

![Generated API documentation](/images/api-docs.png)

To stop the application, press `Ctrl+C` from your terminal.

## Known Issues

- In the generated documentation, examples like `hxxp:\/\/somewebsite[dot]com` are showing up as `hxxp:\\/\\/somewebsite[dot]com` where the backslash is repeated twice. Appears to be a bug in Swagger UI.

## Developer Notes

This project uses an API-first approach. The API spec is written in OpenAPI 3
and is defined in [openapi/openapi.yaml](openapi/openapi.yaml).

[openapi-generator](https://github.com/OpenAPITools/openapi-generator) takes the
OpenAPI spec and auto-generates the [controllers](fangfangfang/controllers),
[models](fangfangfang/models), and [basic integration tests](fangfangfang/test).

To auto-generate the files (requires [Java 8+](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)):

```
cd bin
./codegen.sh
```

The auto-generated [controllers](fangfangfang/controllers) call the
implementation controller modules like [default_controller_impl.py](fangfangfang/controllers/default_controller.py).

[Connexion](https://connexion.readthedocs.io/en/latest/) uses the
[controllers](fangfangfang/controllers) to serve the REST
endpoints. It also serves static files like the
[Swagger UI documentation](https://swagger.io/tools/swagger-ui/).

## Credits

- [uwsgi-nginx-flask-docker](https://github.com/tiangolo/uwsgi-nginx-flask-docker) for Docker image
- [Connexion](https://github.com/zalando/connexion) for serving REST endpoints and Swagger docs
- [openapi-generator](https://github.com/OpenAPITools/openapi-generator) for code generation
- [homoglyphs](https://pypi.org/project/homoglyphs/) for converting to and from homoglyphs
- [defang](https://pypi.org/project/defang/) for example test cases
- [IOC Fanger](https://github.com/ioc-fang/ioc_fanger) for example test cases
