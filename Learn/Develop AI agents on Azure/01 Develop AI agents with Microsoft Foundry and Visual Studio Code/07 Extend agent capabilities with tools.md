หนึ่งในความสามารถที่ทรงพลังที่สุดของ AI agents คือการใช้ tools เพื่อขยายขีดความสามารถให้มากกว่าการสร้างข้อความ tools ช่วยให้ agent ดำเนินการ เข้าถึงข้อมูล และเชื่อมต่อกับระบบภายนอกได้ Microsoft Foundry มีทั้ง built-in tools และรองรับ custom integrations ทำให้ agent พัฒนาจาก chat interface ธรรมดาไปเป็นระบบ automation ขั้นสูง

## Understanding agent tools

tools คือฟังก์ชันเชิงโปรแกรมที่ agent สามารถเรียกใช้เพื่อทำงานให้สำเร็จ เมื่อ agent ประเมินว่าต้องใช้ tool เพื่อตอบคำขอของผู้ใช้ มันจะเรียก tool ที่เหมาะสม ประมวลผลผลลัพธ์ และรวมผลเข้ากับ response โดยอัตโนมัติ ความสามารถนี้ทำให้ agent ใช้ข้อมูลแบบ real-time, execute code, ค้นฐานความรู้ และโต้ตอบกับ external services ได้

lifecycle ของการเรียก tools ทำงานอัตโนมัติเป็นลำดับดังนี้:

1. ผู้ใช้ส่งข้อความถึง agent
2. agent วิเคราะห์คำขอและตัดสินใจว่าต้องใช้ tools ใดบ้าง (ถ้าจำเป็น)
3. agent เรียก tools ที่เหมาะสมพร้อมพารามิเตอร์ที่เกี่ยวข้อง
4. tools ทำงานและส่งผลลัพธ์กลับ
5. agent นำผลลัพธ์มาสร้างคำตอบแบบ natural language
6. ส่ง response กลับไปยังผู้ใช้

การผสานแบบไร้รอยต่อนี้ช่วยให้คุณเพิ่มความสามารถขั้นสูงให้ agent ได้ โดยไม่ต้องเขียน orchestration code ที่ซับซ้อน

## Built-in tools overview

Microsoft Foundry มี **tool catalog** ที่จัด tools เป็น 3 หมวด: **Configured** (built-in tools ที่พร้อมใช้), **Catalog** (tools เพิ่มเติมที่เพิ่มได้จาก registry รวมถึง MCP servers) และ **Custom** (tools ของคุณเองผ่าน OpenAPI specifications หรือ custom implementations) คุณเข้าถึง tool catalog ได้จาก **Build > Tools** ใน portal หรือผ่าน VS Code extension

ต่อไปนี้คือ tools ที่ใช้งานบ่อย:

### Code Interpreter

Code Interpreter ช่วยให้ agent เขียนและ execute Python code ในสภาพแวดล้อมที่ปลอดภัยแบบ sandboxed เหมาะกับการคำนวณคณิตศาสตร์ วิเคราะห์ข้อมูล สร้างกราฟ ประมวลผลไฟล์ และแก้ปัญหาที่ซับซ้อน ตัวอย่างเช่น หากผู้ใช้ขอให้ agent คำนวณดอกเบี้ยทบต้นจากเงินลงทุน $10,000 ที่อัตรา 5% ต่อปีเป็นเวลา 10 ปี agent จะเขียนและ execute Python code เพื่อคำนวณผลลัพธ์ที่แม่นยำ

### File Search

File Search รองรับ retrieval-augmented generation (RAG) โดยให้ agent ค้นข้อมูลจากเอกสารที่คุณอัปโหลด เครื่องมือจะ index เอกสารใน **vector store** และดึงข้อมูลที่เกี่ยวข้องเมื่อจำเป็น เพื่อ ground คำตอบของ agent ด้วยฐานความรู้เฉพาะของคุณ

File Search รองรับ PDF, Word (.docx), plain text (.txt), Markdown (.md) และรูปแบบอื่นๆ เมื่อเพิ่ม File Search ให้ agent คุณจะสร้างหรือเลือก vector store อัปโหลดเอกสาร และระบบจะ index ให้สำหรับ semantic search โดยอัตโนมัติ

### Bing Web Search

Bing Web Search เชื่อม agent เข้ากับข้อมูลอินเทอร์เน็ตแบบ real-time ช่วยให้เข้าถึงข่าวสารปัจจุบัน เทรนด์ และข้อมูลที่อยู่นอกเหนือ training data พร้อมระบบสร้าง citation อัตโนมัติ เพื่ออ้างอิงแหล่งที่มาของข้อมูล

