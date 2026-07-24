เมื่อคุณมี declarative agent แล้ว (สร้างจาก Foundry portal หรือผ่าน SDK) ขั้นตอนสำคัญถัดไปคือการตั้งค่าพฤติกรรม instructions และ properties ให้ตรงกับความต้องการของคุณ Microsoft Foundry VS Code extension มีตัวเลือกการตั้งค่าที่ครบทั้งผ่าน Agent Designer แบบ visual และการแก้ไขไฟล์ YAML โดยตรง จึงยืดหยุ่นต่อวิธีทำงานของแต่ละทีม

> [!NOTE]
> workflow การตั้งค่าใน unit นี้ใช้กับ **declarative prompt-based agents** เป็นหลัก ส่วน hosted agents จะตั้งค่าผ่านโค้ด และ workflow agents จะใช้ YAML schema คนละแบบสำหรับ multi-agent orchestration

## Configuring agent properties

Agent Designer มี interface ที่ใช้งานง่ายสำหรับตั้งค่า properties หลักของ agent ซึ่งเป็นค่าพื้นฐานที่กำหนดว่า agent ของคุณจะทำงานอย่างไรและให้ผลลัพธ์แบบไหน

### Essential configuration options

ใน Agent Designer คุณจะตั้งค่าหลักได้ดังนี้:

**Agent name** - ใส่ชื่อที่สื่อความหมายและสะท้อนวัตถุประสงค์ของ agent ชื่อนี้จะแสดงใน list, logs และตอนที่นักพัฒนาคนอื่นทำงานร่วมกับ agent ของคุณ

**Model selection** - เลือก model deployment จาก dropdown โดยตัวเลือกนี้จะกำหนดว่า AI model ใดเป็นตัวขับเคลื่อน response ของ agent และ dropdown จะแสดงเฉพาะ model ที่คุณ deploy แล้วใน project

**Description** - เพิ่มคำอธิบายสั้น ชัดเจน ว่า agent ตัวนี้ทำอะไร เพื่อให้สมาชิกทีมเข้าใจบทบาทได้โดยไม่ต้องอ่าน instructions หรือโค้ดทั้งหมด

**System instructions** - กำหนดพฤติกรรม บุคลิก และสไตล์การตอบของ agent นี่คือจุดที่คุณออกแบบว่า agent เข้าใจบทบาทตัวเองและโต้ตอบกับผู้ใช้อย่างไร

**Agent ID** - extension สร้างให้อัตโนมัติเมื่อคุณสร้าง agent เป็นตัวระบุแบบ unique ที่ใช้ตอนเรียก agent ผ่าน APIs

### Model configuration options

นอกเหนือจากการเลือก model คุณยัง fine-tune พฤติกรรมด้วยพารามิเตอร์เพิ่มเติมได้:

**Temperature** - ควบคุมความสร้างสรรค์และความสุ่มของ response ค่าแบบต่ำ (0.1-0.3) จะให้ผลลัพธ์ที่คงที่และโฟกัส ส่วนค่าสูง (0.7-1.0) จะให้คำตอบที่สร้างสรรค์และหลากหลายขึ้น สำหรับ business agents ที่ทำงานเชิงโครงสร้าง ค่า 0.3-0.7 มักใช้งานได้ดี

**Top P** - ควบคุมความหลากหลายโดยจำกัดชุดคำที่ model เลือกใช้ระหว่าง generation โดยทั่วไปค่าดีฟอลต์ 1.0 ใช้ได้ดีในหลายกรณี แต่สามารถลดค่าเพื่อให้ output คาดเดาได้มากขึ้น

ค่าตั้งเหล่านี้จะแสดงทั้งในหน้า Designer และในไฟล์ YAML โดยซิงก์กันระหว่างสองมุมมอง

## Understanding the agent YAML structure

ไฟล์ YAML เก็บ configuration ทั้งหมดของ declarative agent ในรูปแบบที่เป็นระบบและอ่านง่าย เมื่อเข้าใจโครงสร้างนี้ คุณจะปรับค่าที่ต้องการได้อย่างแม่นยำ และทำงานได้เร็วขึ้นในกรณีที่ visual interface ไม่ใช่ทางเลือกที่เหมาะที่สุด

