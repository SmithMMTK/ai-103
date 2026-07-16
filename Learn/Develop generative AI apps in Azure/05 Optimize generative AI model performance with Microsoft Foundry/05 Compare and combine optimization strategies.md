
เมื่อคุณได้สำรวจ prompt engineering, RAG และ fine-tuning แยกกันไปแล้ว ลองมาดูว่าทั้งหมดนี้เชื่อมโยงกันอย่างไร กลยุทธ์เหล่านี้ไม่ได้ขัดแย้งกันเอง แต่เป็นแนวทางเสริมกันที่สามารถนำมาผสมผสานเพื่อให้บรรลุ optimization goals ที่ต่างกันได้

## Understand the optimization spectrum

กลยุทธ์ optimization ทั้งสามแบบแก้ปัญหาคนละมิติของ model performance:

![Diagram showing the various strategies to optimize the model's performance, from prompt engineering to RAG and fine-tuning.](https://learn.microsoft.com/en-us/training/wwl-data-ai/optimize-generative-ai-model-performance/media/model-optimization.png)

- **Optimize for context**: เมื่อโมเดลขาด domain-specific knowledge และคุณต้องการเพิ่มความแม่นยำของ responses ให้สูงสุด RAG จะแก้จุดนี้ด้วยการดึงข้อมูลที่เกี่ยวข้องจาก external sources
- **Optimize the model**: เมื่อคุณต้องการปรับปรุง format, style หรือ tone ของ response โดยเพิ่มความสม่ำเสมอของ behavior ให้สูงสุด fine-tuning จะแก้จุดนี้ด้วยการฝึกโมเดลจากตัวอย่างที่แสดง output ตามที่ต้องการ

prompt engineering คือฐานที่รองรับทั้งสองทิศทาง คุณใช้ prompt engineering เพื่อบอกโมเดลว่าควรทำงานอย่างไรและโฟกัสอะไร จากนั้นค่อยเสริมด้วย RAG หรือ fine-tuning เมื่อ prompt engineering อย่างเดียวไม่เพียงพอ

## Compare strategies

แต่ละกลยุทธ์มี trade-offs ต่างกันในด้านเวลาในการนำไปใช้ ความซับซ้อน ต้นทุน และจุดที่ทำได้ดีที่สุด:

|Strategy|Time to implement|Complexity|Cost|Best for|
|---|---|---|---|---|
|**Prompt engineering**|Low|Low|Low (per-token only)|กำกับ tone, format และ behavior; iterate ได้รวดเร็ว; ให้ instructions และ examples|
|**RAG**|Medium|Medium|Medium (search infrastructure + storage + per-token)|Factual accuracy, domain-specific knowledge, ข้อมูลที่ dynamic หรือเปลี่ยนบ่อย|
|**Fine-tuning**|High|High|High (training compute + model hosting + per-token)|Behavioral consistency, บังคับ style ให้คงที่, ลด prompt length, model distillation|

### Prompt engineering trade-offs

prompt engineering เป็นกลยุทธ์ optimization ที่เร็วที่สุดและมีต้นทุนต่ำที่สุด คุณเริ่มได้ทันทีโดยไม่ต้องเปลี่ยน infrastructure อย่างไรก็ตาม prompts ที่ยาวขึ้นจะใช้ tokens ต่อ request มากขึ้น และโมเดลอาจยังทำตามคำสั่งที่ซับซ้อนได้ไม่สม่ำเสมอ นอกจากนี้ prompt engineering ยังไม่สามารถทำให้โมเดลเข้าถึงข้อมูลที่ไม่เคยถูกฝึกมาได้

### RAG trade-offs

RAG ช่วยให้โมเดลมีข้อมูลที่เกี่ยวข้องและเป็นปัจจุบัน ณ เวลาที่ query ซึ่งช่วยเพิ่ม factual accuracy ได้อย่างมีนัยสำคัญ แต่ก็ต้องมีการตั้งค่า search service, สร้างและดูแล index และประมวลผล embeddings คุณภาพของ RAG responses จึงขึ้นอยู่กับคุณภาพของ search index และคุณภาพการ chunk และ index ข้อมูลของคุณด้วย

### Fine-tuning trade-offs

fine-tuning ให้ model behavior ที่สม่ำเสมอที่สุด เพราะ patterns ที่ต้องการถูกฝังไว้ใน weights ของโมเดล อีกทั้งยังอาจลดต้นทุนต่อ request ได้จากการใช้ prompts ที่สั้นลง แต่ fine-tuning มีต้นทุนเริ่มต้นสูงที่สุด: คุณต้องเตรียม training data, จ่ายค่า training compute และโฮสต์ custom model นอกจากนี้ fine-tuned model อาจต้อง retrain เมื่อ base model มีการอัปเดตหรือเมื่อความต้องการของคุณเปลี่ยนไป

## Combine strategies for better results

generative AI applications ที่มีประสิทธิภาพสูงมักใช้หลายกลยุทธ์ร่วมกัน ต่อไปนี้คือ combinations ที่พบบ่อย:

### Prompt engineering + RAG

นี่คือ combination ที่พบบ่อยที่สุด คุณใช้ prompt engineering เพื่อกำหนด behavior ของโมเดล (ผ่าน system messages และ instructions) และใช้ RAG เพื่อเติม factual context ที่จำเป็นต่อคำตอบที่แม่นยำ ตัวอย่างเช่น:

- system message สั่งให้โมเดลทำหน้าที่เป็น travel advisor และจัดรูปแบบ responses ตามที่กำหนด
- RAG ดึงรายละเอียดจาก hotel catalog เพื่อให้โมเดลตอบด้วยชื่อโรงแรมและราคาจริง

combination นี้ครอบคลุมทั้ง _how the model should act_ และ _what the model needs to know_

### Prompt engineering + fine-tuning

ใช้ combination นี้เมื่อคุณต้องการให้โมเดลทำตาม style หรือ format เฉพาะอย่างสม่ำเสมอ โดย fine-tuned model จะดูแล baseline behavior และ system message จะเพิ่ม context เฉพาะรายบทสนทนา ตัวอย่างเช่น:

- fine-tuned model ถูกฝึกให้ตอบด้วย brand voice ของ travel agency เสมอ
- system message เพิ่มคำสั่งเฉพาะ session เช่น ให้ความสำคัญกับ seasonal promotion

### RAG + fine-tuning

ผสานสองกลยุทธ์นี้เมื่อคุณต้องการทั้ง factual grounding และ behavior ที่สม่ำเสมอ โดย fine-tuned model ช่วยคุม style ของ response ให้เสถียร และ RAG ช่วยให้ได้ข้อมูลล่าสุดที่เฉพาะโดเมน ตัวอย่างเช่น:

- fine-tuned model สร้าง responses ด้วย brand voice และ structured format ของเอเจนซี่
- RAG ดึงข้อมูลราคาและสถานะห้องว่างล่าสุดจาก catalog

### All three strategies together

สำหรับ applications ที่ต้องการความสามารถสูงสุด คุณสามารถใช้ prompt engineering, RAG และ fine-tuned model ร่วมกัน โดยแต่ละ layer รับผิดชอบคนละเรื่อง:

1. **Fine-tuning** ช่วยให้ style และ format สม่ำเสมอ
2. **RAG** ให้ domain knowledge ที่แม่นยำและเป็นปัจจุบัน
3. **Prompt engineering** เติมคำสั่งเฉพาะบทสนทนาและ guardrails

## Apply a decision framework

เมื่อต้องตัดสินใจว่าจะใช้กลยุทธ์ใด ให้เริ่มจากสิ่งที่ง่ายก่อน แล้วค่อยเพิ่มความซับซ้อนเมื่อจำเป็น:

1. **Start with prompt engineering**: ทดสอบ system messages, few-shot examples และ parameter tuning ก่อน แล้วประเมินว่าผลลัพธ์ตรง requirements หรือไม่
2. **Add RAG if accuracy matters**: ถ้าโมเดลต้องเข้าถึงข้อมูลเฉพาะ ข้อมูลปัจจุบัน หรือข้อมูล private เพื่อให้ตอบถูกต้อง ให้ implement RAG ร่วมกับ Azure AI Search
3. **Add fine-tuning if consistency matters**: ถ้าโมเดลยังรักษา style, tone หรือ format ที่ต้องการไม่ได้แม้มี prompts ที่ละเอียด ให้ fine-tune โมเดลด้วย representative examples
4. **Combine as needed**: วางชั้นกลยุทธ์ตาม requirements เฉพาะของแอปพลิเคชัน โดยไม่จำเป็นว่าทุกแอปต้องใช้ครบทั้งสามแบบ

แนวทางแบบ incremental นี้ช่วยให้คุณหลีกเลี่ยงต้นทุนและความซับซ้อนที่ไม่จำเป็น พร้อมทั้งทำให้บรรลุระดับ optimization ที่แอปพลิเคชันของคุณต้องการได้

---

## Next unit: Exercise - Optimize generative AI model performance