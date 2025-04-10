<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Modern Audio Player</title>
  <link rel="stylesheet" href="audio.css" />
  <style>
    body, html {
      margin: 0;
      padding: 0;
      height: 100%;
      overflow: hidden;
    }
    #bgVideo {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      object-fit: cover;
      z-index: -1;
    }
    #demo {
      position: relative;
      z-index: 2;
    }


    @keyframes spin {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    #songTitle {
      font-size: 18px;
      text-align: center;
      margin: 10px 0;
      color: #1db954;
    }

    #progressContainer {
      width: 100%;
      height: 6px;
      background: #333;
      border-radius: 5px;
      margin: 10px 0;
      overflow: hidden;
    }

    #progressBar {
      height: 100%;
      background: #1db954;
      width: 0%;
    }

    #volumeControl {
      width: 100%;
      margin: 10px 0;
    }
  </style>
</head>
<body>
  <video id="bgVideo" autoplay muted loop>
    <source src="video/video1.mp4" type="video/mp4">
  </video>

  <div id="demo">
    <div id="songTitle">Select a song...</div>
    <audio id="demoAudio" controls></audio>
    <div id="progressContainer">
      <div id="progressBar"></div>
    </div>
    <input type="range" id="volumeControl" min="0" max="1" step="0.01" value="1" />
    <div id="demoList">
      <div class="song" data-src="song1.mp3" data-cover="images/image1.png">Song One</div>
      <div class="song" data-src="song2.mp3" data-cover="images/image2.png">Song Two</div>
      <div class="song" data-src="song3.mp3" data-cover="images/image3.png">Song Three</div>
      <div class="song" data-src="song4.mp3" data-cover="images/image4.png">Song Four</div>
      <div class="song" data-src="song5.mp3" data-cover="images/image5.png">Song Five</div>
      <div class="song" data-src="song6.mp3" data-cover="images/image6.png">Song Six</div>
      <div class="song" data-src="song7.mp3" data-cover="images/image7.png">Song Seven</div>
      <div class="song" data-src="song8.mp3" data-cover="images/image8.png">Song Eight</div>
      <div class="song" data-src="song9.mp3" data-cover="images/image9.png">Song Nine</div>
      <div class="song" data-src="song10.mp3" data-cover="images/image10.png">Song Ten</div>
      <div class="song" data-src="song11.mp3" data-cover="images/image11.png">Song Eleven</div>
      <div class="song" data-src="song12.mp3" data-cover="images/image12.png">Song Twelve</div>
      <div class="song" data-src="song13.mp3" data-cover="images/image13.png">Song Thirteen</div>
      <div class="song" data-src="song14.mp3" data-cover="images/image14.png">Song Fourteen</div>
      <div class="song" data-src="song15.mp3" data-cover="images/image15.png">Song Fifteen</div>
      <div class="song" data-src="song16.mp3" data-cover="images/image16.png">Song Sixteen</div>
      <div class="song" data-src="song17.mp3" data-cover="images/image17.png">Song Seventeen</div>
    </div>
  </div>

  <script src="audio.js"></script>
  <script>
    const player = document.getElementById("demoAudio");
    const bgVideo = document.getElementById("bgVideo");
    const videoMap = [
      "video/video1.mp4",
      "video/video2.mp4",
      "video/video3.mp4",
      "video/video4.mp4",
      "video/video5.mp4",
      "video/video6.mp4",
      "video/video7.mp4",
      "video/video8.mp4",
      "video/video9.mp4",
      "video/video10.mp4",
      "video/video11.mp4",
      "video/video12.mp4",
      "video/video13.mp4",
      "video/video14.mp4",
      "video/video15.mp4",
      "video/video16.mp4",
      "video/video17.mp4"
    ];

    player.ontimeupdate = () => {
      const percent = (player.currentTime / player.duration) * 100;
      document.getElementById("progressBar").style.width = percent + "%";
    };

    player.onpause = () => {
      document.getElementById("coverArt").classList.remove("playing");
    };

    player.onplay = () => {
      document.getElementById("coverArt").classList.add("playing");
    };

    document.getElementById("volumeControl").oninput = function () {
      player.volume = this.value;
    };

    document.querySelectorAll(".song").forEach((el, i) => {
      el.addEventListener("click", () => {
        bgVideo.src = videoMap[i];
        bgVideo.load();
        bgVideo.play();

        player.src = "audio/" + el.dataset.src;
        player.play();

        document.getElementById("coverArt").src = el.dataset.cover;
        document.getElementById("songTitle").textContent = el.textContent;

        document.querySelectorAll(".song").forEach(s => s.classList.remove("now"));
        el.classList.add("now");
      });
    });
  </script>
</body>
</html>