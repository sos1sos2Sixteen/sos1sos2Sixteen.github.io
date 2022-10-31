function img_click(slf){
    console.log('clicked')
    console.log(slf)
    let player = document.getElementById('global-player');
    player.src = "audios/raw/raw1.wav";
    player.play();
}


function play_audio(wavepath){
    console.log(wavepath);
    let player = document.getElementById('global-player');
    player.src = wavepath
    player.play()
}
