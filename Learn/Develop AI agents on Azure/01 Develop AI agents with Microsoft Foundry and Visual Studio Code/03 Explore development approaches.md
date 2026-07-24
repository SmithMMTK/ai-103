
Microsoft Foundry Agent Service ให้ความยืดหยุ่นในการพัฒนา agent ด้วยตัวเลือกที่ครอบคลุมตั้งแต่ visual interface ไปจนถึง workflow แบบ code-centric การเข้าใจแนวทางการพัฒนาที่แตกต่างกันจะช่วยให้คุณเลือกเครื่องมือที่เหมาะกับแต่ละสถานการณ์และรูปแบบการทำงานของทีม

## Foundry portal development

Foundry portal มี web-based interface สำหรับสร้างและจัดการ AI agents โดยไม่ต้องเขียนโค้ด แนวทางนี้เหมาะอย่างยิ่งเมื่อคุณต้องการ prototype ไอเดียอย่างรวดเร็ว ทำงานร่วมกับ stakeholder ที่ไม่ใช่สายเทคนิค หรือจัดการ agent ผ่านศูนย์กลางเดียว

### When to use the Foundry portal

portal เหมาะกับสถานการณ์ต่อไปนี้:

- **Quick prototyping** - ทดสอบแนวคิดและ configuration ของ agent ได้รวดเร็ว โดยไม่ต้องตั้งค่า development environment
- **Visual configuration** - ตั้งค่า agent ผ่านฟอร์มและ dropdown ที่ใช้งานง่าย แทนการเขียนโค้ด
- **Centralized management** - ดูและจัดการ agent ทั้งหมดข้ามหลายโปรเจ็กต์ได้ในที่เดียว
- **Team collaboration** - แชร์ configuration ของ agent ให้ stakeholder ที่ชอบการทำงานผ่าน visual interface
- **Resource oversight** - ติดตามการใช้ token, latency และผลการประเมินผ่าน dashboard

Azure portal ช่วยให้เริ่มสร้าง agent ได้ทันทีโดยไม่ต้องติดตั้งเครื่องมือเพิ่ม เพียงเข้าไปยัง Foundry project ของคุณ เลือกส่วน Agents แล้วเริ่มสร้างได้เลย

## Visual Studio Code development

Microsoft Foundry extension สำหรับ Visual Studio Code นำความสามารถ AI ระดับ enterprise-grade เข้ามาใน development environment ของคุณโดยตรง แนวทางนี้เหมาะกับนักพัฒนาที่ชอบทำงานใน code editor ที่คุ้นเคย และต้องการ integration ที่แน่นกับ workflow การพัฒนา

### Key capabilities of the VS Code extension

extension จัดความสามารถออกเป็น 3 ส่วนหลัก:

**Resources** - เรียกดูและจัดการ asset ของ Foundry project ได้โดยตรงจาก VS Code ได้แก่:

- **Deployed models** - ดูและจัดการ model deployments
- **Declarative agents** - ดูและตั้งค่า prompt-based agents และ workflow agents
- **Hosted agents** - ดูและจัดการ containerized agents ที่ deploy ด้วยโค้ด
- **Connections** - จัดการการเชื่อมต่อกับ external services
- **Vector stores** - จัดระเบียบชุดเอกสารสำหรับ File Search

**Tools** - เข้าถึงความสามารถด้านการพัฒนาและการทดสอบ:

- **Model Catalog** - เรียกดูและ deploy models จาก catalog
- **Model Playground** - ทดลองใช้งาน models ได้โดยตรง
- **Agent Playgrounds** - ทดสอบ agents ผ่าน playground แบบ remote หรือ local
- **Local Visualizer** - debug และดูพฤติกรรมของ agent แบบ local
- **Deploy Hosted Agents** - deploy containerized agents ขึ้น production

**Help and Feedback** - เข้าถึง documentation และแหล่งข้อมูลการสนับสนุน

extension ยังมี **Agent Designer** แบบ visual สำหรับตั้งค่า property ของ agent, **code generation** ที่ผสานในตัวเพื่อเชื่อมต่อกับแอปพลิเคชัน และการแก้ไข **YAML configuration** โดยตรงเพื่อการควบคุมที่ละเอียดแม่นยำ