### Azure AI Search

Azure AI Search รองรับการดึงความรู้ขั้นสูงจาก search index ที่คุณมีอยู่ ต่างจาก File Search (ที่ทำงานกับเอกสารที่อัปโหลดตรงให้ agent) เพราะ Azure AI Search เชื่อมกับแหล่งข้อมูลระดับ enterprise-scale ทั้งแบบ structured และ unstructured

### OpenAPI tools

OpenAPI tools ช่วยให้ agent โต้ตอบกับ external APIs ที่นิยามด้วย OpenAPI 3.0 specifications เพื่อเชื่อมต่อ web services และระบบองค์กร โดยคุณเพียงให้ specification แล้ว Microsoft Foundry จะจัดการทั้ง parameter mapping และ response parsing

### Additional built-in tools

tool catalog ยังมี tools อีกจำนวนมากสำหรับสถานการณ์เฉพาะทาง:

| Tool | Description |
| --- | --- |
| **Browser Automation** | โต้ตอบกับเว็บเพจ กรอกฟอร์ม และดึงเนื้อหา |
| **Computer Use** | โต้ตอบกับ desktop applications |
| **Image Generation** | สร้างภาพจากคำบรรยายข้อความ |
| **SharePoint** | เข้าถึงเนื้อหาและ document libraries ใน SharePoint |
| **Microsoft Fabric** | เชื่อมต่อกับ Fabric data agents เพื่อ data analytics |
| **Deep Research** | ทำการค้นคว้าเชิงลึกจากหลายแหล่งข้อมูล |
| **Agent-to-Agent** | มอบหมายงานต่อให้ agent อื่น |
| **Custom Code Interpreter** | ปรับแต่งสภาพแวดล้อม code execution สำหรับงานเฉพาะทาง |

tool catalog มีการขยายอย่างต่อเนื่อง ตรวจสอบ Foundry portal เพื่อดู tools ล่าสุดที่รองรับ

## Adding tools in Visual Studio Code

Microsoft Foundry extension มี interface ที่ใช้งานง่ายสำหรับการเพิ่มและตั้งค่า tools โดยคุณเลือกได้ว่าจะเพิ่มผ่าน visual designer หรือแก้ YAML โดยตรง

### Using the visual designer

การเพิ่ม tools ผ่าน Agent Designer:

1. เปิด agent ของคุณใน Agent Designer
2. ไปที่ส่วน **Tools** ใน configuration panel
3. เลือก **Add Tool** หรือไอคอน **+**
4. เลือกดู tools ที่มีใน tool library
5. เลือก tool ที่ต้องการเพิ่ม
6. ตั้งค่าเฉพาะของ tool (ถ้ามี)
7. บันทึกการเปลี่ยนแปลง

