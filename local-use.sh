#!/bin/bash

# JS & CSS
sed -i 's!//cdn.bootcss.com/.*.js$!!' themes/next/_config.yml
sed -i 's!//cdn.bootcss.com/.*.css$!!' themes/next/_config.yml
sed -i 's!http://o7l077v4h.bkt.clouddn.com/!!' themes/next/_config.yml

# images
sed -i 's/- .\/pandoc-filters.js//' _config.yml
sed -i 's!http://7j1zxm.com1.z0.glb.clouddn.com/!!' themes/next/_config.yml
