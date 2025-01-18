from utils import load_images,os
from turtuosity import arc_chord_ratio, total_curvature, total_squared_curvature, tortuosity_index
from Extract import crae, crve, avr


def process_dataset(folder_path):
    av_images = load_images(os.path.join(folder_path, 'av'))
    vessels_images = load_images(os.path.join(folder_path, 'vessels'))
    images = load_images(os.path.join(folder_path, 'images'))

    # Example calculation (you will need to define the parameters for each function call)
    arc_ratio = arc_chord_ratio(arc_length=1.0, chord_length=0.5)  # Example values
    total_curv = total_curvature(curvatures=[0.1, 0.2, 0.3])  # Example list of curvature values
    total_sq_curv = total_squared_curvature(curvatures=[0.1, 0.2, 0.3], chord_lengths=[1, 1, 1])  # Example lists
    tau_index = tortuosity_index(arc_lengths=[1.0, 1.2], chord_lengths=[0.8, 1.0])  # Example values

    crve_value = crve(diameters=[100, 120, 115])  # Example diameters
    crae_value = crae(diameters=[80, 85, 90])  # Example diameters
    avr_value = avr(crae_value, crve_value)
  # Print or store the calculated values
    print("Tortuosity Metrics:", arc_ratio, total_curv, total_sq_curv, tau_index)
    print("Arteriolar Narrowing Metrics:", crve_value, crae_value, avr_value)

# Run the processing for both training and testing sets
process_dataset(r"C:/Users/kpbrb/Downloads/Img")


