import pydicom
import matplotlib.pyplot as plt

# Cesta k DICOM súboru
dicom_path = r'C:\Users\petre\PycharmProjects\Dicom\MRBRAIN.DCM'

# Načítaj DICOM súbor, Funkcie vytvori objekt, ktory obsahuje data aj metadata
dicom_data = pydicom.dcmread(dicom_path)


print(f"ID pacienta: {dicom_data.PatientID}")
print(f"Meno pacienta: {dicom_data.PatientName}")
print(f"Dátum vyšetrenia: {dicom_data.StudyDate}")
print(f"Typ snímky: {dicom_data.SOPClassUID}")
print(f"Rozmery snímku: {dicom_data.pixel_array.shape}")

# Získaj počet snímok, Zistuje sa ci je snimka 3D
num_slices = dicom_data.pixel_array.shape[0] if len(dicom_data.pixel_array.shape) == 3 else 1
if num_slices == 1:
    plt.imshow(dicom_data.pixel_array, cmap='Grays')
    plt.show()
else:
    cols = 5  # počet stĺpcov v mriežke
    rows = (num_slices // cols) + (num_slices % cols > 0) # Vypocitanie poctu riadkov na zaklade poctu snimkov

    fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 4)) # Vytvorenie mriezky a nadstavi velkost kazdeho podgrafu
    axes = axes.flatten()  #Jednorozmerny zoznam

    # Prejdi všetky snímky a zobraz ich // gray,plasma,inferno
    for i in range(num_slices):
        axes[i].imshow(dicom_data.pixel_array[i], cmap='grey') # Zobrazenie snimky
        axes[i].axis('off') # skrytie osi
        axes[i].set_title(i + 1) # oznacenie podframov


    plt.tight_layout() # rozmiestnenie grafov
    plt.show() # Zobrazi graficky vystup v okne
