
แม้ว่าคุณจะทำงานหลายอย่างที่จำเป็นต่อการพัฒนาโซลูชัน AI ได้โดยตรงในพอร์ทัล Microsoft Foundry แต่นักพัฒนายังจำเป็นต้องเขียน ทดสอบ และปรับใช้โค้ดด้วย

## เครื่องมือและสภาพแวดล้อมสำหรับการพัฒนา

มีเครื่องมือและสภาพแวดล้อมสำหรับการพัฒนาจำนวนมากให้เลือกใช้ และนักพัฒนาควรเลือกเครื่องมือที่รองรับภาษา SDK และ API ที่ต้องใช้งาน รวมถึงเป็นเครื่องมือที่ตนเองถนัดที่สุด ตัวอย่างเช่น นักพัฒนาที่เน้นสร้างแอปพลิเคชันบน Windows ด้วย .NET Framework อาจชอบทำงานในสภาพแวดล้อมพัฒนาแบบครบวงจร (IDE) อย่าง Microsoft Visual Studio ในทางกลับกัน นักพัฒนาเว็บแอปที่ทำงานกับภาษาและไลบรารีโอเพนซอร์สหลากหลาย อาจชอบใช้ตัวแก้ไขโค้ดอย่าง Visual Studio Code (VS Code) มากกว่า ทั้งสองตัวเลือกนี้เหมาะสำหรับการพัฒนาแอปพลิเคชัน AI บน Azure

### ส่วนขยาย Foundry Toolkit สำหรับ Visual Studio Code

เมื่อพัฒนาแอปพลิเคชัน Generative AI บน Microsoft Foundry ด้วย Visual Studio Code คุณสามารถใช้ส่วนขยาย Foundry Toolkit สำหรับ Visual Studio Code เพื่อช่วยให้งานสำคัญในเวิร์กโฟลว์ง่ายขึ้น เช่น

- เรียกดูและจัดการทรัพยากรของโปรเจกต์ รวมถึงโมเดลที่ปรับใช้แล้ว เอเจนต์ การเชื่อมต่อ และเวกเตอร์สโตร์
- ปรับใช้โมเดลจากแคตตาล็อกโมเดล
- ทดสอบโมเดลและเอเจนต์ในเพลย์กราวด์แบบรวมในตัว
- กำหนดค่าเอเจนต์แบบ Declarative และ Hosted ด้วยตัวออกแบบภาพและไฟล์ YAML
- สร้างโค้ดเชื่อมต่อสำหรับผสานเอเจนต์เข้ากับแอปพลิเคชันของคุณ

![ภาพหน้าจอของส่วนขยาย Foundry Toolkit สำหรับ Visual Studio Code](https://learn.microsoft.com/en-us/training/wwl-data-ai/prepare-azure-ai-development/media/vs-code.png)

เคล็ดลับ

ข้อมูลเพิ่มเติมเกี่ยวกับการใช้ Foundry Toolkit สำหรับ Visual Studio Code ดูได้ที่ **[Foundry Toolkit for Visual Studio Code](https://code.visualstudio.com/docs/intelligentapps/overview)**

### GitHub และ GitHub Copilot

GitHub เป็นแพลตฟอร์มยอดนิยมที่สุดของโลกสำหรับการควบคุมซอร์สโค้ดและการจัดการ DevOps และสามารถเป็นองค์ประกอบสำคัญของการพัฒนาแบบทีมได้ ทั้ง Visual Studio และ VS Code ต่างก็มีการเชื่อมต่อกับ GitHub โดยตรง และเข้าถึง GitHub Copilot ได้ ซึ่งเป็นผู้ช่วย AI ที่ช่วยเพิ่มประสิทธิภาพและความสามารถในการทำงานของนักพัฒนาได้อย่างมาก

![ภาพหน้าจอ GitHub Copilot ใน Visual Studio Code](https://learn.microsoft.com/en-us/training/wwl-data-ai/prepare-azure-ai-development/media/github-copilot.png)

เคล็ดลับ

ข้อมูลเพิ่มเติมเกี่ยวกับการใช้ GitHub Copilot ใน Visual Studio Code ดูได้ที่ **[GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)**

## ภาษาโปรแกรม API และ SDK

คุณสามารถพัฒนาแอปพลิเคชัน AI ได้ด้วยภาษาโปรแกรมและเฟรมเวิร์กยอดนิยมหลายแบบ เช่น Microsoft C#, Python, Node, TypeScript, Java และอื่นๆ เมื่อสร้างโซลูชัน AI บน Azure API และ SDK ที่พบบ่อยและควรวางแผนใช้งาน ได้แก่

- **[Microsoft Foundry SDK](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview)** ช่วยให้คุณเขียนโค้ดเพื่อเชื่อมต่อกับโปรเจกต์ Microsoft Foundry และเข้าถึงทรัพยากรเฉพาะของ Foundry เช่น เอเจนต์ และคลังความรู้ Foundry IQ
- **[The OpenAI API](https://learn.microsoft.com/en-us/azure/foundry/openai/latest)** ช่วยให้คุณใช้ OpenAI SDK เพื่อสร้างแอปแชตโดยอิงจากโมเดล Foundry ที่รองรับไวยากรณ์แบบ OpenAI
- **[Foundry Tools SDKs](https://learn.microsoft.com/en-us/azure/ai-services/reference/sdk-package-resources)** เป็นไลบรารีเฉพาะบริการ AI สำหรับหลายภาษาและหลายเฟรมเวิร์ก ที่ช่วยให้คุณใช้งานทรัพยากร Foundry Tools ในซับสคริปชันของคุณได้ นอกจากนี้ยังสามารถใช้งาน Foundry Tools ผ่าน [REST APIs](https://learn.microsoft.com/en-us/azure/ai-services/reference/rest-api-resources) ได้เช่นกัน