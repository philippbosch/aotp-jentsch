var currentTrack = -1;

function nextTrack() {
    currentTrack++;
    if (!tracks[currentTrack]) currentTrack = 0;
    $('#background').fadeOut(1000, function() {
        $(this).attr('src', tracks[currentTrack].image);
        $(this).load(function() {
            $(this).fadeIn(1000);
        });
    });
    var volume = $('#player').data("jPlayer.config").volume;
    var interval = window.setInterval(function() {
        var currentVolume = $('#player').data("jPlayer.config").volume;
        if (currentVolume <= 0) {
            window.clearInterval(interval);
            $('#player').volume(volume);
            $('#player').setFile(tracks[currentTrack].audio).play();
            return;
        }
        $('#player').volume(currentVolume-1);
    }, 10);
}

$(document).ready(function(){
   $("#player").jPlayer({
        ready: function () {
            nextTrack();
        },
        swfPath: MEDIA_URL + 'player'
    });
    $('#player').onSoundComplete(function() {
        nextTrack();
    });
    $("#skip").click(function() {
        nextTrack();
    });
});

