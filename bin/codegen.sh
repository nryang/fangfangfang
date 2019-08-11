#!/bin/bash
#
# Usage: bash codegen.sh
#
# Description: This downloads the openapi-generator JAR (if it does not already
# exist) and generates Python Connexion server files from an OpenAPI document
# using openapi-generator
#
# Requirements: Java 8+
#

wget -nc http://central.maven.org/maven2/org/openapitools/openapi-generator-cli/4.1.0/openapi-generator-cli-4.1.0.jar -O openapi-generator-cli.jar

java -jar ./openapi-generator-cli.jar generate  \
-i ../openapi/openapi.yaml \
-g python-flask \
-o ../ \
-t ../openapi-generator-templates \
--additional-properties=packageName=fangfangfang,serverPort=56732

mv ../fangfangfang/test/test_*.py ../tests
