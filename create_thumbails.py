from PIL import Image
import os
from pathlib import Path


def create_thumbnails(source_dir, thumb_size=(800, 800)):
    """
    Create thumbnails for all JPG images in the source directory and its subdirectories.

    Args:
        source_dir (str): Path to the source directory containing original images
        thumb_size (tuple): Maximum width and height for thumbnails (maintains aspect ratio)
    """
    # Get the parent directory of source_dir
    parent_dir = os.path.dirname(source_dir)

    # Create a 'thumbs' directory parallel to the source directory
    thumbs_base_dir = os.path.join(parent_dir, 'thumbs')
    if not os.path.exists(thumbs_base_dir):
        os.makedirs(thumbs_base_dir)

    # Walk through all directories
    for root, dirs, files in os.walk(source_dir):
        # Get the relative path from source_dir
        rel_path = os.path.relpath(root, source_dir)

        # Create corresponding directory in thumbs
        if rel_path != '.':
            thumb_dir = os.path.join(thumbs_base_dir, rel_path)
            if not os.path.exists(thumb_dir):
                os.makedirs(thumb_dir)
        else:
            thumb_dir = thumbs_base_dir

        # Process each file
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.JPG', '.JPEG')):
                # Construct full file paths
                input_path = os.path.join(root, filename)

                # Create thumbnail filename with -th suffix
                thumb_filename = f"{Path(filename).stem}-th{Path(filename).suffix}"
                output_path = os.path.join(thumb_dir, thumb_filename)

                try:
                    # Open and process image
                    with Image.open(input_path) as img:
                        # Convert RGBA to RGB if necessary
                        if img.mode in ('RGBA', 'LA'):
                            img = img.convert('RGB')

                        # Calculate new dimensions maintaining aspect ratio
                        img.thumbnail(thumb_size, Image.Resampling.LANCZOS)

                        # Save thumbnail
                        img.save(output_path, 'JPEG', quality=85, optimize=True)
                        print(f"Created thumbnail: {output_path}")

                except Exception as e:
                    print(f"Error processing {input_path}: {str(e)}")


if __name__ == "__main__":
    # Specify the source directory where your original photos are
    source_directory = "assets/photos"  # Adjust this path to match your directory structure

    # Create thumbnails (800px max dimension, maintaining aspect ratio)
    create_thumbnails(source_directory)
    print("Thumbnail creation complete!")