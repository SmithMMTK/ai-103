ลองนึกภาพว่าคุณทำงานในองค์กรด้าน healthcare ที่ต้องการ automate การโต้ตอบกับผู้ป่วยโดยยังคงมาตรฐานความปลอดภัยระดับสูง คุณต้องการ AI agent ที่สามารถตอบคำถามผู้ป่วย จัดตารางนัดหมาย และเข้าถึงข้อมูลทางการแพทย์แบบ real-time ได้ การสร้างระบบลักษณะนี้แบบดั้งเดิมมักต้องจัดการ infrastructure จำนวนมาก ใช้ความพยายามด้าน coding สูง และต้องใส่ใจ data security อย่างรอบคอบ Microsoft Foundry Agent Service นำเสนอแนวทางที่ช่วยลดความซับซ้อนนี้ได้ โดยยังคงความปลอดภัยระดับ enterprise-grade

Microsoft Foundry Agent Service เป็น fully managed platform ที่ช่วยให้คุณ build, deploy และ scale AI agents ได้โดยไม่ต้องจัดการ compute และ storage resources ที่อยู่เบื้องหลัง ไม่ว่าคุณจะชอบทำงานผ่าน Foundry portal หรือพัฒนาโดยตรงใน Visual Studio Code คุณก็มีทางเลือกที่ยืดหยุ่นในการสร้าง intelligent agents เพื่อ automate workflows และยกระดับ user experiences

ในโมดูลนี้ คุณจะได้เรียนรู้วิธีพัฒนา AI agents ทั้งผ่าน Foundry portal และ Microsoft Foundry extension สำหรับ Visual Studio Code คุณจะได้เรียนรู้วิธี configure agents ด้วย custom instructions, ขยายความสามารถด้วย tools และ integrate agents เข้ากับแอปพลิเคชันของคุณ เมื่อเรียนจบ คุณจะสามารถเลือกแนวทางการพัฒนาที่เหมาะกับแต่ละ scenario และ deploy AI agents ที่พร้อมใช้งานระดับ production ได้

## Learning objectives

เมื่อจบโมดูลนี้ คุณจะสามารถ:

- อธิบายเป้าหมายและความสามารถของ AI agents
- อธิบาย key features ของ Microsoft Foundry Agent Service
- ตั้งค่าและ configure Microsoft Foundry extension ใน Visual Studio Code
- build และ configure AI agents ด้วยแนวทางการพัฒนาที่หลากหลาย
- ขยายความสามารถของ agent ด้วย tools และ functions
- ทดสอบ agents ผ่าน integrated playgrounds
- deploy และ integrate agents เข้ากับแอปพลิเคชัน

## Prerequisites

- มีความคุ้นเคยกับ Azure และ Azure portal
- มีความเข้าใจเรื่อง generative AI (แนะนำโมดูล: [Fundamentals of Generative AI](https://learn.microsoft.com/en-us/training/modules/fundamentals-generative-ai/))
- มีความคุ้นเคยเบื้องต้นกับ Visual Studio Code

> [!NOTE]
> เราเข้าใจว่าผู้เรียนแต่ละคนมีรูปแบบการเรียนรู้ที่แตกต่างกัน คุณสามารถเลือกเรียนโมดูลนี้ในรูปแบบวิดีโอ หรืออ่านเนื้อหาแบบข้อความและรูปภาพก็ได้ เนื้อหาแบบข้อความมีรายละเอียดมากกว่าวิดีโอ ดังนั้นในบางกรณีคุณอาจใช้เป็น supplemental material ควบคู่กับการรับชมวิดีโอ

---

## Next unit: Understand AI agents and Microsoft Foundry Agent Service