---
title: "Photography"
permalink: /photography/
layout: single
classes: wide
header:
  overlay_image: /assets/photos/nepal/1.JPG
  overlay_filter: 0.5
  caption: "Capturing moments across diverse landscapes"

nepal_gallery:
  - url: /assets/photos/nepal/1.JPG
    image_path: /assets/photos/nepal/1.JPG
    alt: "Nepal photograph 1"
    title: "Phewa Lake, Pokhara with pregnant clouds"
  - url: /assets/photos/nepal/2.JPG
    image_path: /assets/photos/nepal/2.JPG
    alt: "Nepal photograph 2"
    title: "Annapurna: A mountain peak signals how the crop will be this year"
  - url: /assets/photos/nepal/3.JPG
    image_path: /assets/photos/nepal/3.JPG
    alt: "Nepal photograph 3"
    title: "Annapurna Range. Mountains in the back are 50 kms apart."
  - url: /assets/photos/nepal/4.JPG
    image_path: /assets/photos/nepal/4.JPG
    alt: "Nepal photograph 4"
    title: "Nepali Staple Food: Lentils, Rice, vegetables, spicy sauce, ghee, All home-grown."
  - url: /assets/photos/nepal/5.JPG
    image_path: /assets/photos/nepal/5.JPG
    alt: "Nepal photograph 5"
    title: "Rice Field"
  - url: /assets/photos/nepal/6.JPG
    image_path: /assets/photos/nepal/6.JPG
    alt: "Nepal photograph 6"
    title: "High on Okra"
  - url: /assets/photos/nepal/7.JPG
    image_path: /assets/photos/nepal/7.JPG
    alt: "Nepal photograph 7"
    title: "Gorakhpur, Uttar Pradesh, India"

china_gallery:
  - url: /assets/photos/china/1.JPG
    image_path: /assets/photos/china/1.JPG
    alt: "China photograph 1"
    title: "Heart in the Clouds"
  - url: /assets/photos/china/2.JPG
    image_path: /assets/photos/china/2.JPG
    alt: "China photograph 2"
    title: "Buddha depiction carved on a tree trunk. More expensive than a Shanghai Apartment."
  - url: /assets/photos/china/3.JPG
    image_path: /assets/photos/china/3.JPG
    alt: "China photograph 3"
    title: "Me in the Tang dress"
  - url: /assets/photos/china/4.JPG
    image_path: /assets/photos/china/4.JPG
    alt: "China photograph 4"
    title: "Traditional Chinese Floral Dress"
  - url: /assets/photos/china/5.JPG
    image_path: /assets/photos/china/5.JPG
    alt: "China photograph 5"
    title: "Progress"
  - url: /assets/photos/china/6.JPG
    image_path: /assets/photos/china/6.JPG
    alt: "China photograph 6"
    title: "Dali, Yunnan"
  - url: /assets/photos/china/7.JPG
    image_path: /assets/photos/china/7.JPG
    alt: "China photograph 7"
    title: "Fisher under Heaven"
  - url: /assets/photos/china/8.JPG
    image_path: /assets/photos/china/8.JPG
    alt: "China photograph 8"
    title: "Temple, Dali, Yunnan"
  - url: /assets/photos/china/9.JPG
    image_path: /assets/photos/china/9.JPG
    alt: "China photograph 9"
    title: "Floral Market. Thanks, Miss :)"

meghalaya_gallery:
  - url: /assets/photos/meghalaya/1.JPG
    image_path: /assets/photos/meghalaya/1.JPG
    alt: "Meghalaya photograph 1"
    title: "Truly green. Greenery overshadowing the blue reflection of the sky."
  - url: /assets/photos/meghalaya/2.JPG
    image_path: /assets/photos/meghalaya/2.JPG
    alt: "Meghalaya photograph 2"
    title: "Gist of the town. Can you spot the spider web?"

brooklyn_gallery:
  - url: /assets/photos/brooklyn/1.JPG
    image_path: /assets/photos/brooklyn/1.JPG
    alt: "Brooklyn photograph 1"
    title: "Shades of green"
  - url: /assets/photos/brooklyn/2.JPG
    image_path: /assets/photos/brooklyn/2.JPG
    alt: "Brooklyn photograph 2"
    title: "Fall Colors, Upstate New York"
  - url: /assets/photos/brooklyn/3.JPG
    image_path: /assets/photos/brooklyn/3.JPG
    alt: "Brooklyn photograph 3"
    title: "July 4th view from Williamsburg, Brooklyn"
---

<div class="gallery-layout">
  <section class="gallery-section">
    <h2>Nepal</h2>
    <p>Exploring the majestic Himalayas: capturing the breathtaking landscapes, ancient temples, and vibrant culture of Nepal.</p>
    <div class="gallery-grid">
      {% for item in page.nepal_gallery %}
        <div class="gallery-item">
          <a href="{{ item.url }}" title="{{ item.title }}">
            <img src="{{ item.image_path }}" alt="{{ item.alt }}">
            <div class="gallery-caption">{{ item.title }}</div>
          </a>
        </div>
      {% endfor %}
    </div>
  </section>

  <section class="gallery-section">
    <h2>China</h2>
    <p>A visual journey through China's diverse landscapes, from ancient architecture to modern cityscapes.</p>
    <div class="gallery-grid">
      {% for item in page.china_gallery %}
        <div class="gallery-item">
          <a href="{{ item.url }}" title="{{ item.title }}">
            <img src="{{ item.image_path }}" alt="{{ item.alt }}">
            <div class="gallery-caption">{{ item.title }}</div>
          </a>
        </div>
      {% endfor %}
    </div>
  </section>

  <section class="gallery-section">
    <h2>Meghalaya</h2>
    <p>Discovering the 'Abode of Clouds': documenting the living root bridges and misty landscapes of Northeast India.</p>
    <div class="gallery-grid">
      {% for item in page.meghalaya_gallery %}
        <div class="gallery-item">
          <a href="{{ item.url }}" title="{{ item.title }}">
            <img src="{{ item.image_path }}" alt="{{ item.alt }}">
            <div class="gallery-caption">{{ item.title }}</div>
          </a>
        </div>
      {% endfor %}
    </div>
  </section>

  <section class="gallery-section">
    <h2>Brooklyn</h2>
    <p>Urban exploration through Brooklyn's diverse neighborhoods, capturing the borough's unique character and charm.</p>
    <div class="gallery-grid">
      {% for item in page.brooklyn_gallery %}
        <div class="gallery-item">
          <a href="{{ item.url }}" title="{{ item.title }}">
            <img src="{{ item.image_path }}" alt="{{ item.alt }}">
            <div class="gallery-caption">{{ item.title }}</div>
          </a>
        </div>
      {% endfor %}
    </div>
  </section>
</div>