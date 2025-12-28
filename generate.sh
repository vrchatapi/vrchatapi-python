#!/usr/bin/env bash

if [ ${#} -le 1 ]
then
  echo "Usage: generate.sh <openapi.yaml> <version>" >&2
  exit 1
fi
rm vrchatapi docs -rf

./node_modules/\@openapitools/openapi-generator-cli/main.js generate \
-g python-legacy \
--additional-properties=packageName=vrchatapi,projectName=vrchatapi \
--git-user-id=vrchatapi \
--git-repo-id=vrchatapi-python \
-o . \
-i "${1}" \
--http-user-agent="vrchatapi-py"

# Fix description, keywords, etc...
# Echo to trim whitespace
sed -i "s/VERSION = \"1.0.0\"/VERSION = \"${2}\"/" ./setup.py
sed -i 's/description="VRChat API Documentation"/description="VRChat API Library for Python"/' ./setup.py
sed -i 's/keywords=\["OpenAPI", "OpenAPI-Generator", "VRChat API Documentation"\]/keywords=["vrchat", "vrchatapi", "vrc"]/' ./setup.py

# Fix long_description error during pypi upload
sed -i 's/.*VRChat API Banner.*/abcdefvrc/g' ./setup.py
sed -i '/abcdefvrc/r README.md' ./setup.py
sed -i 's/abcdefvrc//g' ./setup.py

# Remove messily pasted markdown at top of every file
find vrchatapi -type f -exec sed -i '/VRChat API Banner/d' {} \;

# Enable Global cookies
patch ./vrchatapi/rest.py < ./patches/cookiejar.patch

# Make 2fa required error readable
patch ./vrchatapi/rest.py < ./patches/error_2fa_verify_readable.patch

# Add common symbols to safe path parameter symbols
patch ./vrchatapi/configuration.py < ./patches/safe_param_symbols.patch

# Boolean to lower str conversion for query parameters
patch ./vrchatapi/api_client.py < ./patches/query_param_bool.patch

# Add URL encoding to basic auth parameters
patch ./vrchatapi/configuration.py < ./patches/encode_basic_auth.patch