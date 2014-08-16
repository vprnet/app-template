if (document.createElement('audio').canPlayType) {
    if (!document.createElement('audio').canPlayType('audio/mpeg')) {
        var all_audio = $('audio');
        all_audio.attr("style", "display: none;");
    }
}

var transition = function(d) {
    return "-webkit-transition: width " + d + "s linear !important;" +
        "-moz-transition: width " + d + "s linear !important;" +
        "-o-transition: width " + d + "s linear !important;" +
        "transition: width " + d + "s linear !important;";
};

$('a.audio_play').click(function() {
    var audioLink = $(this),
        audio = this.firstChild,
        progressBar = $(this).next('div.progress_bar'),
        fullWidth = $(this).parent('div.audio_player').width(),
        duration = progressBar.attr('data'),
        remaining = progressBar.attr('remaining'),
        glyphicon = $(this).children('div.play_btn').children('span.glyphicon');

    if (!audioLink.hasClass('can_play')) {
        glyphicon.attr('class', 'icon ion-loading-c');
        audioLink.addClass('can_play');
    }

    audio.addEventListener('ended', canPlay(audio, progressBar, fullWidth, duration, remaining, glyphicon, audioLink));
});


var canPlay = function(audio, progressBar, fullWidth, duration, remaining, glyphicon, audioLink) {
    // Next step: check for other audio playing, pause it!
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
};
