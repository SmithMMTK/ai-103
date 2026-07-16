
prompt engineering ช่วยให้คุณกำกับ behavior ของโมเดลได้ และ RAG ช่วยให้ responses grounded กับข้อมูลข้อเท็จจริง แต่ในบางครั้งโมเดลก็ยังไม่สร้าง responses ที่มี style, tone หรือ format สม่ำเสมอตามที่คุณต้องการ เมื่อคุณพบว่าโมเดลเพิกเฉยหรือทำตามคำสั่งไม่สม่ำเสมอ แม้จะมี system messages ที่ละเอียดและ few-shot examples แล้วก็ตาม นี่อาจเป็นเวลาที่ควร **fine-tune** โมเดล

**Fine-tuning** คือกระบวนการนำ pretrained language model มาฝึกเพิ่มเติมด้วย dataset ที่เล็กกว่าและเฉพาะงานมากขึ้น วิธีนี้จะปรับ internal weights ของโมเดล เพื่อให้โมเดลสร้าง responses ที่สอดคล้องกับ patterns ใน training data ของคุณ

## Understand fine-tuning

Foundation models อย่าง GPT-4o ถูกฝึกด้วยข้อมูลทั่วไปจำนวนมหาศาล โดย fine-tuning จะต่อยอดบนพื้นฐานนั้นผ่านการฝึกด้วยตัวอย่างเพิ่มเติมที่สะท้อนความต้องการเฉพาะของคุณ ลองมองว่าเป็นการทำให้ generalist กลายเป็น specialist: โมเดลยังคงความสามารถด้านภาษาที่กว้างอยู่ แต่เรียนรู้ที่จะตอบในรูปแบบเฉพาะที่ training data ของคุณแสดงไว้

fine-tuning ใช้ **LoRA (Low-Rank Adaptation)** ซึ่งเป็นเทคนิคที่ประมาณการการเปลี่ยนแปลงของ weights ด้วย lower-rank representation แทนที่จะ retrain parameters ทั้งหมดของโมเดล LoRA จะอัปเดตเพียง subset ขนาดเล็กของ parameters ที่สำคัญ ทำให้การฝึกเร็วขึ้นและคุ้มค่าต้นทุนมากขึ้นโดยยังรักษาคุณภาพโมเดลไว้ได้

ข้อดีหลักของ fine-tuning เมื่อเทียบกับการเทรนโมเดลจากศูนย์คือประสิทธิภาพ คุณใช้เวลาน้อยกว่า ใช้ computing resources น้อยกว่า และใช้ข้อมูลน้อยกว่ามากในการปรับแต่ง behavior ของโมเดล

## Know when to fine-tune

fine-tuning เหมาะกับสถานการณ์ที่ prompt engineering อย่างเดียวไม่พอสำหรับความสม่ำเสมอที่คุณต้องการ use cases ที่พบบ่อย ได้แก่:

- **Consistent style and tone**: องค์กรของคุณมี brand voice เฉพาะ และโมเดลต้องทำตามได้อย่างสม่ำเสมอในทุก interaction เช่น travel agency ต้องการให้ทุก response ใช้โทนอุ่น เป็นมิตร และย่อหน้าสั้น
- **Specific output formats**: คุณต้องการให้โมเดลสร้าง structured output ได้อย่างสม่ำเสมอ เช่น JSON responses ตาม schema ที่กำหนด และ few-shot examples อย่างเดียวไม่เพียงพอ
- **Reducing prompt length**: system messages ที่ยาวและมีตัวอย่างจำนวนมากใช้ tokens มากและเพิ่ม latency โดย fine-tuning จะฝัง patterns เหล่านั้นไว้ในโมเดล ช่วยลดขนาด prompt ที่ต้องใช้ต่อ request
- **Distillation**: คุณต้องการถ่ายทอดความสามารถจากโมเดลขนาดใหญ่ที่มีต้นทุนสูงไปยังโมเดลขนาดเล็กที่มีประสิทธิภาพกว่า เช่น เก็บ outputs จากโมเดลที่ทำผลงานดี แล้วใช้ fine-tune โมเดลเล็กให้ได้คุณภาพใกล้เคียงกันด้วยต้นทุนและ latency ต่ำกว่า
- **Enhancing tool usage**: เมื่อแอปพลิเคชันของคุณใช้ tool calling การ fine-tune ด้วยตัวอย่างการใช้ tools สามารถเพิ่มความแม่นยำในการเลือก tools และการสร้าง parameters

> [!IMPORTANT]
> fine-tuning เป็นความสามารถขั้นสูง ควรเริ่มจากประเมิน baseline performance ของ standard model เทียบกับความต้องการของคุณก่อนเสมอ ก่อนตัดสินใจ fine-tune หากไม่มี baseline จะประเมินได้ยากว่า fine-tuning ทำให้ประสิทธิภาพดีขึ้นหรือแย่ลง

## Explore types of fine-tuning

Microsoft Foundry มีหลายเทคนิคสำหรับ fine-tuning:

