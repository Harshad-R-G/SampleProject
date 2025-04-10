var aud = {
  player: null,
  playlist: null,
  now: 0,

  init: () => {
    aud.player = document.getElementById("demoAudio");
    aud.playlist = document.querySelectorAll("#demoList .song");

    // Click to play
    aud.playlist.forEach((el, i) => {
      el.onclick = () => aud.play(i);
    });

    // Autoplay on load
    aud.player.oncanplay = aud.player.play;

    // Auto next song
    aud.player.onended = () => {
      aud.now++;
      if (aud.now >= aud.playlist.length) aud.now = 0;
      aud.play(aud.now);
    };
  },

  play: id => {
    aud.now = id;
    const selected = aud.playlist[id];

    // Set audio source
    aud.player.src = "audio/" + selected.dataset.src;
    aud.player.play();

    // Update UI
    document.getElementById("songTitle").textContent = selected.textContent;
    document.getElementById("coverArt").src = selected.dataset.cover;

    // Highlight active song
    aud.playlist.forEach(el => el.classList.remove("now"));
    selected.classList.add("now");
  }
};

window.addEventListener("DOMContentLoaded", aud.init);
