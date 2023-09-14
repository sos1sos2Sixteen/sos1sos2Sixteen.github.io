function img_click(slf){
    console.log('clicked')
    console.log(slf)
    let player = document.getElementById('global-player');
    player.src = "audios/raw/raw1.wav";
    player.load();
    player.play();
}


function play_audio(wavepath){
    // https://stackoverflow.com/questions/55953639/the-mediaelement-play-method-returns-a-promise-that-is-rejected
    console.log(wavepath);
    let player = document.getElementById('global-player');
    player.src = wavepath
    let play_promise = player.play()
    console.log(play_promise)

    if (play_promise != undefined){
        play_promise.then(_ => {
            console.log('wave played')
        }, error => {console.log('error is', error)})
    }
}
