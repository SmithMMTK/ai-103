
หลังจากเลือกโมเดลจากแคตตาล็อกแล้ว คุณต้องปรับใช้โมเดลเพื่อให้เข้าถึงได้ผ่าน endpoint ที่แอปพลิเคชันของคุณเรียกใช้งานได้ Microsoft Foundry portal จะช่วยนำทางคุณตลอดกระบวนการ deploy และมีเครื่องมือให้ทดสอบโมเดลที่ deploy แล้วได้ทันที

![Screenshot of the Deploy model interface in Foundry portal.](https://learn.microsoft.com/en-us/training/wwl-data-ai/model-catalog-evaluate/media/deploy-model.png)

## Understand deployment types

Microsoft Foundry รองรับ deployment หลายรูปแบบ โดยแต่ละแบบมีคุณลักษณะต่างกันด้าน data residency, การสเกล และการคิดค่าบริการ:

- **Global Standard** model deployments ใช้ได้กับทุก Azure region และคิดค่าบริการแบบจ่ายตามโทเค็น (pay-per-token) เหมาะกับงานทั่วไปและให้โควต้าสูงที่สุด
- **Global Provisioned** deployments ใช้ได้กับทุก Azure region และใช้งานบนพื้นฐานการจอง _provision throughput units_ (PTU) เพื่อให้ได้ throughput สูงที่คาดการณ์ได้
- **Global Batch** deployments ใช้ได้กับทุก Azure region โดยได้ส่วนลด 50% สำหรับงาน asynchronous ขนาดใหญ่ภายใน 24 ชั่วโมง
- **Data Zone Standard** deployments ช่วยให้ข้อมูลอยู่ภายใน data zone ที่กำหนด และคิดค่าบริการแบบ pay-per-token เหมาะกับกรณีที่ต้องปฏิบัติตามข้อกำหนด data zone ของ EU/US
- **Data Zone Provisioned** deployments ให้ throughput ที่คาดการณ์ได้ โดยอิงจาก PTU ที่จองไว้ภายใน data zone
- **Data Zone Batch** deployments ออกแบบมาสำหรับงาน batch แบบ asynchronous ขนาดใหญ่ภายใน data zone
- **Standard** deployments ถูกปรับใช้ใน region เดียว และคิดค่าบริการแบบ pay-per-token เหมาะเมื่อคุณต้องการ compliance ด้าน data residency ระดับ region หรือเป็นงานปริมาณไม่มาก
- **Regional Provisioned** deployments ให้ PTU ที่จองไว้ภายใน region เดียว
- **Developer** Developer deployments ใช้ได้กับทุก Azure region แบบ pay-per-token และใช้สำหรับประเมินโมเดลที่ fine-tuned เท่านั้น

แต่ละโมเดลในแคตตาล็อกจะระบุว่า support deployment แบบใดบ้าง พอร์ทัลจะเลือกตัวเลือก deployment ที่เหมาะสมที่สุดให้อัตโนมัติตามสภาพแวดล้อมและความต้องการของโมเดล โดยทั่วไปควรใช้ Global Standard deployments ใน Foundry resources เมื่อทำได้ เพื่อให้ได้ความสามารถสูงสุด

## Deploy a model

การ deploy โมเดลจาก Microsoft Foundry portal ทำได้ดังนี้:

เริ่มจากไปยังโมเดลที่คุณเลือกไว้ใน **Model catalog** จากหน้าแรกของ Foundry portal ให้เลือก **Discover** ในเมนูนำทาง แล้วเลือก **Models** ที่แถบซ้าย จากนั้นเปิด model card เพื่อตรวจสอบสเปกและ deployment types ที่รองรับ

เลือก **Deploy** เพื่อเริ่มกระบวนการ deploy โดยคุณสามารถเลือกได้ว่า:

- **Default settings** เพื่อ deploy อย่างรวดเร็วด้วยค่าที่แนะนำ
- **Custom settings** เพื่อปรับแต่งตัวเลือก deployment เอง

หากโมเดลต้องใช้การสมัคร Azure Marketplace (พบบ่อยในโมเดลจากพาร์ตเนอร์และชุมชน) ระบบจะแสดงเงื่อนไขการใช้งาน ให้ตรวจสอบเงื่อนไขแล้วเลือก **Agree and Proceed** เพื่อยอมรับ โมเดลที่ Azure จำหน่ายโดยตรง เช่น Azure OpenAI รุ่น GPT-4o-mini ไม่ต้องสมัคร marketplace เพิ่ม

ตั้งค่า deployment ของคุณ:

- **Deployment name**: ค่าเริ่มต้นระบบจะใช้ชื่อโมเดล คุณสามารถแก้ไขเพื่อให้ตั้งชื่อที่สื่อความหมายได้ดี โดยเฉพาะเมื่อ deploy โมเดลเดียวกันหลายชุด ตอน inference โค้ดของคุณจะใช้ deployment ชื่อนี้ในพารามิเตอร์ `model` เพื่อ route คำขอ
- **Deployment type**: พอร์ทัลจะเลือก deployment type ที่เหมาะสมให้อัตโนมัติตามโมเดลและสภาพแวดล้อมของคุณ โดยแต่ละโมเดลรองรับ deployment type ต่างกัน และให้การรับประกันด้าน data residency หรือ throughput ต่างกัน

สำหรับ managed compute deployments คุณต้องกำหนดเพิ่ม:

- **Virtual machine SKU**: เลือกจากประเภท VM ที่รองรับ โดย subscription ของคุณต้องมี Azure Machine Learning compute quota สำหรับ SKU ที่เลือก
- **Instance count**: ระบุจำนวน instance ที่จะ deploy เพื่อกระจายโหลดและเพิ่มความทนทาน

หลังตั้งค่าทั้งหมดแล้ว ให้เลือก **Deploy** เมื่อ deploy เสร็จ คุณจะถูกพาไปที่ Foundry Playground เพื่อทดสอบโมเดลแบบโต้ตอบได้ทันที และควรตรวจสอบว่า status ในรายการ deployment แสดงเป็น **Succeeded**

## Manage deployed models

หลัง deploy แล้ว คุณสามารถจัดการโมเดลได้จากส่วน **Build** ใน Microsoft Foundry portal โดยเลือก **Build** จากเมนูนำทาง แล้วเลือก **Models** ที่แถบซ้าย เพื่อดูรายการ deployment ใน resource ของคุณ

จากรายการ deployment ให้เลือกโมเดลที่ต้องการเพื่อดูรายละเอียด:

- การตั้งค่า deployment และสถานะ
- Endpoint URL สำหรับเรียกใช้ API
- คีย์หรือโทเค็นสำหรับยืนยันตัวตน
- เมตริกการมอนิเตอร์และการใช้งาน
- ตัวเลือกสำหรับปรับค่า deployment หรือลบ deployment

หน้ารายละเอียด deployment มีข้อมูลที่แอปพลิเคชันของคุณต้องใช้ในการเชื่อมต่อและเรียกใช้งานโมเดล

## Test in the playground

Microsoft Foundry portal มี playground แบบโต้ตอบที่ให้คุณทดสอบโมเดลที่ deploy แล้วได้ทันที โดยไม่ต้องเขียนโค้ด หลัง deploy เสร็จ ระบบจะพาคุณไปยัง playground อัตโนมัติ หรือคุณจะเลือก deployment จากรายการโมเดลเพื่อเปิด playground ก็ได้

Playground จะเลือก deployment ของคุณไว้ล่วงหน้า ทำให้เริ่มทดสอบได้ทันที ในหน้าต่างแชต:

ให้พิมพ์ prompt ลงในกล่องข้อความและสังเกตผลลัพธ์ตอบกลับ Playground จะแสดงทั้ง input ของคุณและ output ที่โมเดลสร้างขึ้น เพื่อช่วยให้เข้าใจพฤติกรรมและคุณภาพของโมเดล

ลองใช้ prompt หลายรูปแบบเพื่อทดสอบความสามารถที่แตกต่างกัน:

- คำถามง่ายๆ เพื่อตรวจสอบความเข้าใจพื้นฐาน
- โจทย์ให้เหตุผลหลายขั้นที่ซับซ้อน
- คำขอที่กำหนดรูปแบบหรือสไตล์เฉพาะ
- เคสขอบ (edge cases) ที่อาจเผยให้เห็นข้อจำกัด

ปรับ system messages เพื่อกำกับพฤติกรรมของโมเดล โดย system messages จะกำหนดบริบท น้ำเสียง และคำสั่งที่มีผลกับทุก input ของผู้ใช้ ตัวอย่างเช่น คุณอาจสั่งให้โมเดล "ตอบในบทบาทเจ้าหน้าที่บริการลูกค้า" หรือ "อธิบายเชิงเทคนิคแบบกระชับ"

ปรับพารามิเตอร์ เช่น temperature (ความสร้างสรรค์เทียบกับความคงเส้นคงวา), max tokens (ความยาวสูงสุดของคำตอบ) และ top-p (nucleus sampling) เพื่อปรับพฤติกรรมการสร้างผลลัพธ์ให้เหมาะสม

เลือกแท็บ **Code** เพื่อดูตัวอย่างการเรียกใช้โมเดลที่ deploy แล้วด้วยโค้ด ตัวอย่างจะแสดงการยืนยันตัวตน การตั้งค่า endpoint และรูปแบบคำขอในภาษาอย่าง Python, C# และ JavaScript ซึ่งคุณสามารถคัดลอกไปใช้ในแอปได้โดยตรง

Playground ทำหน้าที่เป็นสภาพแวดล้อมพัฒนาสำหรับ prompt engineering และการทดสอบก่อนนำโมเดลไปผสานในแอปพลิเคชันจริง

## Access models programmatically

เมื่อพร้อมจะนำโมเดลไปเชื่อมเข้ากับแอปของคุณ คุณต้องใช้ข้อมูลสำคัญ 3 ส่วนจากรายละเอียด deployment:

**Endpoint URL**: API endpoint ที่แอปของคุณใช้ส่งคำขอ Microsoft Foundry รองรับทั้ง project endpoints สำหรับความสามารถเฉพาะของ Foundry และ OpenAI v1 endpoints เพื่อรองรับความเข้ากันได้กับ OpenAI model APIs ในวงกว้าง

**Authentication key**: คีย์ลับหรือโทเค็นที่แอปของคุณใช้ยืนยันตัวตนเมื่อส่งคำขอ อีกทางเลือกคือใช้การยืนยันตัวตนด้วย Microsoft Entra ID และให้แอปส่งโทเค็นตามตัวตนของแอปเอง โดย Entra ID เหมาะและแนะนำสำหรับงาน production

**Deployment name**: ชื่อที่คุณกำหนดตอน deploy ซึ่งใช้ในพารามิเตอร์ `model` ของ API request เพื่อ route ไปยัง deployment ที่ต้องการ

แอปพลิเคชันของคุณจะใช้ข้อมูลเหล่านี้ในการสร้าง API requests โดย Microsoft Foundry portal มีทั้ง SDK และเอกสาร REST API สำหรับหลายภาษา พร้อมตัวอย่างโค้ดที่แสดงรูปแบบคำขอ การยืนยันตัวตน และการจัดการผลตอบกลับ

เมื่อโมเดลถูก deploy และทดสอบเรียบร้อยแล้ว คุณก็พร้อมที่จะผสานโมเดลเข้ากับแอปพลิเคชัน หรือไปต่อสู่การประเมินที่ครอบคลุมยิ่งขึ้นด้วยเมตริกอัตโนมัติและชุดข้อมูลทดสอบ