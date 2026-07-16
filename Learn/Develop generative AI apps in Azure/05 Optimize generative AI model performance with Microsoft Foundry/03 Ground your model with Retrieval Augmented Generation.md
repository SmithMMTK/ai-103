
prompt engineering ช่วยกำกับวิธีที่โมเดลตอบได้ แต่ไม่สามารถมอบความรู้ที่โมเดลไม่มีอยู่เดิมได้ Language models ถูกฝึกจาก datasets ขนาดใหญ่ แต่ training data เหล่านั้นมี cutoff date และไม่ได้รวมข้อมูล private ขององค์กรคุณ เมื่อโมเดลขาด context ที่เกี่ยวข้อง ก็อาจสร้าง responses ที่ฟังดูสมเหตุสมผลแต่ข้อเท็จจริงไม่ถูกต้อง

เพื่อแก้โจทย์นี้ คุณสามารถ **ground** โมเดลได้โดยส่งข้อมูลที่เกี่ยวข้องและเป็นข้อเท็จจริงให้โมเดลใช้เป็นฐานในการตอบ โดย **Retrieval Augmented Generation (RAG)** คือเทคนิคที่นิยมมากที่สุดสำหรับ grounding language model

## Understand grounding

เมื่อคุณใช้ language model โดยไม่มี grounding ข้อมูลเดียวที่โมเดลมีคือ training data ของมัน ผลลัพธ์อาจถูกต้องตามไวยากรณ์และดูเป็นเหตุเป็นผล แต่ยังอาจไม่แม่นยำหรือมีรายละเอียดที่แต่งขึ้นได้ ตัวอย่างเช่น การถามว่า "Which hotels do you offer in Paris?" โดยไม่มี grounding data อาจทำให้ได้ชื่อโรงแรมที่ไม่มีจริง