- **Supervised fine-tuning (SFT)**: ฝึกโมเดลด้วย labeled dataset ที่เป็นคู่ prompt-and-response โมเดลจะเรียนรู้การสร้าง outputs ให้ตรงกับ patterns ใน training data ของคุณ เทคนิคนี้เหมาะเมื่อวิธีทำงานมีรูปแบบที่ชัดเจน
- **Reinforcement fine-tuning (RFT)**: optimize behavior ของโมเดลผ่าน iterative feedback โดยใช้ grader ให้รางวัลกับ responses ที่ดีกว่าแบบค่อยเป็นค่อยไป RFT เหมาะกับงานซับซ้อนหรือเปลี่ยนแปลงสูง ที่มีได้หลายแนวทางและต้องการยกระดับคุณภาพ reasoning
- **Direct Preference Optimization (DPO)**: align โมเดลจาก human preferences โดยให้คู่ response ที่ preferred และ non-preferred โดย DPO ใช้การคำนวณน้อยกว่าแนวทาง reinforcement learning แบบดั้งเดิม แต่ยังมีประสิทธิภาพด้าน alignment เทียบเท่า

คุณยังสามารถผสานเทคนิคเข้าด้วยกันได้ เช่น เริ่มจาก supervised fine-tuning เพื่อสร้าง customized model แล้วใช้ DPO เพื่อ align responses ให้ตรงกับ preferences เฉพาะของคุณยิ่งขึ้น

## Prepare training data

fine-tuning ต้องใช้ dataset ของตัวอย่างคุณภาพสูงในรูปแบบ JSONL (JSON Lines) สำหรับ chat completion models แต่ละตัวอย่างจะเป็นบทสนทนาที่มี system, user และ assistant messages:

```json
{"messages": [{"role": "system", "content": "You are a friendly travel advisor for Margie's Travel."}, {"role": "user", "content": "What's a good beach destination in Europe?"}, {"role": "assistant", "content": "For a beautiful European beach experience, consider the Algarve in southern Portugal! It offers stunning golden cliffs, warm waters, and charming coastal towns. The best time to visit is from May through September."}]}
{"messages": [{"role": "system", "content": "You are a friendly travel advisor for Margie's Travel."}, {"role": "user", "content": "I need a budget hotel in Tokyo."}, {"role": "assistant", "content": "Here are some great budget-friendly options in Tokyo:\n\n- **Sakura Hotel Jimbocho** - Central location, from $45/night\n- **Khaosan World Asakusa** - Near Senso-ji temple, from $35/night\n- **Imano Tokyo Ginza Hostel** - Modern design, from $40/night\n\nAll three options are close to public transit, making it easy to explore the city."}]}
```

เมื่อเตรียม training data:

- ควรมี system message ที่สม่ำเสมอในทุกตัวอย่าง
- ใช้ตัวอย่างที่มีคุณภาพสูงและเป็นตัวแทนสถานการณ์ที่คุณคาดว่าจะเจอ
- ควรมีอย่างน้อยระดับหลายร้อยตัวอย่าง และโดยทั่วไปยิ่งมากยิ่งดี
- ตรวจให้แน่ใจว่า assistant responses สะท้อน style, format และ tone ที่คุณต้องการอย่างตรงไปตรงมา

> [!NOTE]
> การใส่ system message ใน training data มีความสำคัญ หากปล่อยว่างมักได้โมเดลที่ความแม่นยำลดลง และเมื่อ deploy fine-tuned model เพื่อ inference ควรใช้ system message เดียวกัน

## Consider the challenges

fine-tuning เพิ่มทั้งต้นทุนและความซับซ้อนที่คุณควรประเมินก่อนตัดสินใจ:

- **Training costs**: fine-tuning มีต้นทุนเริ่มต้นสำหรับการฝึก และมีต้นทุนรายชั่วโมงต่อเนื่องสำหรับการโฮสต์ custom model
- **Data quality requirements**: training data ที่คุณภาพต่ำหรือไม่เป็นตัวแทนที่ดี อาจทำให้เกิด overfitting, underfitting หรือ bias
- **Maintenance**: fine-tuned models อาจต้อง retrain เมื่อข้อมูลเปลี่ยนหรือเมื่อมี base models เวอร์ชันใหม่
- **Experimentation**: การหา hyperparameters ที่เหมาะสม (epochs, batch size, learning rate) ต้องอาศัยการทดสอบและ iteration
- **Model drift**: การปรับโมเดลให้เฉพาะทางแคบเกินไป อาจทำให้โมเดลทำงานด้านภาษาทั่วไปนอกโดเมนที่ fine-tune ไว้ได้แย่ลง

สำหรับ travel agency, fine-tuning หมายถึงทุก response จะสอดคล้องกับ brand voice และ formatting guidelines ของบริษัทอย่างสม่ำเสมอ แม้ไม่มี system messages ที่ยาวมาก แต่ทีมต้องชั่งน้ำหนักประโยชน์นี้เทียบกับต้นทุนในการเตรียม training data และการดูแล fine-tuned model ในระยะยาว

---

## Next unit: Compare and combine optimization strategies