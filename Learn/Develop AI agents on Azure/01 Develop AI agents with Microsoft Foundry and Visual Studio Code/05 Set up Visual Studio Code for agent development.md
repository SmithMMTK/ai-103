การตั้งค่า Visual Studio Code สำหรับการพัฒนา AI agent ช่วยนำความสามารถระดับ enterprise-grade เข้ามาอยู่ใน development environment ที่คุณคุ้นเคยโดยตรง Microsoft Foundry extension เปลี่ยน VS Code ให้เป็นแพลตฟอร์มแบบครบวงจรสำหรับการ build, test และ deploy agents โดยไม่ต้องออกจาก editor

## Understanding the Microsoft Foundry extension

Microsoft Foundry สำหรับ Visual Studio Code extension ให้คุณเข้าถึงความสามารถของ Microsoft Foundry Agent Service ได้โดยตรง extension นี้สร้างประสบการณ์แบบบูรณาการสำหรับการพัฒนา agent โดยผสานทั้ง visual design tools และการตั้งค่าแบบ code-based

extension จัดความสามารถออกเป็น 3 ส่วน ได้แก่ **Resources** (สำหรับจัดการ deployed models, declarative agents, hosted agents, connections และ vector stores), **Tools** (สำหรับเข้าถึง model catalog, playgrounds และฟีเจอร์ deployment) และ **Help and Feedback**

![Screenshot of the Microsoft Foundry VS Code extension interface showing the Resources, Tools, and Help and Feedback sections.](https://learn.microsoft.com/en-us/training/wwl-data-ai/develop-ai-agents-azure-vs-code/media/vs-code-agent.png)

## Installing and configuring the extension

การตั้งค่า Microsoft Foundry extension ใช้เวลาเพียงไม่กี่นาทีและต้องการ configuration เพียงเล็กน้อย

### Installation steps

1. เปิด Visual Studio Code บนเครื่องของคุณ
2. เลือก **Extensions** จากแถบด้านซ้าย หรือกด Ctrl+Shift+X (Windows/Linux) หรือ Cmd+Shift+X (Mac)
3. ค้นหา **Foundry** ในช่องค้นหา marketplace
4. เลือก extension **Microsoft Foundry** จากผลลัพธ์
5. เลือก **Install** เพื่อเพิ่ม extension ลงใน VS Code
6. รอให้การติดตั้งเสร็จสิ้น (สถานะจะแสดงใน Extensions panel)

หลังติดตั้งแล้ว ไอคอน Microsoft Foundry จะปรากฏใน VS Code activity bar ทางด้านซ้ายของหน้าต่าง

### Connecting to Azure

ก่อนเริ่มทำงานกับ agents ให้เชื่อมต่อ extension เข้ากับ Azure account และ project ของคุณก่อน:

1. เลือกไอคอน **Azure** ใน VS Code activity bar
2. ใน pane **Azure Resources** ให้ sign in เข้า Azure account หากระบบแจ้ง
3. ขยาย **Azure subscription** ของคุณใน resource tree
4. ขยายส่วน **Foundry** เพื่อดู projects ของคุณ
5. คลิกขวาที่ **Microsoft Foundry project** ของคุณ
6. เลือก **Open in Foundry Extension**

จากนั้น extension จะแสดง project resources ของคุณใน Microsoft Foundry panel รวมถึง agents ที่มีอยู่, model deployments, connections และ vector stores

## Preparing for agent development

ก่อนทำงานกับ agents ใน VS Code ให้ตรวจสอบว่าคุณมี resources ที่จำเป็นถูก deploy แล้ว

### Deploying a model

Agents ต้องใช้ deployed AI models ในการทำงาน หากคุณยังไม่มี model deployment:

1. ใน extension **Microsoft Foundry** ไปที่ส่วน **Resources**
2. ขยายหัวข้อย่อย **Model deployments**
3. เลือกไอคอน **+** (plus) เพื่อสร้าง deployment ใหม่
4. เลือก model (เช่น GPT-4o หรือ GPT-4) จากตัวเลือกที่มี
5. ตั้งค่า deployment:
    - **Deployment name**: ใส่ชื่อที่สื่อความหมาย ซึ่งคุณจะใช้ตอนตั้งค่า agents
    - **Model version**: เลือก model version ที่ต้องการ
    - **Capacity settings**: ตั้งค่า throughput ตามความต้องการ
6. เลือก **Deploy** แล้วรอให้ deployment เสร็จสิ้น

deployed model จะพร้อมให้เลือกใน dropdown menus เมื่อคุณตั้งค่า agents

## Working with agents in VS Code

โดยทั่วไป agents จะถูกสร้างใน Foundry portal ก่อน (ตามที่อธิบายใน unit ก่อนหน้า) แล้วจึงนำมาจัดการและตั้งค่าใน VS Code ผ่าน extension เมื่อคุณสร้าง agent ใน portal แล้ว agent จะปรากฏอัตโนมัติในส่วน **Resources** ของ extension

การเปลี่ยนแปลง agents ใน VS Code สามารถบันทึกกลับไปที่ Foundry ได้โดยตรง จึงทำให้คุณทำงานกับ agent เดิมข้ามแพลตฟอร์มได้สะดวก

## Managing multiple agents

เมื่อ project เติบโตขึ้น คุณมักต้องจัดการ agents หลายตัวที่มีวัตถุประสงค์ต่างกัน Microsoft Foundry extension ทำเรื่องนี้ให้ตรงไปตรงมา:

- **Browse agents** ในมุมมอง Resources ที่จัดตาม project
- **Switch between agents** โดยเลือกจากรายการ
- **Compare configurations** โดยเปิดไฟล์ YAML หลายไฟล์เทียบกันแบบ side by side
- **Duplicate agents** เพื่อสร้าง variation โดยไม่ต้องเริ่มจากศูนย์
- **Archive unused agents** เพื่อให้ workspace เป็นระเบียบ

extension ช่วยให้มองเห็น agents ทั้งหมดได้ชัดเจน ทำให้นำทางระหว่าง automation projects ต่างๆ ได้ง่าย

การตั้งค่า Visual Studio Code สำหรับการพัฒนา agent ช่วยสร้างสภาพแวดล้อมแบบบูรณาการที่ทรงพลัง และเร่งทั้ง development lifecycle ด้วย Microsoft Foundry extension คุณจะได้ความสามารถการพัฒนา agent ระดับ enterprise-grade โดยยังทำงานใน code editor ที่คุ้นเคย พร้อมรองรับ rapid iteration และ deployment ของ intelligent automation ได้อย่างไร้รอยต่อ

---

## Next unit: Configure AI agents in Visual Studio Code