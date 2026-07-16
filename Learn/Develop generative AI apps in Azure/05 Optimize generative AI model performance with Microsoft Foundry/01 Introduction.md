
Language models เป็นเครื่องมือที่ทรงพลังสำหรับการสร้าง generative AI applications แต่การใช้ base model เพียงอย่างเดียวอาจยังไม่ตอบโจทย์ทุกความต้องการของคุณ คุณภาพ ความแม่นยำ และความสม่ำเสมอของ responses ที่โมเดลสร้างขึ้น ขึ้นอยู่กับวิธีที่คุณ configure และ augment โมเดลนั้น

ลองจินตนาการว่าคุณเป็น developer ที่ทำงานให้กับ travel agency และกำลังสร้าง chat application เพื่อช่วยลูกค้าตอบคำถามเกี่ยวกับการเดินทาง แม้ base model จะให้ responses ได้ดีในระดับหนึ่ง แต่ทีมของคุณมีความต้องการเฉพาะ: responses ต้องสอดคล้องกับ tone of voice ของบริษัท มีข้อมูลที่ถูกต้องเกี่ยวกับ hotel catalog และคงรูปแบบให้สม่ำเสมอในทุก interaction แล้วคุณจะทำอย่างไรให้โมเดลทำงานได้ถึงระดับนี้?

มีหลายกลยุทธ์ที่สามารถใช้ร่วมกันเพื่อ optimize ประสิทธิภาพของ generative AI model ได้ กลยุทธ์เหล่านี้มีตั้งแต่การปรับแบบรวดเร็วและต้นทุนต่ำ ไปจนถึงเทคนิคที่ซับซ้อนขึ้นซึ่งต้องใช้เวลาและทรัพยากรเพิ่มเติม

![Diagram showing the various strategies to optimize the model's performance, from prompt engineering to RAG and fine-tuning.|822](https://learn.microsoft.com/en-us/training/wwl-data-ai/optimize-generative-ai-model-performance/media/model-optimization.png)

ตลอดทั้งโมดูลนี้ คุณจะได้สำรวจแต่ละกลยุทธ์ และเรียนรู้ว่าควรนำไปใช้อย่างไร เมื่อใดควรใช้เดี่ยวๆ และเมื่อใดควรใช้ร่วมกัน

> [!NOTE]
> เราเข้าใจว่าผู้เรียนแต่ละคนมีรูปแบบการเรียนรู้ที่แตกต่างกัน คุณสามารถเลือกเรียนโมดูลนี้ในรูปแบบวิดีโอ หรืออ่านเนื้อหาแบบข้อความและรูปภาพก็ได้ เนื้อหาแบบข้อความมีรายละเอียดมากกว่าวิดีโอ ดังนั้นในบางกรณีคุณอาจใช้เป็น supplemental material ควบคู่กับการรับชมวิดีโอ

---

## Next unit: Optimize model output with prompt engineering