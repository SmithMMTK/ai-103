
tool _file_search_ ช่วยให้โมเดลของคุณดึงข้อมูลที่เกี่ยวข้องจากเอกสารที่คุณอัปโหลดไว้ระหว่างการสร้าง response ได้

## What is the file_search tool?

file_search tool ช่วยให้โมเดลตอบคำถามโดยใช้ไฟล์แบบ private หรือไฟล์เฉพาะโดเมน เช่น policy documents, manuals, contracts และ internal knowledge bases แทนที่จะพึ่งพาเพียง general training data โมเดลสามารถค้นหาเนื้อหาไฟล์ที่ถูก index แล้ว และส่งกลับคำตอบแบบ grounded ได้

สิ่งนี้มีประโยชน์มากเมื่อคุณต้องการคำตอบที่แม่นยำจากเอกสารภายในที่เชื่อถือได้

ความสามารถหลักประกอบด้วย:

- **Document-grounded answers** - response อ้างอิงจากไฟล์ที่คุณอัปโหลด
- **Semantic retrieval** - ค้นหา passages ที่เกี่ยวข้องจากความหมาย ไม่ใช่แค่ exact keyword matches
- **Vector store integration** - ค้นหาได้ข้าม indexed document collections หนึ่งชุดหรือหลายชุด
- **Citations and transparency** - ใส่ผลลัพธ์ที่ match กันเพื่อใช้ debugging และ traceability
- **Better enterprise relevance** - ใช้ความรู้เฉพาะองค์กรใน model outputs

## Common use cases

|Use Case|Example|
|---|---|
|**Policy Q&A**|ตอบคำถามพนักงานจากไฟล์ HR policy PDF|
|**Support Assistants**|ดึงขั้นตอนเกี่ยวกับผลิตภัณฑ์จาก internal troubleshooting guides|
|**Legal Review**|ค้นหา clauses เฉพาะจากเอกสารสัญญาหลายฉบับ|
|**Knowledge Discovery**|สรุปคำตอบจากชุดเอกสารทางเทคนิค|

## A simple example

ตัวอย่างต่อไปนี้แสดงการใช้ OpenAI Responses API โดยเปิดใช้งาน file_search:

Python

```python
from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

# Create vector store and upload a file
vector_store = client.vector_stores.create(name="policy-docs")
client.vector_stores.files.upload_and_poll(
    vector_store_id=vector_store.id,
    file=open("expenses_policy.pdf", "rb")
)

# Get response using the file_search tool
response = client.responses.create(
    model=model_deployment,
    instructions="You are an AI assistant that provides information from HR policy documents.",
    input="What's the maximum amount I can claim for a taxi ride?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store.id]
    }],
    include=["file_search_call.results"]
)
print(response.output_text)
```

ใน flow นี้ โมเดลจะค้นหา policy file ที่ถูก index แล้ว และใช้ passages ที่ดึงมาเพื่อสร้างคำตอบแบบ grounded

## How the file_search tool works

กระบวนการทั่วไปในการใช้ file_search tool มีดังนี้:

1. **You prepare files** - อัปโหลดเอกสารไปยัง vector store
2. **You send a request** - ใส่ file_search ใน tools array พร้อม vector store IDs
3. **Model performs retrieval** - โมเดลค้นหา indexed chunks ที่เกี่ยวข้อง
4. **Results are injected** - passages ที่ match จะถูกส่งให้โมเดล
5. **Response is generated** - โมเดลตอบโดยใช้ retrieved document context

## Best practices

- **Use high-quality source files** - เอกสารที่สะอาดและเป็นปัจจุบันช่วยเพิ่ม retrieval accuracy
- **Write focused prompts** - ถามให้เฉพาะเจาะจงเพื่อลด ambiguous matches
- **Scope vector stores carefully** - แยกโดเมน (HR, legal, finance) เมื่อเหมาะสม
- **Include retrieval results in development** - ใช้ response includes เพื่อ troubleshooting
- **Review answers for critical workflows** - คงการตรวจสอบโดยมนุษย์ไว้ในกรณี high-stakes

## Limitations to know about

- คุณภาพคำตอบขึ้นอยู่กับคุณภาพเอกสาร ความครอบคลุม และความเกี่ยวข้องของ chunks
- stores ที่ใหญ่มากหรือผสมหลายโดเมนอาจให้ context ที่โฟกัสน้อยลง
- หากอัปเดต source files อาจต้อง re-indexing ก่อนที่เนื้อหาใหม่จะค้นหาได้
- retrieval ช่วยเพิ่ม grounding แต่ไม่สามารถแทนที่การตรวจสอบโดยมนุษย์สำหรับการตัดสินใจที่อ่อนไหว

หากใช้อย่างเหมาะสม file_search จะเปลี่ยน general-purpose model ให้เป็น domain-aware assistant ที่ตอบจากเอกสารที่ทีมของคุณใช้งานจริงได้

> [!NOTE]
>  
> file_search tool เป็นวิธีที่ดีในการ ground โมเดลกับชุดเอกสารหรือ data files เฉพาะทาง อย่างไรก็ตาม สำหรับ enterprise-scale agents ที่ต้องเข้าถึงข้อมูลปริมาณมากจากหลาย data stores คุณควรพิจารณาใช้โซลูชัน _Foundry IQ_ knowledge store ร่วมกับ Microsoft Foundry agent หากต้องการเรียนรู้เพิ่มเติม โปรดดู [Build knowledge-enhanced AI agents with Foundry IQ](https://learn.microsoft.com/en-us/training/modules/introduction-foundry-iq)

---

## Next unit: Use the function tool