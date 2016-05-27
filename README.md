## SeisMan博客

本项目是 [SeisMan博客][] v2.0的源码。博客v2.0使用 [Hexo][] 作为网站生成引擎，
主题修改自 [NexT][] by [iissnan][]。

### 简介

博客自v2.0版本开始，将网站生成引擎配置、主题和博文独立开来，三者位于独立的仓库中。
主题和博文均作为网站生成引擎（即本项目）的子模块。
本项目会追踪主题的 `seisman` 分支和博文的 `master` 分支。

- 引擎： [![Hexo](https://img.shields.io/badge/Hexo-master-blue.svg)](https://github.com/seisman/seisman.info/tree/master)
- 主题： [![NexT](https://img.shields.io/badge/NexT-seisman-blue.svg)](https://github.com/seisman/hexo-theme-next/tree/seisman)
- 博文： [![Posts](https://img.shields.io/badge/Posts-master-blue.svg)](https://github.com/seisman/seisman.info.posts/tree/master)

这样的设计具有如下一些优点：

1. 主题的 `master` 分支可以与 [NexT]() 保持同步更新，方便 `seisman` 分支进行rebase
2. 可以随时切换主题，而不用担心旧主题占据大量的项目空间
3. Hexo或者其他绝大多数博客引擎都使用 `![AltText](/images/xxx.png)` 这种“伪绝对路径”的
   方式引用图片，这样做使得 markdown 文件在 GitHub 上无法正常显示图片，而将博文存放在
   单独的仓库中则图片可以正常显示
4. 若未来切换博客引擎，所有博文可在少量修改的前提下迁移到新的博客引擎下，且能够保留
   所有修订历史

[SeisMan博客]: https://seisman.info
[Hexo]: https://hexo.io/
[NexT]: https://github.com/iissnan/hexo-theme-next
[iissnan]: https://github.com/iissnan

### 本地预览

读者可以通过访问网址 https://seisman.info 阅读博客内容，也可以在自己的机器上离线预览博客。
只需要通过如下几个简单的步骤，即可实现离线预览。整个过程大概不到10分钟（前提是网速还可以，
相关网站没有被墙）。

#### 初次使用

```bash
# 1. 安装 [nvm](https://github.com/creationix/nvm)
$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.1/install.sh | bash
$ exec $SHELL -l

# 2. 安装 [Node.js](https://nodejs.org/)
$ nvm install v4

# 3. 安装 [pandoc](http://pandoc.org/)
# Ubuntu 用户
$ sudo apt-get install pandoc
# CentOS 用户
$ sudo yum install pandoc

# 4. Clone项目源码至本地
$ git clone https://github.com/seisman/seisman.info.git
$ cd seisman.info

# 5. 初始化并更新子模块
$ git submodule update --init --recursive --remote

# 6. 全局安装 [Hexo](https://hexo.io/)
$ npm install hexo gulp -g

# 7. 安装项目依赖
$ npm install

# 8. 生成网站，到 `http://localhost:4000/` 查看
$ hexo s
```

#### 更新以追踪博客的更新

通过如下两个命令即可将本地的博客更新至最新版本：
```bash
$ git pull
$ git submodule update --remote
```

### 优化

#### 安装最新版 pandoc

本项目使用 pandoc 作为 markdown 解析器，生成网页时对 pandoc 版本无要求，但生成 PDF 时
要求 pandoc 版本>1.16。因而如果想要本地生成 PDF 则需要手动安装最新版 pandoc。

1. 下载：到 https://github.com/jgm/pandoc/releases/latest 下载最新版本deb安装包

2. 安装

   对于Ubuntu用户
   ```
   $ sudo dpkg -i pandoc-xxx-amd64.deb
   ```

   对于CentOS用户
   ```
   $ ar p pandoc-xxx-amd64.deb data.tar.gz | sudo tar xvz --strip-components 2 -C /usr
   ```

3. 检查pandoc版本
   ```
   $ pandoc -v
   ```

#### 网页压缩与优化

对HTML、CSS、JS以及图片进行压缩以减小数据量，加快访问速度。

每次生成网站并发布之前均需要对HTML、CSS、JS进行压缩：
```bash
# 安装相关依赖（在之前已经执行过了，无须再执行）
$ npm install gulp -g
$ npm install gulp gulp-clean-css gulp-imagemin gulp-uglify --save
$ npm install gulp-htmlclean gulp-htmlmin --save
# 生成网页
$ hexo g
# 压缩 HTML, JS 和 CSS
$ gulp
# 部署到GitHub
$ hexo d
```

压缩图片只需要偶尔执行一次即可：
```bash
$ gulp imagemin
```

#### 网页自动刷新

`hexo s` 会自动监测所有文件的变化，但不会去主动刷新浏览器，因而需要
经常按F5以刷新页面。`hexo-browsersync` 插件可以实现浏览器的自动刷新，
但该插件会导致个别HTML页面的尾部出现乱码，因而仅供个人使用，不写到
`package.json` 中。

```bash
$ npm install -g browser-sync
$ npm install hexo-browsersync
# 在 _config.yml 中指定使用 hexo-browsersync 插件
$ hexo s
```
