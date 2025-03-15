import os

# Klasör yolunu belirle
labels_dir = "labels"  # Label dosyalarının bulunduğu klasör

# Değişim kuralları
class_mapping = {
    "1": "5",
    "7":"4",
    "10":"2",
    "13":"4",
    "14":"3",
    "16":"4",
    "19":"4",
}

# Label klasöründeki tüm txt dosyalarını al
for label_file in os.listdir(labels_dir):
    if label_file.endswith(".txt"):
        label_path = os.path.join(labels_dir, label_file)

        # Dosyayı oku ve satırları güncelle
        with open(label_path, "r") as f:
            lines = f.readlines()

        updated_lines = []
        for line in lines:
            parts = line.split()
            class_id = parts[0]
            if class_id in class_mapping:
                parts[0] = class_mapping[class_id]  # Sınıf ID'sini değiştir
            updated_lines.append(" ".join(parts))  # Güncellenmiş satırı ekle

        # Güncellenmiş içeriği dosyaya yaz
        with open(label_path, "w") as f:
            f.write("\n".join(updated_lines) + "\n")  # Satır sonları korunur

print("Sınıf numaraları güncellendi.")
