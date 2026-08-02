<h1 align="center">🌸 Toko Bunga Cendana</h1>

<p align="center">
  Website e-commerce toko bunga berbasis HTML, CSS, Bootstrap, dan PHP.
  <br/>
  Dibuat sebagai proyek tugas mata kuliah Pemrograman Web.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/>
  <img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white"/>
  <img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white"/>
</p>

---

## 📋 Deskripsi

**Toko Bunga Cendana** adalah website toko bunga online yang menampilkan katalog produk bunga, memungkinkan pengguna untuk memilih produk, menambahkan ke keranjang belanja, dan melanjutkan proses checkout yang terintegrasi langsung dengan **WhatsApp** penjual.

---

## ✨ Fitur Utama

| Fitur | Keterangan |
|---|---|
| 🏠 Halaman Beranda | Hero slider, kategori unggulan, produk terbaru, dan testimoni pelanggan |
| 🛍️ Katalog Toko | Grid produk dengan filter kategori dan harga menggunakan jQuery UI Slider |
| 🔍 Detail Produk | Galeri foto, deskripsi, pilihan jumlah, dan tombol tambah ke keranjang |
| 🛒 Keranjang Belanja | Kelola item, ubah kuantitas, dan lihat subtotal secara dinamis (PHP session) |
| 💳 Checkout | Form data pemesan + integrasi otomatis link WhatsApp penjual |
| ℹ️ Tentang Kami | Profil toko, tim, dan nilai-nilai perusahaan |
| 📞 Kontak | Form pesan dan informasi kontak lengkap |
| 💖 Wishlist | Halaman daftar keinginan produk favorit |
| 📱 Responsif | Tampilan optimal di desktop, tablet, dan smartphone |

---

## 🗂️ Struktur Folder

```
toko-bunga-cendana/
│
├── index.html              # Halaman beranda
├── shop.html               # Halaman katalog toko
├── product-details.html    # Halaman detail produk
├── about-us.html           # Halaman tentang kami
├── contact-us.html         # Halaman kontak
├── cart.php                # Halaman keranjang belanja (PHP session)
├── checkout.php            # Halaman checkout + integrasi WhatsApp
├── wishlist.html           # Halaman wishlist
│
├── assets/
│   ├── css/
│   │   ├── style.css               # CSS utama kustom
│   │   ├── plugins/                # CSS plugin pihak ketiga
│   │   │   ├── animate.min.css
│   │   │   ├── swiper-bundle.min.css
│   │   │   ├── magnific-popup.css
│   │   │   ├── nice-select.min.css
│   │   │   └── jquery-ui.min.css
│   │   └── vendor/                 # CSS framework
│   │       ├── bootstrap.min.css
│   │       ├── font.awesome.min.css
│   │       └── linearicons.min.css
│   │
│   ├── js/
│   │   ├── main.js                 # JS utama kustom
│   │   ├── plugins/                # JS plugin pihak ketiga
│   │   │   ├── swiper-bundle.min.js
│   │   │   ├── jquery.magnific-popup.min.js
│   │   │   ├── nice-select.min.js
│   │   │   ├── jquery-ui.min.js
│   │   │   └── jquery.countdown.min.js
│   │   └── vendor/                 # JS library utama
│   │       ├── jquery-3.6.0.min.js
│   │       ├── bootstrap.bundle.min.js
│   │       └── modernizr-3.7.1.min.js
│   │
│   ├── fonts/                      # Font ikon (Linearicons, FontAwesome)
│   └── images/                     # Semua aset gambar
│       ├── product/                # Foto produk bunga
│       ├── slider/                 # Gambar hero banner
│       ├── logo/                   # Logo toko
│       └── ...                     # Subfolder lainnya
│
└── scripts/
    └── fix_nav.py                  # Utility script pembaruan navigasi HTML
```

---

## 🛠️ Tech Stack

**Frontend:**
- HTML5 & CSS3
- [Bootstrap 4](https://getbootstrap.com/docs/4.6/) — grid system & komponen UI
- [jQuery 3.6](https://jquery.com/) — manipulasi DOM
- [Swiper.js](https://swiperjs.com/) — slider/carousel
- [Magnific Popup](https://dimsemenov.com/plugins/magnific-popup/) — lightbox galeri
- [Nice Select](https://hernansartorio.com/jquery-nice-select/) — custom dropdown
- [jQuery Countdown](https://hilios.github.io/jQuery.countdown/) — hitung mundur promo

**Backend:**
- PHP (Native) — manajemen session keranjang belanja

**Integrasi:**
- WhatsApp API (wa.me) — link checkout otomatis ke penjual

**Icons:**
- Font Awesome 4.x
- Linearicons Free

---

## 🚀 Cara Menjalankan Lokal

> Diperlukan **PHP server lokal** karena fitur cart & checkout menggunakan PHP session.

**Menggunakan XAMPP / Laragon / MAMP:**

1. Clone atau download repository ini:
   ```bash
   git clone https://github.com/ruhulikram/toko-bunga-cendana.git
   ```

2. Letakkan folder project di dalam direktori server:
   - **XAMPP** → `C:\xampp\htdocs\toko-bunga-cendana\`
   - **Laragon** → `C:\laragon\www\toko-bunga-cendana\`

3. Jalankan Apache dari XAMPP/Laragon Control Panel.

4. Buka browser dan akses:
   ```
   http://localhost/toko-bunga-cendana/
   ```

> **Catatan:** Halaman `.html` bisa dibuka langsung di browser tanpa server. Namun `cart.php` dan `checkout.php` **wajib** dijalankan melalui PHP server.

---

## 📄 Halaman

| Halaman | File | Keterangan |
|---|---|---|
| Beranda | `index.html` | Landing page utama |
| Toko | `shop.html` | Katalog semua produk |
| Detail Produk | `product-details.html` | Info detail + galeri produk |
| Tentang Kami | `about-us.html` | Profil & tim toko |
| Kontak | `contact-us.html` | Informasi & form kontak |
| Keranjang | `cart.php` | Manajemen item belanja |
| Checkout | `checkout.php` | Form & integrasi WhatsApp |
| Wishlist | `wishlist.html` | Daftar produk favorit |

---

## 🎓 Tentang Proyek

Proyek ini dibuat sebagai tugas akhir mata kuliah **Pemrograman Web** dengan tujuan:
- Menerapkan konsep desain UI/UX website e-commerce modern
- Mengimplementasikan fitur cart sederhana berbasis PHP session
- Mengintegrasikan layanan pihak ketiga (WhatsApp) dalam alur checkout

---

## 📬 Kontak

Jika ada pertanyaan atau saran, silakan hubungi melalui fitur **Issues** di repository ini.

---

<p align="center">Dibuat dengan ❤️ sebagai proyek kuliah</p>
