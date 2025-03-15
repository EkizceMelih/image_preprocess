import os
import shutil
import random

# 🔹 Kendi bilgisayarındaki dataset yolu
dataset_dir = os.getcwd()  # Bulunduğun dizini otomatik alır, istersen elle yaz: "C:/Users/.../dataset"

# 🔹 Ana klasörleri belirle
images_dir = os.path.join(dataset_dir, "images")
labels_dir = os.path.join(dataset_dir, "labels")

# 🔹 Yeni bölme klasörlerini oluştur
split_dirs = {
    "train": {
        "images": os.path.join(images_dir, "train"),
        "labels": os.path.join(labels_dir, "train"),
    },
    "val": {
        "images": os.path.join(images_dir, "val"),
        "labels": os.path.join(labels_dir, "val"),
    },
    "test": {
        "images": os.path.join(images_dir, "test"),
        "labels": os.path.join(labels_dir, "test"),
    }
}

# 🔹 Yeni klasörleri oluştur
for split in split_dirs.values():
    os.makedirs(split["images"], exist_ok=True)
    os.makedirs(split["labels"], exist_ok=True)

# 🔹 Tüm görüntü dosyalarını al ve alfabetik sıraya göre düzenle
image_files = sorted([f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png', '.jpeg'))])

# 🔹 Aynı rastgele bölme için seed kullan
random.seed(42)
random.shuffle(image_files)

# 🔹 %80-10-10 oranında böl
train_split = int(0.80 * len(image_files))
val_split = int(0.90 * len(image_files))

train_files = image_files[:train_split]
val_files = image_files[train_split:val_split]
test_files = image_files[val_split:]

# 🔹 Dosyaları taşıma fonksiyonu
def move_files(file_list, split_name):
    for file in file_list:
        image_src = os.path.join(images_dir, file)
        label_src = os.path.join(labels_dir, os.path.splitext(file)[0] + ".txt")  # Aynı isimdeki label dosyası

        image_dst = os.path.join(split_dirs[split_name]["images"], file)
        label_dst = os.path.join(split_dirs[split_name]["labels"], os.path.splitext(file)[0] + ".txt")

        shutil.move(image_src, image_dst)  # Görüntüyü taşı
        if os.path.exists(label_src):  # Eğer etiket dosyası varsa taşı
            shutil.move(label_src, label_dst)

# 🔹 Dosyaları böl ve taşı
move_files(train_files, "train")
move_files(val_files, "val")
move_files(test_files, "test")

print(f"✅ Bölme tamamlandı: {len(train_files)} train, {len(val_files)} val, {len(test_files)} test.")
