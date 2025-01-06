
# Türkçe Metin Özetleme Modeli (T5 Fine-Tuning)

Bu proje, Türkçe metin özetleme görevi için T5 (Text-to-Text Transfer Transformer) modelinin **fine-tuning** işlemine odaklanmaktadır. Eğitim sürecinde, [musabg/wikipedia-tr-summarization](https://huggingface.co/datasets/musabg/wikipedia-tr-summarization) veri seti kullanılmıştır.

## 🚀 Özellikler
- **Dil:** Türkçe
- **Model:** T5-small
- **Veri Seti:** Türkçe metinler ve özetlerden oluşan bir veri seti
- **Eğitim Süreci:**
  - Büyük veri setini bellek sınırlarını aşmamak için parçalara böler.
  - Küçük batch boyutları ve gradient accumulation kullanılarak bellek verimliliği sağlanır.
  - Bellek temizleme işlemleriyle GPU kullanım optimizasyonu yapılır.
- **Değerlendirme Metriği:** ROUGE

## 🔧 Gereksinimler
Bu proje için gerekli Python kütüphaneleri:
- `transformers`
- `datasets`
- `accelerate`
- `torch`
- `rouge_score`

Kurulum:
```bash
pip install transformers datasets accelerate rouge_score
```

## 📖 Kullanım
Model, metinleri özetlemek için aşağıdaki adımları takip eder:

1. **Model ve Tokenizer'ı Yükleyin:**
   ```python
   from transformers import T5Tokenizer, T5ForConditionalGeneration

   tokenizer = T5Tokenizer.from_pretrained("path/to/fine_tuned_model")
   model = T5ForConditionalGeneration.from_pretrained("path/to/fine_tuned_model")
   ```

2. **Bir Metni Özetleyin:**
   ```python
   input_text = "Türkçe özetleme yapmak için bu metni kullanabilirsiniz."
   inputs = tokenizer(input_text, return_tensors="pt", max_length=256, truncation=True, padding="max_length")
   summary_ids = model.generate(inputs["input_ids"], max_length=64, num_beams=4, early_stopping=True)
   predicted_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
   print("Özetlenmiş Metin:", predicted_summary)
   ```

## 🏋️‍♂️ Eğitim Süreci
- Model, eğitim için parçalanmış veri seti üzerinde her parça ayrı ayrı işlenerek eğitilmiştir.
- Her parça eğitildikten sonra model kaydedilmiş ve bellek temizlenmiştir.

**Adımlar:**
1. Veri seti parçalanır (ör. 10.000 satırlık parçalara).
2. Her parça ayrı ayrı tokenleştirilir.
3. T5-small modeli her parça üzerinde eğitilir.
4. Bellek optimizasyonu için `torch.cuda.empty_cache()` kullanılır.

## 📂 Proje Yapısı
- `fine_tuning_dataset_split.py`: Eğitim işlemini parçalara bölen ve GPU belleği optimizasyonuyla eğitim yapan Python kodu.
- `results/`: Eğitimden elde edilen model sonuçları.
- `logs/`: Eğitim sırasında oluşan log dosyaları.

## 📊 Değerlendirme
- Eğitimden sonra model, ROUGE metrikleri ile değerlendirilmiştir.

## 📜 Lisans
Bu proje **MIT lisansı** ile paylaşılmaktadır.
