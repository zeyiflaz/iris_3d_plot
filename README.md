# İris Veri Seti Görselleştirme

Merhaba! Bu projede **Iris veri seti** ile veri görselleştirme çalışmaları yaptım.  
Amacım hem 2B scatter plot hem de PCA ile boyut indirgenmiş 3B scatter plot oluşturarak veriyi daha iyi anlamak.

---

## Neler Yaptım?

1. **2B Scatter Plot**
   - İlk iki özelliği (sepal length ve sepal width) kullanarak her çiçek türünü renklendirdim.
   - Böylece hangi türlerin birbirine daha yakın olduğunu görselleştirdim.
   
2. **3B Scatter Plot (PCA ile)**
   - Veri setindeki 4 özelliği PCA kullanarak 3 boyuta indirdim.
   - Bu sayede verinin genel yapısını 3B olarak görebildim.
   - Her bir bileşen, verinin varyansını en iyi temsil eden doğrulara karşılık geliyor.

---

## Kullanılan Kütüphaneler

- `matplotlib` → Grafikler için
- `scikit-learn` → Veri seti ve PCA
- `numpy` → Hesaplamalar için (opsiyonel, burada direkt kullanılmadı)

---

## Nasıl Çalıştırılır?

1. Öncelikle gerekli kütüphaneleri yükle:
```bash
pip install matplotlib scikit-learn
"# iris_3d_plot" 
