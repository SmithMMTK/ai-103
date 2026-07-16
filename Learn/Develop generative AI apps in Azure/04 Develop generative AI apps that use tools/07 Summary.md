
ในโมดูลนี้ คุณได้เรียนรู้ว่า tool calling ช่วยขยายความสามารถของ generative AI model จากการ reasoning ด้วยข้อความอย่างเดียว ไปสู่การลงมือทำที่ใช้งานได้จริงและ grounded

คุณได้สำรวจวิธี configure tools ใน OpenAI Responses API requests และเข้าใจว่าแต่ละ tool เพิ่มความสามารถที่แตกต่างกันอย่างไร:

- tool **code_interpreter** ช่วยให้โมเดล generate และรัน Python code เพื่อการคำนวณ การวิเคราะห์ข้อมูล และ iterative problem solving
- tool **web_search** ช่วยดึงข้อมูลภายนอกที่เป็นปัจจุบัน เพื่อให้ response มีเนื้อหาที่ทันเวลาและ grounded กับแหล่งข้อมูล
- tool **file_search** ช่วยให้โมเดลตอบคำถามจาก indexed documents และ knowledge files ของคุณเอง
- tool **function** ช่วยให้แอปพลิเคชันของคุณรัน custom business logic และส่งผลลัพธ์กลับให้โมเดล

ไม่ว่าจะเป็น tool ใดก็ตาม core implementation pattern จะคล้ายกันเสมอ: กำหนด tool ใน request, ให้โมเดลตัดสินใจว่าเมื่อใดควรใช้, ส่ง tool output กลับเมื่อจำเป็น และ validate responses ให้ถูกต้องและปลอดภัย

ในขั้นถัดไป คุณสามารถผสานเทคนิคเหล่านี้เข้าด้วยกันเพื่อสร้าง assistants ที่มีความสามารถมากขึ้น และพัฒนาไปสู่ agentic solutions แบบเต็มรูปแบบที่มี persisted instructions, tools และ orchestration

## Further reading

หากต้องการเรียนรู้เพิ่มเติมเกี่ยวกับการใช้ tools ร่วมกับ models โปรดดู resources ต่อไปนี้:

- [OpenAI developer guide: Tools](https://developers.openai.com/api/docs/guides/tools)
- [OpenAI developers Guide: Function calling](https://developers.openai.com/api/docs/guides/function-calling)