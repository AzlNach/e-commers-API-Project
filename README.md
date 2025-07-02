# E-Commerce API Project - FlashCart

Sebuah aplikasi e-commerce modern yang dibangun menggunakan Flask dan terintegrasi dengan DummyJSON API untuk menampilkan produk. FlashCart menyediakan pengalaman berbelanja online yang lengkap dengan fitur pencarian, kategori produk, dan manajemen keranjang belanja.

## 🚀 Fitur Utama

### 1. **Katalog Produk**
- Menampilkan daftar produk dengan pagination
- Tampilan grid responsif dengan kartu produk yang menarik
- Detail produk lengkap dengan gambar, harga, rating, dan deskripsi
- Badge diskon dan indikator stok
- Gallery gambar produk dengan thumbnail navigation

### 2. **Pencarian & Filter**
- Pencarian produk berdasarkan kata kunci
- Filter produk berdasarkan kategori
- Navigasi kategori dinamis yang dimuat dari API
- Breadcrumb navigation untuk kemudahan navigasi

### 3. **Keranjang Belanja**
- Tambah produk ke keranjang dengan animasi
- Update quantity produk dalam keranjang
- Hapus item dari keranjang
- Ringkasan pesanan dengan kalkulasi pajak
- Persistent cart menggunakan Flask session

### 4. **UI/UX Modern**
- Desain responsif dengan Bootstrap 5
- Animasi dan transisi yang smooth
- Toast notifications untuk feedback user
- Loading states dan error handling
- Dark mode friendly color scheme

## 🛠️ Teknologi yang Digunakan

### Backend
- **Flask** - Web framework Python
- **Python 3.x** - Programming language
- **Requests** - HTTP library untuk API calls
- **Flask Session** - Session management

### Frontend
- **HTML5** - Markup language
- **CSS3** - Styling dengan custom variables
- **JavaScript (ES6+)** - Interactive functionality
- **Bootstrap 5** - CSS framework
- **Font Awesome 6** - Icon library
- **Google Fonts (Poppins)** - Typography

### API Integration
- **DummyJSON API** - External API untuk data produk
  - Products endpoint: `https://dummyjson.com/products`
  - Categories endpoint: `https://dummyjson.com/products/categories`
  - Search endpoint: `https://dummyjson.com/products/search`

## 📁 Struktur Project

```
e-commers-API-Project/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── index.html         # Homepage & product listing
│   ├── product_detail.html # Product detail page
│   └── view_cart.html     # Shopping cart page
├── static/
│   └── css/
│       └── product_detail.html # Additional CSS (legacy)
└── README.md              # Project documentation
```

## 🔧 Instalasi & Setup

### Prasyarat
- Python 3.7 atau versi terbaru
- pip (Python package manager)

### Langkah Instalasi

1. **Clone repository**
```bash
git clone https://github.com/username/e-commers-API-Project.git
cd e-commers-API-Project
```

2. **Install dependencies**
```bash
pip install flask requests
```

3. **Jalankan aplikasi**
```bash
python app.py
```

4. **Akses aplikasi**
Buka browser dan kunjungi: `http://localhost:5000`

## 🌐 API Endpoints

### Internal Routes
- `GET /` - Homepage dengan daftar produk
- `GET /product/<id>` - Detail produk
- `GET /search?q=<query>` - Pencarian produk
- `GET /category/<category>` - Produk berdasarkan kategori
- `GET /cart` - Halaman keranjang belanja
- `GET /add-to-cart/<id>` - Tambah produk ke keranjang
- `GET /remove-from-cart/<id>` - Hapus produk dari keranjang
- `POST /update-cart/<id>` - Update quantity produk
- `GET /api/categories` - Daftar kategori (JSON)

### External API Integration
- **DummyJSON Products API**
  - Base URL: `https://dummyjson.com/products`
  - Mendukung pagination, search, dan filter kategori
  - Response format: JSON dengan metadata lengkap

## 🔄 Alur Sistem

### 1. **Inisialisasi Aplikasi**
```
Flask App Start → Load Routes → Initialize Session → Ready to Serve
```

### 2. **Flow Tampilan Produk**
```
User Request → Flask Route → API Call to DummyJSON → 
Process Response → Render Template → Return HTML
```

### 3. **Flow Pencarian**
```
User Input Search → Submit Form → Flask Search Route → 
API Call with Query → Filter Results → Display Results
```

### 4. **Flow Keranjang Belanja**
```
Add to Cart → Get Product Data from API → 
Store in Session → Update Cart Count → 
Redirect to Cart Page → Display Cart Items
```

### 5. **Flow Update Keranjang**
```
User Modify Quantity → POST Request → 
Update Session Data → Recalculate Total → 
Redirect Back to Cart
```

## 📊 Manajemen Data

### Session Management
- **Cart Storage**: Menggunakan Flask session untuk menyimpan data keranjang
- **Data Structure**: List of dictionaries dengan fields:
  ```python
  {
      'id': product_id,
      'title': product_title,
      'price': product_price,
      'thumbnail': product_image,
      'quantity': item_quantity
  }
  ```

### API Data Handling
- **Error Handling**: Graceful handling untuk API failures
- **Data Validation**: Validasi response dari external API
- **Caching Strategy**: Real-time data fetching (no caching)

## 🎨 Fitur UI/UX

### Responsive Design
- Mobile-first approach
- Breakpoints untuk tablet dan desktop
- Flexible grid system

### Interactive Elements
- Hover effects pada product cards
- Smooth transitions dan animations
- Loading indicators
- Toast notifications
- Image zoom pada product detail

### Accessibility
- Semantic HTML structure
- ARIA labels untuk screen readers
- Keyboard navigation support
- High contrast color scheme

## 🔒 Keamanan

- **Session Security**: Secret key untuk session encryption
- **Input Validation**: Validasi input user
- **XSS Protection**: Escape HTML dalam templates
- **CSRF Protection**: Form validation (dapat ditingkatkan)

## 🚧 Pengembangan Selanjutnya

### Fitur yang Dapat Ditambahkan
- [ ] User authentication & registration
- [ ] Wishlist functionality
- [ ] Product reviews dan ratings
- [ ] Payment gateway integration
- [ ] Order history dan tracking
- [ ] Admin panel untuk manage products
- [ ] Real-time inventory management
- [ ] Multi-language support

### Optimisasi
- [ ] Database integration (PostgreSQL/MySQL)
- [ ] Caching dengan Redis
- [ ] API rate limiting
- [ ] Image optimization
- [ ] SEO improvements
- [ ] Performance monitoring

## 📈 Monitoring & Analytics

### Error Logging
- Flask error handling
- API call monitoring
- User action tracking

### Performance Metrics
- Page load times
- API response times
- User engagement metrics

## 🤝 Kontribusi

1. Fork repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 Lisensi

Project ini menggunakan lisensi MIT. Lihat file `LICENSE` untuk detail.

## 👨‍💻 Developer

- **Email**: azelpandy2@gmail.com
- **Phone**: (+62) 87770144273
- **Address**: Jl. Bojongsantos

## 🙏 Acknowledgments

- [DummyJSON](https://dummyjson.com/) - Untuk API data produk
- [Bootstrap](https://getbootstrap.com/) - CSS framework
- [Font Awesome](https://fontawesome.com/) - Icon library
- [Google Fonts](https://fonts.google.com/) - Typography