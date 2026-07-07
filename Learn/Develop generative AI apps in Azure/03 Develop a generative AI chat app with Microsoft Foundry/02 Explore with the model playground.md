
ก่อนที่คุณจะเขียน code เพื่อสร้าง generative AI chat application การสำรวจว่าฟีเจอร์ใดที่ project ของคุณสามารถทำได้ผ่าน Foundry portal จะช่วยได้มาก โดย portal มี interactive tools สำหรับทดสอบ models และสร้าง code samples ที่คุณสามารถนำไปใช้เป็นจุดเริ่มต้นของ applications ได้

[![Screenshot of the Model playground in Microsoft Foundry portal.|778](https://learn.microsoft.com/en-us/training/wwl-data-ai/foundry-sdk/media/foundry-playground.png)](https://learn.microsoft.com/en-us/training/wwl-data-ai/foundry-sdk/media/foundry-playground.png#lightbox)

## Exploring with the Model playground

**Model playground** ใน Foundry portal มอบสภาพแวดล้อมแบบ interactive สำหรับทดสอบ models ก่อนที่คุณจะเขียน code ใดๆ โดยคุณเข้าถึงได้ผ่านการเลือก **Model playground** จากเมนูนำทางด้านซ้าย

The playground lets you:

- ส่ง prompts ไปยัง deployed models และดู responses แบบ real time
- ปรับ settings เช่น temperature และ max tokens
- เพิ่ม system messages เพื่อปรับแต่ง model behavior
- ทดลองกับ models และ configurations ที่แตกต่างกัน

no-code environment นี้ช่วยให้คุณเข้าใจว่า models ตอบสนองต่อ inputs และ settings ที่ต่างกันอย่างไร ทำให้ออกแบบ application ได้ง่ายขึ้น

## Generating code samples

หนึ่งในฟีเจอร์ที่มีประโยชน์ที่สุดของ Model playground คือปุ่ม **Code** ใน chat pane คุณสามารถกดปุ่มนี้ได้ทุกเมื่อระหว่างการทดลอง เพื่อดู code samples สำหรับนำ chat session ไปสร้างซ้ำใน app ของคุณ

The generated code samples include choices for:

- **API** - ใช้ Responses API หรือ API อื่นอย่าง ChatCompletions
- **Language** - เลือก programming language ที่คุณต้องการ
- **SDK** - เลือกว่าอยากดูตัวอย่างของ SDK ใด

samples เหล่านี้จะถูก pre-populated ด้วย project endpoint, model deployment name และ settings ปัจจุบันของคุณ จึงเป็นจุดเริ่มต้นแบบพร้อมใช้งานสำหรับการสร้าง application

คุณสามารถคัดลอก code นี้ไปยัง development environment ของคุณได้โดยตรง แล้วแก้ไขให้เหมาะกับความต้องการของคุณ

## From playground to code

workflow ทั่วไปสำหรับการสร้าง AI application ด้วย Microsoft Foundry มีลักษณะดังนี้:

1. **Explore in the playground** - ทดสอบ prompts, ปรับ settings และหาแนวทางที่ใช่
2. **Generate code samples** - ใช้แท็บ **Code** เพื่อรับ SDK samples
3. **Develop your application** - นำ generated code ไปปรับแต่งตามความต้องการเฉพาะของคุณ
4. **Iterate and refine** - กลับไปที่ playground เพื่อทดสอบไอเดียใหม่ แล้วอัปเดต code ของคุณ

แนวทางนี้ช่วยให้คุณทำ prototype และ validate ไอเดียได้รวดเร็ว ก่อนลงทุนเวลาในขั้นตอน development

ใน unit ถัดไป คุณจะได้เรียนรู้เกี่ยวกับ endpoints และ SDKs ที่พร้อมใช้งานสำหรับพัฒนา client application

---

## Next unit: Choose an endpoint and SDK