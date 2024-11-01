# #%%
# # Import libraries
# import pandas as pd
# import matplotlib.pyplot as plt
# #%%
# # Defining data for the dataframe
# data = {
#     'Basket': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
#     'Apples': [10, 20, 30, 56, 40, 40, 67, 47, 40, 4, 49, 52, 5, 56, 35, 45],
#     'Bananas': [15, 6, 3, 45, 67, 44, 45, 11, 14, 18, 13, 12, 1, 34, 12, 12]
# }
#
# # Creating the dataframe
# df = pd.DataFrame(data)
#
# df
# #%%
# # Calculate the sums
# sum_apples = df['Apples'].sum()
# sum_bananas = df['Bananas'].sum()
#
# # Create a bar chart
# plt.bar(['Apples', 'Bananas'], [sum_apples, sum_bananas], color=['red', 'blue'])
#
# # Set a title
# plt.title('Comparison of total Apples and Bananas')
#
# # Show the plot
# plt.show()


from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

def svg_to_png(input_svg_path, output_png_path, dpi=288):
    # Load the SVG as a reportlab drawing object
    drawing = svg2rlg(input_svg_path)

    # Convert the SVG drawing to a PNG image at the specified DPI
    renderPM.drawToFile(drawing, output_png_path, fmt="PNG", dpi=dpi)

name = "Remaning Years 1"

# Usage example
input_svg = f"svg/{name}.svg"  # Input SVG file path
output_png = f"png/{name}.png"  # Output PNG file path
svg_to_png(input_svg, output_png)
