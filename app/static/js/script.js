var transition = function(d) {
    return "-webkit-transition: width " + d + "s linear !important;" +
        "-moz-transition: width " + d + "s linear !important;" +
        "-o-transition: width " + d + "s linear !important;" +
        "transition: width " + d + "s linear !important;";
};

$('a.audio_play').click(function() {
    var progressBar = $(this).next('div.progress_bar'),
        fullWidth = $(this).parent('div.audio_player').width(),
        duration = progressBar.attr('data'),
        remaining = progressBar.attr('remaining');
    progressBar.toggleClass('play');
    if (this.firstChild.paused === false) {
        this.firstChild.pause();
        var currentProgress = progressBar.width();
        remaining = duration - parseInt(duration * currentProgress / fullWidth, 10);
        progressBar.attr('remaining', remaining);
        progressBar.attr("style", "width: " + currentProgress + "px;");
        $(this).children('div.play_btn').children('span.glyphicon')
            .attr('class', 'glyphicon glyphicon-play');
    } else {
        this.firstChild.play();
        progressBar.attr("style", transition(remaining));
        $(this).children('div.play_btn').children('span.glyphicon')
            .attr('class', 'glyphicon glyphicon-pause');
    }
});
