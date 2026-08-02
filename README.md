<h1 align="center">🌸 Toko Bunga Cendana</h1>

<p align="center">
  Website e-commerce toko bunga sederhana berbasis HTML, CSS, Bootstrap, dan JavaScript.<br/>
  Dibuat sebagai proyek tugas mata kuliah Pemrograman Web.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
  <img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white"/>
</p>

---

## 📋 Deskripsi

**Toko Bunga Cendana** adalah website toko bunga online sederhana yang memungkinkan pengunjung melihat katalog produk, menambahkan ke keranjang belanja, dan melanjutkan pemesanan langsung via **WhatsApp**. Tidak memerlukan database atau login akun — semua data keranjang disimpan di `localStorage` browser.

---

## ✨ Fitur yang Tersedia

| Fitur | Keterangan | Status |
|---|---|---|
| 🏠 Beranda | Hero slider, kategori, produk unggulan | ✅ Berfungsi |
| 🛍️ Katalog Toko | Grid produk dengan filter harga | ✅ Berfungsi |
| 🔍 Detail Produk | Galeri foto, deskripsi, harga, rating, qty selector | ✅ Berfungsi |
| 🛒 Keranjang Belanja | Tambah/ubah/hapus item, kalkulasi total otomatis | ✅ Berfungsi |
| 💬 Checkout via WhatsApp | Ringkasan pesanan dikirim otomatis ke WhatsApp penjual | ✅ Berfungsi |
| 🎟️ Kode Kupon | Diskon 10% (`CENDANA10`) dan 20% (`CENDANA20`) | ✅ Berfungsi |
| 📞 Kontak | Form pesan + info kontak toko | ✅ Berfungsi |
| ℹ️ Tentang Kami | Profil toko | ✅ Berfungsi |
| 📱 Responsif | Tampilan optimal di semua ukuran layar | ✅ Berfungsi |

> **Catatan:** Fitur login akun, database pesanan, dan payment gateway tidak tersedia karena proyek ini bersifat frontend-only (tugas kuliah).

---

## 🗂️ Struktur Halaman

| Halaman | File | Keterangan |
|---|---|---|
| Beranda | `index.html` | Landing page utama |
| Toko | `shop.html` | Katalog semua produk |
| Detail Produk | `product-details.html` | Info produk + tombol Add to Cart |
| Tentang Kami | `about-us.html` | Profil toko |
| Kontak | `contact-us.html` | Form kontak via WhatsApp |
| Keranjang | `cart.html` | Manajemen item belanja (localStorage) |
| Checkout (legacy) | `cart.php` / `checkout.php` | File PHP lama, tidak digunakan aktif |

---

## ⚙️ Cara Kerja Keranjang Belanja

Keranjang menggunakan **`localStorage`** browser, sehingga:

- ✅ Tidak perlu server atau login
- ✅ Data tersimpan selama tab/browser tidak ditutup atau cache tidak dibersihkan
- ✅ Item yang ditambahkan dari halaman produk langsung muncul di `cart.html`
- ⚠️ Data akan hilang jika user membersihkan cache browser

**Alur Pemesanan:**
```
Pilih Produk → Atur Qty → Tambah ke Cart → Buka Keranjang → Pesan via WhatsApp
```

---

## 🛠️ Tech Stack

**Frontend:**
- HTML5 & CSS3
- [Bootstrap 4](https://getbootstrap.com/docs/4.6/) — layout & komponen UI
- [jQuery 3.6](https://jquery.com/) — manipulasi DOM & event
- [Swiper.js](https://swiperjs.com/) — slider/carousel produk
- [Magnific Popup](https://dimsemenov.com/plugins/magnific-popup/) — lightbox galeri foto
- [Nice Select](https://hernansartorio.com/jquery-nice-select/) — custom dropdown
- JavaScript `localStorage` — penyimpanan data keranjang

**Integrasi:**
- [WhatsApp API (wa.me)](https://wa.me/) — link pesan otomatis ke penjual

**Icon:**
- Font Awesome 4.x
- Linearicons Free

---

## 🚀 Cara Menjalankan Lokal

### Opsi A — Buka langsung di browser (untuk halaman `.html`)
Semua halaman `.html` bisa dibuka langsung tanpa server:
```
Klik dua kali → index.html
```

### Opsi B — Menggunakan PHP server (jika ingin menjalankan `cart.php` / `checkout.php`)

1. Clone repository:
   ```bash
   git clone https://github.com/ruhulikram/toko-bunga-cendana.git
   ```

2. Letakkan folder di direktori server lokal:
   - **XAMPP** → `C:\xampp\htdocs\toko-bunga-cendana\`
   - **Laragon** → `C:\laragon\www\toko-bunga-cendana\`

3. Jalankan Apache dari XAMPP/Laragon Control Panel.

4. Buka browser:
   ```
   http://localhost/toko-bunga-cendana/
   ```

---

## 📁 Struktur Folder

```
toko-bunga-cendana/
│
├── index.html              # Beranda
├── shop.html               # Katalog toko
├── product-details.html    # Detail produk
├── about-us.html           # Tentang kami
├── contact-us.html         # Kontak
├── cart.html               # Keranjang (localStorage-based)
├── cart.php                # Keranjang lama (PHP, legacy)
├── checkout.php            # Checkout lama (PHP, legacy)
│
├── assets/
│   ├── css/
│   │   ├── style.css               # CSS kustom utama
│   │   ├── plugins/                # CSS plugin
│   │   └── vendor/                 # CSS framework (Bootstrap, FontAwesome)
│   │
│   ├── js/
│   │   ├── main.js                 # JS utama (slider, offcanvas, cart qty)
│   │   ├── plugins/                # JS plugin (Swiper, Magnific, dll)
│   │   └── vendor/                 # JS library (jQuery, Bootstrap)
│   │
│   ├── images/
│   │   ├── product/                # Foto produk (small-size & large-size)
│   │   ├── slider/                 # Gambar hero banner
│   │   └── logo/                   # Logo toko
│   │
│   └── fonts/                      # Font icon (Linearicons, FontAwesome)
│
└── scripts/
    └── fix_nav.py                  # Utility: update navigasi HTML secara batch
```

---

## 📬 Kontak Toko

- 📞 WhatsApp / Telp: **081382920920**
- 📧 Email: **tokobungacendana@gmail.com**
- 📍 Alamat: Jl. Cendana No. 12, Kota Bandung, Jawa Barat

---

<p align="center">Dibuat dengan ❤️ sebagai proyek tugas kuliah Pemrograman Web</p>
