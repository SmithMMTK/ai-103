
แม้ว่าโมเดลและเอเจนต์ด้าน Generative AI มักเป็นจุดสนใจหลักของโครงการพัฒนาโซลูชัน AI สมัยใหม่ แต่ในหลายกรณี การใช้ความสามารถแบบ "พร้อมใช้งาน" สำหรับงาน AI ทั่วไปก็มีประโยชน์มาก

Microsoft Foundry มี _Foundry Tools_ ซึ่งเป็นชุด API และโมเดลสำเร็จรูปที่พร้อมใช้งานทันที (out-of-the-box) และสามารถนำไปผสานเข้ากับแอปพลิเคชันของคุณได้ การใช้เครื่องมือเหล่านี้ช่วยให้คุณสร้างโซลูชันที่คุ้มค่าและคาดการณ์ผลลัพธ์ได้มากกว่าการพึ่งพาเอเจนต์ที่อิง Generative AI เพียงอย่างเดียว

|เครื่องมือ|คำอธิบาย|
|---|---|
|![Azure Language icon.](https://learn.microsoft.com/en-us/training/wwl-data-ai/prepare-azure-ai-development/media/azure-language.png)  <br>**Azure Language**|Azure Language ใน Foundry Tools มีโมเดลและ API ที่ใช้วิเคราะห์ข้อความภาษาธรรมชาติ และทำงานต่างๆ เช่น การดึงเอนทิตี (entity extraction), การวิเคราะห์ความรู้สึก (sentiment analysis) และการสรุปความ (summarization) นอกจากนี้ยังมีความสามารถสำหรับช่วยสร้างโมเดลภาษาสนทนาและโซลูชันตอบคำถาม (question answering)|
|![Azure Speech icon.](https://learn.microsoft.com/en-us/training/wwl-data-ai/prepare-azure-ai-development/media/azure-speech.png)  <br>**Azure Speech**|Azure Speech ใน Foundry Tools มี API สำหรับแปลง _ข้อความเป็นเสียง_ (text to speech) และ _เสียงเป็นข้อความ_ (speech to text) รวมถึงรองรับเสียงพูดแบบเรียลไทม์สำหรับแอปสนทนาและเอเจนต์|
|![Azure Translator icon.](https://learn.microsoft.com/en-us/training/wwl-data-ai/prepare-azure-ai-development/media/azure-translator.png)  <br>**Azure Translator**|Azure Translator ใน Foundry Tools ใช้โมเดลภาษาที่ล้ำสมัยเพื่อแปลข้อความระหว่างภาษาจำนวนมาก|
|![Azure Document Intelligence icon.](https://learn.microsoft.com/en-us/training/wwl-data-ai/prepare-azure-ai-development/media/azure-document-intelligence.png)  <br>**Azure Document Intelligence**|ด้วย Azure Document Intelligence ใน Foundry Tools คุณสามารถใช้โมเดลสำเร็จรูปหรือโมเดลที่ปรับแต่งเองเพื่อดึงข้อมูลฟิลด์จากเอกสารที่ซับซ้อน เช่น ใบแจ้งหนี้ ใบเสร็จ และแบบฟอร์ม|
|![Azure Content Understanding icon.](https://learn.microsoft.com/en-us/training/wwl-data-ai/prepare-azure-ai-development/media/azure-content-understanding.png)  <br>**Azure Content Understanding**|Azure Content Understanding ใน Foundry Tools มีความสามารถในการวิเคราะห์เนื้อหาแบบหลายโมดัล (multi-modal) ที่ช่วยให้คุณสร้างโมเดลสำหรับดึงข้อมูลจากแบบฟอร์มและเอกสาร รวมถึงรูปภาพ วิดีโอ และสตรีมเสียง|

ในการใช้งาน Foundry Tools คุณจะสร้างแอปพลิเคชันไคลเอนต์เพื่อเชื่อมต่อกับ endpoint เฉพาะของเครื่องมือในทรัพยากร Microsoft Foundry ของคุณ โดยระบุคีย์ยืนยันตัวตนของโปรเจกต์ หรือใช้การยืนยันตัวตนแบบโทเค็น จากนั้นจึงเรียกใช้ API และ SDK ของเครื่องมือนั้นๆ เพื่อใช้งานความสามารถที่มีให้

เครื่องมือบางตัวมีส่วนติดต่อผู้ใช้ (UI) สำหรับการตั้งค่าและทดสอบในพอร์ทัล Foundry

หมายเหตุ

ก่อนหน้านี้ Azure tools เคยใช้ชื่อว่า _Azure AI Services_ และก่อนหน้านั้นคือ _Azure Cognitive Services_ ชื่อเหล่านี้ยังคงปรากฏอยู่ใน API และ SDK บางส่วน และคุณยังสามารถจัดเตรียม (provision) เครื่องมือบางอย่างเป็นทรัพยากร Azure แบบแยกเดี่ยวที่อยู่นอก Foundry resource ได้ อย่างไรก็ตาม สำหรับโครงการใหม่ ควรใช้เครื่องมือที่อยู่ใน Microsoft Foundry resource เป็นหลัก