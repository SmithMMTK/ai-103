
วิธีที่เข้าถึงง่ายที่สุดในการ optimize ประสิทธิภาพของโมเดลคือการทำ **prompt engineering** โดย prompt engineering คือกระบวนการออกแบบและปรับปรุง prompts เพื่อเพิ่มคุณภาพ ความแม่นยำ และความเกี่ยวข้องของ responses ที่ language model สร้างขึ้น วิธีนี้ไม่ต้องมี infrastructure หรือ training data เพิ่มเติม และคุณสามารถเริ่มทดลองได้ทันที

## Understand prompt components

เมื่อคุณโต้ตอบกับ language model คุณภาพของคำถามจะส่งผลโดยตรงต่อคุณภาพของ response prompt ที่ออกแบบมาอย่างดีจะช่วยให้โมเดลเข้าใจความต้องการของคุณและสร้างคำตอบที่มีประโยชน์มากขึ้น

Prompts สำหรับ chat completion models โดยทั่วไปจะมีองค์ประกอบต่อไปนี้:

- **System message**: คำสั่งที่กำหนด behavior, role และ constraints ของโมเดล
- **User message**: คำถามหรือ input จากผู้ใช้
- **Assistant message**: responses ก่อนหน้าของโมเดลที่ใช้ใน multi-turn conversations
- **Examples**: คู่ตัวอย่าง input/output ที่แสดงรูปแบบ response ที่คาดหวัง

วิธีที่คุณจัดโครงสร้างและผสานองค์ประกอบเหล่านี้เข้าด้วยกัน จะเป็นตัวกำหนดว่าโมเดลตอบได้มีประสิทธิภาพเพียงใด

## Design effective system messages

**system message** คือชุดคำสั่งที่คุณส่งให้โมเดลเพื่อกำกับ responses โดยทั่วไป system messages จะอยู่ต้นบทสนทนาและทำหน้าที่เป็นชุดคำสั่งระดับสูงสุด คุณใช้ system messages เพื่อ:

- กำหนด role และ boundaries ของ assistant
- กำหนด tone และ communication style
- ระบุ output formats เช่น JSON หรือ bullet points
- เพิ่ม safety และ quality constraints ให้เหมาะกับ scenario ของคุณ

system message อาจเรียบง่ายได้ เช่น:

```text
You are a helpful AI assistant.
```

หรืออาจมีทั้งกฎรายละเอียดและข้อกำหนดด้านรูปแบบ เช่น chat application ของ travel agency อาจใช้ว่า:

```text
You are a friendly travel advisor for Margie's Travel.
Answer only questions related to travel, hotels, and trip planning.
Use a warm, conversational tone.
If you don't have enough information to answer, ask a clarifying question.
Format hotel recommendations as a bulleted list with the hotel name, location, and price range.
```

> [!IMPORTANT]
> system message มีอิทธิพลต่อโมเดล แต่ไม่ได้รับประกันว่าโมเดลจะทำตามเสมอไป คุณควรทดสอบและ iterate system messages อย่างต่อเนื่อง และเสริมด้วยมาตรการอื่น เช่น content filtering และ evaluation

เมื่อออกแบบ system message ให้ใช้ checklist นี้:

1. **Start with the assistant's role**: ระบุ role และ expected outcome สำหรับคำขอทั่วไป
2. **Define boundaries**: ระบุหัวข้อ การกระทำ และประเภทเนื้อหาที่ assistant ควรหลีกเลี่ยง
3. **Specify the output format**: หากต้องการรูปแบบเฉพาะ ให้ระบุให้ชัดเจนและใช้ให้สม่ำเสมอ
4. **Add a "when unsure" policy**: บอกโมเดลว่าควรทำอย่างไรเมื่อคำขอผู้ใช้กำกวม นอกขอบเขต หรือเมื่อโมเดลมีข้อมูลไม่พอ

## Apply prompt patterns

prompts ที่มีประสิทธิภาพมักใช้ patterns ที่ช่วยให้โมเดลสร้าง responses ได้ดีขึ้น ต่อไปนี้คือ patterns ที่ใช้บ่อย:

### Persona pattern

กำหนดให้โมเดลรับมุมมองหรือ role เฉพาะ เช่น การสั่งให้โมเดลตอบในบทบาท seasoned marketing professional จะได้ผลลัพธ์ต่างจากการไม่กำหนด persona

| |No persona|With persona|
|---|---|---|
|System message|_None_|You're a seasoned marketing professional writing for technical customers.|
|User prompt|Write a one-sentence description of a CRM product.|Write a one-sentence description of a CRM product.|
|Response|A CRM product is a software tool designed to manage a company's interactions with customers.|Experience seamless customer relationship management with our CRM, designed to streamline operations and drive sales growth with robust analytics.|

### Format template pattern

ใส่ template หรือโครงสร้างใน prompt เพื่อให้ได้ output ในรูปแบบที่ต้องการ เช่น หากต้องการ structured response เกี่ยวกับโรงแรม:

```text
Format the result to show:
- Hotel name
- Location
- Star rating
- Price range per night
```

pattern นี้ช่วยให้ responses มีความสม่ำเสมอ เป็นระเบียบ และ parse ได้ง่ายในแอปพลิเคชันของคุณ

### Chain-of-thought pattern

ขอให้โมเดลอธิบาย reasoning แบบทีละขั้น เทคนิคนี้เรียกว่า **chain of thought** ซึ่งช่วยลดโอกาสเกิดผลลัพธ์ที่คลาดเคลื่อนและทำให้ตรวจสอบตรรกะของโมเดลได้ง่ายขึ้น

