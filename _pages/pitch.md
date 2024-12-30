---
title: "PITCH"
permalink: /pitch/
layout: single
classes: wide
description: "AI-assisted Tagging of Deepfake Audio Calls using Challenge-Response"
og_title: "PITCH: AI-assisted Tagging of Deepfake Audio Calls"
og_description: "A novel system for detecting deepfake audio calls through challenge-response verification"
og_image: /assets/pitch_assets/thumbnail.png
header:
  overlay_color: "#2196F3"
---

<div class="content-wrapper" markdown="1">
  <div class="project-title" markdown="1">
  # Audio Samples for AI-assisted Tagging of Deepfake Audio Calls using Challenge-Response
  {: .text-center}

  <div class="sample-description">
  First is the imposter voice. Second is the verified ground truth. Third is a deepfake: an imposter creates using the target's recording, other than the ground truth. Last column is a short caption.
  </div>
  </div>

  ## Audio Samples of Regular Speech
  <div class="audio-category">
    <div class="challenge-type">
      <div class="label">No Challenge</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df00.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/gt00.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df10.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Deepfake Sounds Genuine</div>
      </div>
    </div>
  </div>

  ## Audio Samples of Top-11 Valid Machine-Detectable Challenges
  <div class="subtitle">Captions are prospective explanations and not machine predictions.</div>

  <div class="audio-category">
    <div class="challenge-type">
      <div class="label">Static Mouth</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df01.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/gt01.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df11.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Audible distortions at 'formalities'</div>
      </div>
    </div>

    <div class="challenge-type">
      <div class="label">Cup Mouth</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df02.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/gt02.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df12.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Non-compliance and Distortions</div>
      </div>
    </div>

    <div class="challenge-type">
      <div class="label">Whisper</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df03.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/gt03.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df13.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Non-compliance</div>
      </div>
    </div>

    <div class="challenge-type">
      <div class="label">Speak Softly</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df04.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/gt04.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df14.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Non-compliance</div>
      </div>
    </div>

    <div class="challenge-type">
      <div class="label">High Pitch</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df05.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/gt05.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df15.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">High Non-Compliance</div>
      </div>
    </div>

    <div class="challenge-type">
      <div class="label">Foreign Words</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df06.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/gt06.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df16.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Vibrating Voice Distortions (also seen with suspends linguistic chain ya ne)</div>
      </div>
    </div>

    <div class="challenge-type">
      <div class="label">Sing</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df07.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/gt07.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df17.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Non-compliance towards the last</div>
      </div>
    </div>

    <div class="challenge-type">
      <div class="label">Emotions</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df08.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/gt08.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df18.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Sounds flatter in comparison to imposter</div>
      </div>
    </div>

    <div class="challenge-type">
      <div class="label">Crosstalk</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df09.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df19.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df20.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Non-compliance and Distortions</div>
      </div>
    </div>
  </div>

  ## Audio Samples of the 9 Weaker Tasks
  <div class="audio-category">
    <div class="challenge-type">
      <div class="label">Speak Loudly</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df21.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df22.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df23.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Non-Compliance (Deepfake still whispers)</div>
      </div>
    </div>

    <div class="challenge-type">
      <div class="label">Read Quickly</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df24.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df25.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df26.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Deepfake Sounds Genuine</div>
      </div>
    </div>

    <div class="challenge-type">
      <div class="label">Read Slowly</div>
      <div class="audio-row">
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df27.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df28.mp3" type="audio/mp3"></audio>
        </div>
        <div class="audio-cell">
          <audio controls><source src="/assets/pitch_assets/final/df29.mp3" type="audio/mp3"></audio>
        </div>
        <div class="result">Mild Distortions</div>
      </div>
    </div>

    <!-- Add remaining weaker tasks -->
  </div>

  ## Video Samples of Selected Challenges
  <div class="video-category">
    <div class="video-row">
      <div class="video-cell">
        <p>High-Pitch</p>
        <video controls>
          <source src="/assets/pitch_assets/video_samples/1.mp4" type="video/mp4">
        </video>
      </div>
      <div class="video-cell">
        <p>Cross-talk (with a self played audio on phone)</p>
        <video controls>
          <source src="/assets/pitch_assets/video_samples/2.mp4" type="video/mp4">
        </video>
      </div>
      <div class="video-cell">
        <p>Whisper</p>
        <video controls>
          <source src="/assets/pitch_assets/video_samples/3.mp4" type="video/mp4">
        </video>
      </div>
    </div>
  </div>
</div>

<style>
.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2em;
}

.project-title {
  margin-bottom: 2em;
}

.sample-description {
  text-align: center;
  color: #666;
  margin: 1em 0;
  font-style: italic;
}

.subtitle {
  color: #666;
  font-style: italic;
  margin: 1em 0;
}

.audio-category {
  margin: 2em 0;
}

.challenge-type {
  margin: 1.5em 0;
  background: white;
  border-radius: 8px;
  padding: 1em;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.challenge-type .label {
  font-weight: bold;
  color: #333;
  margin-bottom: 0.5em;
}

.audio-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr) auto;
  gap: 1em;
  align-items: center;
}

.audio-cell audio {
  width: 100%;
}

.result {
  color: #666;
  font-style: italic;
}

.video-category {
  margin: 2em 0;
}

.video-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1em;
}

.video-cell {
  text-align: center;
}

.video-cell p {
  margin: 0.5em 0;
  font-weight: bold;
  color: #333;
}

.video-cell video {
  width: 100%;
  border-radius: 4px;
}

@media (max-width: 768px) {
  .audio-row {
    grid-template-columns: 1fr;
  }
  
  .video-row {
    grid-template-columns: 1fr;
  }
  
  .result {
    margin-top: 0.5em;
    text-align: center;
  }
}
</style>