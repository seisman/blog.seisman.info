## SeisMan博客

本项目是 [SeisMan博客][] v3.0的源码。博客v3.0使用 [Hugo][] 作为网站生成引擎，
主题为 [Even][]。

### 简介

博客自v2.0版本开始，将网站生成引擎配置、主题和博文独立开来，三者位于独立的仓库中。
主题和博文均作为网站生成引擎（即本项目）的子模块。
本项目会追踪主题的 `seisman` 分支和博文的 `master` 分支。

- 引擎： [![Hugo](https://img.shields.io/badge/Hugo-master-blue.svg)](https://github.com/seisman/blog.seisman.info/tree/master)
- 主题： [![Even](https://img.shields.io/badge/Even-seisman-blue.svg)](https://github.com/seisman/hugo-theme-even/tree/seisman)
- 博文： [![Posts](https://img.shields.io/badge/Posts-master-blue.svg)](https://github.com/seisman/seisman.info.posts/tree/master)

这样的设计具有如下一些优点：

1. 主题的 `master` 分支可以与上游 [Even]() 的master保持同步更新，方便 `seisman`
   分支进行rebase
2. 可以随时切换主题，而不用担心旧主题占据大量的项目空间
3. Hexo或者其他绝大多数博客引擎都使用 `![AltText](/images/xxx.png)` 这种“伪绝对路径”的
   方式引用图片，这样做使得 markdown 文件在 GitHub 上无法正常显示图片，而将博文存放在
   单独的仓库中则图片可以正常显示
4. 若未来切换博客引擎，所有博文可在少量修改的前提下迁移到新的博客引擎下，且能够保留
   所有修订历史

[SeisMan博客]: https://blog.seisman.info
[Hugo]: https://gohugo.io/
[Even]: https://github.com/seisman/hugo-theme-even

### 本地预览

读者可以通过直接访问 [SeisMan博客][] 阅读博客内容，也可以在自己的机器上离线预览博客。
只需执行如下几个步骤，即可实现在Linux、Windows、macOS下实现网站的离线预览。整个
过程不超过5分钟（前提是网速还可以，相关网站没有被墙）。

#### 初次使用

1.  安装 [Hugo][]

    本博客使用 Hugo 作为博客引擎，Hugo具有跨平台、速度快等特性。

    到 [releases](https://github.com/gohugoio/hugo/releases) 页面下载自己平台对应的
    文件，解压，并将可执行文件放在PATH所在目录即可。

2.  Clone项目源码至本地

        $ git clone --recursive https://github.com/seisman/blog.seisman.info.git

3.  预览网站

        $ cd blog.seisman.info
        $ hugo server

    浏览器打开 `http://localhost:1314/` 以离线查看

#### 更新以追踪博客的更新

通过如下两个命令即可将本地的博客更新至最新版本：
```bash
$ git pull
$ git submodule update --remote
```
