#!/bin/bash

rm vrchatapi docs -rf
openapi-generator-cli generate \
-g python \
--additional-properties=packageName=vrchatapi,projectName=vrchatapi \
--git-user-id=vrchatapi \
--git-repo-id=vrchatapi-python \
-o . \
-i https://vrchatapi.github.io/specification/openapi.yaml \
--http-user-agent="vrchatapi-py"

# Enable Global cookies
sed -i '/cert_reqs = ssl.CERT_NONE/r patches/cookiejar_init.py' ./vrchatapi/rest.py
sed -i '/headers = headers or {}/r patches/cookiejar_add.py' ./vrchatapi/rest.py

sed -i 's/if _preload_content/abcdefvrc\n\n        if _preload_content/g' ./vrchatapi/rest.py
sed -i '/abcdefvrc/r patches/cookiejar_extract.py' ./vrchatapi/rest.py
sed -i 's/        abcdefvrc//g' ./vrchatapi/rest.py

# Fix long_description error during pypi upload
sed -i 's/.*VRChat API Banner.*/abcdefvrc/g' ./setup.py
sed -i '/abcdefvrc/r README.md' ./setup.py
sed -i 's/abcdefvrc//g' ./setup.py
sed -i '/license/a long_description_content_type="text/markdown",' ./setup.py