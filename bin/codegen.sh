#!/bin/bash
#
# Usage: bash codegen.sh
#
# Description: Generates Python Connexion server stubs from an OpenAPI document
# using openapi-generator
#
# Requirements: Java 8+
#

java -jar ./openapi-generator-cli.jar generate  \
-i ../openapi/openapi.yaml \
-g python-flask \
-o ../ \
-t ../openapi-generator-templates \
--additional-properties=packageName=fangfangfang,serverPort=56732

mv ../fangfangfang/test/test_*.py ../tests
