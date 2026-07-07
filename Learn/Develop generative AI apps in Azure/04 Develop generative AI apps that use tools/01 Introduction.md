
Generative AI models มีความสามารถสูงในการทำความเข้าใจและสร้างข้อความ แต่ยังทำงานอยู่ภายในขอบเขตความรู้ของตนเอง โดยสามารถให้เหตุผลได้เฉพาะข้อมูลที่อยู่ใน training data เท่านั้น เมื่อผสาน **tools** เข้ากับการโต้ตอบของ generative AI คุณจะปลดล็อกความสามารถที่กว้างไกลเกินกว่าที่โมเดลเพียงอย่างเดียวจะทำได้

> [!Note]
> การใช้ _tools_ ใน prompts ของ generative AI model ไม่ควรถูกสับสนกับ _[Foundry Tools](https://learn.microsoft.com/en-us/azure/ai-services/reference/sdk-package-resources)_ ซึ่งเป็น Azure AI APIs ที่คุณสามารถนำไปใช้ใน applications และ agents ของคุณได้

## Why tools matter

Tools ช่วยเชื่อมช่องว่างระหว่างการให้เหตุผลของ AI กับการลงมือทำในโลกจริง โดยทำให้ generative AI applications ของคุณสามารถ:

- **Access real-time information**: Fetch ข้อมูลปัจจุบัน เช่น สภาพอากาศ ราคาหุ้น หรือ API responses ที่ไม่ได้อยู่ใน training data ของโมเดล
- **Take actions**: ทำงานต่าง ๆ เช่น ส่งอีเมล สร้าง database records หรือ trigger workflows ตามการตัดสินใจของ AI
- **Ground responses in facts**: ดึงข้อมูลที่เฉพาะเจาะจงและน่าเชื่อถือเพื่อลด incorrect information และเพิ่มความแม่นยำ
- **Extend functionality**: เชื่อมต่อกับ systems, databases และ business logic ที่คุณมีอยู่ได้อย่างราบรื่น
- **Build intelligent workflows**: เชื่อมหลาย operations เข้าด้วยกันเพื่อให้ AI ประสานกระบวนการที่ซับซ้อนหลายขั้นตอนได้

หากไม่มี tools, generative AI จะทำงานแบบแยกเดี่ยว แต่เมื่อมี tools ก็จะกลายเป็น intelligent assistant ที่สามารถสังเกต ให้เหตุผล และลงมือทำกับสิ่งรอบตัวได้

ในโมดูลนี้ เราจะเน้นการระบุ tools ใน prompts ที่ client application ส่งให้โมเดล ในโซลูชันลักษณะนี้ การตั้งค่าเครื่องมือจะถูกจัดการโดย client application ซึ่งโดยพื้นฐานแล้วคือการสร้าง custom generative AI-powered assistant ไว้ภายใน application logic เอง การเรียนรู้วิธีใช้ tools แบบ on-demand กับ generative AI model คือก้าวแรกที่สำคัญในการเรียนรู้การสร้างโซลูชัน _agentic AI_ ซึ่ง model, instructions และ tools จะถูก encapsulate และ persisted อยู่ใน _agent_ ที่มีชื่อเฉพาะ

> [!Tip]
> คุณสามารถศึกษาวิธีใช้ Microsoft Foundry Agents SDK เพื่อสร้าง agents ที่มี persisted configurations ได้เพิ่มเติมที่ [Develop AI agents on Azure](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-azure/)

> [!Note]
> เราเข้าใจว่าผู้เรียนแต่ละคนมีสไตล์การเรียนรู้ที่ต่างกัน คุณสามารถเลือกเรียนโมดูลนี้ในรูปแบบวิดีโอ หรืออ่านเนื้อหาในรูปแบบข้อความและภาพก็ได้ เนื้อหาแบบข้อความมีรายละเอียดมากกว่าวิดีโอ ดังนั้นในบางกรณีคุณอาจใช้เป็นสื่อเสริมควบคู่กับการเรียนผ่านวิดีโอ

---

## Next unit: What are tools?
