tool _code_interpreter_ มอบ Python runtime ให้กับโมเดลของคุณ เพื่อให้สามารถสร้างและรัน Python code ได้

## What is the code_interpreter tool?

code_interpreter tool ช่วยให้ generative AI model สามารถเขียนและรัน Python code แบบ dynamic ระหว่างการสนทนาได้ แทนที่จะเพียงอธิบาย code หรือ algorithm โมเดลสามารถทดสอบตรรกะของตัวเอง ประมวลผลข้อมูล และส่งผลลัพธ์จริงจากการรัน code กลับมาได้ สิ่งนี้ทำให้โมเดลเปลี่ยนจากผู้คิดไปเป็นผู้ลงมือทำ

ความสามารถหลักประกอบด้วย:

- **Dynamic Python Execution**: โมเดลเขียนและรัน Python code ใน sandboxed environment
- **File Handling**: อัปโหลด ประมวลผล และดาวน์โหลดไฟล์ (CSV, JSON, รูปภาพ และอื่นๆ)
- **Data Analysis**: ทำการคำนวณ วิเคราะห์เชิงสถิติ และแปลงข้อมูลได้ทันที
- **Real-time Feedback**: โมเดลเห็นผลลัพธ์จากการรัน code และสามารถ iterate หรือแก้ error ได้
- **Complex Problem Solving**: แก้โจทย์คณิตศาสตร์ การจำลองสถานการณ์ และปัญหาเชิงตรรกะผ่าน executable code

## Common use cases

|Use Case|Example|
|---|---|
|**Data Analysis**|Parse ไฟล์ CSV และสร้าง summary statistics|
|**Math & Physics**|แก้ differential equations หรือจำลองสถานการณ์ทางฟิสิกส์|
|**File Conversion**|แปลงระหว่าง data formats (JSON ↔ CSV และอื่นๆ)|
|**Prototyping**|ทดสอบ algorithm และแนวคิดก่อนนำไป implement อย่างเป็นทางการ|

## A simple example

ตัวอย่างต่อไปนี้คือวิธีใช้ code_interpreter กับ OpenAI Responses API:

Python

```python
from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

# Get response using the code_interpreter tool
response = client.responses.create(
    model={model_deployment},
    instructions="You are an AI assistant that provides information. Use the python tool to run code for math problems.",
    input="What is the square root of 16?",
    tools=[{"type": "code_interpreter",
            "container": {"type": "auto"}}]
)
print(response.output_text)
```

output จาก code นี้จะมีลักษณะใกล้เคียงดังนี้:

```
The square root of 16 is 4.
```

ที่สำคัญกว่านั้น เมื่อ inspect รายละเอียดของ **response** object ที่โมเดลส่งกลับมา จะเห็นว่าผลลัพธ์ถูกคำนวณและส่งกลับให้โมเดลด้วย Python code ที่ generate แบบ dynamic ในลักษณะดังนี้:

Python

```python
import math

# Calculate the square root of 16
square_root = math.sqrt(16)
square_root
```

## How the code_interpreter tool works

กระบวนการทั่วไปในการใช้ code_interpreter tool มีดังนี้:

1. **You send a request**: ใส่ code_interpreter เข้าไปใน tools array ของคุณ
2. **Model analyzes the task**: โมเดลพิจารณาว่าจำเป็นต้องรัน code หรือไม่
3. **Model generates code**: โมเดลเขียน Python code เพื่อทำงานให้สำเร็จ
4. **Code runs**: code จะถูกรันใน sandboxed environment ที่เข้าถึง common libraries ได้ (เช่น _pandas_, *numpy*, และ _math_)
5. **Results returned**: โมเดลรับ output และนำไปประกอบใน response ของตน

## Best practices

- **Be specific**: อธิบาย data format และ expected output ให้ชัดเจน หลายโมเดลใช้ชื่อ _python tool_ ภายในเพื่ออ้างถึง code_interpreter tool ดังนั้นควรใช้ภาษานี้ใน instructions
- **Provide context**: ใส่ domain knowledge ที่เกี่ยวข้องไว้ใน prompts
- **Validate results**: ตรวจสอบความถูกต้องของ AI-generated code ทุกครั้งก่อนใช้ใน production
- **Monitor costs**: การรัน code เพิ่มจำนวน tokens และงานที่ซับซ้อนอาจใช้ resource มากขึ้น
- **Leverage libraries**: packages ทั่วไปอย่าง pandas, numpy, และ matplotlib ถูกติดตั้งไว้ล่วงหน้า
- **Error handling**: โมเดลมองเห็น errors และจะพยายามแก้ไขให้อัตโนมัติ

## Limitations to know about

- Executions ทำงานใน **sandboxed environment** และไม่สามารถเข้าถึง external network ได้
- บาง libraries อาจไม่พร้อมใช้งาน; ให้แจ้งโมเดลหาก standard library ใดทำงานไม่สำเร็จ
- มี **Timeout limits** สำหรับงานที่ใช้เวลารันนาน
- code ทำงานภายใต้ **memory constraints** โดย dataset ขนาดใหญ่มากอาจต้องใช้ streaming หรือ chunking

---

## Next unit: Use the web_search tool
