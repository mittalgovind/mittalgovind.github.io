---
title: "Photography"
permalink: /photography/
layout: single
classes: wide
description: "A collection of photographs from Nepal, Meghalaya, and Brooklyn"
og_title: "Govind Mittal | Photography"
og_description: "A collection of photographs from Nepal, Meghalaya, and Brooklyn"
og_image: /assets/thumbs/meghalaya/1-th.JPG 
header:
  overlay_image: /assets/thumbs/background-th.JPG
  overlay_filter: 0.5
  caption: "Capturing moments across diverse landscapes"

nepal_gallery:
  - url: /assets/photos/nepal/1.JPG
    image_path: /assets/thumbs/nepal/1-th.JPG
    alt: "Nepal photograph 1"
    title: "Phewa Lake, Pokhara with pregnant clouds"
    orientation: horizontal
  - url: /assets/photos/nepal/2.JPG
    image_path: /assets/thumbs/nepal/2-th.JPG
    alt: "Nepal photograph 2"
    title: "Annapurna: A mountain peak signals how the crop will be this year"
    orientation: horizontal
  - url: /assets/photos/nepal/3.JPG
    image_path: /assets/thumbs/nepal/3-th.JPG
    alt: "Nepal photograph 3"
    title: "Annapurna Range. Mountains in the back are 50 kms apart."
    orientation: horizontal
  - url: /assets/photos/nepal/4.JPG
    image_path: /assets/thumbs/nepal/4-th.JPG
    alt: "Nepal photograph 4"
    title: "Nepali Staple Food: Lentils, Rice, vegetables, spicy sauce, ghee, All home-grown."
    orientation: horizontal
  - url: /assets/photos/nepal/5.JPG
    image_path: /assets/thumbs/nepal/5-th.JPG
    alt: "Nepal photograph 5"
    title: "Rice Field"
    orientation: horizontal
  - url: /assets/photos/nepal/6.JPG
    image_path: /assets/thumbs/nepal/6-th.JPG
    alt: "Nepal photograph 6"
    title: "High on Okra"
    orientation: vertical
  - url: /assets/photos/nepal/7.JPG
    image_path: /assets/thumbs/nepal/7-th.JPG
    alt: "Nepal photograph 7"
    title: "Gorakhpur, Uttar Pradesh, India"
    orientation: horizontal

meghalaya_gallery:
  - url: /assets/photos/meghalaya/1.JPG
    image_path: /assets/thumbs/meghalaya/1-th.JPG
    alt: "Meghalaya photograph 1"
    title: "Truly green. Greenery overshadowing the blue reflection of the sky."
    orientation: horizontal
  - url: /assets/photos/meghalaya/2.JPG
    image_path: /assets/thumbs/meghalaya/2-th.JPG
    alt: "Meghalaya photograph 2"
    title: "Gist of the town. Can you spot the spider web?"
    orientation: horizontal
  - url: /assets/photos/meghalaya/3.JPG
    image_path: /assets/thumbs/meghalaya/3-th.JPG
    alt: "Meghalaya photograph 3"
    title: "Cloudy Valley"
    orientation: horizontal

brooklyn_gallery:
  - url: /assets/photos/brooklyn/1.JPG
    image_path: /assets/thumbs/brooklyn/1-th.JPG
    alt: "Brooklyn photograph 1"
    title: "Shades of green"
    orientation: vertical
  - url: /assets/photos/brooklyn/2.JPG
    image_path: /assets/thumbs/brooklyn/2-th.JPG
    alt: "Brooklyn photograph 2"
    title: "Fall Colors, Upstate New York"
    orientation: horizontal
  - url: /assets/photos/brooklyn/3.JPG
    image_path: /assets/thumbs/brooklyn/3-th.JPG
    alt: "Brooklyn photograph 3"
    title: "July 4th view from Williamsburg, Brooklyn"
    orientation: horizontal
  - url: /assets/photos/brooklyn/4.JPG
    image_path: /assets/thumbs/brooklyn/4-th.JPG
    alt: "Brooklyn photograph 4"
    title: "Skies over the Prospect Park"
    orientation: horizontal
  - url: /assets/photos/brooklyn/5.JPG
    image_path: /assets/thumbs/brooklyn/5-th.JPG
    alt: "Brooklyn photograph 5"
    title: "Snow bordered bricks."
    orientation: vertical
---

<div class="gallery-layout">
  <section class="gallery-section">
    <h2>Nepal</h2>
    <p>Exploring the majestic Himalayas: capturing the breathtaking 
landscapes and vibrant culture of Nepal.</p>
    <div class="gallery-grid">
      {% for item in page.nepal_gallery %}
        <div class="gallery-item {% if item.orientation == 'horizontal' %}horizontal{% else %}vertical{% endif %}">
          <a href="{{ item.url }}" title="{{ item.title }}" class="image-link">
            <img src="{{ item.image_path }}" alt="{{ item.alt }}" loading="lazy">
            <div class="gallery-caption">
              <span class="caption-text">{{ item.title }}</span>
            </div>
          </a>
        </div>
      {% endfor %}
    </div>
  </section>

  <section class="gallery-section">
    <h2>Meghalaya</h2>
    <p>Discovering the 'Abode of Clouds': misty landscapes of Northeast India.</p>
    <div class="gallery-grid">
      {% for item in page.meghalaya_gallery %}
        <div class="gallery-item {% if item.orientation == 'horizontal' %}horizontal{% else %}vertical{% endif %}">
          <a href="{{ item.url }}" title="{{ item.title }}" class="image-link">
            <img src="{{ item.image_path }}" alt="{{ item.alt }}" loading="lazy">
            <div class="gallery-caption">
              <span class="caption-text">{{ item.title }}</span>
            </div>
          </a>
        </div>
      {% endfor %}
    </div>
  </section>

  <section class="gallery-section">
    <h2>Brooklyn</h2>
    <p>Brooklyn and New York's Non-touristy vibes</p>
    <div class="gallery-grid">
      {% for item in page.brooklyn_gallery %}
        <div class="gallery-item {% if item.orientation == 'horizontal' %}horizontal{% else %}vertical{% endif %}">
          <a href="{{ item.url }}" title="{{ item.title }}" class="image-link">
            <img src="{{ item.image_path }}" alt="{{ item.alt }}" loading="lazy">
            <div class="gallery-caption">
              <span class="caption-text">{{ item.title }}</span>
            </div>
          </a>
        </div>
      {% endfor %}
    </div>
  </section>
</div>