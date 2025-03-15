import os
from collections import defaultdict

# Klasör yolunu belirle
labels_dir = "labels"  # Label dosyalarının bulunduğu klasör

# Sınıf dağılımını tutacak sözlük
class_counts = defaultdict(int)

# Label klasöründeki tüm txt dosyalarını al
for label_file in os.listdir(labels_dir):
    if label_file.endswith(".txt"):
        label_path = os.path.join(labels_dir, label_file)

        # Label dosyasındaki tüm satırları oku ve sınıfları say
        with open(label_path, "r") as f:
            lines = f.readlines()
        
        for line in lines:
            class_id = line.split()[0]
            class_counts[class_id] += 1  # Sınıf sayısını artır

# Sonuçları ekrana yazdır
print("Class Partition:")
for class_id, count in sorted(class_counts.items()):
    print(f"Class {class_id}: {count} adet")
