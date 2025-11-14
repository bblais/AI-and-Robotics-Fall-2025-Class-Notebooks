#!/usr/bin/env python
# coding: utf-8

# In[4]:


from PIL import Image

def create_checkered_board(width, height, board_cols, board_rows, output_file):
    """
    Create a checkered board image with alternating white and light gray squares.

    Args:
        width: Image width in pixels
        height: Image height in pixels
        board_cols: Number of columns in the board
        board_rows: Number of rows in the board
        output_file: Output PNG filename
    """
    # Create a new image with white background
    img = Image.new('RGB', (width, height), color='white')
    pixels = img.load()

    # Calculate square dimensions
    square_width = width / board_cols
    square_height = height / board_rows

    # Define colors
    white = (255, 255, 255)
    light_gray = (150, 150, 150)

    # Fill in the squares
    for row in range(board_rows):
        for col in range(board_cols):
            # Determine color based on position (checkerboard pattern)
            if (row + col) % 2 == 0:
                color = white
            else:
                color = light_gray

            # Calculate pixel boundaries for this square
            x_start = int(col * square_width)
            x_end = int((col + 1) * square_width)
            y_start = int(row * square_height)
            y_end = int((row + 1) * square_height)

            # Fill the square
            for y in range(y_start, y_end):
                for x in range(x_start, x_end):
                    pixels[x, y] = color

    # Save the image
    img.save(output_file)
    print(f"Image saved as {output_file}")

# Example usage: 6x7 board
create_checkered_board(2048, 2048, 7, 6, 'checkered_board_6x7.png')


# In[5]:


for board_size in [ 
    [3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[6,7],
            ]:

    create_checkered_board(2048, 2048, board_size[1], board_size[0], 
                       f'2025-11-14 khepera1/textures/squares{board_size[0]}x{board_size[1]}.png')


# In[ ]:




