ในโมดูลนี้ คุณได้สำรวจ workflow แบบครบวงจรสำหรับการ selecting, deploying และ evaluating Foundry Models คุณได้เรียนรู้วิธีตัดสินใจเลือก model อย่างมีข้อมูลด้วย benchmarks วิธี deploy models ไปยัง endpoints และวิธีประเมิน performance ของ models ด้วย evaluation approaches ที่หลากหลาย

## Key takeaways

**model catalog** ของ Microsoft Foundry portal ให้คุณเข้าถึง models มากกว่า 1,900 รายการจาก providers เช่น Microsoft, OpenAI, Meta, Mistral และ Hugging Face การ filter อย่างมีประสิทธิภาพด้วย collection, capabilities, deployment options และ attributes อื่นๆ จะช่วยให้คุณจำกัด catalog ให้เหลือ models ที่ตรงกับ requirements ของคุณ

**Model benchmarks** ช่วยให้เปรียบเทียบแบบ objective ในมิติ quality, safety, cost และ performance โดย quality metrics เช่น accuracy, coherence และ fluency ใช้ประเมินว่า models สร้าง responses ที่เหมาะสมได้ดีเพียงใด ส่วน safety metrics ใช้ระบุความเสี่ยงด้าน harmful content, cost benchmarks ช่วยสร้างสมดุลระหว่าง quality กับข้อจำกัดด้าน budget และ performance metrics เช่น latency กับ throughput บ่งชี้ระดับ responsiveness สำหรับ real-time applications

**Deployment options** ประกอบด้วย serverless API สำหรับความยืดหยุ่นแบบ pay-per-call, provisioned deployments สำหรับ workloads ปริมาณสูงที่ต้องการความสม่ำเสมอ, managed compute สำหรับ VM-based hosting และ batch processing สำหรับ non-interactive jobs ที่เน้นการ optimize cost แต่ละ option มีคุณลักษณะที่ต่างกันในด้าน scaling, billing และ control

**Testing in the playground** ให้ feedback ต่อ model behavior ได้ทันทีโดยไม่ต้องเขียน code คุณสามารถทดลอง prompts, ปรับ parameters และสังเกต responses เพื่อทำความเข้าใจ capabilities ของ model ก่อนนำไป integrate กับ applications

**Evaluation approaches** มีตั้งแต่ manual testing ไปจนถึง automated metrics โดย manual evaluation ช่วยเก็บมุมมองเชิง subjective ด้าน quality เช่น user satisfaction และความเหมาะสมตาม context, AI-assisted metrics ช่วยประเมิน generation quality และ safety risks แบบอัตโนมัติ และ NLP metrics เช่น F1-score กับ ROUGE ช่วยเปรียบเทียบเชิงคณิตศาสตร์กับ ground truth data

**Comprehensive evaluation flows** ใน Microsoft Foundry portal ช่วยให้คุณทำ systematic assessments ด้วย test datasets และ metrics หลายประเภท โดยผลลัพธ์จะชี้ให้เห็น strengths, weaknesses และจุดที่ต้องปรับปรุง เพื่อนำไปสู่ iterative development ของ generative AI applications

## Next steps

With models deployed and evaluated, consider these next steps:

**Integrate models into applications** ด้วย SDKs, REST APIs และ code samples ที่มีใน Microsoft Foundry portal โดย applications ของคุณสามารถ consume deployed models ผ่าน authenticated API calls ได้แล้ว

**Implement Retrieval Augmented Generation (RAG)** เพื่อทำให้ model responses อ้างอิงข้อมูลขององค์กรคุณได้อย่างมั่นคง โดย RAG ผสาน models เข้ากับ search capabilities เพื่อสร้าง responses ที่แม่นยำและสอดคล้องกับ context จาก documents และ knowledge bases ของคุณ

**Apply Azure AI Content Safety** services เพื่อเพิ่มชั้นการป้องกันเพิ่มเติมจาก harmful content โดย content filters สามารถ block inputs และ outputs ที่ไม่เหมาะสมได้ และช่วยเสริม model-level safety features

**Fine-tune models** (when supported) บน domain หรือ use case เฉพาะของคุณ เพื่อยกระดับ performance สำหรับสถานการณ์เฉพาะทาง โดย Fine-tuning จะปรับ general-purpose models ให้ตรงกับ requirements เฉพาะของคุณ

**Monitor production performance** ด้วย Azure Monitor และ Application Insights เพื่อติดตาม usage, latency, costs และ errors การ monitoring อย่างต่อเนื่องช่วยให้ applications ของคุณยังคง healthy และ performant

**Iterate based on user feedback** ด้วยการเก็บ real-world usage data และทำ re-evaluations เป็นระยะ การปรับปรุงอย่างต่อเนื่องช่วยให้ generative AI applications ของคุณสอดคล้องกับความต้องการของผู้ใช้เสมอ

ทักษะที่คุณพัฒนาในโมดูลนี้ ได้แก่ การเลือก models ที่เหมาะสม การ deploy อย่างมีประสิทธิภาพ และการ evaluate performance ซึ่งทั้งหมดนี้คือรากฐานสำคัญในการสร้าง generative AI applications ที่ robust และมีคุณภาพสูงด้วย Microsoft Foundry