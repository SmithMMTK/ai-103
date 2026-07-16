
tool _web_search_ ช่วยให้โมเดลของคุณดึงข้อมูลใหม่จากเว็บระหว่างการสร้าง response ได้

## What is the web_search tool?

web_search tool ช่วยให้ generative AI model เข้าถึงข้อมูลภายนอกที่เป็นปัจจุบันได้ในช่วง runtime แทนที่จะพึ่งพาแค่ training data โมเดลสามารถส่ง search query ตรวจสอบแหล่งข้อมูลที่เกี่ยวข้อง และสร้างคำตอบที่ grounded กับเนื้อหาล่าสุดได้

ความสามารถนี้มีประโยชน์อย่างยิ่งเมื่อข้อเท็จจริงเปลี่ยนแปลงบ่อย เช่น ราคา การเปิดตัวผลิตภัณฑ์ การอัปเดตนโยบาย หรือเหตุการณ์ปัจจุบัน

ความสามารถหลักประกอบด้วย:

- **Live information retrieval** - ดึงข้อมูลล่าสุดที่ไม่มีอยู่ใน static model training data
- **Source-grounded responses** - สร้างคำตอบจาก web content ที่ดึงมา
- **Reduced hallucination risk** - เพิ่มความน่าเชื่อถือด้วยการตรวจสอบแหล่งข้อมูลภายนอก
- **Automatic query generation** - โมเดลตัดสินใจได้เองว่าเมื่อใดและควรค้นหาอย่างไรตาม user intent
- **Seamless user experience** - การค้นหาและการสร้าง response เกิดขึ้นใน flow เดียว

## Common use cases

|Use Case|Example|
|---|---|
|**Current Events**|สรุปประเด็นอัปเดตสำคัญของประกาศเทคโนโลยีใหม่ที่กำลังเป็นข่าว|
|**Market Research**|เปรียบเทียบ features หรือราคาล่าสุดของผลิตภัณฑ์จากหลาย vendors|
|**Policy Monitoring**|ตรวจสอบว่า regulations หรือ guidance มีการเปลี่ยนแปลงหรือไม่|
|**Fact Verification**|ยืนยัน claims กับ public sources ที่น่าเชื่อถือ|

## A simple example

ตัวอย่างขั้นต่ำต่อไปนี้แสดงการใช้ OpenAI Responses API โดยเปิดใช้งาน web search:

Python

```python
from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

# Get response using the web_search tool
response = client.responses.create(
    model={model_deployment},
    instructions="You are an AI assistant. Use web search when current information is required.",
    input="What are three major announcements from Microsoft Build this week?",
    tools=[{"type": "web_search"}]
)

print(response.output_text)
```

output จะแตกต่างกันไปตามผลลัพธ์บนเว็บ ณ เวลานั้น แต่ควรเป็นคำตอบแบบกระชับที่ grounded กับแหล่งข้อมูลล่าสุด

## How the web_search tool works

กระบวนการทั่วไปในการใช้ web_search tool มีดังนี้:

1. **You send a request** - ใส่ web search tool ลงใน tools array
2. **Model evaluates the question** - โมเดลพิจารณาว่าจำเป็นต้องใช้ข้อมูลใหม่จากเว็บหรือไม่
3. **Search is performed** - โมเดลส่ง search query หนึ่งรายการหรือมากกว่า
4. **Results are reviewed** - เลือกและสรุปหน้าเว็บที่เกี่ยวข้อง
5. **Response is generated** - โมเดลนำผลการค้นหามาประกอบเป็นคำตอบสุดท้าย

## Best practices

- **Ask time-aware questions clearly** - ใส่คำอย่าง "latest", "current" หรือช่วงวันที่เมื่อจำเป็น
- **Set expectations for sources** - ระบุให้ชัดว่าอยากได้ reputable sources หรือ official sources เมื่อความแม่นยำสำคัญ
- **Request concise outputs** - ขอคำตอบแบบสรุปสั้นพร้อม key points เพื่อลด noise
- **Verify critical facts** - สำหรับกรณี high-stakes ควรตรวจสอบ claims สำคัญซ้ำอย่างอิสระ
- **Track usage and latency** - การดึงข้อมูลจากเว็บอาจเพิ่มทั้ง response time และ token usage

## Limitations to know about

- ผลลัพธ์ขึ้นอยู่กับข้อมูลที่เปิดเผยสาธารณะและถูก index ได้ในช่วงเวลาที่ query
- คุณภาพของ sources อาจแตกต่างกัน ดังนั้น output ยังอาจต้องให้มนุษย์ตรวจทาน
- เนื้อหาที่ดึงมาอาจเปลี่ยนไปตามเวลา ทำให้การรันซ้ำอาจได้คำตอบต่างกัน
- บางสภาพแวดล้อมอาจมีข้อจำกัดด้านภูมิภาค นโยบาย หรือเครือข่ายต่อการเข้าถึงเว็บ

หากใช้อย่างเหมาะสม web_search จะช่วยให้โมเดลของคุณก้าวจาก static knowledge ไปสู่คำตอบที่ทันเหตุการณ์และรับรู้แหล่งที่มา ซึ่งมีประโยชน์มากขึ้นใน workflow การทำงานจริง

---

## Next unit: Use the file_search tool