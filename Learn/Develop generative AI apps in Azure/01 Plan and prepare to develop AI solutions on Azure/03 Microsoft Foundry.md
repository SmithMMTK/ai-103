
**Microsoft Foundry** เป็นแพลตฟอร์มสำหรับการพัฒนา AI บน Microsoft Azure แม้ว่าคุณจะสามารถสร้างทรัพยากร AI (AI resources) แต่ละรายการและพัฒนาแอปพลิเคชันที่ใช้งานทรัพยากรเหล่านั้นได้โดยไม่ต้องใช้ Microsoft Foundry แต่ความสามารถด้านการจัดการโครงการ (Project Organization), การจัดการทรัพยากร (Resource Management) และเครื่องมือสำหรับการพัฒนา AI ของ Microsoft Foundry ทำให้แพลตฟอร์มนี้เป็นแนวทางที่แนะนำสำหรับการสร้างโซลูชัน AI แทบทุกประเภท ยกเว้นงานที่เรียบง่ายมาก ๆ

Microsoft Foundry ประกอบด้วย:

- **Microsoft Foundry portal** – อินเทอร์เฟซแบบเว็บ (Web-based Visual Interface) สำหรับจัดการและพัฒนาโครงการ AI ผ่านหน้าจอกราฟิก ช่วยให้สามารถสร้าง จัดการ และติดตามโครงการได้อย่างสะดวก
- **Microsoft Foundry SDK** – ชุดเครื่องมือสำหรับนักพัฒนา (Software Development Kit) ที่ช่วยให้สามารถพัฒนาและจัดการโซลูชัน AI ผ่านการเขียนโค้ด (Programmatically) ได้ เหมาะสำหรับการสร้างระบบอัตโนมัติ การผสานรวมกับระบบอื่น และการพัฒนาแอปพลิเคชัน AI ขั้นสูง

## Microsoft Foundry projects

ใน Microsoft Foundry คุณจะจัดการการเชื่อมต่อทรัพยากร (Resource Connections), ข้อมูล (Data), โค้ด (Code) และองค์ประกอบอื่น ๆ ของโซลูชัน AI ภายใน **โปรเจ็กต์ (Project)**

แต่ละโปรเจ็กต์จะสังกัด **Microsoft Foundry Resource** เพียงรายการเดียวบน Azure ซึ่งเป็นทรัพยากรหลักที่ให้บริการด้านต่าง ๆ เช่น

- Compute สำหรับประมวลผล
- พื้นที่จัดเก็บข้อมูล (Data Storage)
- เครื่องมือ AI
- และบริการอื่น ๆ ที่จำเป็นสำหรับการพัฒนาโซลูชัน AI

Microsoft Foundry Resource หนึ่งรายการสามารถรองรับ **โปรเจ็กต์ลูก (Child Projects)** ได้ตั้งแต่หนึ่งโปรเจ็กต์ขึ้นไป โดยจะมีหนึ่งโปรเจ็กต์ที่ถูกกำหนดให้เป็น **โปรเจ็กต์เริ่มต้น (Default Project)** สำหรับใช้งานเป็นค่าเริ่มต้นของ Resource นั้น ๆ