![Screenshot of the tool catalog interface in the Microsoft Foundry VS Code extension.](https://learn.microsoft.com/en-us/training/wwl-data-ai/develop-ai-agents-azure-vs-code/media/vs-code-tools.png)

เมื่อเพิ่มบาง tools, extension จะแจ้งให้ตั้งค่า assets ที่เกี่ยวข้อง เช่น การเพิ่ม File Search จะให้คุณสร้างหรือเลือก vector store สำหรับ document indexing

### Adding tools through YAML

คุณสามารถเพิ่ม tools ได้ด้วยการแก้ไฟล์ YAML ของ agent โดยตรง วิธีนี้เหมาะเมื่อคุณรู้ว่าต้องใช้ tools อะไร หรืออยาก apply การตั้งค่าจาก template

ตัวอย่าง YAML ที่มีหลาย tools:

```yaml
version: 1.0.0
name: research-assistant
description: Helps with research tasks using code analysis and web search
model:
  id: 'gpt-4o-deployment'
instructions: |
  You're a research assistant helping users gather and analyze information.
  Use Code Interpreter for data analysis and Bing Search for current information.
tools:
  - type: code_interpreter
  - type: bing_grounding
    bing_grounding:
      connection_id: "your-connection-id"
  - type: file_search
    file_search:
      vector_store_ids:
        - "vectorstore-123"
```

array `tools` จะแสดงแต่ละ tool ที่เปิดใช้งานพร้อม configuration ของมัน โดยบาง tools ต้องมีพารามิเตอร์เพิ่ม เช่น connection ID หรือ vector store reference

## Model Context Protocol (MCP) servers

Model Context Protocol (MCP) เป็นมาตรฐานสำหรับเพิ่ม custom tools ให้ agent โดย MCP servers อยู่ในส่วน **Catalog** ของ tool catalog และให้ reusable tool interfaces ที่ทำงานได้สม่ำเสมอข้าม agent implementations ต่างๆ

### Types of MCP servers

Foundry tool catalog รองรับ MCP servers 3 ประเภท:

- **Remote MCP servers** - โฮสต์ภายนอกและเข้าถึงผ่านเครือข่าย เหมาะกับ production มากที่สุด
- **Local MCP servers** - รันบนเครื่อง local ระหว่าง development เหมาะกับการทดสอบ custom tools ก่อน deploy
- **Custom MCP servers** - MCP server ที่คุณพัฒนาเองตามความต้องการเฉพาะ

### Benefits of MCP servers

MCP servers มีข้อดีหลายด้าน:

**Standardized protocol** - รูปแบบการสื่อสารของ tools ที่สม่ำเสมอ ช่วยให้ integration คาดเดาได้และเชื่อถือได้

**Reusable components** - สร้าง tools ครั้งเดียวแล้วใช้ซ้ำได้ในหลาย agents และหลาย projects

**Community-driven tools** - เข้าถึง tools จากชุมชนผ่าน MCP registries เพื่อขยายความสามารถโดยไม่ต้องพัฒนาเองทั้งหมด

**Simplified integration** - interface ที่สม่ำเสมอช่วยลดความซับซ้อนและภาระการดูแลรักษา integration

### Using MCP servers in VS Code

Microsoft Foundry extension รองรับการผสาน MCP server:

1. เรียกดู MCP servers ที่มีผ่าน tool registry ของ extension
2. เพิ่ม MCP servers ลงใน agent configuration
3. ตั้งค่าเฉพาะของ server และ parameters
4. ทดสอบการทำงานของ MCP server ใน integrated playground
5. deploy agents ที่มี MCP server integrations ขึ้น production

MCP servers ช่วยขยายขีดความสามารถของ agent ด้วยฟังก์ชันเฉพาะทาง โดยยังคงประสบการณ์การพัฒนาแบบสม่ำเสมอ

## Tool configuration best practices

การจัดการ tools อย่างมีประสิทธิภาพช่วยให้ agent ทำงานได้เสถียร:

- **Start with built-in tools** ก่อนสร้าง custom solutions เพราะ built-in tools ผ่านการทดสอบ บำรุงรักษา และ optimize มาแล้วสำหรับแพลตฟอร์ม
- **Match tools to requirements** - ระบุให้ชัดว่า agent ต้องทำอะไร แล้วเลือก tools ตามนั้น ไม่ควรเพิ่ม tools โดยไม่มีเหตุผลชัดเจน เพราะแต่ละ tool เพิ่ม latency
- **Provide clear instructions** - บอก agent ให้ชัดว่าเมื่อไรและอย่างไรที่ควรใช้แต่ละ tool (เช่น "Use Code Interpreter for any mathematical calculations") และเมื่อไรที่ไม่ควรใช้
- **Keep knowledge bases current** - หากใช้ File Search ควรอัปเดตเอกสารสม่ำเสมอ เพราะข้อมูลล้าสมัยจะทำให้ตอบผิด
- **Test tool behavior** อย่างละเอียดผ่าน integrated playground โดยส่งข้อความที่ควรกระตุ้นการใช้ tool ตรวจสอบการเรียกใช้อย่างถูกต้อง และทดสอบกรณี error

agents สามารถใช้หลาย tools ร่วมกันเพื่อจัดการสถานการณ์ซับซ้อนได้ เช่น research agent อาจใช้ Bing Web Search เพื่อค้นข้อมูลล่าสุด ใช้ Code Interpreter เพื่อวิเคราะห์ข้อมูล และใช้ File Search เพื่ออ้างอิงเอกสารภายใน ทั้งหมดถูก orchestrate อัตโนมัติตามคำขอของผู้ใช้

การขยายความสามารถของ agent ด้วย tools ช่วยเปลี่ยน chat interface ธรรมดาให้กลายเป็นระบบ automation ที่ทรงพลัง ด้วยการผสาน built-in tools, custom integrations และ MCP servers คุณสามารถสร้าง agents ที่โต้ตอบกับข้อมูล ระบบ และบริการของคุณได้อย่างลื่นไหล พร้อมรักษาความปลอดภัยและความน่าเชื่อถือระดับ enterprise

เนื้อหาเชิงลึกเกี่ยวกับ tools และ MCP servers จะมีอธิบายเพิ่มเติมในโมดูลถัดไป

---

## Next unit: Test, deploy, and integrate agents