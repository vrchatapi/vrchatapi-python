#!/bin/bash

npm install @openapitools/openapi-generator-cli

rm vrchatapi docs -rf

./node_modules/\@openapitools/openapi-generator-cli/main.js generate \
-g python-legacy \
--additional-properties=packageName=vrchatapi,projectName=vrchatapi \
--git-user-id=vrchatapi \
--git-repo-id=vrchatapi-python \
-o . \
-i https://raw.githubusercontent.com/vrchatapi/specification/gh-pages/openapi.yaml \
--http-user-agent="vrchatapi-py"

# Enable Global cookies
sed -i '/cert_reqs = ssl.CERT_NONE/r patches/cookiejar_init.py' ./vrchatapi/rest.py
sed -i '/headers = headers or {}/r patches/cookiejar_add.py' ./vrchatapi/rest.py

sed -i 's/if _preload_content/abcdefvrc\n\n        if _preload_content/g' ./vrchatapi/rest.py
sed -i '/abcdefvrc/r patches/cookiejar_extract.py' ./vrchatapi/rest.py
sed -i 's/        abcdefvrc//g' ./vrchatapi/rest.py

# Fix description, keywords, etc...
# Echo to trim whitespace
VERSION=`echo $(cat setup.py | grep "The version of the OpenAPI document" | cut -d ":" -f 2)`
sed -i "s/VERSION = \"1.0.0\"/VERSION = \"$VERSION\"/" ./setup.py
sed -i 's/description="VRChat API Documentation"/description="VRChat API Library for Python"/' ./setup.py
sed -i 's/keywords=\["OpenAPI", "OpenAPI-Generator", "VRChat API Documentation"\]/keywords=["vrchat", "vrchatapi", "vrc"]/' ./setup.py

# Fix long_description error during pypi upload
sed -i 's/.*VRChat API Banner.*/abcdefvrc/g' ./setup.py
sed -i '/abcdefvrc/r README.md' ./setup.py
sed -i 's/abcdefvrc//g' ./setup.py

# Remove messily pasted markdown at top of every file
find vrchatapi -type f -exec sed -i '/VRChat API Banner/d' {} \;

# Make 2fa required error readable
patch ./vrchatapi/rest.py < ./patches/error_2fa_verify_readable.patch