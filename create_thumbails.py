from PIL import Image
import os
from pathlib import Path


def create_thumbnails(source_dir, max_dimension=800):
    # Define which images should be treated as vertical
    vertical_images = [
        'assets/photos/nepal/6.JPG',  # Okra image
        # Add other vertical image paths here
        'assets/photos/china/1.JPG',
        'assets/photos/china/4.JPG',
        'assets/photos/brooklyn/1.JPG',
    ]

    parent_dir = os.path.dirname(source_dir)
    thumbs_base_dir = os.path.join(parent_dir, 'thumbs')
    if not os.path.exists(thumbs_base_dir):
        os.makedirs(thumbs_base_dir)

    for root, dirs, files in os.walk(source_dir):
        rel_path = os.path.relpath(root, source_dir)
        thumb_dir = os.path.join(thumbs_base_dir,
                                 rel_path) if rel_path != '.' else thumbs_base_dir
        if not os.path.exists(thumb_dir):
            os.makedirs(thumb_dir)

        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.JPG', '.JPEG')):
                input_path = os.path.join(root, filename)
                thumb_filename = f"{Path(filename).stem}-th{Path(filename).suffix}"
                output_path = os.path.join(thumb_dir, thumb_filename)
                if os.path.isfile(output_path):
                    continue
                try:
                    with Image.open(input_path) as img:
                        # Convert RGBA to RGB if necessary
                        if img.mode in ('RGBA', 'LA'):
                            img = img.convert('RGB')

                        # Check if this image is in our vertical list
                        if input_path in vertical_images:
                            print(f"Processing {filename} as vertical")
                            img = img.rotate(90, expand=True)

                        # Calculate dimensions maintaining aspect ratio
                        width, height = img.size
                        aspect = width / height

                        if width > height:
                            if width > max_dimension:
                                new_width = max_dimension
                                new_height = int(max_dimension / aspect)
                            else:
                                new_width = width
                                new_height = height
                        else:
                            if height > max_dimension:
                                new_height = max_dimension
                                new_width = int(max_dimension * aspect)
                            else:
                                new_width = width
                                new_height = height

                        # Resize image
                        img = img.resize((new_width, new_height),
                                         Image.Resampling.LANCZOS)

                        # Save thumbnail
                        img.save(output_path, 'JPEG', quality=85, optimize=True)
                        print(
                            f"Created thumbnail: {output_path} ({new_width}x{new_height})")

                except Exception as e:
                    print(f"Error processing {input_path}: {str(e)}")


if __name__ == "__main__":
    source_directory = "assets/photos"
    create_thumbnails(source_directory)
    print("Thumbnail creation complete!")