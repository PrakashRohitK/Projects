import os
import numpy as np
import cv2
import matplotlib.pyplot as plt



def CalculateArcCordRatio(Liarc, Lichord):
    if len(Liarc) != len(Lichord):
        raise ValueError("Liarc and Lichord must have the same length.")
    ACRi = [Liarc[i] / Lichord[i] if Lichord[i] != 0 else 0 for i in range(len(Liarc))]
    return ACRi


def CalculateCRAE(diameters_arterioles):
    n = len(diameters_arterioles)
    if n == 0: return 0
    squared_diameters = [wa ** 2 for wa in diameters_arterioles]
    average_squared = sum(squared_diameters) / n
    CRAE = np.sqrt(average_squared)
    return CRAE


def CalculateCRVE(diameters_venules):
    n = len(diameters_venules)
    if n == 0: return 0
    squared_diameters = [wv ** 2 for wv in diameters_venules]
    average_squared = sum(squared_diameters) / n
    CRVE = np.sqrt(average_squared)
    return np.float64(CRVE)


def ProcessRFIData(segmented_vessels):
    diameters_arterioles = segmented_vessels.get('arteries', [])
    diameters_venules = segmented_vessels.get('veins', [])
    Lichord = segmented_vessels.get('LiChord', [])
    Liarc = segmented_vessels.get('LiArc', [])

    CRAE = CalculateCRAE(diameters_arterioles)
    CRVE = CalculateCRVE(diameters_venules)
    ACR = CalculateArcCordRatio(Liarc, Lichord)

    biomarkers = {
        'CRAE': round(float(CRAE), 2),
        'CRVE': round(float(CRVE), 2),
        'ACR': ACR if ACR is None else [round(float(acri), 2) for acri in ACR]
    }
    return biomarkers


def ExtractVesselParameters(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(closed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    diameters_arterioles = []
    diameters_venules = []
    Lichord = []
    Liarc = []

    for contour in contours:
        arc_length = cv2.arcLength(contour, True)
        chord_length = cv2.norm(contour[0] - contour[-1])

        if len(contour) >= 5:
            ellipse = cv2.fitEllipse(contour)
            (x, y), (major_axis, minor_axis), angle = ellipse
            diameter = (major_axis + minor_axis) / 2

            if diameter < 10:  # Example threshold
                diameters_arterioles.append(diameter)
            else:
                diameters_venules.append(diameter)

        Liarc.append(arc_length)
        Lichord.append(chord_length)

    segmented_vessels = {
        'arteries': diameters_arterioles,
        'veins': diameters_venules,
        'LiArc': Liarc,
        'LiChord': Lichord,
    }
    return segmented_vessels


folder_path = r"C:\Users\kpbrb\Downloads\Img"
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.tif', '.jpg', '.png'))]
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if image is not None:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image_rgb)
        plt.title(f'Original Image: {image_file}')
        plt.axis('off')
        plt.show()
        segmented_vessels = ExtractVesselParameters(image)
        biomarkers = ProcessRFIData(segmented_vessels)
        print(f'Biomarkers for {image_file}: {biomarkers}')
    else:
        print(f"Failed to load image: {image_file}")
