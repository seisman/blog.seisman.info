#!/usr/bin/env node
/*
 *  Pandoc filter to deal with images
 *      ![](/images/xxx.png) => ![](/absolute/path/to/images/xxx.png)
 *
 *  Usage:
 *      pandoc --filter ./filter.js post.md -t markdown
 */

var pandoc = require('pandoc-filter');
var cdn = "http://7j1zxm.com1.z0.glb.clouddn.com";

function action(type, value, format, meta) {
    if (type === 'Image') value[2][0] = cdn + value[2][0];
}

pandoc.stdio(action);
