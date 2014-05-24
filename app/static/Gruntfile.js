module.exports = function (grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        compass: {
            dist: {
                options: {
                    sassDir: 'dev/sass',
                    cssDir: 'css'
                }
            }
        },
        concat: {
            dist: {
                src: [
                    // Explicitly list files to determine order
                    'dev/js/*.js'
                ],
                dest: 'js/script.js'
            }
        },
        uglify: {
            build: {
                src: 'js/script.js',
                dest: 'js/script.min.js'
            }
        },
        imagemin: {
            dynamic: {
                files: [{
                    expand: true,
                    cwd: 'dev/img/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: 'img'
                    }]
            }
        },
        watch: {
            scripts: {
                files: ['dev/js/*.js'],
                tasks: ['concat', 'uglify'],
                options: {
                    spawn: false,
                    livereload: true
                }
            },
            css: {
                files: 'dev/sass/*.scss',
                tasks: ['compass']
            },
            images: {
                files: 'dev/img/*',
                tasks: ['imagemin']
            }
        },
        browserSync: {
            dev: {
                bsFiles: {
                    src: 'css/*.css'
                },
                options: {
                    watchTask: true
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-browser-sync');

    // What tasks should be run when "grunt" is entered in the command line
    grunt.registerTask('default', ['browserSync', 'watch']);

};