![Screenshot of the Microsoft Foundry VS Code extension interface showing the Resources, Tools, and Help and Feedback sections.](https://learn.microsoft.com/en-us/training/wwl-data-ai/develop-ai-agents-azure-vs-code/media/vs-code-agent.png)

### When to use Visual Studio Code

VS Code extension เหมาะสำหรับ:

- **Developer-centric workflows** - build agents ควบคู่กับ application code ใน environment เดียว
- **Version control integration** - ติดตาม configuration ของ agent ใน Git ไปพร้อมกับ codebase
- **Rapid iteration** - ปรับแก้ได้รวดเร็วและทดสอบได้ทันทีโดยไม่ต้องสลับเครื่องมือ
- **Code-first development** - แก้ไข YAML configurations โดยตรงเพื่อการควบคุมที่แม่นยำ
- **Local development** - ออกแบบ agent แบบ offline ก่อน deploy ไปยัง Azure

extension ติดตั้งได้โดยตรงจาก Visual Studio Code Marketplace และเชื่อมต่อกับ Foundry projects ที่มีอยู่แล้วของคุณ ขั้นตอนการติดตั้งและการตั้งค่าแบบละเอียดจะอยู่ใน unit ถัดไป

## Typical development workflow

ไม่ว่าคุณจะเลือกแนวทางไหน การพัฒนา agent จะเป็นไปตามรูปแบบที่คล้ายกัน:

1. **Connect** ไปยัง Microsoft Foundry project ของคุณ
2. **Create** AI agent ใน Foundry portal พร้อมชื่อและวัตถุประสงค์ที่ชัดเจน
3. **Configure** agent instructions เพื่อกำหนดพฤติกรรมและความสามารถ (ทำใน portal หรือ VS Code ก็ได้)
4. **Add tools** เพื่อขยายสิ่งที่ agent ทำได้
5. **Test** agent ผ่าน playground ที่มีมาในตัว
6. **Iterate** ปรับปรุงดีไซน์จากผลการทดสอบ
7. **Deploy** agent ไปยัง production
8. **Integrate** agent เข้ากับแอปพลิเคชันของคุณ

ทั้ง Foundry portal และ VS Code extension รองรับ workflow นี้เหมือนกัน โดยแตกต่างกันหลักๆ ที่รูปแบบ interface มากกว่าความสามารถ

## Required Azure resources

ทั้งสองแนวทางการพัฒนาใช้ Azure resources พื้นฐานเหมือนกัน ในการพัฒนา agents ด้วย Microsoft Foundry Agent Service คุณต้องมี:

- **Microsoft Foundry project** - จัดระเบียบ agents, models และ asset ที่เกี่ยวข้องไว้ในที่เดียว
- **Model deployments** - AI models ที่ deploy แล้ว (เช่น GPT-4.1 หรือ Claude Sonnet 4.6) เพื่อใช้ขับเคลื่อน agents ของคุณ

เมื่อคุณสร้าง Microsoft Foundry project ระบบจะ provision โครงสร้างพื้นฐานที่จำเป็นให้อัตโนมัติ และเมื่อคุณเพิ่มความสามารถให้ agent เช่น File Search หรือ custom tools บริการจะเชื่อมต่อ supporting services ที่ต้องใช้ให้แบบเบื้องหลังอย่างไร้รอยต่อ หากคุณต้องการขยายความสามารถของ agent เพิ่มเติม เช่น ใช้ Foundry IQ คุณอาจต้อง deploy Azure services เพิ่มบางส่วน

### Optional Azure services

ขึ้นอยู่กับความสามารถของ agent คุณ อาจมีการเชื่อมต่อ Azure services เพิ่มเติมดังนี้:

- **Azure AI Search** - สำหรับการดึงความรู้ขั้นสูงเมื่อใช้ Foundry IQ หรือ File Search tools
- **Azure Storage** - สำหรับจัดเก็บและจัดการไฟล์ที่ agents เข้าถึงได้
- **Azure Key Vault** - สำหรับจัดการ secrets และ credentials อย่างปลอดภัย
- **Azure Functions** - สำหรับ implement custom tools และ business logic

services เหล่านี้สามารถเชื่อมต่อกับ Foundry project ของคุณเมื่อจำเป็น แต่ไม่ใช่ข้อบังคับในการเริ่มต้นสร้าง agent

## Choosing your development approach

ทั้ง Foundry portal และ Visual Studio Code extension ให้ความสามารถด้านการพัฒนา agent ได้ครบถ้วน การเลือกใช้งานขึ้นอยู่กับความชอบด้าน workflow องค์ประกอบของทีม และความต้องการด้าน integration:

เลือก **Foundry portal** เมื่อคุณต้องการ visual configuration, centralized management หรือ quick prototyping โดยไม่ต้องตั้งค่า local development

เลือก **Visual Studio Code** เมื่อคุณชอบ developer-centric workflow ต้องการ integration ที่แน่นกับ application code หรือต้องการ configuration files ที่อยู่ภายใต้ version control

หลายทีมใช้ทั้งสองแนวทางร่วมกัน โดยใช้ portal สำหรับการสำรวจช่วงแรกและการรีวิวกับ stakeholder และใช้ VS Code สำหรับการพัฒนาเชิงลึกและการ deploy ขึ้น production ความยืดหยุ่นในการสลับแนวทางตามความต้องการเฉพาะหน้าเป็นจุดแข็งสำคัญของ Microsoft Foundry Agent Service

---

## Next unit: Build your first agent in Microsoft Foundry