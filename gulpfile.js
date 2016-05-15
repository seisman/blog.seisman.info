var gulp = require('gulp');
var cleanCSS = require('gulp-clean-css');
var uglify = require('gulp-uglify');
var htmlmin = require('gulp-htmlmin');
var htmlclean = require('gulp-htmlclean');
var imagemin = require('gulp-imagemin');

// 压缩 public 目录 css
gulp.task('clean-css', function() {
    return gulp.src('./public/**/*.css')
        .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(gulp.dest('./public'));
});

// 压缩 public 目录 html
gulp.task('minify-html', function() {
  return gulp.src('./public/**/*.html')
    .pipe(htmlclean())
    .pipe(htmlmin({
         removeComments: true,
         minifyJS: true,
         minifyCSS: true,
         minifyURLs: true,
    }))
    .pipe(gulp.dest('./public'))
});

// 压缩 public/js 目录 js
gulp.task('minify-js', function() {
    return gulp.src('./public/**/*.js')
        .pipe(uglify())
        .pipe(gulp.dest('./public'));
});

// 压缩 source/images/ 目录下的所有图片
// 生成 public 时无需再压缩
gulp.task('imagemin', function() {
    return gulp.src('./source/images/**')
        .pipe(imagemin({
            verbose: true,
        }))
        .pipe(gulp.dest('./source/images'))
});

// 执行 gulp 命令时执行的任务
gulp.task('default', [
    'minify-html','clean-css','minify-js',
]);
