'use strict';
const path = require('path');
const gulp = require('gulp');
const pkg = require('./package.json');
const $ = require('gulp-load-plugins')();
const gulpSequence = require('gulp-sequence');
const importOnce = require('node-sass-import-once');
const stylemod = require('gulp-style-modules');
const browserSync = require('browser-sync').create();
const gulpif = require('gulp-if');
const combiner = require('stream-combiner2');
const bump = require('gulp-bump');
const argv = require('yargs').argv;

const sassOptions = {
  importer: importOnce,
  importOnce: {
    index: true,
    bower: true
  }
};

gulp.task('clean', function() {
  return gulp.src(['.tmp', 'css'], {
    read: false
  }).pipe($.clean());
});

function handleError(err){
  console.log(err.toString());
  this.emit('end');
}

function buildCSS(){
  return combiner.obj([
    $.sass(sassOptions),
    $.autoprefixer({
      browsers: ['last 2 versions', 'Safari 8.0'],
      cascade: false
    }),
    gulpif(!argv.debug, $.cssmin())
  ]).on('error', handleError);
}

gulp.task('sass', function() {
  return gulp.src(['./sass/*.scss', '!./sass/*sketch.scss'])
    .pipe(buildCSS())
    .pipe(gulpif(/.*predix/,
      $.rename(function(path){
        path.basename = new RegExp('.+?(?=\-predix)').exec(path.basename)[0];
      })
    ))
    .pipe(stylemod({
      moduleId: function(file) {
        return 'px-dark-theme-styles';
      }
    }))
    .pipe(gulp.dest('.'))
    .pipe(browserSync.stream({match: 'css/*.html'}));
});

gulp.task('watch', function() {
  gulp.watch(['sass/*.scss'], ['sass']);
});

gulp.task('serve', function() {
  browserSync.init({
    port: 8080,
    notify: false,
    reloadOnRestart: true,
    logPrefix: `${pkg.name}`,
    https: false,
    server: ['./', 'bower_components'],
  });

  gulp.watch(['css/*-styles.html', '*.html', '*.js']).on('change', browserSync.reload);
  gulp.watch(['sass/*.scss'], ['sass']);

});

gulp.task('bump:patch', function(){
  gulp.src(['./bower.json', './package.json'])
  .pipe(bump({type:'patch'}))
  .pipe(gulp.dest('./'));
});

gulp.task('bump:minor', function(){
  gulp.src(['./bower.json', './package.json'])
  .pipe(bump({type:'minor'}))
  .pipe(gulp.dest('./'));
});

gulp.task('bump:major', function(){
  gulp.src(['./bower.json', './package.json'])
  .pipe(bump({type:'major'}))
  .pipe(gulp.dest('./'));
});

gulp.task('default', function(callback) {
  gulpSequence('clean', 'sass')(callback);
});
