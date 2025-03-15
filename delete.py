import os

# Klasör yollarını belirle
labels_dir = "labels"  # Label dosyalarının bulunduğu klasör
images_dir = "images"  # Görsellerin bulunduğu klasör

# Kullanılabilir classlar
valid_classes = {"1","7","10","13","14","16","19"}

# Label klasöründeki tüm txt dosyalarını al
for label_file in os.listdir(labels_dir):
    if label_file.endswith(".txt"):
        label_path = os.path.join(labels_dir, label_file)
        image_path = os.path.join(images_dir, label_file.replace(".txt", ".jpg"))  # JPG uzantılı resim varsayıldı
        image_path_png = os.path.join(images_dir, label_file.replace(".txt", ".png"))  # PNG de kontrol için

        # Yeni içerik oluştur
        with open(label_path, "r") as f:
            lines = f.readlines()

        # Geçerli class'ları filtrele
        filtered_lines = [line for line in lines if line.split()[0] in valid_classes]

        if filtered_lines:
            # Eğer 2 veya 3 class'ı varsa, dosyayı güncelle
            with open(label_path, "w") as f:
                f.writelines(filtered_lines)
        else:
            # Eğer hiç 2 veya 3 class'ı kalmadıysa, label ve image dosyalarını sil
            os.remove(label_path)
            if os.path.exists(image_path):
                os.remove(image_path)
            elif os.path.exists(image_path_png):  # PNG uzantılı resim varsa onu da sil
                os.remove(image_path_png)

print("İşlem tamamlandı.")