![Diagram showing an ungrounded model returning an uncontextualized response based only on training data.](https://learn.microsoft.com/en-us/training/wwl-data-ai/optimize-generative-ai-model-performance/media/ungrounded.png)

เมื่อคุณ **ground** prompt คุณจะส่งข้อมูลที่เกี่ยวข้องจาก trusted source ไปพร้อมกับคำถามของผู้ใช้ จากนั้นโมเดลจะสร้าง response โดยอิงข้อมูลนั้น ทำให้ได้คำตอบที่แม่นยำและสอดคล้องกับบริบทมากขึ้น

ลองดูความแตกต่าง:

- **Ungrounded**: โมเดลพึ่งพาเพียง training data และอาจแต่งชื่อหรือรายละเอียดโรงแรมขึ้นมา
- **Grounded**: โมเดลได้รับข้อมูล hotel catalog จริงของคุณเป็น context และตอบด้วยชื่อโรงแรม ราคา และสถานะห้องว่างที่เป็นข้อมูลจริง

![Diagram comparing an ungrounded model returning generic responses versus a grounded model returning data-backed responses.](https://learn.microsoft.com/en-us/training/wwl-data-ai/optimize-generative-ai-model-performance/media/grounded.png)

grounding ช่วยเพิ่มความถูกต้องเชิงข้อเท็จจริงของ responses โดยเชื่อมโมเดลเข้ากับข้อมูลที่เฉพาะเจาะจง เป็นปัจจุบัน และเกี่ยวข้องกับความต้องการของผู้ใช้

## How RAG works

RAG คือ pattern ที่ดึงข้อมูลที่เกี่ยวข้องจาก data source แล้วใส่ลงใน prompt ก่อนที่โมเดลจะสร้าง response กระบวนการมี 3 ขั้นตอน:

![Diagram showing the three-step RAG pattern: retrieve grounding data, augment the prompt with that data, and generate a grounded response.](https://learn.microsoft.com/en-us/training/wwl-data-ai/optimize-generative-ai-model-performance/media/rag-pattern.png)

1. **Retrieve**: ค้นหา data source เพื่อหาข้อมูลที่เกี่ยวข้องกับคำถามของผู้ใช้
2. **Augment**: เพิ่มข้อมูลที่ดึงมาเข้าไปใน prompt ในรูปแบบ context
3. **Generate**: ส่ง augmented prompt ให้ language model เพื่อสร้าง grounded response

การดึง context จาก data source ที่กำหนดไว้ จะช่วยให้มั่นใจว่าโมเดลใช้ข้อมูลที่เกี่ยวข้องและเป็นปัจจุบัน แทนการพึ่งพา training data เพียงอย่างเดียว

## Create embeddings for search

องค์ประกอบสำคัญของ RAG คือความสามารถในการค้นหาข้อมูลที่เกี่ยวข้องที่สุดใน data source ของคุณอย่างมีประสิทธิภาพ ซึ่งตรงนี้เองที่ **embeddings** และ **vector search** เข้ามามีบทบาท

**embedding** คือการแทนข้อความในรูปแบบคณิตศาสตร์เป็น vector ซึ่งเป็นรายการตัวเลข floating-point ที่สะท้อนความหมายของคำ ประโยค หรือเอกสาร คุณสร้าง embeddings ได้โดยส่งเนื้อหาไปยัง embedding model เช่น Azure OpenAI embedding model ที่มีใน Microsoft Foundry

ตัวอย่างเช่น ลองพิจารณาเอกสารสองประโยคนี้:

- _"The children played joyfully in the park."_
- _"Kids happily ran around the playground."_

แม้ประโยคทั้งสองใช้คำต่างกัน แต่มีความหมายคล้ายกัน เมื่อสร้าง embeddings แล้ว vectors ของทั้งสองจะอยู่ใกล้กันใน multidimensional space ซึ่งสะท้อน semantic similarity

![Diagram showing text keywords plotted as vectors in multidimensional space, with the distance between vectors representing semantic similarity.](https://learn.microsoft.com/en-us/training/wwl-data-ai/optimize-generative-ai-model-performance/media/vector-embeddings.jpg)

**Cosine similarity** ใช้วัดความใกล้กันของสอง vectors โดยคำนวณมุมระหว่างกัน ค่าใกล้ 1 หมายถึง vectors มีความคล้ายสูง แนวทางเชิงคณิตศาสตร์นี้ช่วยให้คุณหาเอกสารที่เกี่ยวข้องได้แม้คำที่ใช้จะไม่ตรงกันแบบ exact match

## Use Azure AI Search for retrieval

**Azure AI Search** ทำหน้าที่เป็น retrieval component สำหรับ RAG solutions ใน Microsoft Foundry โดยช่วยให้คุณ bring your own data, สร้าง searchable index และ query เพื่อดึงข้อมูลที่เกี่ยวข้อง

![Diagram showing an Azure AI Search index being queried to retrieve grounding data for a user question.](https://learn.microsoft.com/en-us/training/wwl-data-ai/optimize-generative-ai-model-performance/media/index.png)

ในการใช้ Azure AI Search กับ RAG คุณจะทำดังนี้:

1. **Add your data** เข้า Microsoft Foundry จากแหล่งข้อมูลอย่าง Azure Blob Storage, Azure Data Lake Storage Gen2 หรือ Microsoft OneLake และสามารถอัปโหลดไฟล์โดยตรงได้เช่นกัน
2. **Create an index** โดยใช้ embedding model เพื่อสร้าง vector representations ของเนื้อหา และจัดเก็บ index ใน Azure AI Search
3. **Query the index** เมื่อผู้ใช้ถามคำถาม โดยระบบจะแปลงคำถามเป็น embedding ค้นหาเนื้อหาที่คล้ายที่สุด และส่งผลลัพธ์ที่เกี่ยวข้องกลับมา

Azure AI Search รองรับหลายเทคนิคการค้นหา:

- **Keyword search**: จับคู่ exact terms ใน query กับข้อความใน index
- **Semantic search**: ใช้ semantic models เพื่อจับคู่ตามความหมายของ query แทนการจับ exact keywords
- **Vector search**: ใช้ embeddings เพื่อค้นหาเนื้อหาที่คล้ายกันเชิงความหมาย
- **Hybrid search**: ผสาน keyword, semantic และ vector search เพื่อความแม่นยำสูงสุด โดยแนะนำให้ใช้กับ generative AI applications

## Implement RAG with the Azure AI Foundry SDK

หลังจากสร้าง Azure AI Search index แล้ว คุณสามารถเชื่อม index นั้นเข้ากับโมเดลผ่าน Microsoft Foundry project ได้ โดย SDK `azure-ai-projects` ช่วยให้คุณสร้าง authenticated OpenAI client และใช้ Responses API เพื่อสร้าง grounded answers

ตัวอย่าง Python ต่อไปนี้แสดง implementation ขั้นพื้นฐาน:

```python
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

client = project.get_openai_client()

response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "system", "content": "You are a helpful travel advisor. "
         "Use the following hotel data to answer: " + retrieved_context},
        {"role": "user", "content": "Which hotels do you offer in Paris?"},
    ],
)

print(response.output_text)
```

ในตัวอย่างนี้ `retrieved_context` คือเอกสารที่ถูกส่งกลับมาจาก Azure AI Search index ของคุณ เมื่อ inject ผลลัพธ์เหล่านี้เข้าไปใน system message คำตอบของโมเดลจะ grounded กับข้อมูลจริงของคุณ แทนการอิงเพียงความรู้ทั่วไปจาก training data

## When to use RAG

RAG จะมีประสิทธิภาพสูงสุดเมื่อ:

- **The model needs domain-specific knowledge**: องค์กรของคุณมี private data ที่โมเดลไม่เคยถูกฝึกด้วย เช่น product catalog, policy documents หรือ internal knowledge base
- **Information changes frequently**: ข้อมูลของคุณมีการอัปเดตสม่ำเสมอ เช่น inventory, pricing หรือข่าวสาร โดย RAG ดึงข้อมูลล่าสุดตอน query ได้โดยไม่ต้อง retraining
- **Factual accuracy is critical**: คุณต้องการ responses ที่ grounded กับข้อมูลจริง ไม่ใช่ความรู้ทั่วไปของโมเดล
- **The base model's training data has a cutoff**: เหตุการณ์หรือข้อมูลที่เกิดหลัง training cutoff date ของโมเดลจำเป็นต้องเข้าถึงได้

สำหรับ travel agency scenario, RAG ช่วยให้ลูกค้าถามคำถามเกี่ยวกับโรงแรมปลายทางเฉพาะ นโยบายการจอง และรายละเอียดต่างๆ ได้ โดย grounded กับ catalog data จริงของเอเจนซี่

> [!TIP]
> หากคุณกำลังสร้าง agents ที่ต้องใช้ grounded knowledge โดยไม่อยากจัดการ search infrastructure เอง ให้พิจารณา **Foundry IQ** ซึ่งเป็น managed knowledge store ที่ช่วยให้การทำ grounding สำหรับ AI agents ง่ายขึ้น ดูเพิ่มเติมได้ที่ [Build knowledge-enhanced AI agents with Foundry IQ](https://learn.microsoft.com/en-us/training/modules/introduction-foundry-iq/)

---

## Next unit: Fine-tune a model for consistent behavior