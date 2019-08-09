#!/bin/bash
#
# Usage: bash codegen.sh
#
# Description: Generates Python Flask server stubs from an OpenAPI document
# using openapi-generator
#
# Requirements: Java 8+
#

java -jar ./openapi-generator-cli.jar generate  \
-i ../app/openapi/openapi.yaml \
-g python-flask \
-o ../app \
-t ../app/gen-templates \
--additional-properties=packageName=gen
