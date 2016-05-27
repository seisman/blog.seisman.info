本目录中包含了一些曾经使用过的脚本。

- `qiniu.py`: 将PDF、图片、JS和CSS同步到七牛云中
- `pandoc-filter.js`: 在所有图片的路径之前加上七牛云的前缀，用于CDN加速图片，该脚本需要
  与 [pandoc-filter-node](https://github.com/mvhenderson/pandoc-filter-node)
  一起使用，并需要修改 `_config.yml`
- `local-use.sh`: 修改配置文件，不使用CDN而直接引用项目内的JS和CSS文件，以方便用户在本地
  预览
