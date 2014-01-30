if (document.createElement('audio').canPlayType) {
    if (!document.createElement('audio').canPlayType('audio/mpeg')) {
        var all_audio = $('audio');
        for (var i = 0; i < all_audio.length; i++) {
            var ogg = all_audio.eq(i).attr('ogg');
            all_audio.eq(i).attr('src', ogg);
            all_audio.eq(i).attr('type', 'audio/ogg');
        }
    }
}

var transition = function(d) {
    return "-webkit-transition: width " + d + "s linear !important;" +
        "-moz-transition: width " + d + "s linear !important;" +
        "-o-transition: width " + d + "s linear !important;" +
        "transition: width " + d + "s linear !important;";
};

$('a.audio_play').click(function() {
    // Next step: check for other audio playing, pause it!
    var audio = this.firstChild,
        progressBar = $(this).next('div.progress_bar'),
        fullWidth = $(this).parent('div.audio_player').width(),
        duration = progressBar.attr('data'),
        remaining = progressBar.attr('remaining'),
        glyphicon = $(this).children('div.play_btn').children('span.glyphicon');

    audio.addEventListener('ended', function () {
        audio.currentTime = 0;
        progressBar.attr("style", "width: 0px;");
        progressBar.attr("remaining", duration);
        progressBar.toggleClass('play');
        glyphicon.attr('class', 'glyphicon glyphicon-play');
    });

    progressBar.toggleClass('play');
    if (audio.paused === false) {
        audio.pause();
        var currentProgress = progressBar.width();
        remaining = duration - parseInt(duration * currentProgress / fullWidth, 10);
        progressBar.attr('remaining', remaining);
        progressBar.attr("style", "width: " + currentProgress + "px;");
        glyphicon.attr('class', 'glyphicon glyphicon-play');
    } else {
        audio.play();
        progressBar.attr("style", transition(remaining));
        glyphicon.attr('class', 'glyphicon glyphicon-pause');
    }
});