![Diagram of a Foundry project.](https://learn.microsoft.com/en-us/training/wwl-data-ai/prepare-azure-ai-development/media/foundry.png)

นักพัฒนาใช้ **โปรเจ็กต์ (Project)** เพื่อจัดการ Asset ต่าง ๆ ที่จำเป็นสำหรับการสร้างโซลูชัน AI ซึ่งประกอบด้วย

- **Models**: Deployment ของ **Large Language Model (LLM)** ที่อ้างอิงจากโมเดลใน **Foundry Models** ซึ่งเป็นแค็ตตาล็อกโมเดลขนาดใหญ่ที่รวมโมเดลจาก Microsoft OpenAI และผู้ให้บริการรายอื่น ๆ ไว้ในที่เดียว คุณสามารถเชื่อมต่อและใช้งานโมเดลเหล่านี้ได้ผ่าน **Project Endpoint** (โดยใช้ Foundry APIs และ SDKs) หรือผ่าน **Azure OpenAI Endpoint** (โดยใช้ OpenAI APIs และ SDKs)
- **Agents**: การกำหนดค่า AI ที่มีชื่อ (Named AI Configuration) ซึ่งรวบรวม **LLM**, **Instructions** และ **Tools** ไว้ด้วยกัน เพื่อสร้างเอนทิตี AI แบบอัตโนมัติ (Autonomous AI Entity) ที่สามารถทำงานอัตโนมัติ รวมถึงทำงานร่วมกับผู้ใช้และ Agent ตัวอื่น ๆ ได้ Agent ใน Foundry ถูกพัฒนาและใช้งานผ่าน **Microsoft Foundry Agent Service** โดยเชื่อมต่อผ่าน Project Endpoint
- **Tools**: เครื่องมือที่ Agent ใช้งานได้ ซึ่งอาจเป็น
       - ความสามารถที่มีมาให้ในระบบ เช่น **Web Search** หรือ **Code Interpreter**
    - การเชื่อมต่อกับเครื่องมือที่พัฒนาขึ้นเองหรือจากผู้ให้บริการภายนอกผ่าน **Model Context Protocol (MCP) Connections**
        นอกจากนี้ **Microsoft Foundry Tools** ยังมีชุดบริการ AI สำหรับงานทั่วไป เช่น
    
    - การวิเคราะห์ข้อความ (Text Analysis)
    - การรู้จำและสังเคราะห์เสียง (Speech Recognition and Synthesis)
    - การแปลภาษา (Translation)
    - การทำความเข้าใจเนื้อหา (Content Understanding)
    
    ซึ่งสามารถนำมาใช้สร้างโซลูชัน AI บน Foundry ได้ โดย Foundry Tools จะโฮสต์อยู่ใน **Foundry Resource** ที่เชื่อมโยงกับโปรเจ็กต์ของคุณ
    
- **Knowledge**: Agent สามารถใช้เครื่องมือเพื่อเชื่อมต่อกับ **Knowledge Store** และนำข้อมูลที่จัดเก็บอยู่มาใช้เป็นบริบท (Context) สำหรับ Prompt ได้ เพื่อให้การเชื่อมต่อกับแหล่งความรู้หลายแห่งเป็นเรื่องง่าย คุณสามารถใช้ **Foundry IQ** ภายในโปรเจ็กต์เพื่อสร้าง **MCP-based Knowledge Connection** เพียงจุดเดียว ซึ่งทำหน้าที่เป็นศูนย์กลางในการเข้าถึงแหล่งข้อมูลทั้งหมด

การแยก **Asset ที่อยู่ในระดับโปรเจ็กต์ (Project-specific Assets)** ออกจาก **Cloud Services** ที่อยู่ใน **Microsoft Foundry Resource** ช่วยรองรับรูปแบบการพัฒนา AI ที่พบบ่อยที่สุด โดยเฉพาะการสร้างแอปพลิเคชันแชตด้วย Generative AI และ AI Agent

การใช้ **Foundry Project** ช่วยให้คุณได้รับระดับการรวมศูนย์ของทรัพยากร (Resource Centralization) และความสามารถในการพัฒนาที่เหมาะสม โดยมีภาระในการบริหารจัดการทรัพยากร (Administrative Resource Management) น้อยที่สุด

## The Microsoft Foundry portal

คุณสามารถใช้ **Microsoft Foundry Portal** เพื่อพัฒนาและจัดการ **โปรเจ็กต์ (Projects)** ที่อยู่ภายใต้ **Microsoft Foundry Resources** ได้

![Screenshot of the Foundry portal.](https://learn.microsoft.com/en-us/training/wwl-data-ai/prepare-azure-ai-development/media/foundry-portal.png)

## **โดยทั่วไป การพัฒนาโซลูชัน AI จะเริ่มต้นจาก Foundry Project**

โครงการพัฒนาโซลูชัน AI ส่วนใหญ่จะเริ่มต้นจาก **Foundry Project** ซึ่งคุณสามารถดำเนินการต่าง ๆ ได้ดังนี้

- ค้นหา เปรียบเทียบ ปรับใช้ (Deploy) และทดสอบโมเดล
- สร้างและทดสอบ Agent
- สร้างการเชื่อมต่อ **MCP (Model Context Protocol)** ไปยังเครื่องมือต่าง ๆ และแหล่งข้อมูลความรู้ของ **Foundry IQ**
- สำรวจและทดลองใช้ **Microsoft Foundry Tools**
- จัดการการกำหนดค่าของ Resource และสิทธิ์การเข้าถึงของผู้ใช้
- ค้นหา Endpoint และ Key ที่จำเป็นสำหรับการเข้าถึง Asset จากแอปพลิเคชันฝั่งไคลเอนต์

นอกจากนี้ หากต้องการทำงานแบบอัตโนมัติ (Automation) กับ Foundry Project คุณสามารถใช้ **Microsoft Foundry SDK** เพื่อสร้างและจัดการ Asset ต่าง ๆ ผ่านสคริปต์ หรือดำเนินการแบบอัตโนมัติในกระบวนการ **CI/CD** ภายใน **DevOps Pipeline**

**หมายเหตุ**

โมดูลนี้มุ่งเน้นไปที่สถาปัตยกรรม **Microsoft Foundry Project** รูปแบบล่าสุด

สำหรับ Foundry Project รุ่นเก่า (**Classic**) อาจใช้สถาปัตยกรรมแบบ **Hub-based**

นอกจากนี้ **Microsoft Foundry Portal** กำลังอยู่ระหว่างการเปลี่ยนผ่านไปยังอินเทอร์เฟซใหม่ที่แสดงในโมดูลนี้ ดังนั้นบางฟีเจอร์หรือบางงานอาจยังไม่รองรับใน Portal เวอร์ชันใหม่

หากต้องการศึกษาข้อมูลเกี่ยวกับ **Microsoft Foundry (Classic)** สามารถดูได้จากเอกสาร **What is Microsoft Foundry? (Classic)**