ตัวอย่างเช่น แทนที่จะถามว่า "Which hotel is best for a family of four?" คุณสามารถเขียน prompt ว่า:

```text
Which hotel is best for a family of four? Take a step-by-step approach: 
consider room size, amenities for children, location, and price.
```

อีกเทคนิคที่เกี่ยวข้องคือการ **break the task down** เป็น sub-steps ที่ชัดเจน _before_ โมเดลตอบ แทนการให้โมเดล reasoning ทุกอย่างรวดเดียว เช่น คุณอาจให้โมเดลดึง key facts จากบทความก่อน แล้วค่อยถามคำถามต่อยอดจาก facts เหล่านั้นใน prompt ถัดไป การแยกงานแบบนี้ช่วยลดข้อผิดพลาดในงานที่ซับซ้อนและมีหลายส่วน

> [!NOTE]
> Chain-of-thought prompting เป็นเทคนิคสำหรับ non-reasoning models ส่วน reasoning models เช่น o-series models สามารถจัดการตรรกะแบบทีละขั้นภายในได้เอง

### Few-shot learning pattern

ให้ตัวอย่าง input และ output ที่ต้องการอย่างน้อยหนึ่งชุดเพื่อช่วยให้โมเดลจับ pattern ที่คุณต้องการ เทคนิคนี้เรียกว่า **few-shot learning** (หรือ **one-shot** หากมีตัวอย่างเดียว) และถ้าไม่ให้ตัวอย่างเลยจะเรียกว่า **zero-shot** learning

ตัวอย่างการ classify customer inquiries:

```text
Classify the following customer messages:

Message: "I need to change my flight to Rome"
Category: Booking change

Message: "What's the weather like in Bali in March?"
Category: Travel information

Message: "Can I get a refund for my cancelled tour?"
Category:
```

โมเดลจะเรียนรู้ pattern การจัดหมวดหมู่จากตัวอย่าง และเติมรายการสุดท้ายได้ถูกต้อง

### Use clear syntax and delimiters

เมื่อ prompt ของคุณมีหลายส่วน เช่น instructions, source text และ examples ให้ใช้ delimiters อย่าง `---`, Markdown headings หรือ XML tags เพื่อแยกส่วนให้ชัดเจน ขอบเขตที่ชัดช่วยให้โมเดลแยกแยะ instructions ออกจากเนื้อหาได้ดีขึ้นและลดโอกาสตีความผิด

> [!TIP]
> Models อาจไวต่อ **recency bias** ซึ่งหมายความว่าข้อความท้าย prompt อาจมีอิทธิพลมากกว่าข้อความต้น prompt หากโมเดลยังทำตามคำสั่งไม่สม่ำเสมอ ให้ลองย้ำคำสั่งสำคัญไว้ท้าย prompt อีกครั้ง

## Configure model parameters

นอกเหนือจากตัวข้อความใน prompts คุณยังสามารถปรับ model parameters ที่ควบคุมวิธีการสร้าง responses ของโมเดลได้:

- **Temperature**: ควบคุมความสุ่มของ output ค่าสูง (เช่น 0.7) จะให้ responses ที่สร้างสรรค์และหลากหลายกว่า ส่วนค่าต่ำ (เช่น 0.2) จะให้ responses ที่โฟกัสและ deterministic มากกว่า ค่าต่ำเหมาะกับงาน factual และค่าสูงเหมาะกับงาน creative
- **Top_p**: ควบคุมความสุ่มเช่นกันแต่คนละวิธี โดยจำกัดโมเดลให้เลือกจากกลุ่ม next tokens ที่มีความเป็นไปได้สูงสุดเท่านั้น เช่น `top_p` เท่ากับ 0.9 หมายถึงโมเดลพิจารณาเฉพาะ 90% แรกของ probable tokens

> [!TIP]
> คำแนะนำทั่วไปคือปรับแค่ temperature หรือ top_p อย่างใดอย่างหนึ่ง ไม่ควรปรับทั้งสองพร้อมกัน

สำหรับ travel agency scenario คุณอาจใช้ temperature ต่ำ (0.2) เมื่อตอบคำถาม factual เกี่ยวกับ hotel amenities และใช้ temperature สูงขึ้น (0.7) เมื่อต้องสร้างข้อเสนอแนะ itinerary การเดินทางเชิงสร้างสรรค์

## When prompt engineering is enough

prompt engineering คือจุดเริ่มต้นที่เหมาะสมสำหรับความพยายาม optimize โมเดลทุกรูปแบบ และจะมีประสิทธิภาพมากเมื่อคุณต้องการ:

- กำกับ tone, format และ behavior ของโมเดล
- ระบุคำสั่งเฉพาะสำหรับงานหนึ่งๆ
- iterate ผลลัพธ์ได้รวดเร็วโดยไม่ต้องเปลี่ยน infrastructure
- ควบคุมต้นทุนให้ต่ำ เพราะไม่ต้องมี training หรือ data storage เพิ่มเติม

อย่างไรก็ตาม prompt engineering ก็มีข้อจำกัด หากโมเดลไม่สามารถเข้าถึงข้อมูลที่ต้องใช้ (เช่น hotel catalog ของบริษัท) หรือยังคงรักษา behavior ที่ต้องการไม่ได้แม้มีคำสั่งละเอียดแล้ว คุณควรพิจารณากลยุทธ์เสริมเพิ่มเติม

---

## Next unit: Ground your model with Retrieval Augmented Generation