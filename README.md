# Kripto Para Dönüştürücü

[Coinlore API](https://www.coinlore.com/cryptocurrency-data-api) üzerinden canlı kripto para fiyatlarını çekip, iki farklı coin arasında anlık dönüşüm hesaplayan basit bir **Streamlit** uygulaması.

##  Özellikler

- Coinlore API'den **canlı fiyat verisi** çekme
- Sidebar üzerinden **eldeki coin**, **miktar** ve **hedef coin** seçimi
- Seçilen miktarın karşılığını hedef coin cinsinden hesaplama
- Coinbase üzerinden ilgili coin çifti için **"Satın Al"** yönlendirme butonu

##  Kullanılan Teknolojiler

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Requests](https://docs.python-requests.org/)

## Kurulum

1. Bu depoyu klonlayın:
   ```bash
   git clone https://github.com/kullanici-adi/repo-adi.git
   cd repo-adi
   ```

2. Gerekli paketleri yükleyin:
   ```bash
   pip install streamlit requests
   ```

3. Uygulamayı çalıştırın:
   ```bash
   streamlit run app.py
   ```

##  Kullanım

1. Uygulama açıldığında sol menüden **elinizdeki coini** seçin.
2. **Miktar** girin (not: mevcut kodda bu değer sabit olarak 20'ye ayarlanmıştır, bkz. *Bilinen Sorunlar*).
3. **Hedef coini** seçin.
4. Hesaplanan karşılık miktarı ekranda görüntülenir.
5. "Satın Al" butonuna tıklayarak Coinbase üzerinden ilgili çifti inceleyebilirsiniz.

##  Bilinen Sorunlar

- Kodda `miktar = st.sidebar.number_input("Miktar")` satırından sonra `miktar = 20` satırı, kullanıcının girdiği değeri geçersiz kılıp sabit olarak 20 yapıyor. Kullanıcı girişinin gerçekten kullanılmasını istiyorsanız bu satırı kaldırmanız gerekir.
- Coinlore API'de her coin sembolü **benzersiz olmayabilir**; bazı farklı coinler aynı sembolü paylaşabilir, bu da `coinfiyat` sözlüğünde üzerine yazılmaya (overwrite) neden olabilir.
- API isteği başarısız olursa (bağlantı hatası, zaman aşımı vb.) uygulama şu an hata yönetimi yapmıyor.

##  Yapılacaklar / Geliştirme Fikirleri

- [ ] Sabit `miktar = 20` satırını kaldırıp kullanıcı girdisini kullanma
- [ ] API çağrısı için try/except ile hata yönetimi ekleme
- [ ] Coin id'lerini sembol yerine kullanarak çakışmaları önleme
- [ ] Sonuçları daha okunabilir formatta (örn. yuvarlama, para birimi ikonları) gösterme

##  Lisans

Bu proje istediğiniz lisans altında paylaşılabilir (örn. MIT).
