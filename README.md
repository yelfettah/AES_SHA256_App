🔐 Kripto Web Uygulaması

Bu proje, modern ve kullanıcı dostu 
bir arayüzle AES ve RSA şifreleme/şifre çözme işlemleri ile SHA-256 özet fonksiyonunu bir araya getiren, Python (Flask) tabanlı bir web uygulamasıdır. Hem metin hem de dosya üzerinde kriptografik işlemler yapabilir, güvenliğin temel taşlarını uygulamalı olarak deneyimleyebilirsiniz.

🚀 Özellikler


🔸 AES Şifreleme & Çözme
Kullanıcının girdiği metni belirlenen anahtar ile AES (CBC modu) kullanarak şifreleyebilir veya çözebilirsiniz.
IV (Initialization Vector) otomatik üretilir ve Base64 formatında gösterilir.
Şifreli metin ve IV kolayca kopyalanabilir. </br>
🔸 RSA Anahtar Üretimi, Şifreleme & Çözme
Tek tıkla yeni bir RSA anahtar çifti (2048 bit) oluşturabilirsiniz.
Public key ile şifreleme, private key ile çözme işlemleri yapılabilir.
Anahtarlar PEM formatında sunulur, kolayca kopyalanabilir.
Şifreli metin Base64 formatındadır.</br>
🔸 SHA-256 Özet Fonksiyonu
Metin ya da dosya girdisi ile SHA-256 özetini anında hesaplayabilirsiniz.
Dosya yükleme desteği ile büyük boyutlu verilerin özeti alınabilir.</br> </br>
🎨 Modern ve Animasyonlu Arayüz </br>
Her algoritma için ayrı ve estetik tasarıma sahip sayfalar.
Kolay gezinme ve kullanıcı dostu deneyim.
Animasyonlarla zenginleştirilmiş sade arayüz. </br></br>
🛠️ Kullanılan Teknolojiler

Backend: Python, Flask, pycryptodome</br>
Frontend: HTML5, CSS3 (modern animasyonlarla), JavaScript (Fetch API)</br>
Kriptografi: AES (CBC), RSA (2048 bit, OAEP), SHA-256</br></br>
⚙️ Kurulum ve Çalıştırma

Gereksinimler:</br>
Python 3.7+</br>
pip</br>
Bağımlılıkları Yükleyin:</br>
pip install -r requirements.txt</br>
Uygulamayı Başlatın:</br>
python app.py</br>
Tarayıcıda Açın:</br>
http://127.0.0.1:5000</br></br>
📄 Sayfalar ve Kullanım

/aes → AES ile metin şifreleme ve çözme</br>
/rsa → RSA anahtar üretimi, şifreleme ve çözme</br>
/ → SHA-256 özet fonksiyonu (metin ve dosya için)</br> </br>
🖼️ Ekran Görüntüleri

<img width="1440" alt="Ekran Resmi 2025-06-04 00 07 31" src="https://github.com/user-attachments/assets/97db6739-66dc-4bee-b307-96c778f38ecc" />
<img width="1440" alt="Ekran Resmi 2025-06-04 00 07 43" src="https://github.com/user-attachments/assets/9f1df78c-8111-4f83-bf07-13a91eabfd18" />
<img width="1440" alt="Ekran Resmi 2025-06-04 00 07 55" src="https://github.com/user-attachments/assets/745ab510-df0a-4c28-b2d0-9a0d4a1c2dba" />
<img width="1440" alt="Ekran Resmi 2025-06-04 00 08 38" src="https://github.com/user-attachm<img width="1440" alt="Ekran Resmi 2025-06-04 00 10 10" src="https://github.com/user-attachments/assets/18b39783-e422-4b2c-8077-9f09f63c8c7d" />
ents/assets/c2644b62-6150-4bd1-8385-daeb6b84b0e9" />
<img width="1440" alt="Ekran Resmi 2025-06-04 00 11 00" src="https://github.com/user-attachments/assets/92a42461-2d33-4f68-8ad0-17b49b3cb897" />

🔒 Güvenlik Notları</br>

⚠️ Bu uygulama eğitim ve demo amaçlıdır. Gerçek hayatta, hassas veriler için profesyonel güvenlik önlemleri alınmalıdır.
Anahtarlar ve şifreli veriler sunucu tarafında saklanmaz.</br>
🤝 Katkı ve Lisans</br>

Katkıda bulunmak isterseniz, bir pull request gönderin!
Bu proje MIT Lisansı ile lisanslanmıştır.
Geri bildirim, öneri ve hata bildirimleriniz için iletişime geçebilirsiniz.</br>
🔐 İyi şifrelemeler dileriz!