### Complete YAML example

ตัวอย่างไฟล์ YAML ที่ตั้งค่าครบ:

```yaml
# yaml-language-server: $schema=https://aka.ms/ai-foundry-vsc/agent/1.0.0
version: 1.0.0
name: healthcare-assistant
description: Assists healthcare staff with patient appointment scheduling and information retrieval
id: 'agent-abc123xyz'
metadata:
  authors:
    - developer-name
  tags:
    - healthcare
    - customer-service
    - scheduling
model:
  id: 'gpt-4.1'
  options:
    temperature: 0.5
    top_p: 1
instructions: |
  You're a healthcare assistant helping staff schedule patient appointments and retrieve information.

  Your responsibilities:
  - Help staff find available appointment slots
  - Answer questions about patient scheduling policies
  - Provide information about different appointment types
  - Assist with rescheduling and cancellations

  Important guidelines:
  - Never access or share patient medical information
  - Always verify appointment details before confirming
  - Be professional but friendly in all interactions
  - If you're unsure about policies, advise staff to check with management
tools: []
```

โครงสร้าง YAML นี้แบ่งออกเป็นส่วนที่ชัดเจน ได้แก่ metadata, model configuration, instructions และ tools ทำให้ง่ายต่อการค้นหาและแก้ไขเฉพาะส่วน

### Benefits of YAML configuration

การแก้ไข YAML โดยตรงมีข้อดีหลายประการ:

- **Version control** - ติดตามการเปลี่ยนแปลงใน Git ควบคู่กับ application code
- **Bulk updates** - ปรับค่าได้หลายจุดในครั้งเดียวอย่างมั่นใจ
- **Templates** - สร้าง agent templates ที่นำกลับมาใช้ซ้ำเพื่อความสม่ำเสมอ
- **Code review** - รวม agent configurations เข้ากับกระบวนการ code review มาตรฐาน
- **Automation** - สร้าง script เพื่อ generate หรือแก้ agent configurations แบบ programmatically

extension จะ validate YAML syntax แบบ real-time พร้อมไฮไลต์ข้อผิดพลาดและแนะนำการแก้ระหว่างพิมพ์

## Best practices for agent configuration

เมื่อเริ่มสร้าง agents ที่ซับซ้อนขึ้น แนวปฏิบัติเหล่านี้ช่วยรักษาคุณภาพและความน่าเชื่อถือ:

**Version control your YAML files** - commit agent configurations ลง Git พร้อมโค้ดแอป เพื่อรองรับ rollback, code review และ change tracking

**Use descriptive names and tags** - ตั้งชื่อและ tags ให้ชัดเจน เพื่อให้ค้นหาและแยกแยะ agent ได้ง่ายเมื่อมีจำนวนมากขึ้น

**Document complex instructions** - ใส่ comment ใน YAML เพื่ออธิบายเหตุผลที่เลือก instruction pattern หรือ configuration แบบนั้น

**Test after every change** - ใช้ integrated playground เพื่อตรวจพฤติกรรมทุกครั้งหลังแก้ค่า เพราะการเปลี่ยนเล็กน้อยอาจส่งผลลัพธ์ที่ไม่คาดคิด

**Start simple, then iterate** - เริ่มจาก instructions พื้นฐาน แล้วค่อยเพิ่มความซับซ้อนตามผลทดสอบ เพราะ instructions ที่ซับซ้อนเกินไปตั้งแต่แรกจะ debug ยาก

**Keep instructions focused** - แต่ละ agent ควรมีวัตถุประสงค์เฉพาะที่ชัดเจน agent ที่พยายามทำหลายอย่างเกินไปมักให้ผลลัพธ์ไม่สม่ำเสมอ

การตั้งค่า agents ใน Visual Studio Code มอบความสามารถที่ทรงพลังสำหรับสร้าง automation ที่ซับซ้อน การผสานระหว่าง visual design tools และการแก้ไข YAML โดยตรง ช่วยให้พัฒนาได้เร็ว พร้อมคงความแม่นยำที่ต้องใช้ในการ deploy ระดับ production

---

## Next unit: Extend agent capabilities with tools