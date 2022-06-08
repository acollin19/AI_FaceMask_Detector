from PIL import Image
import os
import sys


def find_smallest_resolution(directories=[]):
    if not directories:
        return None

    sorted_widths = []
    sorted_heights = []
    avg_height = None
    avg_width = None
    formats = []
    for directory in directories:
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            # Check if it is a file
            if os.path.isfile(f):
                image = Image.open(f)
                if avg_height is None:
                    avg_height = image.height
                if avg_width is None:
                    avg_width = image.width

                avg_height += image.height
                avg_width += image.width

                sorted_heights.append((image.height, f))
                sorted_widths.append((image.width, f))

                found_format = False
                for f in formats:
                    if f[0] == image.format:
                        index = formats.index(f)
                        f = (image.format, f[1] + 1)
                        formats[index] = f
                        found_format = True

                if not found_format:
                    formats.append((image.format, 1))

    avg_height = round(avg_height / len(sorted_heights))
    avg_width = round(avg_width / len(sorted_widths))

    sorted_heights.sort()
    sorted_widths.sort()

    print('Number of images = {len}'.format(len=len(sorted_heights)))
    print('Min width = {min_width}\nMin height = {min_height}'.format(min_width=min(sorted_widths),
                                                                      min_height=min(sorted_heights)))
    print('Max width = {max_width}\nMax height = {max_height}'.format(max_width=max(sorted_widths),
                                                                      max_height=max(sorted_heights)))
    print('Average width = {avg_width}\nAverage height = {avg_height}'.format(avg_width=avg_height,
                                                                              avg_height=avg_width))
    print('Number of images for each format = {formats}'.format(formats=formats))
    return (avg_width, avg_height)


if __name__ == '__main__':
    v = sys.version_info
    print('Python version: {v0}.{v1}.{v2}'.format(v0=v[0], v1=v[1], v2=v[2]))

    directories = ['../resized_images/ClothMask', '../resized_images/N95Mask', '../resized_images/SurgicalMask', '../resized_images/NoMask']
    # directories = ['ClothMask', 'N95Mask', 'SurgicalMask', 'NoMask']
    find_smallest_resolution(directories)