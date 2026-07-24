
การสร้าง AI agent ตัวแรกของคุณใน Foundry portal เป็นจุดเริ่มต้นที่เข้าถึงได้ง่ายสำหรับการพัฒนา agent โดย visual interface ของ portal จะนำทางคุณผ่านขั้นตอนการตั้งค่าโดยไม่ต้องเขียนโค้ด ทำให้เข้าใจแนวคิดของ agent ได้ง่ายพร้อมกับสร้างระบบอัตโนมัติที่ใช้งานได้จริง

## Creating an agent in the Foundry portal

Foundry portal ทำให้การสร้าง agent เป็นเรื่องง่ายขึ้นผ่าน interface ที่ใช้งานได้อย่างเป็นธรรมชาติ:

1. **Navigate to Microsoft Foundry** ที่ [https://ai.azure.com](https://ai.azure.com/) และ sign in ด้วย Azure credentials ของคุณ
2. **Select your project** จากรายการ project ที่มีอยู่ หรือสร้าง project ใหม่
3. **Select Build > Agents** จากเมนูนำทางด้านซ้าย
4. **Select Create** เพื่อเริ่มสร้าง agent ใหม่
5. **Enter agent details**:
    - **Name**: ระบุชื่อ agent ที่สื่อความหมายชัดเจน
    - **Description**: เพิ่มคำอธิบายวัตถุประสงค์ของ agent ให้ชัดเจน
    - **Model**: เลือก deployed model จาก dropdown หรือ deploy model ใหม่

portal จะสร้าง agent ให้คุณและเปิดหน้า configuration interface เพื่อให้ปรับแต่งพฤติกรรมและความสามารถได้ละเอียดขึ้น

## Configuring agent instructions and properties

Agent instructions คือรากฐานของพฤติกรรม agent ในช่อง **Instructions** คุณจะกำหนดว่า agent เข้าใจบทบาทของตัวเองอย่างไร ตอบผู้ใช้อย่างไร และจัดการสถานการณ์ต่างๆ อย่างไร instructions ที่ชัดเจนและเจาะจงจะทำให้พฤติกรรมของ agent สม่ำเสมอและเชื่อถือได้มากขึ้น คุณจะได้ตั้งค่า instructions แบบละเอียดอีกครั้งเมื่อลงมือทำใน Visual Studio Code ช่วงถัดไปของโมดูลนี้

นอกจาก instructions แล้ว portal ยังให้คุณตั้งค่า model parameters เช่น **Temperature** (ควบคุมความสุ่มของ response) และ **Top P** (ควบคุมความหลากหลายของ response) โดยตัวเลือก configuration เหล่านี้จะอธิบายเพิ่มเติมใน unit การตั้งค่า Visual Studio Code

## Testing your agent in the portal

Foundry portal มี playground ที่ผสานมาในตัวสำหรับทดสอบ agent ก่อน deployment สภาพแวดล้อมทดสอบนี้ช่วยให้คุณตรวจสอบ instructions ทดลองหลายสถานการณ์ และปรับพฤติกรรมจากผลลัพธ์ที่ได้

ในการทดสอบ agent ให้เลือกแท็บ Playground แล้วเริ่มบทสนทนา playground จะเก็บ conversation history ตลอด session ทำให้คุณทดสอบ multi-turn interactions และตรวจสอบได้ว่า agent รักษา context ได้เหมาะสม

## Adding basic tools

ก่อน deployment คุณสามารถเพิ่มความสามารถให้ agent ด้วย tools จาก tool catalog ในส่วน **Tools** ของหน้า agent configuration (เข้าถึงได้ผ่าน **Build > Tools** ใน portal เช่นกัน) โดย catalog แบ่ง tools ออกเป็น 3 หมวด:

- **Configured** - Built-in tools ที่พร้อมใช้งานทันที เช่น Code Interpreter และ File Search
- **Catalog** - Additional tools ที่คุณเพิ่มได้ เช่น Bing Web Search, Azure AI Search, SharePoint และอื่นๆ
- **Custom** - tools ของคุณเองที่เพิ่มผ่าน OpenAPI specifications หรือ MCP servers

ความสามารถและการตั้งค่า tools จะอธิบายแบบละเอียดใน unit _Extend agent capabilities_ ช่วงถัดไปของโมดูลนี้

## Deploying your agent

เมื่อคุณพอใจกับพฤติกรรมของ agent จากการทดสอบแล้ว ก็สามารถ deploy เพื่อใช้งานจริงใน production ได้ โดย portal จะแสดงสถานะ deployment อย่างชัดเจน และสร้างข้อมูลการเชื่อมต่อที่จำเป็นสำหรับ integration agent เข้ากับแอปพลิเคชันของคุณ หลัง deployment แล้ว คุณสามารถเข้าถึง agent ผ่าน Microsoft Foundry SDK หรือ REST APIs

การสร้าง agents ใน Foundry portal เป็นแนวทางการพัฒนาแบบ visual ที่เข้าถึงได้ง่าย interface จะช่วยนำทางการตั้งค่าพร้อมมอบความสามารถที่ทรงพลังสำหรับสร้างระบบอัตโนมัติที่ซับซ้อนได้

---

## Next unit: Set up Visual Studio Code for agent development